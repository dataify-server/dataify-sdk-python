"""Dataify MCP SDK — Python client for the Dataify MCP API.

Provides access to web unlocker, search engines (Google, Bing, Yandex, DuckDuckGo),
and platform scrapers (Amazon, YouTube, TikTok, Facebook, Instagram, etc.) through
the Model Context Protocol.
"""

from dataify_mcp._version import __version__
from dataify_mcp.client._base import DataifyClient
from dataify_mcp.client._http import HTTPTransport
from dataify_mcp.client._sse import SSETransport
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

__all__ = [
    "__version__",
    "DataifyClient",
    "HTTPTransport",
    "SSETransport",
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
