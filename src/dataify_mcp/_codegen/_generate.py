"""Generate typed tool wrappers from a tool manifest.

Reads a tool manifest (list of ``{name, description, inputSchema}`` dicts)
and produces Pydantic models + convenience methods for each tool.
"""

from __future__ import annotations

import re
from pathlib import Path
from textwrap import dedent, indent
from typing import Any

# ---------------------------------------------------------------------------
# Mapping from tool name prefix → output module name
# ---------------------------------------------------------------------------
CATEGORY_MAP: list[tuple[str, str]] = [
    # Task status / statistics
    ("web_unlock_task", "task_status"),
    ("web_unlock_statistics", "task_status"),
    ("scraper_task_list", "task_status"),
    ("scraper_statistics", "task_status"),
    ("scraper_serp_products", "task_status"),
    ("scraper_serp_tools", "task_status"),
    # User management
    ("query_user_", "user"),
    # Web unlocker
    ("request_web_unlocker", "web_unlocker"),
    # Google SERP (use google_serp module)
    ("google_search", "google_serp"),
    ("google_ai_mode", "google_serp"),
    ("google_news", "google_serp"),
    ("google_images", "google_serp"),
    ("google_maps", "google_serp"),
    ("google_flights", "google_serp"),
    ("google_jobs", "google_serp"),
    ("google_local", "google_serp"),
    ("google_videos", "google_serp"),
    ("google_shopping", "google_serp"),
    ("google_trends", "google_serp"),
    ("google_play", "google_serp"),
    ("google_scholar", "google_serp"),
    ("google_finance", "google_serp"),
    ("google_hotels", "google_serp"),
    ("google_patents", "google_serp"),
    ("google_lens", "google_serp"),
    # Google scraper tools
    ("google_map_details", "google_scraper"),
    ("google_map_comment", "google_scraper"),
    ("google_shopping_info", "google_scraper"),
    ("google_play_store_information", "google_scraper"),
    ("google_play_store_reviews", "google_scraper"),
    # Bing
    ("bing_", "bing"),
    # Other search engines
    ("yandex_search", "other_search"),
    ("duckduckgo_search", "other_search"),
    # Amazon
    ("scrape_amazon_", "amazon"),
    # YouTube
    ("scrape_youtube_", "youtube"),
    # TikTok
    ("scrape_tiktok_", "tiktok"),
    # Facebook
    ("scrape_facebook_", "facebook"),
    # Instagram
    ("scrape_instagram_", "instagram"),
    # Reddit
    ("scrape_reddit_", "reddit"),
    # Twitter
    ("scrape_twitter_", "twitter"),
    # LinkedIn
    ("scrape_linkedin_", "linkedin"),
    # Glassdoor
    ("scrape_glassdoor_", "glassdoor"),
    # Indeed
    ("scrape_indeed_", "indeed"),
    # Other scrapers
    ("scrape_airbnb_", "other_scrapers"),
    ("scrape_booking_", "other_scrapers"),
    ("scrape_crunchbase_", "other_scrapers"),
    ("scrape_ebay_", "other_scrapers"),
    ("scrape_github_", "other_scrapers"),
    ("scrape_walmart_", "other_scrapers"),
    ("scrape_zillow_", "other_scrapers"),
]


def tool_to_module(tool_name: str) -> str:
    """Return the Python module name for a tool."""
    for prefix, module in CATEGORY_MAP:
        if tool_name.startswith(prefix):
            return module
    return "misc"


def generate_tool_modules(
    tools: list[dict[str, Any]],
    output_dir: str | Path,
) -> dict[str, list[str]]:
    """Generate tool wrapper modules from a tool manifest.

    Parameters
    ----------
    tools:
        Raw tool definitions from ``tools/list``.
    output_dir:
        Path to the ``tools/`` package directory.

    Returns
    -------
    dict[str, list[str]]
        Mapping from module name to list of tool names written.
    """
    output_dir = Path(output_dir)

    # Group tools by module
    grouped: dict[str, list[dict[str, Any]]] = {}
    for tool in tools:
        name = tool["name"]
        module = tool_to_module(name)
        grouped.setdefault(module, []).append(tool)

    written: dict[str, list[str]] = {}

    for module_name, module_tools in grouped.items():
        module_path = output_dir / f"{module_name}.py"
        content = _render_module(module_name, module_tools)
        module_path.write_text(content, encoding="utf-8")
        written[module_name] = [t["name"] for t in module_tools]

    return written


# ---------------------------------------------------------------------------
# Module rendering
# ---------------------------------------------------------------------------


