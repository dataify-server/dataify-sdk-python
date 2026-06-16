"""Bing search tools.

Wraps all Bing search variant MCP tools: search, images, maps, news,
shopping, and videos.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# bing_search
# ---------------------------------------------------------------------------


class BingSearchParams(BaseModel):
    """Parameters for ``bing_search`` — Bing 网页搜索。

    通过 Bing 搜索公开网页信息，按位置、国家/地区、语言等条件获取结果。
    """

    model_config = {"protected_namespaces": ()}

    q: str = Field(default="Pizza", description="搜索查询内容")
    json: str | None = Field(default="1", description="输出格式: 1 JSON, 2 JSON+HTML, 3 HTML, 4 Light JSON")
    location: str | None = Field(default="", description="搜索发起的地理位置")
    lat: str | None = Field(default="", description="GPS 纬度")
    lon: str | None = Field(default="", description="GPS 经度")
    mkt: str | None = Field(default="", description="显示语言 <语言代码>-<国家/地区代码>，如 en-US")
    cc: str | None = Field(default="", description="国家/地区代码 (两位)")
    first: str | None = Field(default="0", description="结果偏移量")
    safeSearch: str | None = Field(default="", description="成人内容过滤: Off, Moderate, Strict")
    filters: str | None = Field(default="", description="高级过滤选项")
    no_cache: str | None = Field(default="false", description="是否跳过缓存")


async def bing_search(self, params: BingSearchParams | None = None) -> Any:
    """Call ``bing_search`` — Bing 网页搜索。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("bing_search", arguments)


# ---------------------------------------------------------------------------
# bing_images
# ---------------------------------------------------------------------------


class BingImagesParams(BaseModel):
    """Parameters for ``bing_images`` — Bing 图片搜索。"""

    model_config = {"protected_namespaces": ()}

    q: str = Field(default="Pizza", description="搜索查询内容")
    json: str | None = Field(default="1", description="输出格式")
    mkt: str | None = Field(default="", description="显示语言")
    cc: str | None = Field(default="", description="国家/地区代码")
    first: str | None = Field(default="0", description="结果偏移量")
    safeSearch: str | None = Field(default="", description="成人内容过滤")
    no_cache: str | None = Field(default="false", description="是否跳过缓存")


async def bing_images(self, params: BingImagesParams | None = None) -> Any:
    """Call ``bing_images`` — Bing 图片搜索。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("bing_images", arguments)


# ---------------------------------------------------------------------------
# bing_maps, bing_news, bing_shopping, bing_videos
# ---------------------------------------------------------------------------


class _BingVariantParams(BaseModel):
    """Shared params for Bing variants (maps, news, shopping, videos)."""

    model_config = {"protected_namespaces": ()}

    q: str = Field(default="Pizza", description="搜索查询内容")
    json: str | None = Field(default="1", description="输出格式")
    mkt: str | None = Field(default="", description="显示语言")
    cc: str | None = Field(default="", description="国家/地区代码")
    first: str | None = Field(default="0", description="结果偏移量")
    safeSearch: str | None = Field(default="", description="成人内容过滤")
    no_cache: str | None = Field(default="false", description="是否跳过缓存")


class BingMapsParams(_BingVariantParams):
    """Parameters for ``bing_maps`` — Bing 地图搜索。"""
    pass


class BingNewsParams(_BingVariantParams):
    """Parameters for ``bing_news`` — Bing 新闻搜索。"""
    pass


class BingShoppingParams(_BingVariantParams):
    """Parameters for ``bing_shopping`` — Bing 购物搜索。"""
    pass


class BingVideosParams(_BingVariantParams):
    """Parameters for ``bing_videos`` — Bing 视频搜索。"""
    pass


_BING_TOOLS = {
    "bing_maps": ("Bing 地图搜索", BingMapsParams),
    "bing_news": ("Bing 新闻搜索", BingNewsParams),
    "bing_shopping": ("Bing 购物搜索", BingShoppingParams),
    "bing_videos": ("Bing 视频搜索", BingVideosParams),
}


def _make_bing_method(tool_name: str, desc: str, param_cls: type[BaseModel]):
    async def _method(self, params: param_cls | None = None) -> Any:  # type: ignore[valid-type]
        arguments = params.model_dump(exclude_none=True) if params else {}
        return await self.call_tool(tool_name, arguments)

    _method.__name__ = tool_name
    _method.__doc__ = f"""Call ``{tool_name}`` — {desc}."""
    return _method


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all Bing methods to the client class."""
    client_cls.bing_search = bing_search
    client_cls.bing_images = bing_images

    for tool_name, (desc, param_cls) in _BING_TOOLS.items():
        setattr(client_cls, tool_name, _make_bing_method(tool_name, desc, param_cls))
