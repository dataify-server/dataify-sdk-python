"""Generate the ``dataify_sdk`` tool layer from the Go reference project.

The Go project (``C:\\dataify\\dataify_mcp_api``) exposes every capability as an
MCP tool whose ``tool.go`` declares, with rich descriptions:

* the upstream request parameters (``mcp.WithString`` / ``WithNumber`` / ...),
* the ``spider_name`` / ``spider_id`` constants (Scraper / platform tools), or
* the engine + request struct (search-engine tools).

This script parses those ``tool.go`` files (and the matching service request
structs) and emits, for **every** ``spider_id`` (Scraper tools) or engine
(search tools), a standalone, fully-typed Python function whose signature and
docstring expose every upstream parameter and its description.  It also writes
a Markdown parameter manual (``docs/api_reference.md``).

Run::

    python -m dataify_sdk._codegen.generate

The output is intentionally dependency-free and deterministic.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
REPO = Path(r"C:/dataify/dataify_mcp_api")
TOOLS_DIR = REPO / "internal" / "tools"
SERVICE_DIR = REPO / "internal" / "service"

OUT_TOOLS = HERE.parent / "tools"
OUT_DOCS = HERE.parent.parent.parent / "docs" / "api_reference.md"

# Tools that talk to a database / are infrastructure / are empty helpers.
EXCLUDED = {"auth", "result", "webunlocker", "zillowprice"}

# Python keywords + names that would shadow imports / builtins when used as a
# parameter name.
_RESERVED = {
    "json", "type", "id", "file", "dict", "list", "str", "int", "float",
    "bool", "from", "import", "class", "def", "return", "if", "else", "elif",
    "while", "for", "try", "except", "finally", "with", "as", "pass", "break",
    "continue", "raise", "yield", "lambda", "global", "nonlocal", "del", "in",
    "not", "and", "or", "is", "async", "await", "None", "True", "False",
}


# ---------------------------------------------------------------------------
# Small parsing helpers
# ---------------------------------------------------------------------------
def balanced(text: str, start: int) -> tuple[str, int]:
    """Return the bracketed content starting at ``text[start]``.

    The opener may be ``(`` or ``{``; the matching closer is used.  String
    literals are skipped so brackets inside quotes do not confuse the scan.

    Returns ``(inner, index_after_close)``.
    """
    opener = text[start]
    assert opener in "({"
    closer = ")" if opener == "(" else "}"
    depth = 0
    i = start
    n = len(text)
    while i < n:
        ch = text[i]
        if ch == '"':
            # skip string literals (handles escaped quotes)
            i += 1
            while i < n:
                if text[i] == "\\":
                    i += 2
                    continue
                if text[i] == '"':
                    i += 1
                    break
                i += 1
            continue
        if ch == opener:
            depth += 1
        elif ch == closer:
            depth -= 1
            if depth == 0:
                return text[start + 1 : i], i + 1
        i += 1
    raise ValueError("unbalanced brackets")


def split_top(text: str, sep: str = ",") -> list[str]:
    """Split ``text`` on ``sep`` ignoring separators inside () or {}."""
    out: list[str] = []
    depth = 0
    cur = ""
    for ch in text:
        if ch in "([":
            depth += 1
            cur += ch
        elif ch in ")]":
            depth -= 1
            cur += ch
        elif ch == "{" :
            depth += 1
            cur += ch
        elif ch == "}":
            depth -= 1
            cur += ch
        elif ch == sep and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


def sanitize(name: str) -> str:
    """Make a Go / upstream field name a safe Python identifier."""
    safe = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    if safe and safe[0].isdigit():
        safe = "f_" + safe
    if safe in _RESERVED:
        safe = safe + "_"
    return safe


def parse_string_consts(txt: str) -> dict[str, str]:
    """Collect ``NAME = "value"`` and ``NAME = "value"`` inside const blocks."""
    consts: dict[str, str] = {}
    for m in re.finditer(r'([A-Za-z_]\w*)\s*=\s*"((?:[^"\\]|\\.)*)"', txt):
        consts[m.group(1)] = m.group(2)
    return consts


def parse_struct_map() -> dict[str, dict[str, str]]:
    """Map each ``*Request`` struct to ``{field: json_tag}``."""
    structs: dict[str, dict[str, str]] = {}
    if not SERVICE_DIR.exists():
        return structs
    for f in SERVICE_DIR.glob("*.go"):
        txt = f.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"type\s+(\w+Request)\s+struct\s*\{(.*?)\n\}", txt, re.S):
            name = m.group(1)
            body = m.group(2)
            fields: dict[str, str] = {}
            for line in body.splitlines():
                fm = re.match(r"\s*([A-Za-z_]\w*)\s+\w+\s+`json:\"([^\"]*)\"`", line)
                if fm:
                    fields[fm.group(1)] = fm.group(2).split(",")[0]
            structs[name] = fields
    return structs


# ---------------------------------------------------------------------------
# Parameter / variant extraction
# ---------------------------------------------------------------------------
def parse_mcp_params(newtool_block: str) -> list[dict[str, Any]]:
    """Extract ``mcp.WithString`` parameters from the NewTool(...) block."""
    params: list[dict[str, Any]] = []
    for wm in re.finditer(r"mcp\.With(String|Number|Boolean)\(\s*\"([^\"]+)\"", newtool_block):
        ptype = wm.group(1)
        pname = wm.group(2)
        # grab the argument slice for this WithX call
        paren_idx = newtool_block.index("(", wm.start())
        _, end = balanced(newtool_block, paren_idx)
        body = newtool_block[wm.start() : end]
        required = "Required()" in body
        dm = re.search(r'Description\(\s*"((?:[^"\\]|\\.)*)"', body)
        desc = dm.group(1) if dm else ""
        default: str | None = None
        if "DefaultString(" in body:
            dsm = re.search(r'DefaultString\(\s*"((?:[^"\\]|\\.)*)"', body)
            default = dsm.group(1) if dsm else ""
        elif "DefaultInt(" in body:
            dim = re.search(r"DefaultInt\(\s*(\d+)", body)
            default = dim.group(1) if dim else None
        elif "DefaultBool(" in body:
            dbm = re.search(r"DefaultBool\(\s*(true|false)", body)
            default = dbm.group(1) if dbm else None
        params.append(
            {
                "name": pname,
                "type": ptype,
                "desc": desc,
                "default": default,
                "required": required,
            }
        )
    return params


def _getstring_default(expr: str, consts: dict[str, str]) -> tuple[str | None, str | None]:
    """From a Go expression return (mcp_param_name, effective_default).

    Handles both ``request.GetString("x", "d")`` and
    ``nonEmpty(request.GetString("x", C), F)`` where ``C``/``F`` may be string
    literals or package-level constants (resolved via ``consts``).
    """
    if not expr:
        return None, None
    gm = re.search(r'GetString\(\s*"(\w+)"\s*(?:,\s*([^)]*?))?\)', expr)
    if not gm:
        return None, None
    name = gm.group(1)
    arg2 = (gm.group(2) or "").strip()
    default: str | None = None
    if arg2:
        if arg2.startswith('"'):
            default = arg2.strip('"')
        else:
            default = consts.get(arg2)  # resolve a constant
    # nonEmpty(value, fallback) — fallback wins when GetString default is empty
    nm = re.search(r"nonEmpty\(\s*[^,]+,\s*([^)]*?)\)", expr)
    if nm:
        fb = nm.group(1).strip()
        if default in (None, ""):
            if fb.startswith('"'):
                default = fb.strip('"')
            else:
                default = consts.get(fb)
    return name, default


def _map_literal_keys(block: str, open_idx: int) -> list[tuple[str, str]]:
    """Parse a ``map[string]string{ "k": expr, ... }`` returning (key, expr)."""
    content, _ = balanced(block, open_idx)
    pairs: list[tuple[str, str]] = []
    for part in split_top(content):
        if ":" not in part:
            continue
        key, _, expr = part.partition(":")
        key = key.strip().strip('"')
        pairs.append((key, expr.strip()))
    return pairs


def parse_scraper_variants(txt: str, consts: dict[str, str]) -> list[dict[str, Any]]:
    """Return one variant per spider_id with its parameter set."""
    # spider_name
    sn_ref = re.search(r"SpiderName:\s*(\w+)", txt)
    spider_name = consts.get(sn_ref.group(1), "") if sn_ref else ""

    variants: list[dict[str, Any]] = []

    if "func buildSpiderParameters" in txt:
        # Multi-spider: parse the switch cases.
        fn = re.search(r"func buildSpiderParameters\(.*?\{(.*?)\n\}", txt, re.S)
        body = fn.group(1) if fn else ""
        # locate each `case spiderX:` then the returned map
        for cm in re.finditer(r"case\s+(\w+)\s*:", body):
            label = cm.group(1)
            # region until next case or end
            nxt = re.search(r"case\s+\w+\s*:", body[cm.end():])
            region = body[cm.end() : cm.end() + nxt.start()] if nxt else body[cm.end():]
            keys = _collect_param_keys(region, txt)
            variants.append(
                {
                    "spider_id": consts.get(label, label),
                    "spider_name": spider_name,
                    "keys": keys,
                }
            )
        # also handle default case if present
        if not variants:
            pass
    else:
        # Single inline spider: find the SpiderID const and the inline map.
        sid_ref = re.search(r"SpiderID:\s*(\w+)", txt)
        spider_id = consts.get(sid_ref.group(1), "") if sid_ref else ""
        # find BuildSingleSpiderParameters(map[string]string{ ... })
        mm = re.search(r"BuildSingleSpiderParameters\(\s*map\[string\]string\{", txt)
        keys: list[tuple[str, str]] = []
        if mm:
            keys = _map_literal_keys(txt, mm.end() - 1)
        else:
            # fallback: any map[string]string{ literal (params := ... then built)
            mm2 = re.search(r"map\[string\]string\{", txt)
            if mm2:
                keys = _map_literal_keys(txt, mm2.end() - 1)
        variants.append(
            {"spider_id": spider_id, "spider_name": spider_name, "keys": keys}
        )

    return variants


def _collect_param_keys(region: str, txt: str) -> list[tuple[str, str]]:
    """Collect spider_parameters keys for a variant region.

    Handles both an inline ``return map[string]string{...}`` (or
    ``params := map[string]string{...}``) and the ``params["k"] = ...``
    conditional assignments.
    """
    keys: list[tuple[str, str]] = []
    seen: set[str] = set()
    rm = re.search(r"map\[string\]string\{", region)
    if rm:
        keys = _map_literal_keys(region, rm.end() - 1)
        seen = {k for k, _ in keys}
    # conditional assignments
    for am in re.finditer(r'params\[\s*"(\w+)"\s*\]\s*=', region):
        k = am.group(1)
        if k not in seen:
            keys.append((k, ""))
            seen.add(k)
    return keys


def parse_serp(txt: str, struct_map: dict[str, dict[str, str]]) -> dict[str, Any]:
    """Extract engine + parameter mapping for a search-engine tool."""
    engine_m = re.search(r"Engine:\s*\"([^\"]+)\"", txt)
    engine = engine_m.group(1) if engine_m else ""
    struct_m = re.search(r"service\.(\w+Request)\{", txt)
    struct_name = struct_m.group(1) if struct_m else ""
    json_tags = struct_map.get(struct_name, {})

    # map mcp param name -> struct field (from handler assignments)
    # e.g. Query: request.GetString("q", "pizza")
    assign: dict[str, str] = {}
    for am in re.finditer(r"(\w+)\s*:\s*request\.GetString\(\s*\"(\w+)\"", txt):
        assign[am.group(2)] = am.group(1)

    params: list[dict[str, Any]] = []
    # we re-parse mcp params from the whole file block passed in separately
    return {
        "engine": engine,
        "struct": struct_name,
        "json_tags": json_tags,
        "assign": assign,
        "params": params,  # filled by caller
    }


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def _render_signature(func_name: str, sig_params: list[dict[str, Any]]) -> str:
    """Build the Python function signature line."""
    parts = [f"def {func_name}("]
    # required first, then optional, then client
    ordered = sorted(sig_params, key=lambda p: (p["default"] is not None, p["py"]))
    args = []
    for p in ordered:
        py = p["py"]
        if p["default"] is None:
            args.append(f"{py}: str")
        else:
            args.append(f'{py}: str = {p["default"]!r}')
    args.append("client: DataifyClient | None = None")
    return "def " + func_name + "(" + ", ".join(args) + ") -> dict[str, Any]:"


def _doc_param_line(p: dict[str, Any], upstream: str) -> str:
    if p["default"] is None:
        flag = "必填"
    elif p["default"] == "":
        flag = "默认: (空)"
    else:
        flag = f"默认: {p['default']}"
    tag = "" if upstream == p["py"] else f" (上游字段: {upstream})"
    return f"    {p['py']}: {p['desc']}  [{flag}]{tag}"


def render_scraper_function(
    func_name: str,
    variant: dict[str, Any],
    mcp_by_name: dict[str, dict[str, Any]],
    consts: dict[str, str],
    tool_desc: str,
) -> str:
    spider_id = variant["spider_id"]
    spider_name = variant["spider_name"]
    sig_params: list[dict[str, Any]] = []
    body_assign: list[str] = []
    for key, expr in variant["keys"]:
        # determine mcp param name + default from expr
        mcp_name, getdefault = _getstring_default(expr, consts)
        lookup = mcp_name or key
        info = mcp_by_name.get(lookup, {})
        desc = info.get("desc", "") or f"上游参数 {key}"
        # default precedence: GetString default > mcp default > "" (optional)
        required = info.get("required", False)
        default = getdefault
        if default is None:
            default = info.get("default")
        if default is None and not required:
            # Optional param whose default the generator could not recover
            # (e.g. an intermediate normalizeXxx()/computed variable). An empty
            # string is dropped at send time, so the upstream applies its own
            # per-variant fallback default — behaviour matches the other
            # optional params, which already default to "".
            default = ""
        py = sanitize(key)
        sig_params.append(
            {
                "py": py,
                "upstream": key,
                "desc": desc,
                "default": default,
                "required": required,
            }
        )
        body_assign.append(f'        "{key}": {py},')

    # add file_name (Builder-level)
    sig_params.append(
        {
            "py": "file_name",
            "upstream": "file_name",
            "desc": "Builder file_name 字段。不传默认为 {{TasksID}}。",
            "default": "{{TasksID}}",
            "required": False,
        }
    )

    sig = _render_signature(func_name, sig_params)
    doc = [
        f'    """{tool_desc}',
        "",
        "    上游接口: Scraper Builder (POST /builder?platform=1)",
        f"    spider_name: {spider_name}",
        f"    spider_id: {spider_id}",
        "",
        "    Parameters",
        "    ----------",
    ]
    for p in sig_params:
        doc.append(_doc_param_line(p, p["upstream"]))
    doc.append("    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。")
    doc.append('    """')
    doc.append("    params_obj = {")
    doc.extend(body_assign)
    doc.append("    }")
    doc.append("    spider_parameters = json.dumps([params_obj], ensure_ascii=False)")
    doc.append("    return _client(client).request_scraper(")
    doc.append(f'        spider_name={spider_name!r},')
    doc.append(f'        spider_id={spider_id!r},')
    doc.append("        spider_parameters=spider_parameters,")
    doc.append("        file_name=file_name,")
    doc.append("    )")
    return sig + "\n" + "\n".join(doc) + "\n"


def render_serp_function(
    func_name: str,
    serp: dict[str, Any],
    mcp_params: list[dict[str, Any]],
) -> str:
    assign = serp["assign"]
    json_tags = serp["json_tags"]
    engine = serp["engine"]

    sig_params: list[dict[str, Any]] = []
    body_assign: list[str] = []
    for mp in mcp_params:
        name = mp["name"]
        field = assign.get(name)  # struct field name
        form_key = json_tags.get(field, name) if field else name
        py = sanitize(name)
        required = mp.get("required", False)
        default = mp["default"]
        if default is None and not required:
            default = ""
        sig_params.append(
            {
                "py": py,
                "upstream": form_key,
                "desc": mp["desc"] or f"上游参数 {form_key}",
                "default": default,
                "required": required,
            }
        )
        body_assign.append(f'        "{form_key}": {py},')

    sig = _render_signature(func_name, sig_params)
    doc = [
        f'    """{mcp_params[0]["desc"] if mcp_params else "Search tool"}',
        "",
        "    上游接口: Search Engine (POST /request)",
        f"    engine: {engine}",
        "",
        "    Parameters",
        "    ----------",
    ]
    for p in sig_params:
        doc.append(_doc_param_line(p, p["upstream"]))
    doc.append("    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。")
    doc.append('    """')
    doc.append("    form = {")
    doc.extend(body_assign)
    doc.append("    }")
    doc.append(f'    return _client(client).request_serp(engine={engine!r}, fields=form)')
    return sig + "\n" + "\n".join(doc) + "\n"


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
MODULE_HEADER = '''"""Auto-generated Dataify tool functions.  Do not edit by hand.

Generated from the Go reference project by ``dataify_sdk._codegen.generate``.
Each function calls the Dataify upstream REST API directly (no MCP layer).
"""

from __future__ import annotations

import json
from typing import Any

from dataify_sdk.client import DataifyClient, get_default_client


def _client(client: DataifyClient | None) -> DataifyClient:
    return client if client is not None else get_default_client()

'''


def process_tool(tool_dir: Path, struct_map: dict[str, dict[str, str]]) -> dict[str, Any] | None:
    go_files = list(tool_dir.glob("*.go"))
    if not go_files:
        return None
    txt = "\n".join(f.read_text(encoding="utf-8", errors="ignore") for f in go_files)
    consts = parse_string_consts(txt)

    # backend detection
    if "ScraperBuilderService" in txt:
        backend = "scraper"
    elif "GoogleSearchService" in txt:
        backend = "google"
    elif "BingSearchService" in txt:
        backend = "bing"
    elif "YandexSearchService" in txt:
        backend = "yandex"
    elif "DuckDuckGoSearchService" in txt:
        backend = "duckduckgo"
    else:
        return None

    # NewTool block for mcp params + tool description
    ntm = re.search(r"mcp\.NewTool\(", txt)
    newtool_block = ""
    tool_name = tool_dir.name
    tool_desc = ""
    if ntm:
        inner, _ = balanced(txt, ntm.end() - 1)
        newtool_block = inner
        tnm = re.search(r'NewTool\(\s*"([^"]+)"', inner)
        if tnm:
            tool_name = tnm.group(1)
        tdm = re.search(r'WithDescription\(\s*"((?:[^"\\]|\\.)*)"', inner)
        if tdm:
            tool_desc = tdm.group(1)

    mcp_params = parse_mcp_params(newtool_block)
    mcp_by_name = {p["name"]: p for p in mcp_params}

    # tool name + description (search the whole file; the inner block no longer
    # contains the leading `NewTool("..."` token)
    tnm = re.search(r'mcp\.NewTool\(\s*"([^"]+)"', txt)
    if tnm:
        tool_name = tnm.group(1)
    tdm = re.search(r'WithDescription\(\s*"((?:[^"\\]|\\.)*)"', txt)
    if tdm:
        tool_desc = tdm.group(1)

    functions: list[str] = []
    docs: list[dict[str, Any]] = []

    if backend == "scraper":
        variants = parse_scraper_variants(txt, consts)
        for v in variants:
            if not v["spider_id"]:
                continue
            func_name = sanitize(v["spider_id"].replace("-", "_"))
            code = render_scraper_function(func_name, v, mcp_by_name, consts, tool_desc)
            functions.append(code)
            docs.append(
                {
                    "func": func_name,
                    "backend": "scraper",
                    "spider_name": v["spider_name"],
                    "spider_id": v["spider_id"],
                    "engine": "",
                    "desc": tool_desc,
                    "params": _variant_doc_params(v, mcp_by_name, consts),
                }
            )
    else:
        serp = parse_serp(txt, struct_map)
        serp["params"] = mcp_params
        func_name = sanitize(tool_name)
        code = render_serp_function(func_name, serp, mcp_params)
        functions.append(code)
        docs.append(
            {
                "func": func_name,
                "backend": backend,
                "spider_name": "",
                "spider_id": "",
                "engine": serp["engine"],
                "desc": tool_desc,
                "params": [
                    {
                        "py": sanitize(p["name"]),
                        "upstream": serp["assign"].get(p["name"], p["name"]),
                        "desc": p["desc"],
                        "default": p["default"],
                        "required": p.get("required", False) and p["default"] is None,
                    }
                    for p in mcp_params
                ],
            }
        )

    if not functions:
        return None

    module_name = tool_dir.name
    module_path = OUT_TOOLS / f"{module_name}.py"
    content = MODULE_HEADER + "\n\n".join(functions) + "\n"
    module_path.write_text(content, encoding="utf-8")

    return {
        "module": module_name,
        "tool": tool_name,
        "backend": backend,
        "functions": [f.split("(")[0].replace("def ", "").strip() for f in functions],
        "docs": docs,
    }


def _variant_doc_params(variant, mcp_by_name, consts) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for key, expr in variant["keys"]:
        mcp_name, getdefault = _getstring_default(expr, consts)
        lookup = mcp_name or key
        info = mcp_by_name.get(lookup, {})
        default = getdefault if getdefault is not None else info.get("default")
        out.append(
            {
                "py": sanitize(key),
                "upstream": key,
                "desc": info.get("desc", "") or f"上游参数 {key}",
                "default": default,
                "required": info.get("required", False) and default is None,
            }
        )
    out.append(
        {
            "py": "file_name",
            "upstream": "file_name",
            "desc": "Builder file_name 字段。不传默认为 {{TasksID}}。",
            "default": "{{TasksID}}",
            "required": False,
        }
    )
    return out


def render_markdown(index: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# Dataify SDK — API 参数手册")
    lines.append("")
    lines.append(
        "本手册由 `dataify_sdk._codegen.generate` 从 Go 参考项目自动生成。"
        "每个函数**直接调用 Dataify 上游 REST 接口**(不走 MCP),"
        "下列参数均为该函数暴露的上游请求参数及其描述。"
    )
    lines.append("")
    n_tools = len(index)
    n_funcs = sum(len(d["functions"]) for d in index)
    lines.append(f"- 工具模块数: {n_tools}")
    lines.append(f"- 生成函数数: {n_funcs}")
    lines.append("")
    lines.append("## 目录")
    lines.append("")
    for d in index:
        for fn in d["docs"]:
            anchor = fn["func"].replace("_", "-")
            lines.append(f"- [{fn['func']}](#{anchor})")
    lines.append("")

    for d in index:
        for fn in d["docs"]:
            lines.append(f"## {fn['func']}")
            lines.append("")
            lines.append(fn["desc"])
            lines.append("")
            if fn["backend"] == "scraper":
                lines.append(f"- 上游接口: Scraper Builder (`POST /builder?platform=1`)")
                lines.append(f"- spider_name: `{fn['spider_name']}`")
                lines.append(f"- spider_id: `{fn['spider_id']}`")
            else:
                lines.append(f"- 上游接口: Search Engine (`POST /request`)")
                lines.append(f"- engine: `{fn['engine']}`")
            lines.append("")
            lines.append("| Python 参数 | 上游字段 | 必填 | 默认值 | 说明 |")
            lines.append("| --- | --- | --- | --- | --- |")
            for p in fn["params"]:
                req = "是" if p["required"] else "否"
                if p["default"] is None:
                    default = "—"
                elif p["default"] == "":
                    default = "—(空)"
                else:
                    default = f"`{p['default']}`"
                desc = (p["desc"] or "").replace("|", "\\|").replace("\n", " ")
                upstream = p["upstream"] if p["upstream"] != p["py"] else f"`{p['upstream']}`"
                lines.append(
                    f"| `{p['py']}` | {upstream} | {req} | {default} | {desc} |"
                )
            lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    OUT_TOOLS.mkdir(parents=True, exist_ok=True)
    if not TOOLS_DIR.exists():
        print(f"ERROR: Go reference project not found at {TOOLS_DIR}", file=sys.stderr)
        return 1

    struct_map = parse_struct_map()

    index: list[dict[str, Any]] = []
    skipped: list[str] = []
    errors: list[str] = []

    for d in sorted(TOOLS_DIR.iterdir()):
        if not d.is_dir() or d.name in EXCLUDED:
            continue
        try:
            result = process_tool(d, struct_map)
            if result:
                index.append(result)
                print(f"  ok   {d.name:28s} -> {len(result['functions'])} func(s)")
            else:
                skipped.append(d.name)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{d.name}: {exc}")
            print(f"  FAIL {d.name:28s}: {exc}", file=sys.stderr)

    # tools/__init__.py
    init_lines = ['"""Generated Dataify tool modules."""', "", "from __future__ import annotations", ""]
    all_funcs: list[str] = []
    for r in index:
        funcs = ", ".join(r["functions"])
        all_funcs.extend(r["functions"])
        init_lines.append(f"from dataify_sdk.tools.{r['module']} import {funcs}")
    init_lines.append("")
    init_lines.append("__all__ = [")
    for fn in all_funcs:
        init_lines.append(f"    {fn!r},")
    init_lines.append("]")
    (OUT_TOOLS / "__init__.py").write_text("\n".join(init_lines) + "\n", encoding="utf-8")

    # markdown manual
    OUT_DOCS.parent.mkdir(parents=True, exist_ok=True)
    OUT_DOCS.write_text(render_markdown(index), encoding="utf-8")

    print("\n==== SUMMARY ====")
    print(f"tools generated : {len(index)}")
    print(f"functions       : {sum(len(r['functions']) for r in index)}")
    print(f"skipped         : {skipped}")
    print(f"errors          : {errors}")
    print(f"docs            : {OUT_DOCS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