def _render_module(module_name: str, tools: list[dict[str, Any]]) -> str:
    """Render a single tool module."""
    lines: list[str] = []
    lines.append('"""Auto-generated tool wrappers.  Do not edit by hand.')
    lines.append("")
    lines.append("Regenerate with: python scripts/codegen.py")
    lines.append('"""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from typing import Any, Literal")
    lines.append("")
    lines.append("from pydantic import BaseModel, Field")
    lines.append("")
    lines.append("")

    # Parameter models
    for tool in tools:
        lines.extend(_render_param_model(tool))
        lines.append("")

    # Convenience methods (as mixin or standalone)
    for tool in tools:
        lines.extend(_render_method(tool))
        lines.append("")

    return "\n".join(lines)


def _render_param_model(tool: dict[str, Any]) -> list[str]:
    """Render a Pydantic BaseModel for a tool's inputSchema."""
    name = tool["name"]
    schema = tool.get("inputSchema", {})
    description = tool.get("description", "").replace('"', '\\"')
    class_name = _param_class_name(name)

    required: set[str] = set(schema.get("required", []))
    properties: dict[str, dict[str, Any]] = schema.get("properties", {})

    lines: list[str] = []
    lines.append(f"class {class_name}(BaseModel):")
    lines.append(f'    """Parameters for the ``{name}`` tool.')

    if description:
        # Word-wrap the description
        desc = description.replace("\n", " ")
        while len(desc) > 70:
            split = desc.rfind(" ", 0, 70)
            if split == -1:
                split = 70
            lines.append(f"")
            lines.append(f"    {desc[:split]}")
            desc = desc[split:].strip()
        if desc:
            lines.append(f"")
            lines.append(f"    {desc}")
    lines.append(f'    """')

    if not properties:
        lines.append("    pass")
        return lines

    for prop_name, prop_schema in properties.items():
        field_args = _build_field_args(prop_name, prop_schema, prop_name in required)
        py_name = _sanitize_name(prop_name)
        lines.append(f"    {py_name}: {field_args}")

    return lines


def _render_method(tool: dict[str, Any]) -> list[str]:
    """Render a convenience method for DataifyClient."""
    name = tool["name"]
    description = tool.get("description", "").replace('"', '\\"')
    properties = tool.get("inputSchema", {}).get("properties", {})
    class_name = _param_class_name(name)
    method_name = _method_name(name)

    lines: list[str] = []
    if description:
        lines.append(f'    # {description[:90]}')

    if properties:
        lines.append(f"    async def {method_name}(self, params: {class_name} | None = None) -> Any:")
        lines.append(f'        """Call ``{name}``.')
        if description:
            lines.append(f"")
            lines.append(f"        {description}")
        lines.append(f'        """')
        lines.append(f"        arguments = params.model_dump(exclude_none=True) if params else {{}}")
        lines.append(f'        return await self.call_tool("{name}", arguments)')
    else:
        # No-parameter tool
        lines.append(f"    async def {method_name}(self) -> Any:")
        lines.append(f'        """Call ``{name}``.')
        if description:
            lines.append(f"")
            lines.append(f"        {description}")
        lines.append(f'        """')
        lines.append(f'        return await self.call_tool("{name}", {{}})')

    return lines


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _param_class_name(tool_name: str) -> str:
    """Convert tool name to PascalCase param class, e.g. google_search → GoogleSearchParams."""
    parts = tool_name.split("_")
    return "".join(p.capitalize() for p in parts) + "Params"


def _method_name(tool_name: str) -> str:
    """Tool name is already a valid Python identifier. Just ensure it's snake_case."""
    return tool_name


def _sanitize_name(name: str) -> str:
    """Sanitize a parameter name for use as a Python identifier.

    JSON Schema property names can contain characters that aren't valid in
    Python.  We keep the original name as the Pydantic field's alias and
    produce a safe Python name.
    """
    # Replace common problematic chars
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    if safe[0].isdigit():
        safe = "f_" + safe
    # Python keywords
    if safe in ("from", "import", "class", "def", "return", "if", "else", "elif",
                "while", "for", "try", "except", "finally", "with", "as", "pass",
                "break", "continue", "raise", "yield", "lambda", "global", "nonlocal",
                "del", "in", "not", "and", "or", "is", "True", "False", "None",
                "async", "await"):
        safe = safe + "_"
    return safe


def _build_field_args(prop_name: str, prop_schema: dict[str, Any], is_required: bool) -> str:
    """Build the Pydantic Field(...) arguments string for a property."""
    py_type = _json_schema_to_python(prop_schema)
    description = prop_schema.get("description", "").replace('"', '\\"').replace("\n", " ")
    default = prop_schema.get("default")

    parts: list[str] = []

    # Type annotation
    if is_required:
        parts.append(py_type)
    elif default is not None:
        parts.append(f"{py_type} = Field({repr(default)}")
    else:
        parts.append(f"{py_type} | None = Field(default=None")

    if "default" in prop_schema and not is_required:
        # already included above
        pass
    elif not is_required and default is None and not parts[0].startswith(py_type + " | None"):
        # Already handled above
        pass

    # Description
    if description:
        if "=" in parts[0]:
            parts.append(f", description={repr(description)}")
        else:
            parts.append(f" = Field(..., description={repr(description)}")

    # Enum → Literal
    if "enum" in prop_schema and "Literal" not in py_type:
        # Already handled by _json_schema_to_python
        pass

    # Close the Field() call
    field_started = any("Field(" in p for p in parts)
    if field_started:
        joined = "".join(parts)
        if not joined.rstrip().endswith(")"):
            joined += ")"
        return joined

    return "".join(parts)


def _json_schema_to_python(schema: dict[str, Any]) -> str:
    """Map a JSON Schema property to a Python type annotation string."""
    # Handle enum constraints
    if "enum" in schema:
        values = ", ".join(repr(v) for v in schema["enum"])
        return f"Literal[{values}]"

    type_map = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "array": "list[Any]",
        "object": "dict[str, Any]",
    }

    json_type = schema.get("type", "string")

    # Handle {type: [..., "null"]} → Optional
    if isinstance(json_type, list):
        non_null = [t for t in json_type if t != "null"]
        if len(non_null) == 1:
            base = type_map.get(non_null[0], "Any")
            return f"{base} | None"
        return "Any | None"

    return type_map.get(json_type, "Any")
