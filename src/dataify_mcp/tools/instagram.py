"""Instagram scraper tools.

Wraps Instagram MCP tools: profiles, comment, and reel.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _IGBase(BaseModel):
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


class ScrapeInstagramProfilesParams(_IGBase):
    """Parameters for ``scrape_instagram_profiles`` — Instagram 用户信息采集。"""
    url: str = Field(..., description="Instagram 用户主页 URL")


class ScrapeInstagramCommentParams(_IGBase):
    """Parameters for ``scrape_instagram_comment`` — Instagram 评论采集。"""
    url: str = Field(..., description="Instagram 帖子 URL")


class ScrapeInstagramReelParams(_IGBase):
    """Parameters for ``scrape_instagram_reel`` — Instagram Reel 采集。"""
    url: str = Field(..., description="Instagram Reel URL")


async def scrape_instagram_profiles(self, params: ScrapeInstagramProfilesParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_instagram_profiles", arguments)


async def scrape_instagram_comment(self, params: ScrapeInstagramCommentParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_instagram_comment", arguments)


async def scrape_instagram_reel(self, params: ScrapeInstagramReelParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_instagram_reel", arguments)


def _attach(client_cls: type) -> None:
    client_cls.scrape_instagram_profiles = scrape_instagram_profiles
    client_cls.scrape_instagram_comment = scrape_instagram_comment
    client_cls.scrape_instagram_reel = scrape_instagram_reel
