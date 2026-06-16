"""Fetch tool definitions from a running Dataify MCP server."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx

from dataify_mcp.client._protocol import (
    METHOD_INITIALIZE,
    METHOD_INITIALIZED,
    METHOD_TOOLS_LIST,
    MCP_PROTOCOL_VERSION,
)
from dataify_mcp.types._mcp import JSONRPCRequest, JSONRPCResponse


async def fetch_tool_manifest(
    base_url: str,
    token: str,
    *,
    tool_codes: str | None = None,
    timeout: float = 30.0,
) -> list[dict[str, Any]]:
    """Connect to the MCP server and return its full ``tools/list`` response.

    Parameters
    ----------
    base_url:
        Server base URL, e.g. ``http://localhost:7780``.
    token:
        Dataify API token.
    tool_codes:
        Optional tool code filter.
    timeout:
        Request timeout in seconds.

    Returns
    -------
    list[dict]
        The raw tool definitions (``name``, ``description``, ``inputSchema``).
    """
    url = f"{base_url.rstrip('/')}/mcp?token={token}"
    if tool_codes:
        url += f"&tools={tool_codes}"

    async with httpx.AsyncClient(timeout=httpx.Timeout(timeout)) as client:
        # Initialize
        init_id = 1
        init_resp = await _rpc(client, url, init_id, METHOD_INITIALIZE, {
            "protocolVersion": MCP_PROTOCOL_VERSION,
            "capabilities": {},
            "clientInfo": {"name": "dataify-codegen", "version": "0.1.0"},
        })
        if "error" in init_resp:
            raise RuntimeError(f"Initialize failed: {init_resp['error']}")

        # Send initialized notification
        await _rpc_notification(client, url, METHOD_INITIALIZED)

        # List tools
        list_id = 2
        list_resp = await _rpc(client, url, list_id, METHOD_TOOLS_LIST, {})
        if "error" in list_resp:
            raise RuntimeError(f"tools/list failed: {list_resp['error']}")

        return list_resp.get("result", {}).get("tools", [])


def load_tool_manifest(path: str | Path) -> list[dict[str, Any]]:
    """Load a previously saved tool manifest from a JSON file."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_tool_manifest(tools: list[dict[str, Any]], path: str | Path) -> None:
    """Save a tool manifest to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)


async def _rpc(
    client: httpx.AsyncClient,
    url: str,
    req_id: int,
    method: str,
    params: dict[str, Any],
) -> dict[str, Any]:
    """Send a JSON-RPC request and return the raw dict."""
    resp = await client.post(
        url,
        json={"jsonrpc": "2.0", "id": req_id, "method": method, "params": params},
        headers={"Content-Type": "application/json"},
    )
    resp.raise_for_status()
    return resp.json()


async def _rpc_notification(
    client: httpx.AsyncClient,
    url: str,
    method: str,
    params: dict[str, Any] | None = None,
) -> None:
    """Send a JSON-RPC notification (no id field)."""
    await client.post(
        url,
        json={"jsonrpc": "2.0", "method": method, "params": params or {}},
        headers={"Content-Type": "application/json"},
    )
