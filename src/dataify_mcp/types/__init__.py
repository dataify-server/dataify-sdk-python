"""Type definitions for the Dataify MCP SDK."""

from dataify_mcp.types._errors import (
    AuthenticationError,
    ConnectionError,
    DataifyError,
    ProtocolError,
    ServerError,
    TimeoutError,
    ToolAccessError,
    ToolError,
)
from dataify_mcp.types._mcp import (
    JSONRPCError,
    JSONRPCRequest,
    JSONRPCResponse,
    MCPServerCapabilities,
    ServerInfo,
    ToolDefinition,
)

__all__ = [
    # MCP types
    "JSONRPCRequest",
    "JSONRPCResponse",
    "JSONRPCError",
    "ToolDefinition",
    "ServerInfo",
    "MCPServerCapabilities",
    # Errors
    "DataifyError",
    "AuthenticationError",
    "ToolAccessError",
    "ConnectionError",
    "ProtocolError",
    "ToolError",
    "TimeoutError",
    "ServerError",
]
