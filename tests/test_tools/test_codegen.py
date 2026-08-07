"""Tests for the Go -> Python code generator (parsing logic)."""

from __future__ import annotations

from pathlib import Path

from dataify_sdk._codegen import generate as gen

REPO = Path(r"C:/dataify/dataify_mcp_api")


def test_sanitize():
    assert gen.sanitize("google_domain") == "google_domain"
    assert gen.sanitize("json") == "json_"  # reserved builtin
    assert gen.sanitize("ai-overview") == "ai_overview"


def test_parse_string_consts():
    txt = 'const defaultASIN = "B0BZYCJK89"\nconst x = "y"'
    consts = gen.parse_string_consts(txt)
    assert consts["defaultASIN"] == "B0BZYCJK89"
    assert consts["x"] == "y"


def test_parse_struct_map():
    if not REPO.exists():
        import pytest

        pytest.skip("Go reference project not available")
    sm = gen.parse_struct_map()
    assert "GoogleSearchRequest" in sm
    assert sm["GoogleSearchRequest"]["Query"] == "q"
    assert sm["GoogleSearchRequest"]["GoogleDomain"] == "google_domain"


def test_docs_reference_exists():
    docs = Path(__file__).resolve().parents[2] / "docs" / "api_reference.md"
    if not docs.exists():
        import pytest

        pytest.skip("docs not generated yet")
    content = docs.read_text(encoding="utf-8")
    assert "amazon_product_by_asin" in content
    assert "google_search" in content
