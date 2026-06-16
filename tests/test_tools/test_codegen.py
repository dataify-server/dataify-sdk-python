"""Tests for the code generation system."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest


@pytest.fixture
def sample_tools() -> list[dict]:
    """A minimal but representative set of tool definitions."""
    return [
        {
            "name": "google_search",
            "description": "Search Google for web results.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "q": {"type": "string", "description": "Search query", "default": "pizza"},
                    "gl": {"type": "string", "description": "Country code", "default": ""},
                    "no_cache": {"type": "string", "description": "Skip cache", "default": "false"},
                },
                "required": ["q"],
            },
        },
        {
            "name": "query_user_info",
            "description": "Query user account info.",
            "inputSchema": {"type": "object", "properties": {}},
        },
        {
            "name": "web_unlock_task",
            "description": "Query task status.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Task ID or domain", "default": ""},
                    "status": {"type": "integer", "description": "Task status", "default": -1},
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
            },
        },
        {
            "name": "bing_search",
            "description": "Search Bing for web results.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "q": {"type": "string", "description": "Query", "default": "Pizza"},
                },
                "required": ["q"],
            },
        },
        {
            "name": "scrape_amazon_product",
            "description": "Scrape Amazon product details.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "spider_id": {
                        "type": "string",
                        "description": "Scraper identifier",
                        "default": "amazon_product_by-asin",
                    },
                },
                "required": ["spider_id"],
            },
        },
    ]


class TestCodeGenerator:
    """Verify the code generator produces valid Python modules."""

    def test_generate_creates_files(self, sample_tools, tmp_path):
        """Generator should create a .py file for each tool category."""
        from dataify_mcp._codegen._generate import generate_tool_modules

        written = generate_tool_modules(sample_tools, tmp_path)

        assert len(written) > 0
        for module_name, tool_names in written.items():
            module_path = tmp_path / f"{module_name}.py"
            assert module_path.exists(), f"Expected {module_path} to exist"
            content = module_path.read_text()
            for tool_name in tool_names:
                # Each tool should have a param model class
                assert "class " in content
                assert tool_name in content

    def test_generated_code_is_valid_python(self, sample_tools, tmp_path):
        """Generated .py files should be syntactically valid Python."""
        import py_compile

        from dataify_mcp._codegen._generate import generate_tool_modules

        written = generate_tool_modules(sample_tools, tmp_path)
        for module_name in written:
            module_path = tmp_path / f"{module_name}.py"
            # Should compile without errors
            py_compile.compile(str(module_path), doraise=True)

    def test_tool_to_module_mapping(self):
        """Verify tool name → module mapping is correct."""
        from dataify_mcp._codegen._generate import tool_to_module

        assert tool_to_module("google_search") == "google_serp"
        assert tool_to_module("google_news") == "google_serp"
        assert tool_to_module("google_map_details") == "google_scraper"
        assert tool_to_module("bing_search") == "bing"
        assert tool_to_module("bing_images") == "bing"
        assert tool_to_module("yandex_search") == "other_search"
        assert tool_to_module("duckduckgo_search") == "other_search"
        assert tool_to_module("web_unlock_task") == "task_status"
        assert tool_to_module("query_user_info") == "user"
        assert tool_to_module("request_web_unlocker") == "web_unlocker"
        assert tool_to_module("scrape_amazon_product") == "amazon"
        assert tool_to_module("scrape_youtube_video") == "youtube"
        assert tool_to_module("scrape_tiktok_posts") == "tiktok"
        assert tool_to_module("scrape_facebook_post") == "facebook"
        assert tool_to_module("scrape_instagram_profiles") == "instagram"
        assert tool_to_module("scrape_reddit_posts") == "reddit"
        assert tool_to_module("scrape_twitter_post") == "twitter"
        assert tool_to_module("scrape_linkedin_company_information") == "linkedin"
        assert tool_to_module("scrape_glassdoor_company") == "glassdoor"
        assert tool_to_module("scrape_indeed_companies_info") == "indeed"
        assert tool_to_module("scrape_airbnb_product") == "other_scrapers"
        assert tool_to_module("scrape_github_repository") == "other_scrapers"
        assert tool_to_module("scrape_walmart_product") == "other_scrapers"
        assert tool_to_module("unknown_tool_name") == "misc"

    def test_param_class_name_generation(self):
        """Verify PascalCase conversion for parameter class names."""
        from dataify_mcp._codegen._generate import _param_class_name

        assert _param_class_name("google_search") == "GoogleSearchParams"
        assert _param_class_name("query_user_info") == "QueryUserInfoParams"
        assert _param_class_name("scrape_youtube_video") == "ScrapeYoutubeVideoParams"
        assert _param_class_name("request_web_unlocker") == "RequestWebUnlockerParams"

    def test_method_name_is_tool_name(self):
        """Method name should be the same as tool name."""
        from dataify_mcp._codegen._generate import _method_name

        assert _method_name("google_search") == "google_search"
        assert _method_name("scrape_amazon_product") == "scrape_amazon_product"

    def test_sanitize_name_handles_special_chars(self):
        """Sanitize should handle non-standard Python identifier chars."""
        from dataify_mcp._codegen._generate import _sanitize_name

        # Valid names stay unchanged
        assert _sanitize_name("q") == "q"
        assert _sanitize_name("google_domain") == "google_domain"
        assert _sanitize_name("no_cache") == "no_cache"

    def test_json_schema_to_python_mapping(self):
        """Verify JSON Schema types map to Python types correctly."""
        from dataify_mcp._codegen._generate import _json_schema_to_python

        assert _json_schema_to_python({"type": "string"}) == "str"
        assert _json_schema_to_python({"type": "integer"}) == "int"
        assert _json_schema_to_python({"type": "number"}) == "float"
        assert _json_schema_to_python({"type": "boolean"}) == "bool"
        assert _json_schema_to_python({"type": "array"}) == "list[Any]"
        assert _json_schema_to_python({"type": "object"}) == "dict[str, Any]"
        # Enum constraints
        result = _json_schema_to_python({"type": "string", "enum": ["a", "b", "c"]})
        assert "Literal" in result
        # Nullable
        result = _json_schema_to_python({"type": ["string", "null"]})
        assert "None" in result
