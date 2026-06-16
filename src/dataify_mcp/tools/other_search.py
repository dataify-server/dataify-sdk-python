"""Other search engine tools.

Wraps Yandex and DuckDuckGo search tools.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# yandex_search
# ---------------------------------------------------------------------------


class YandexSearchParams(BaseModel):
    """Parameters for ``yandex_search`` — Yandex 网页搜索。

    通过 Yandex 搜索公开网页信息，按关键词、地区、语言等条件获取结果。
    """

    model_config = {"protected_namespaces": ()}

    text: str = Field(default="", description="搜索查询内容")
    json: str | None = Field(default="1", description="输出格式: 1 JSON, 2 JSON+HTML, 3 HTML, 4 Light JSON")
    yandex_domain: str | None = Field(default="yandex.com", description="Yandex 域名")
    lang: str | None = Field(default="en", description="搜索语言")
    lr: str | None = Field(default="", description="限制搜索的国家或地区 ID")
    p: str | None = Field(default="0", description="页码，从 0 开始")
    family_mode: str | None = Field(default="1", description="家庭模式: 0 关闭, 1 中等, 2 严格")
    fix_typo: str | None = Field(default="true", description="自动拼写纠正: true/false")
    groups_on_page: str | None = Field(default="10", description="单页最大群组数")
    no_cache: str | None = Field(default="false", description="是否跳过缓存")


async def yandex_search(self, params: YandexSearchParams | None = None) -> Any:
    """Call ``yandex_search`` — Yandex 网页搜索。

    通过 Yandex 搜索公开网页信息，按关键词、地区、语言等条件获取搜索结果。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("yandex_search", arguments)


# ---------------------------------------------------------------------------
# duckduckgo_search
# ---------------------------------------------------------------------------


class DuckDuckGoSearchParams(BaseModel):
    """Parameters for ``duckduckgo_search`` — DuckDuckGo 网页搜索。

    通过 DuckDuckGo 搜索公开网页信息，获取隐私搜索结果。
    """

    model_config = {"protected_namespaces": ()}

    q: str = Field(default="Pizza", description="搜索查询内容")
    json: str | None = Field(default="1", description="输出格式: 1 JSON, 2 JSON+HTML, 3 HTML, 4 Light JSON")
    kl: str | None = Field(default="", description="地区代码，如 us-en, uk-en, fr-fr")
    search_assist: str | None = Field(default="false", description="AI 搜索辅助: true/false")
    safe: str | None = Field(default="-1", description="成人内容过滤: 1 严格, -1 中等, -2 关闭")
    df: str | None = Field(default="", description="日期过滤: d/w/m/y 或 start_date..end_date")
    start: str | None = Field(default="0", description="结果偏移量")
    m: str | None = Field(default="10", description="最大结果数 (1-50)")
    no_cache: str | None = Field(default="false", description="是否跳过缓存")


async def duckduckgo_search(self, params: DuckDuckGoSearchParams | None = None) -> Any:
    """Call ``duckduckgo_search`` — DuckDuckGo 网页搜索。

    通过 DuckDuckGo 搜索公开网页信息，获取隐私搜索结果。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("duckduckgo_search", arguments)


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all other search engine methods to the client class."""
    client_cls.yandex_search = yandex_search
    client_cls.duckduckgo_search = duckduckgo_search
