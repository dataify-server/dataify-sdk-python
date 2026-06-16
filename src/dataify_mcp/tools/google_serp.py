"""Google SERP (Search Engine Results Page) tools.

Wraps all Google search variant MCP tools with typed parameter models.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Shared base parameter sets
# ---------------------------------------------------------------------------


class _GoogleBaseParams(BaseModel):
    """Base parameters shared by most Google SERP tools."""

    model_config = {"protected_namespaces": ()}

    json: str | None = Field(default="1", description="输出格式: 1 JSON, 2 JSON+HTML, 3 HTML, 4 Light JSON")
    google_domain: str | None = Field(default="google.com", description="Google 域名")
    gl: str | None = Field(default="", description="国家/地区代码 (两位)")
    hl: str | None = Field(default="", description="语言代码 (两位)")
    start: str | None = Field(default="0", description="结果偏移量，用于分页")
    no_cache: str | None = Field(default="false", description="true 跳过缓存，false 使用缓存")
    device: str | None = Field(default="desktop", description="设备: desktop, tablet, mobile")
    render_js: str | None = Field(default="", description="设为 true 启用浏览器 JS 渲染")


# ---------------------------------------------------------------------------
# google_search
# ---------------------------------------------------------------------------


class GoogleSearchParams(_GoogleBaseParams):
    """Parameters for ``google_search``.

    通过 Google 搜索公开网页信息，按国家、语言、位置等条件控制结果。
    """

    q: str = Field(default="pizza", description="搜索查询内容")
    cr: str | None = Field(default="", description="限制搜索国家/地区")
    lr: str | None = Field(default="", description="限制搜索语言")
    location: str | None = Field(default="", description="搜索发起的地理位置")
    uule: str | None = Field(default="", description="Google 编码位置")
    tbs: str | None = Field(default="", description="高级搜索参数")
    safe: str | None = Field(default="", description="成人内容过滤: active 或 off")
    nfpr: str | None = Field(default="", description="排除自动更正结果: 1 排除，0 包含")
    filter: str | None = Field(default="1", description="过滤器: 1 启用，0 禁用")
    ai_overview: str | None = Field(default="", description="获取 AI 概览内容")


async def google_search(self, params: GoogleSearchParams | None = None) -> Any:
    """Call ``google_search`` — Google 网页搜索。

    通过 Google 搜索公开网页信息，支持按国家、语言、位置、设备、
    时间条件等控制搜索结果。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_search", arguments)


# ---------------------------------------------------------------------------
# google_ai_mode
# ---------------------------------------------------------------------------


class GoogleAiModeParams(BaseModel):
    """Parameters for ``google_ai_mode`` — Google AI Mode 搜索。"""

    model_config = {"protected_namespaces": ()}

    q: str = Field(default="pizza", description="搜索查询内容")
    json: str | None = Field(default="1", description="输出格式: 1 JSON, 2 JSON+HTML, 3 HTML, 4 Light JSON")
    gl: str | None = Field(default="", description="国家/地区代码")
    hl: str | None = Field(default="", description="语言代码")
    no_cache: str | None = Field(default="false", description="是否跳过缓存")


async def google_ai_mode(self, params: GoogleAiModeParams | None = None) -> Any:
    """Call ``google_ai_mode`` — Google AI Mode 搜索。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_ai_mode", arguments)


# ---------------------------------------------------------------------------
# google_news
# ---------------------------------------------------------------------------


class GoogleNewsParams(BaseModel):
    """Parameters for ``google_news`` — Google News 新闻搜索。"""

    model_config = {"protected_namespaces": ()}

    q: str = Field(default="pizza", description="搜索查询内容")
    json: str | None = Field(default="1", description="输出格式")
    gl: str | None = Field(default="", description="国家/地区代码")
    hl: str | None = Field(default="", description="语言代码")
    no_cache: str | None = Field(default="false", description="是否跳过缓存")
    topic_token: str | None = Field(default="", description="新闻主题令牌")
    kgmid: str | None = Field(default="", description="知识图谱 ID")
    publication_token: str | None = Field(default="", description="出版物令牌 (如 CNN, BBC)")
    section_token: str | None = Field(default="", description="版块令牌")
    story_token: str | None = Field(default="", description="报道令牌")
    so: str | None = Field(default="0", description="排序: 0 相关性, 1 日期")


async def google_news(self, params: GoogleNewsParams | None = None) -> Any:
    """Call ``google_news`` — Google News 新闻搜索。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_news", arguments)


