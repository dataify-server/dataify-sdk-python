"""Facebook scraper tools.

Wraps Facebook-related MCP tools: post, profile, comment, and event.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _FBBase(BaseModel):
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


class ScrapeFacebookPostParams(_FBBase):
    """Parameters for ``scrape_facebook_post`` — Facebook 帖子采集。"""
    url: str = Field(..., description="Facebook 帖子 URL")


class ScrapeFacebookProfileParams(_FBBase):
    """Parameters for ``scrape_facebook_profile`` — Facebook 用户信息采集。"""
    url: str = Field(..., description="Facebook 用户主页 URL")


class ScrapeFacebookCommentParams(_FBBase):
    """Parameters for ``scrape_facebook_comment`` — Facebook 评论采集。"""
    url: str = Field(..., description="Facebook 帖子 URL")


class ScrapeFacebookEventParams(_FBBase):
    """Parameters for ``scrape_facebook_event`` — Facebook 活动采集。"""
    url: str = Field(..., description="Facebook 活动 URL")


async def scrape_facebook_post(self, params: ScrapeFacebookPostParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_facebook_post", arguments)


async def scrape_facebook_profile(self, params: ScrapeFacebookProfileParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_facebook_profile", arguments)


async def scrape_facebook_comment(self, params: ScrapeFacebookCommentParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_facebook_comment", arguments)


async def scrape_facebook_event(self, params: ScrapeFacebookEventParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_facebook_event", arguments)


def _attach(client_cls: type) -> None:
    client_cls.scrape_facebook_post = scrape_facebook_post
    client_cls.scrape_facebook_profile = scrape_facebook_profile
    client_cls.scrape_facebook_comment = scrape_facebook_comment
    client_cls.scrape_facebook_event = scrape_facebook_event
