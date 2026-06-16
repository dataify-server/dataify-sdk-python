"""Tests for the HTTP transport and DataifyClient."""

from __future__ import annotations

import pytest
from pytest_httpx import HTTPXMock

from dataify_mcp import DataifyClient
from dataify_mcp.types._errors import AuthenticationError, ToolError

from tests.conftest import (
    make_call_tool_response,
    make_initialize_response,
    make_tools_list_response,
)


def _token_url(base: str, token: str) -> str:
    return f"{base}/mcp?token={token}"


class TestDataifyClientHTTP:
    """Integration-style tests using httpx mock.

    pytest-httpx matches mocks in FIFO order when no match filters
    are specified.  Each test registers mocks in the exact order
    that requests are sent:

    1. initialize request  → initialize response
    2. initialized notification  → 202 (ack)
    3. (optional) tools/list → tool list response
    4. (optional) tools/call → call result
    5. (optional) ping → ping result
    """

    @pytest.mark.asyncio
    async def test_initialize(self, httpx_mock: HTTPXMock, mock_server_url: str, api_token: str):
        """Client should complete the MCP handshake successfully."""
        url = _token_url(mock_server_url, api_token)

        # Request 1: initialize
        httpx_mock.add_response(method="POST", url=url, json=make_initialize_response(1))
        # Request 2: initialized notification
        httpx_mock.add_response(method="POST", url=url, status_code=202)

        async with DataifyClient(mock_server_url, api_token) as client:
            assert client.is_initialized
            assert client.server_info is not None
            assert client.server_info.name == "dataify-task-status-mcp"

    @pytest.mark.asyncio
    async def test_list_tools(self, httpx_mock: HTTPXMock, mock_server_url: str, api_token: str):
        """Client should list available tools."""
        url = _token_url(mock_server_url, api_token)

        httpx_mock.add_response(method="POST", url=url, json=make_initialize_response(1))
        httpx_mock.add_response(method="POST", url=url, status_code=202)
        httpx_mock.add_response(method="POST", url=url, json=make_tools_list_response(2))

        async with DataifyClient(mock_server_url, api_token) as client:
            tools = await client.list_tools()
            assert len(tools) == 3
            assert tools[0].name == "google_search"

    @pytest.mark.asyncio
    async def test_call_tool(self, httpx_mock: HTTPXMock, mock_server_url: str, api_token: str):
        """Client should call a tool and return the result."""
        url = _token_url(mock_server_url, api_token)

        httpx_mock.add_response(method="POST", url=url, json=make_initialize_response(1))
        httpx_mock.add_response(method="POST", url=url, status_code=202)
        httpx_mock.add_response(method="POST", url=url, json=make_tools_list_response(2))
        httpx_mock.add_response(
            method="POST", url=url,
            json=make_call_tool_response(3, {"results": [{"title": "Test"}]}),
        )

        async with DataifyClient(mock_server_url, api_token) as client:
            await client.list_tools()
            result = await client.call_tool("google_search", {"q": "test"})
            assert result is not None

    @pytest.mark.asyncio
    async def test_call_tool_error(self, httpx_mock: HTTPXMock, mock_server_url: str, api_token: str):
        """Client should raise ToolError when the server returns isError: true."""
        url = _token_url(mock_server_url, api_token)

        httpx_mock.add_response(method="POST", url=url, json=make_initialize_response(1))
        httpx_mock.add_response(method="POST", url=url, status_code=202)
        httpx_mock.add_response(method="POST", url=url, json=make_tools_list_response(2))
        httpx_mock.add_response(
            method="POST", url=url,
            json=make_call_tool_response(3, "Invalid parameters", is_error=True),
        )

        async with DataifyClient(mock_server_url, api_token) as client:
            await client.list_tools()
            with pytest.raises(ToolError):
                await client.call_tool("google_search", {"q": ""})

    @pytest.mark.asyncio
    async def test_auth_error(self, httpx_mock: HTTPXMock, mock_server_url: str, api_token: str):
        """Client should raise AuthenticationError on HTTP 401."""
        url = _token_url(mock_server_url, api_token)
        httpx_mock.add_response(method="POST", url=url, status_code=401, json={"error": "Unauthorized"})

        with pytest.raises(AuthenticationError):
            async with DataifyClient(mock_server_url, api_token):
                pass

    @pytest.mark.asyncio
    async def test_tool_codes_in_url(self, httpx_mock: HTTPXMock, mock_server_url: str, api_token: str):
        """Client should append tool_codes to the URL query string."""
        url = f"{mock_server_url}/mcp?token={api_token}&tools=serp,google"

        httpx_mock.add_response(method="POST", url=url, json=make_initialize_response(1))
        httpx_mock.add_response(method="POST", url=url, status_code=202)

        async with DataifyClient(
            mock_server_url, api_token, tool_codes="serp,google"
        ) as client:
            assert client.is_initialized

    @pytest.mark.asyncio
    async def test_ping(self, httpx_mock: HTTPXMock, mock_server_url: str, api_token: str):
        """Client should support ping."""
        url = _token_url(mock_server_url, api_token)

        httpx_mock.add_response(method="POST", url=url, json=make_initialize_response(1))
        httpx_mock.add_response(method="POST", url=url, status_code=202)
        httpx_mock.add_response(method="POST", url=url, json=make_tools_list_response(2))
        httpx_mock.add_response(method="POST", url=url, json={"jsonrpc": "2.0", "id": 3, "result": {}})

        async with DataifyClient(mock_server_url, api_token) as client:
            await client.list_tools()
            await client.ping()