# ---------------------------------------------------------------------------
# google_images
# ---------------------------------------------------------------------------


class GoogleImagesParams(_GoogleBaseParams):
    """Parameters for ``google_images`` — Google 图片搜索。"""

    q: str = Field(default="pizza", description="搜索查询内容")
    cr: str | None = Field(default="", description="限制搜索国家/地区")
    lr: str | None = Field(default="", description="限制搜索语言")
    location: str | None = Field(default="", description="地理位置")
    uule: str | None = Field(default="", description="Google 编码位置")
    lat: str | None = Field(default="", description="GPS 纬度")
    lon: str | None = Field(default="", description="GPS 经度")
    radius: str | None = Field(default="", description="范围半径（米）")
    tbm: str | None = Field(default="isch", description="搜索类型: isch")
    ludocid: str | None = Field(default="", description="Google CID")
    lsig: str | None = Field(default="", description="知识图谱地图视图标识")
    kgmid: str | None = Field(default="", description="知识图谱 ID")
    si: str | None = Field(default="", description="缓存搜索参数")
    ibp: str | None = Field(default="", description="布局和扩展渲染")
    uds: str | None = Field(default="", description="搜索过滤")
    tbs: str | None = Field(default="", description="高级搜索参数")
    safe: str | None = Field(default="", description="成人内容过滤")
    nfpr: str | None = Field(default="", description="排除自动更正")
    filter: str | None = Field(default="1", description="过滤器")
    ai_overview: str | None = Field(default="", description="AI 概览")


async def google_images(self, params: GoogleImagesParams | None = None) -> Any:
    """Call ``google_images`` — Google 图片搜索。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_images", arguments)


# ---------------------------------------------------------------------------
# google_maps
# ---------------------------------------------------------------------------


class GoogleMapsParams(BaseModel):
    """Parameters for ``google_maps`` — Google Maps 地点搜索。"""

    model_config = {"protected_namespaces": ()}

    q: str = Field(..., description="搜索查询内容")
    json: str | None = Field(default="1", description="输出格式")
    ll: str | None = Field(default="", description="GPS 坐标: @lat,lon,zoom 格式")
    location: str | None = Field(default="", description="地理位置")
    lat: str | None = Field(default="", description="GPS 纬度")
    lon: str | None = Field(default="", description="GPS 经度")
    z: str | None = Field(default="", description="地图缩放级别 (3-23)")
    m: str | None = Field(default="", description="地图高度（米）")
    nearby: str | None = Field(default="", description="强制返回附近结果: true/false")
    google_domain: str | None = Field(default="google.com", description="Google 域名")
    hl: str | None = Field(default="", description="语言代码")
    gl: str | None = Field(default="", description="国家/地区代码")
    start: str | None = Field(default="0", description="结果偏移量")
    type: str | None = Field(default="", description="搜索类型: search 或 place")
    data: str | None = Field(default="", description="(弃用) 请改用 place_id 或 data_cid")
    place_id: str | None = Field(default="", description="地点唯一 ID")
    data_cid: str | None = Field(default="", description="Google CID")
    no_cache: str | None = Field(default="false", description="是否跳过缓存")


async def google_maps(self, params: GoogleMapsParams | None = None) -> Any:
    """Call ``google_maps`` — Google Maps 地点搜索。

    查询 Google Maps 地点、商家、本地位置、地图搜索结果。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_maps", arguments)


# ---------------------------------------------------------------------------
# Remaining Google SERP tools
# Each follows the pattern: q + json + no_cache + engine-specific params
# ---------------------------------------------------------------------------


