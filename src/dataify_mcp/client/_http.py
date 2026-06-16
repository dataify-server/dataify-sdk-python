"""Streamable HTTP transport for MCP.

Implements the Streamable HTTP transport defined by the MCP spec:
POST ``/mcp`` with JSON-RPC bodies; the server may return the response
directly or stream it via SSE.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Any

import httpx

from dataify_mcp.types._errors import (
    ConnectionError,
    ProtocolError,
    ServerError,
    TimeoutError,
)
from dataify_mcp.types._mcp import JSONRPCError, JSONRPCRequest, JSONRPCResponse

logger = logging.getLogger(__name__)

# Headers used by the MCP Streamable HTTP transport.
HEADER_SESSION_ID = "Mcp-Session-Id"
HEADER_LAST_EVENT_ID = "Last-Event-ID"
HEADER_CONTENT_TYPE = "Content-Type"
MIME_JSON = "application/json"


@dataclass
class HTTPTransport:
    """Streamable HTTP transport that talks to the ``/mcp`` endpoint.

    Parameters
    ----------
    base_url:
        Base URL of the MCP server, e.g. ``http://localhost:7780``.
        Must not include a trailing slash.
    token:
        Dataify API token passed as the ``?token=`` query parameter.
    tool_codes:
        Optional comma-separated tool codes passed as ``?tools=``.
    timeout:
        HTTP request timeout in seconds (default 30).
    """

    base_url: str
    token: str
    tool_codes: str | None = None
    timeout: float = 30.0

    # --- internal state -------------------------------------------------

    _client: httpx.AsyncClient | None = None
    _session_id: str | None = None

    # --- URL construction -----------------------------------------------

    @property
    def endpoint(self) -> str:
        """Full URL of the MCP endpoint including auth query params."""
        url = f"{self.base_url.rstrip('/')}/mcp?token={self.token}"
        if self.tool_codes:
            url += f"&tools={self.tool_codes}"
        return url

    # --- lifecycle ------------------------------------------------------

    async def open(self) -> None:
        """Create the underlying HTTP client if not already open."""
        if self._client is not None:
            return
        self._client = httpx.AsyncClient(timeout=httpx.Timeout(self.timeout))

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        if self._client is not None:
            await self._client.aclose()
            self._client = None
            self._session_id = None

    @property
    def is_open(self) -> bool:
        """Check whether the transport is currently open."""
        return self._client is not None and not self._client.is_closed

    # --- request/response -----------------------------------------------

    async def send_request(self, request: JSONRPCRequest) -> JSONRPCResponse:
        """Send a JSON-RPC request and return the parsed response.

        Raises
        ------
        ConnectionError
            On network-level failures.
        ProtocolError
            When the server response is not valid JSON or lacks the expected fields.
        ServerError
            When the server returns HTTP 5xx.
        TimeoutError
            When the request exceeds the configured timeout.
        """
        if self._client is None:
            raise ConnectionError("Transport is not open. Call open() first.")

        headers: dict[str, str] = {
            HEADER_CONTENT_TYPE: MIME_JSON,
            "Accept": MIME_JSON,
        }
        if self._session_id:
            headers[HEADER_SESSION_ID] = self._session_id

        body = {
            "jsonrpc": request.jsonrpc,
            "id": request.id,
            "method": request.method,
            "params": request.params or {},
        }

        logger.debug("MCP request  id=%d method=%s", request.id, request.method)

        try:
            http_resp = await self._client.post(
                self.endpoint,
                json=body,
                headers=headers,
            )
        except httpx.TimeoutException as exc:
            raise TimeoutError(
                f"Request id={request.id} method={request.method} timed out "
                f"after {self.timeout}s"
            ) from exc
        except httpx.NetworkError as exc:
            raise ConnectionError(
                f"Network error sending request id={request.id}: {exc}"
            ) from exc

        # Capture session id from server response
        session_id = http_resp.headers.get(HEADER_SESSION_ID)
        if session_id:
            self._session_id = session_id

        # Handle HTTP errors
        if http_resp.status_code >= 500:
            raise ServerError(
                f"Server returned HTTP {http_resp.status_code}: {http_resp.text[:500]}"
            )
        if http_resp.status_code == 401 or http_resp.status_code == 403:
            from dataify_mcp.types._errors import AuthenticationError

            raise AuthenticationError(
                f"Authentication failed (HTTP {http_resp.status_code}). "
                "Check your API token at https://dashboard.dataify.com"
            )

        # Try to parse the response body as JSON
        try:
            data = http_resp.json()
        except json.JSONDecodeError as exc:
            raise ProtocolError(
                f"Invalid JSON response for id={request.id}: {http_resp.text[:500]}"
            ) from exc

        # Build JSONRPCResponse
        return JSONRPCResponse(
            jsonrpc=data.get("jsonrpc", "2.0"),
            id=data.get("id", request.id),
            result=data.get("result"),
            error=JSONRPCError(**data["error"]) if "error" in data and data["error"] else None,
        )

    async def send_notification(self, request: JSONRPCRequest) -> None:
        """Send a JSON-RPC notification (no response expected)."""
        if self._client is None:
            raise ConnectionError("Transport is not open. Call open() first.")

        headers: dict[str, str] = {
            HEADER_CONTENT_TYPE: MIME_JSON,
            "Accept": MIME_JSON,
        }
        if self._session_id:
            headers[HEADER_SESSION_ID] = self._session_id

        body = {
            "jsonrpc": request.jsonrpc,
            "method": request.method,
            "params": request.params or {},
        }

        logger.debug("MCP notification method=%s", request.method)

        try:
            await self._client.post(
                self.endpoint,
                json=body,
                headers=headers,
            )
        except httpx.TimeoutException:
            logger.warning("Notification %s timed out (ignoring)", request.method)
        except httpx.NetworkError as exc:
            logger.warning("Notification %s failed: %s", request.method, exc)
