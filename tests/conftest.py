"""Shared test fixtures for the Dataify MCP SDK."""

from __future__ import annotations

import json
from typing import Any

import httpx
import pytest


# ---------------------------------------------------------------------------
# Mock server responses
# ---------------------------------------------------------------------------


def make_tools_list_response(req_id: int) -> dict[str, Any]:
    """Return a minimal tools/list response with a few representative tools."""
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {
            "tools": [
                {
                    "name": "google_search",
                    "description": "Search Google for web results.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "q": {
                                "type": "string",
                                "description": "Search query",
                                "default": "pizza",
                            },
                            "gl": {
                                "type": "string",
                                "description": "Country code",
                                "default": "",
                            },
                        },
                        "required": ["q"],
                    },
                },
                {
                    "name": "query_user_info",
                    "description": "Query user account info.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {},
                    },
                },
                {
                    "name": "request_web_unlocker",
                    "description": "Unlock a web page.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "url": {
                                "type": "string",
                                "description": "Target URL",
                            },
                            "type": {
                                "type": "string",
                                "description": "Output format",
                                "default": "html",
                            },
                        },
                        "required": ["url"],
                    },
                },
            ]
        },
    }


def make_initialize_response(req_id: int) -> dict[str, Any]:
    """Return a minimal initialize response."""
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {
            "protocolVersion": "2024-11-05",
            "serverInfo": {
                "name": "dataify-task-status-mcp",
                "version": "1.0.0",
            },
            "capabilities": {"tools": {}},
        },
    }


def make_call_tool_response(req_id: int, result_content: Any = None, is_error: bool = False) -> dict[str, Any]:
    """Return a tools/call response."""
    content = result_content if result_content is not None else {"status": "ok", "data": []}
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {
            "content": [{"type": "text", "text": json.dumps(content, ensure_ascii=False)}],
            "isError": is_error,
        },
    }


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_server_url() -> str:
    return "http://mock-server:7780"


@pytest.fixture
def api_token() -> str:
    return "test-token-12345"


@pytest.fixture
def tool_manifest() -> list[dict[str, Any]]:
    """Return a small, representative tool manifest for testing codegen."""
    return make_tools_list_response(1)["result"]["tools"]
