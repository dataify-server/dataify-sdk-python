"""DataifyClient — the main entry point for the Dataify MCP SDK.

Usage::

    import asyncio
    from dataify_mcp import DataifyClient

    async def main():
        async with DataifyClient(
            base_url="http://localhost:7780",
            token="your-api-token",
        ) as client:
            tools = await client.list_tools()
            print(f"Available tools: {len(tools)}")

            result = await client.call_tool("google_search", {"q": "weather"})
            print(result)

    asyncio.run(main())
"""

from __future__ import annotations

import logging
from types import TracebackType
from typing import Any

from dataify_mcp._version import __version__
from dataify_mcp.client._http import HTTPTransport
from dataify_mcp.client._protocol import MCPProtocol
from dataify_mcp.client._sse import SSETransport
from dataify_mcp.types._errors import ConnectionError
from dataify_mcp.types._mcp import ServerInfo, ToolDefinition

logger = logging.getLogger(__name__)

CLIENT_NAME = "dataify-mcp-sdk"


class DataifyClient:
    """Async client for the Dataify MCP API.

    Wraps an MCP transport and protocol to provide a simple, Pythonic
    interface for listing and calling MCP tools.

    Parameters
    ----------
    base_url:
        Base URL of the MCP server, e.g. ``http://localhost:7780``.
    token:
        Dataify API token. Obtain from https://dashboard.dataify.com.
    tool_codes:
        Optional comma-separated list of ``class_code,tool_code`` pairs
        to filter which tools are available.  Without this parameter only
        free tools are visible.
    timeout:
        HTTP request timeout in seconds (default 30).
    transport:
        Transport mode: ``"http"`` (default) or ``"sse"``.
    """

    def __init__(
        self,
        base_url: str,
        token: str,
        *,
        tool_codes: str | None = None,
        timeout: float = 30.0,
        transport: str = "http",
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._token = token
        self._tool_codes = tool_codes
        self._timeout = timeout

        self._protocol = MCPProtocol()

        if transport == "sse":
            self._transport = SSETransport(
                base_url=base_url,
                token=token,
                tool_codes=tool_codes,
                timeout=timeout,
            )
        else:
            self._transport = HTTPTransport(
                base_url=base_url,
                token=token,
                tool_codes=tool_codes,
                timeout=timeout,
            )

        self._transport_type = transport

    # ------------------------------------------------------------------
    # Context manager
    # ------------------------------------------------------------------

    async def __aenter__(self) -> "DataifyClient":
        await self.initialize()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    async def initialize(self) -> ServerInfo:
        """Open the transport, perform the MCP handshake, and return server info.

        This is called automatically when using the async context manager.
        If you create a client manually you must call this before using it.
        """
        await self._transport.open()

        # Step 1: initialize
        init_req = self._protocol.build_initialize_request(CLIENT_NAME, __version__)
        init_resp = await self._transport.send_request(init_req)
        info = self._protocol.process_initialize_response(init_resp)

        logger.info(
            "Connected to %s v%s (protocol %s)",
            info.name,
            info.version,
            info.protocol_version,
        )

        # Step 2: send initialized notification
        notif = self._protocol.build_initialized_notification()
        await self._transport.send_notification(notif)

        return info

    async def close(self) -> None:
        """Close the underlying transport."""
        await self._transport.close()

    @property
    def server_info(self) -> ServerInfo | None:
        """Information returned by the server during initialization."""
        return self._protocol.server_info

    @property
    def is_initialized(self) -> bool:
        """Whether the MCP handshake has completed."""
        return self._protocol.initialized

    # ------------------------------------------------------------------
    # MCP operations
    # ------------------------------------------------------------------

    async def list_tools(self) -> list[ToolDefinition]:
        """Fetch the list of available tools from the server.

        The returned list respects the ``tool_codes`` filter if one was
        provided at construction time.
        """
        if not self.is_initialized:
            raise ConnectionError("Client not initialized. Call initialize() first.")

        req = self._protocol.build_list_tools_request()
        resp = await self._transport.send_request(req)
        return self._protocol.process_list_tools_response(resp)

    async def call_tool(self, name: str, arguments: dict[str, Any]) -> Any:
        """Call an MCP tool by name with the given keyword arguments.

        Parameters
        ----------
        name:
            Tool name (e.g. ``"google_search"``, ``"request_web_unlocker"``).
        arguments:
            Tool parameters as a dictionary.  All values are passed as
            strings matching the server's expected format.

        Returns
        -------
        Any
            The tool result content (usually a dict).

        Raises
        ------
        ToolError
            When the tool execution fails on the server side.
        ConnectionError
            When the transport is not initialized or has been closed.
        """
        if not self.is_initialized:
            raise ConnectionError("Client not initialized. Call initialize() first.")

        req = self._protocol.build_call_tool_request(name, arguments)
        resp = await self._transport.send_request(req)
        return self._protocol.process_call_tool_response(resp)

    async def ping(self) -> None:
        """Send a ping to verify the server is reachable."""
        req = self._protocol.build_ping_request()
        resp = await self._transport.send_request(req)
        self._protocol.process_ping_response(resp)

    # ------------------------------------------------------------------
    # -- High-level convenience methods (auto-attached) --
    #
    # Typed tool methods (google_search, request_web_unlocker, etc.) are
    # attached to this class at import time by ``dataify_mcp.tools.attach_all``.
    # See ``src/dataify_mcp/tools/__init__.py``.
    #
    # When the server adds new tools, regenerate the tool modules by running:
    #     python scripts/codegen.py --server http://localhost:7780
    # ------------------------------------------------------------------


# Attach all typed tool methods to the DataifyClient class at import time.
from dataify_mcp.tools import attach_all  # noqa: E402

attach_all(DataifyClient)
