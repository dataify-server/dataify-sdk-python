"""Error hierarchy for the Dataify MCP SDK.

Every exception raised by the SDK inherits from `DataifyError`, making it
easy to catch any SDK-related error with a single except clause.
"""

from __future__ import annotations


class DataifyError(Exception):
    """Base exception for all SDK errors."""


class AuthenticationError(DataifyError):
    """Raised when the API token is missing, invalid, or expired.

    The user should obtain a valid token from https://dashboard.dataify.com
    and pass it to the client constructor or as a query parameter.
    """


class ToolAccessError(DataifyError):
    """Raised when the token does not have permission to use a specific tool.

    This typically means the tool is not in the user's plan.  The user can
    upgrade via https://dashboard.dataify.com or pass a ``tools=`` query
    parameter to limit which tools are requested.
    """


class ConnectionError(DataifyError):
    """Raised when the SDK cannot connect to the MCP server.

    This covers DNS resolution failures, TCP connection refused, TLS errors,
    and other transport-level issues.
    """


class ProtocolError(DataifyError):
    """Raised when the server sends an invalid or unexpected JSON-RPC response.

    Examples include missing ``id`` fields, invalid JSON, or responses that
    don't match any pending request.
    """


class ToolError(DataifyError):
    """Raised when a tool call returns ``isError: true``.

    The tool executed on the server side but failed (e.g. upstream API
    returned an error, invalid parameters, etc.).  The error message
    comes from the server.
    """


class TimeoutError(DataifyError):
    """Raised when a request to the MCP server exceeds the configured timeout."""


class ServerError(DataifyError):
    """Raised when the server returns an HTTP 5xx status code."""


# Maps JSON-RPC error codes to SDK exception types.
# Reference: https://www.jsonrpc.org/specification#error_object
ERROR_CODE_MAP: dict[int, type[DataifyError]] = {
    -32000: ServerError,      # Server error (generic)
    -32600: ProtocolError,    # Invalid Request
    -32601: ProtocolError,    # Method not found
    -32602: ProtocolError,    # Invalid params
    -32603: ServerError,      # Internal error
    -32001: AuthenticationError,  # Unauthorized (common MCP convention)
}
