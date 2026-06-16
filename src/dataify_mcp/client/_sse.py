"""SSE (Server-Sent Events) transport for MCP.

Implements the SSE transport: GET ``/sse`` for server-to-client events,
POST ``/message?sessionId=...`` for client-to-server requests.

Session auth bridging: the initial ``/sse`` connection carries ``?token=``.
The server stores the auth parameters in Redis keyed by sessionId (24h TTL).
Subsequent ``/message`` requests only need ``?sessionId=`` — the server
reads auth from Redis.
"""

from __future__ import annotations

import asyncio
import json
import logging
import uuid
from dataclasses import dataclass
from typing import Any

import httpx

from dataify_mcp.types._errors import (
    AuthenticationError,
    ConnectionError,
    ProtocolError,
    ServerError,
    TimeoutError,
)
from dataify_mcp.types._mcp import JSONRPCError, JSONRPCRequest, JSONRPCResponse

logger = logging.getLogger(__name__)

HEADER_SESSION_ID = "Mcp-Session-Id"


@dataclass
class SSETransport:
    """SSE transport that uses ``/sse`` + ``/message`` endpoints.

    Parameters
    ----------
    base_url:
        Base URL of the MCP server, e.g. ``http://localhost:7780``.
    token:
        Dataify API token passed as ``?token=`` on the initial SSE connection.
    tool_codes:
        Optional comma-separated tool codes passed as ``?tools=``.
    timeout:
        HTTP request timeout in seconds (default 30).
    reconnect_delay:
        Initial delay in seconds before reconnecting on SSE disconnect (default 2).
    max_reconnect_delay:
        Maximum delay in seconds for exponential backoff (default 60).
    """

    base_url: str
    token: str
    tool_codes: str | None = None
    timeout: float = 30.0
    reconnect_delay: float = 2.0
    max_reconnect_delay: float = 60.0

    # --- internal state -------------------------------------------------

    _http_client: httpx.AsyncClient | None = None
    _session_id: str | None = None
    _pending: dict[int, asyncio.Future[JSONRPCResponse]] | None = None
    _sse_task: asyncio.Task[None] | None = None
    _stop_event: asyncio.Event | None = None

    # --- URL construction -----------------------------------------------

    @property
    def sse_url(self) -> str:
        """SSE endpoint URL with auth params."""
        url = f"{self.base_url.rstrip('/')}/sse?token={self.token}"
        if self.tool_codes:
            url += f"&tools={self.tool_codes}"
        return url

    @property
    def message_url(self) -> str:
        """Message endpoint URL."""
        session = self._session_id or ""
        return f"{self.base_url.rstrip('/')}/message?sessionId={session}"

    # --- lifecycle ------------------------------------------------------

    async def open(self) -> None:
        """Open the transport: create HTTP client and start the SSE listener."""
        if self._http_client is not None:
            return

        self._http_client = httpx.AsyncClient(timeout=httpx.Timeout(self.timeout))
        self._pending = {}
        self._stop_event = asyncio.Event()
        self._sse_task = asyncio.create_task(self._listen_sse())

    async def close(self) -> None:
        """Close the transport: stop SSE listener and clean up."""
        if self._stop_event:
            self._stop_event.set()

        if self._sse_task:
            self._sse_task.cancel()
            try:
                await self._sse_task
            except asyncio.CancelledError:
                pass
            self._sse_task = None

        if self._http_client is not None:
            await self._http_client.aclose()
            self._http_client = None

        # Resolve any pending futures as errors
        if self._pending:
            for fut in self._pending.values():
                if not fut.done():
                    fut.set_exception(ConnectionError("Transport closed"))
            self._pending.clear()

    @property
    def is_open(self) -> bool:
        """Check whether the transport is currently open."""
        return (
            self._http_client is not None
            and not self._http_client.is_closed
            and self._stop_event is not None
            and not self._stop_event.is_set()
        )

    # --- request / response ---------------------------------------------

    async def send_request(self, request: JSONRPCRequest) -> JSONRPCResponse:
        """Send a JSON-RPC request via POST to ``/message`` and wait for the SSE response.

        Creates a Future keyed by the request id, posts the request, and
        waits for the SSE listener to resolve the future.
        """
        if self._http_client is None or self._pending is None:
            raise ConnectionError("Transport is not open. Call open() first.")

        if self._session_id is None:
            raise ConnectionError(
                "SSE session not yet established. Wait for the SSE listener to connect."
            )

        # Create a future to bridge POST → SSE
        fut: asyncio.Future[JSONRPCResponse] = asyncio.get_event_loop().create_future()
        self._pending[request.id] = fut

        try:
            body = {
                "jsonrpc": request.jsonrpc,
                "id": request.id,
                "method": request.method,
                "params": request.params or {},
            }

            logger.debug("SSE request  id=%d method=%s", request.id, request.method)

            http_resp = await self._http_client.post(
                self.message_url,
                json=body,
                headers={"Content-Type": "application/json"},
            )

            if http_resp.status_code >= 500:
                raise ServerError(f"Server returned HTTP {http_resp.status_code}")

            # The response may come back synchronously or via SSE.
            # If it's a direct response, use it immediately.
            if http_resp.status_code == 200 and http_resp.text.strip():
                try:
                    data = http_resp.json()
                    resp = JSONRPCResponse(
                        jsonrpc=data.get("jsonrpc", "2.0"),
                        id=data.get("id", request.id),
                        result=data.get("result"),
                        error=JSONRPCError(**data["error"]) if "error" in data else None,
                    )
                    if not fut.done():
                        fut.set_result(resp)
                    return resp
                except json.JSONDecodeError:
                    pass  # response will come via SSE

            # Wait for the SSE event to deliver the response
            return await asyncio.wait_for(fut, timeout=self.timeout)

        except asyncio.TimeoutError:
            raise TimeoutError(
                f"Request id={request.id} method={request.method} timed out "
                f"after {self.timeout}s"
            )
        except httpx.NetworkError as exc:
            raise ConnectionError(f"Network error: {exc}") from exc
        finally:
            self._pending.pop(request.id, None)

    async def send_notification(self, request: JSONRPCRequest) -> None:
        """Send a JSON-RPC notification (no response expected)."""
        if self._http_client is None:
            raise ConnectionError("Transport is not open.")

        body = {
            "jsonrpc": request.jsonrpc,
            "method": request.method,
            "params": request.params or {},
        }

        try:
            await self._http_client.post(
                self.message_url,
                json=body,
                headers={"Content-Type": "application/json"},
            )
        except httpx.NetworkError as exc:
            logger.warning("SSE notification %s failed: %s", request.method, exc)

    # --- SSE listener ---------------------------------------------------

    async def _listen_sse(self) -> None:
        """Long-running task that consumes SSE events from ``/sse``.

        Handles:
        * ``endpoint`` event — captures the sessionId for subsequent /message calls.
        * ``message`` event — delivers JSON-RPC responses, resolving pending futures.
        * Reconnection with exponential backoff on disconnect.
        """
        if self._stop_event is None or self._http_client is None:
            return

        delay = self.reconnect_delay

        while not self._stop_event.is_set():
            try:
                async with self._http_client.stream("GET", self.sse_url) as resp:
                    if resp.status_code == 401 or resp.status_code == 403:
                        raise AuthenticationError(
                            "SSE authentication failed. Check your API token."
                        )
                    if resp.status_code >= 500:
                        raise ServerError(f"SSE server error: HTTP {resp.status_code}")

                    delay = self.reconnect_delay  # reset backoff on successful connect

                    async for line in resp.aiter_lines():
                        if self._stop_event.is_set():
                            return

                        if not line:
                            continue

                        if line.startswith("data:"):
                            data_str = line[5:].strip()
                            await self._handle_sse_data(data_str)
                        elif line.startswith("event:"):
                            event_type = line[6:].strip()
                            if event_type == "endpoint":
                                # The next data line will contain the session endpoint
                                pass

            except asyncio.CancelledError:
                return
            except AuthenticationError:
                raise  # don't reconnect on auth failures
            except Exception as exc:
                logger.warning("SSE stream error: %s. Reconnecting in %.1fs...", exc, delay)
                try:
                    await asyncio.wait_for(
                        self._stop_event.wait(), timeout=delay
                    )
                    return  # stop was set
                except asyncio.TimeoutError:
                    pass  # time to reconnect

                # Exponential backoff
                delay = min(delay * 2, self.max_reconnect_delay)

    async def _handle_sse_data(self, data_str: str) -> None:
        """Parse an SSE data line and dispatch to pending futures."""
        if not data_str or self._pending is None:
            return

        try:
            data = json.loads(data_str)
        except json.JSONDecodeError:
            return

        # endpoint event: contains the session URI
        if isinstance(data, str) and "sessionId=" in data:
            # Extract sessionId from the URL
            import urllib.parse
            parsed = urllib.parse.urlparse(data)
            qs = urllib.parse.parse_qs(parsed.query)
            session_ids = qs.get("sessionId", [])
            if session_ids:
                self._session_id = session_ids[0]
                logger.debug("SSE session established: %s", self._session_id)
            return

        if not isinstance(data, dict):
            return

        # It's a JSON-RPC response
        resp_id = data.get("id")
        if resp_id is not None and resp_id in self._pending:
            resp = JSONRPCResponse(
                jsonrpc=data.get("jsonrpc", "2.0"),
                id=resp_id,
                result=data.get("result"),
                error=JSONRPCError(**data["error"]) if "error" in data else None,
            )
            fut = self._pending[resp_id]
            if not fut.done():
                fut.set_result(resp)
