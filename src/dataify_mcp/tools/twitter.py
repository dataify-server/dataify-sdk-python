"""Twitter/X scraper tools.

Wraps Twitter/X MCP tools: post and profile.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _TwitterBase(BaseModel):
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


class ScrapeTwitterPostParams(_TwitterBase):
    """Parameters for ``scrape_twitter_post`` — Twitter/X 帖子采集。"""
    url: str = Field(..., description="Twitter/X 帖子 URL")


class ScrapeTwitterProfileParams(_TwitterBase):
    """Parameters for ``scrape_twitter_profile`` — Twitter/X 用户信息采集。"""
    url: str = Field(..., description="Twitter/X 用户主页 URL")


async def scrape_twitter_post(self, params: ScrapeTwitterPostParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_twitter_post", arguments)


async def scrape_twitter_profile(self, params: ScrapeTwitterProfileParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_twitter_profile", arguments)


def _attach(client_cls: type) -> None:
    client_cls.scrape_twitter_post = scrape_twitter_post
    client_cls.scrape_twitter_profile = scrape_twitter_profile
