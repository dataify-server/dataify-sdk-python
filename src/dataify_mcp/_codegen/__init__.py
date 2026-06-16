"""Code generation tooling for Dataify MCP SDK.

This package connects to a running Dataify MCP server, introspects its
``tools/list`` endpoint, and generates typed Pydantic models and convenience
methods for every tool.  The generated code is written into
``src/dataify_mcp/tools/``.

**This package is NOT shipped in the wheel** (excluded in pyproject.toml).
"""

from dataify_mcp._codegen._introspect import fetch_tool_manifest, load_tool_manifest
from dataify_mcp._codegen._generate import generate_tool_modules

__all__ = ["fetch_tool_manifest", "load_tool_manifest", "generate_tool_modules"]
