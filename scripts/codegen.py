#!/usr/bin/env python3
"""Regenerate the Dataify SDK tool layer from the Go reference project.

The Go project at ``C:\\dataify\\dataify_mcp_api`` is the source of truth.  This
script invokes the generator, which writes ``src/dataify_sdk/tools/*.py`` and
``docs/api_reference.md``.

Usage::

    python scripts/codegen.py
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "src"))

from dataify_sdk._codegen.generate import main





if __name__ == "__main__":
    raise SystemExit(main())
