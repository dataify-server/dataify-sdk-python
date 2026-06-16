#!/usr/bin/env python3
"""Code generation CLI for the Dataify MCP SDK.

Usage::

    # Fetch tools from a running server and generate wrappers
    python scripts/codegen.py --server http://localhost:7780 --token YOUR_TOKEN

    # Generate from a previously saved manifest
    python scripts/codegen.py --manifest tool_manifest.json

    # Save the manifest without generating
    python scripts/codegen.py --server http://localhost:7780 --token YOUR_TOKEN --save-only
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

# Allow running directly from the scripts directory
_scripts_dir = Path(__file__).resolve().parent
_sdk_root = _scripts_dir.parent
sys.path.insert(0, str(_sdk_root / "src"))

from dataify_mcp._codegen._generate import generate_tool_modules
from dataify_mcp._codegen._introspect import (
    fetch_tool_manifest,
    load_tool_manifest,
    save_tool_manifest,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate typed tool wrappers for Dataify MCP SDK",
    )
    parser.add_argument(
        "--server",
        help="Dataify MCP server URL (e.g. http://localhost:7780)",
    )
    parser.add_argument(
        "--token",
        help="API token for the MCP server",
    )
    parser.add_argument(
        "--tools",
        help="Optional tool code filter (comma-separated)",
    )
    parser.add_argument(
        "--manifest",
        help="Path to a previously saved tool_manifest.json",
    )
    parser.add_argument(
        "--output",
        default=str(_sdk_root / "src" / "dataify_mcp" / "tools"),
        help="Output directory for generated modules",
    )
    parser.add_argument(
        "--save-manifest",
        default=str(_sdk_root / "tool_manifest.json"),
        help="Path to save the tool manifest JSON",
    )
    parser.add_argument(
        "--save-only",
        action="store_true",
        help="Only save the manifest, do not generate code",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP request timeout in seconds",
    )

    args = parser.parse_args()

    if args.server and args.token:
        print(f"Fetching tool manifest from {args.server} ...")
        tools = asyncio.run(
            fetch_tool_manifest(
                args.server,
                args.token,
                tool_codes=args.tools,
                timeout=args.timeout,
            )
        )
        print(f"  → {len(tools)} tools discovered")

        save_tool_manifest(tools, args.save_manifest)
        print(f"  → saved to {args.save_manifest}")

        if args.save_only:
            return

    elif args.manifest:
        print(f"Loading tool manifest from {args.manifest} ...")
        tools = load_tool_manifest(args.manifest)
        print(f"  → {len(tools)} tools loaded")

    else:
        parser.error("Either --server + --token, or --manifest is required")

    print(f"Generating tool wrappers in {args.output} ...")
    written = generate_tool_modules(tools, args.output)
    for module, tool_names in sorted(written.items()):
        print(f"  {module}.py: {len(tool_names)} tools")
    print(f"  → {sum(len(v) for v in written.values())} tools across {len(written)} modules")

    print("Done.")
    print()
    print("Next steps:")
    print("  1. Review generated code for correctness")
    print("  2. Run: ruff check src/dataify_mcp/tools/")
    print("  3. Run: python -c 'from dataify_mcp.tools import *'  # verify imports")


if __name__ == "__main__":
    main()
