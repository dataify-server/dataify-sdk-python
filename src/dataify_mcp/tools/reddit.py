"""Reddit scraper tools.

Wraps Reddit MCP tools: posts and comment.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _RedditBase(BaseModel):
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


class ScrapeRedditPostsParams(_RedditBase):
    """Parameters for ``scrape_reddit_posts`` — Reddit 帖子采集。"""
    url: str = Field(..., description="Reddit 帖子/子版块 URL")


class ScrapeRedditCommentParams(_RedditBase):
    """Parameters for ``scrape_reddit_comment`` — Reddit 评论采集。"""
    url: str = Field(..., description="Reddit 帖子 URL")


async def scrape_reddit_posts(self, params: ScrapeRedditPostsParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_reddit_posts", arguments)


async def scrape_reddit_comment(self, params: ScrapeRedditCommentParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_reddit_comment", arguments)


def _attach(client_cls: type) -> None:
    client_cls.scrape_reddit_posts = scrape_reddit_posts
    client_cls.scrape_reddit_comment = scrape_reddit_comment
