"""MCP protocol lifecycle management.

Handles JSON-RPC 2.0 message IDs, the ``initialize`` → ``initialized``
handshake, ``tools/list``, ``tools/call``, and ``ping``.
"""

from __future__ import annotations

import logging
from typing import Any

from dataify_mcp.types._errors import ERROR_CODE_MAP, ProtocolError, ToolError
from dataify_mcp.types._mcp import (
    JSONRPCError,
    JSONRPCRequest,
    JSONRPCResponse,
    ServerInfo,
    ToolDefinition,
)

logger = logging.getLogger(__name__)

# MCP protocol version requested by this SDK.
MCP_PROTOCOL_VERSION = "2024-11-05"

# Standard MCP method names.
METHOD_INITIALIZE = "initialize"
METHOD_INITIALIZED = "notifications/initialized"
METHOD_TOOLS_LIST = "tools/list"
METHOD_TOOLS_CALL = "tools/call"
METHOD_PING = "ping"


class MCPProtocol:
    """Manages the MCP JSON-RPC conversation with a single transport.

    The protocol is responsible for:

    * Tracking monotonically increasing message IDs.
    * Performing the MCP handshake (``initialize`` + ``initialized``).
    * Exposing high-level methods that match MCP capabilities
      (``list_tools``, ``call_tool``, ``ping``).
    """

    def __init__(self) -> None:
        self._next_id = 0
        self._server_info: ServerInfo | None = None
        self._initialized = False

    # ------------------------------------------------------------------
    # ID management
    # ------------------------------------------------------------------

    def _allocate_id(self) -> int:
        """Return the next JSON-RPC message id."""
        self._next_id += 1
        return self._next_id

    @property
    def server_info(self) -> ServerInfo | None:
        """Information returned by the server during initialization."""
        return self._server_info

    @property
    def initialized(self) -> bool:
        """Whether the MCP handshake has completed."""
        return self._initialized

    # ------------------------------------------------------------------
    # Request builders
    # ------------------------------------------------------------------

    def build_initialize_request(self, client_name: str, client_version: str) -> JSONRPCRequest:
        """Build the ``initialize`` request."""
        return JSONRPCRequest(
            method=METHOD_INITIALIZE,
            id=self._allocate_id(),
            params={
                "protocolVersion": MCP_PROTOCOL_VERSION,
                "capabilities": {},
                "clientInfo": {
                    "name": client_name,
                    "version": client_version,
                },
            },
        )

    def build_initialized_notification(self) -> JSONRPCRequest:
        """Build the ``notifications/initialized`` notification."""
        return JSONRPCRequest(
            method=METHOD_INITIALIZED,
            id=self._allocate_id(),
            params={},
        )

    def build_list_tools_request(self) -> JSONRPCRequest:
        """Build the ``tools/list`` request."""
        return JSONRPCRequest(
            method=METHOD_TOOLS_LIST,
            id=self._allocate_id(),
            params={},
        )

    def build_call_tool_request(self, name: str, arguments: dict[str, Any]) -> JSONRPCRequest:
        """Build the ``tools/call`` request."""
        return JSONRPCRequest(
            method=METHOD_TOOLS_CALL,
            id=self._allocate_id(),
            params={"name": name, "arguments": arguments},
        )

    def build_ping_request(self) -> JSONRPCRequest:
        """Build the ``ping`` request."""
        return JSONRPCRequest(
            method=METHOD_PING,
            id=self._allocate_id(),
            params={},
        )

    # ------------------------------------------------------------------
    # Response processors
    # ------------------------------------------------------------------

    def process_initialize_response(self, response: JSONRPCResponse) -> ServerInfo:
        """Validate and extract server info from an ``initialize`` response."""
        self._check_response(response)
        result = response.result

        capabilities_raw = result.get("capabilities", {})
        from dataify_mcp.types._mcp import MCPServerCapabilities

        info = ServerInfo(
            name=result.get("serverInfo", {}).get("name", "unknown"),
            version=result.get("serverInfo", {}).get("version", "0.0.0"),
            protocol_version=result.get("protocolVersion", ""),
            capabilities=MCPServerCapabilities(
                tools=capabilities_raw.get("tools"),
                resources=capabilities_raw.get("resources"),
                prompts=capabilities_raw.get("prompts"),
                logging=capabilities_raw.get("logging"),
                experimental=capabilities_raw.get("experimental"),
            ),
            instructions=result.get("instructions"),
        )
        self._server_info = info
        self._initialized = True
        return info

    def process_list_tools_response(self, response: JSONRPCResponse) -> list[ToolDefinition]:
        """Extract tool definitions from a ``tools/list`` response."""
        self._check_response(response)
        tools_data: list[dict[str, Any]] = response.result.get("tools", [])
        return [
            ToolDefinition(
                name=t["name"],
                description=t.get("description", ""),
                inputSchema=t.get("inputSchema", {}),
            )
            for t in tools_data
        ]

    def process_call_tool_response(self, response: JSONRPCResponse) -> Any:
        """Extract the tool result from a ``tools/call`` response.

        Returns the ``content`` field of the result.  Raises ``ToolError``
        when ``isError`` is true.
        """
        self._check_response(response)

        # MCP tools/call result may be nested inside content array
        result = response.result
        is_error = result.get("isError", False)

        content = result.get("content", result)
        if isinstance(content, list) and len(content) == 1:
            item = content[0]
            if isinstance(item, dict) and "text" in item:
                content = item["text"]
            elif isinstance(item, dict) and "data" in item:
                content = item["data"]
            else:
                content = item

        if is_error:
            error_text = content if isinstance(content, str) else result.get("content", [{}])[0].get("text", str(content)) if isinstance(result.get("content"), list) else str(content)
            raise ToolError(error_text)

        return content

    def process_ping_response(self, response: JSONRPCResponse) -> None:
        """Validate a ``ping`` response (no-op on success)."""
        self._check_response(response)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _check_response(response: JSONRPCResponse) -> None:
        """Raise the appropriate SDK exception if the response is an error."""
        if response.error is not None:
            err = response.error
            exc_cls = ERROR_CODE_MAP.get(err.code, ProtocolError)
            raise exc_cls(f"[{err.code}] {err.message}" + (f": {err.data}" if err.data else ""))