class _GoogleSearchBase(BaseModel):
    """Minimal base for Google variants that only need q + json + no_cache."""

    model_config = {"protected_namespaces": ()}

    q: str = Field(default="pizza", description="搜索查询内容")
    json: str | None = Field(default="1", description="输出格式")
    gl: str | None = Field(default="", description="国家/地区代码")
    hl: str | None = Field(default="", description="语言代码")
    no_cache: str | None = Field(default="false", description="是否跳过缓存")


class GoogleFlightsParams(_GoogleSearchBase):
    """Parameters for ``google_flights`` — Google Flights 航班搜索。"""
    pass


class GoogleJobsParams(_GoogleSearchBase):
    """Parameters for ``google_jobs`` — Google Jobs 职位搜索。"""
    pass


class GoogleLocalParams(_GoogleSearchBase):
    """Parameters for ``google_local`` — Google Local 本地搜索。"""
    pass


class GoogleVideosParams(_GoogleSearchBase):
    """Parameters for ``google_videos`` — Google Videos 视频搜索。"""
    pass


class GoogleShoppingParams(_GoogleSearchBase):
    """Parameters for ``google_shopping`` — Google Shopping 购物搜索。"""
    pass


class GoogleTrendsParams(_GoogleSearchBase):
    """Parameters for ``google_trends`` — Google Trends 趋势搜索。"""
    pass


class GooglePlayParams(_GoogleSearchBase):
    """Parameters for ``google_play`` — Google Play 应用搜索。"""
    pass


class GoogleScholarParams(_GoogleSearchBase):
    """Parameters for ``google_scholar`` — Google Scholar 学术搜索。"""
    pass


class GoogleFinanceParams(_GoogleSearchBase):
    """Parameters for ``google_finance`` — Google Finance 财经搜索。"""
    pass


class GoogleHotelsParams(_GoogleSearchBase):
    """Parameters for ``google_hotels`` — Google Hotels 酒店搜索。"""
    pass


class GooglePatentsParams(_GoogleSearchBase):
    """Parameters for ``google_patents`` — Google Patents 专利搜索。"""
    pass


class GoogleLensParams(_GoogleSearchBase):
    """Parameters for ``google_lens`` — Google Lens 图像识别。"""
    pass


# ---------------------------------------------------------------------------
# Method definitions for all Google SERP tools
# ---------------------------------------------------------------------------


_GOOGLE_SERP_TOOLS = {
    "google_flights": ("Google Flights 航班搜索", GoogleFlightsParams),
    "google_jobs": ("Google Jobs 职位搜索", GoogleJobsParams),
    "google_local": ("Google Local 本地搜索", GoogleLocalParams),
    "google_videos": ("Google Videos 视频搜索", GoogleVideosParams),
    "google_shopping": ("Google Shopping 购物搜索", GoogleShoppingParams),
    "google_trends": ("Google Trends 趋势搜索", GoogleTrendsParams),
    "google_play": ("Google Play 应用搜索", GooglePlayParams),
    "google_scholar": ("Google Scholar 学术搜索", GoogleScholarParams),
    "google_finance": ("Google Finance 财经搜索", GoogleFinanceParams),
    "google_hotels": ("Google Hotels 酒店搜索", GoogleHotelsParams),
    "google_patents": ("Google Patents 专利搜索", GooglePatentsParams),
    "google_lens": ("Google Lens 图像识别", GoogleLensParams),
}


def _make_serp_method(tool_name: str, desc: str, param_cls: type[BaseModel]):
    """Factory: create an async method for a Google SERP tool."""

    async def _method(self, params: param_cls | None = None) -> Any:
        arguments = params.model_dump(exclude_none=True) if params else {}
        return await self.call_tool(tool_name, arguments)

    _method.__name__ = tool_name
    _method.__doc__ = f"""Call ``{tool_name}`` — {desc}."""
    return _method


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all Google SERP methods to the client class."""
    client_cls.google_search = google_search
    client_cls.google_ai_mode = google_ai_mode
    client_cls.google_news = google_news
    client_cls.google_images = google_images
    client_cls.google_maps = google_maps

    for tool_name, (desc, param_cls) in _GOOGLE_SERP_TOOLS.items():
        setattr(client_cls, tool_name, _make_serp_method(tool_name, desc, param_cls))
