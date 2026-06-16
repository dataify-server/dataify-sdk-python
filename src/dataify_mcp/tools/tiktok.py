"""TikTok scraper tools.

Wraps TikTok-related MCP tools: posts, profiles, comment, and shop.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _TikTokBase(BaseModel):
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


class ScrapeTikTokPostsParams(_TikTokBase):
    """Parameters for ``scrape_tiktok_posts`` — TikTok 帖子信息采集。"""

    url: str = Field(default="https://www.tiktok.com/discover/dog", description="TikTok 列表 URL")
    num_of_posts: str | None = Field(default="5", description="收集的帖子数量")


class ScrapeTikTokProfilesParams(_TikTokBase):
    """Parameters for ``scrape_tiktok_profiles`` — TikTok 用户信息采集。"""

    url: str = Field(..., description="TikTok 用户主页 URL")


class ScrapeTikTokCommentParams(_TikTokBase):
    """Parameters for ``scrape_tiktok_comment`` — TikTok 评论采集。"""

    url: str = Field(..., description="TikTok 视频 URL")


class ScrapeTikTokShopParams(_TikTokBase):
    """Parameters for ``scrape_tiktok_shop`` — TikTok Shop 采集。"""

    url: str = Field(..., description="TikTok Shop 商品/店铺 URL")


def _make_method(tool_name: str, desc: str, param_cls: type[BaseModel]):
    async def _method(self, params: param_cls | None = None) -> Any:  # type: ignore[valid-type]
        arguments = params.model_dump(exclude_none=True) if params else {}
        return await self.call_tool(tool_name, arguments)
    _method.__name__ = tool_name
    _method.__doc__ = f"""Call ``{tool_name}`` — {desc}."""
    return _method


async def scrape_tiktok_posts(self, params: ScrapeTikTokPostsParams | None = None) -> Any:
    """Call ``scrape_tiktok_posts`` — TikTok 帖子信息采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_tiktok_posts", arguments)


async def scrape_tiktok_profiles(self, params: ScrapeTikTokProfilesParams | None = None) -> Any:
    """Call ``scrape_tiktok_profiles`` — TikTok 用户信息采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_tiktok_profiles", arguments)


async def scrape_tiktok_comment(self, params: ScrapeTikTokCommentParams | None = None) -> Any:
    """Call ``scrape_tiktok_comment`` — TikTok 评论采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_tiktok_comment", arguments)


async def scrape_tiktok_shop(self, params: ScrapeTikTokShopParams | None = None) -> Any:
    """Call ``scrape_tiktok_shop`` — TikTok Shop 采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_tiktok_shop", arguments)


def _attach(client_cls: type) -> None:
    client_cls.scrape_tiktok_posts = scrape_tiktok_posts
    client_cls.scrape_tiktok_profiles = scrape_tiktok_profiles
    client_cls.scrape_tiktok_comment = scrape_tiktok_comment
    client_cls.scrape_tiktok_shop = scrape_tiktok_shop
