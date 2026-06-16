"""MCP protocol type definitions.

These map to the JSON-RPC 2.0 structures used by the Model Context Protocol.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class JSONRPCRequest:
    """A JSON-RPC 2.0 request."""

    method: str
    params: dict[str, Any] | None = None
    jsonrpc: str = "2.0"
    id: int = 0


@dataclass
class JSONRPCError:
    """A JSON-RPC 2.0 error object."""

    code: int
    message: str
    data: Any = None


@dataclass
class JSONRPCResponse:
    """A JSON-RPC 2.0 response."""

    id: int
    jsonrpc: str = "2.0"
    result: Any = None
    error: JSONRPCError | None = None

    @property
    def is_error(self) -> bool:
        """Check if this response contains an error."""
        return self.error is not None


@dataclass
class ToolDefinition:
    """An MCP tool definition as returned by tools/list."""

    name: str
    description: str = ""
    inputSchema: dict[str, Any] = field(default_factory=dict)


@dataclass
class MCPServerCapabilities:
    """Server capabilities reported during initialization."""

    tools: dict[str, Any] | None = None
    resources: dict[str, Any] | None = None
    prompts: dict[str, Any] | None = None
    logging: dict[str, Any] | None = None
    experimental: dict[str, Any] | None = None


@dataclass
class ServerInfo:
    """Server information returned by the initialize response."""

    name: str
    version: str
    protocol_version: str = ""
    capabilities: MCPServerCapabilities = field(default_factory=MCPServerCapabilities)
    instructions: str | None = None


@dataclass
class CallToolResult:
    """Structured result of a tools/call invocation.

    When ``isError`` is True, the tool execution failed and ``content``
    contains an error message.  Otherwise ``content`` holds the
    structured output and ``structured_content`` may carry a typed
    payload the server attached.
    """

    content: Any
    isError: bool = False
    structured_content: Any = None
