"""Google scraper tools.

Wraps MCP tools that scrape specific Google properties via the
Scraper Builder API (maps details, map comments, shopping info, etc.).

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# google_map_details
# ---------------------------------------------------------------------------


class GoogleMapDetailsParams(BaseModel):
    """Parameters for ``google_map_details`` — Google 地图详情采集。"""

    data_cid: str = Field(default="", description="Google CID (客户标识符)")
    place_id: str | None = Field(default="", description="地点唯一 ID")
    hl: str | None = Field(default="", description="语言代码")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name 字段")


async def google_map_details(self, params: GoogleMapDetailsParams | None = None) -> Any:
    """Call ``google_map_details`` — Google 地图详情采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_map_details", arguments)


# ---------------------------------------------------------------------------
# google_map_comment
# ---------------------------------------------------------------------------


class GoogleMapCommentParams(BaseModel):
    """Parameters for ``google_map_comment`` — Google 地图评论采集。"""

    data_cid: str = Field(default="", description="Google CID")
    place_id: str | None = Field(default="", description="地点唯一 ID")
    hl: str | None = Field(default="", description="语言代码")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name 字段")


async def google_map_comment(self, params: GoogleMapCommentParams | None = None) -> Any:
    """Call ``google_map_comment`` — Google 地图评论采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_map_comment", arguments)


# ---------------------------------------------------------------------------
# google_shopping_info
# ---------------------------------------------------------------------------


class GoogleShoppingInfoParams(BaseModel):
    """Parameters for ``google_shopping_info`` — Google 购物详情采集。"""

    url: str = Field(..., description="商品 URL")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name 字段")


async def google_shopping_info(self, params: GoogleShoppingInfoParams | None = None) -> Any:
    """Call ``google_shopping_info`` — Google 购物详情采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_shopping_info", arguments)


# ---------------------------------------------------------------------------
# google_play_store_information
# ---------------------------------------------------------------------------


class GooglePlayStoreInformationParams(BaseModel):
    """Parameters for ``google_play_store_information`` — Google Play 应用信息。"""

    url: str = Field(..., description="Google Play 应用 URL")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name 字段")


async def google_play_store_information(self, params: GooglePlayStoreInformationParams | None = None) -> Any:
    """Call ``google_play_store_information`` — Google Play 应用信息采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_play_store_information", arguments)


# ---------------------------------------------------------------------------
# google_play_store_reviews
# ---------------------------------------------------------------------------


class GooglePlayStoreReviewsParams(BaseModel):
    """Parameters for ``google_play_store_reviews`` — Google Play 应用评论。"""

    url: str = Field(..., description="Google Play 应用 URL")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name 字段")


async def google_play_store_reviews(self, params: GooglePlayStoreReviewsParams | None = None) -> Any:
    """Call ``google_play_store_reviews`` — Google Play 应用评论采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("google_play_store_reviews", arguments)


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all Google scraper methods to the client class."""
    client_cls.google_map_details = google_map_details
    client_cls.google_map_comment = google_map_comment
    client_cls.google_shopping_info = google_shopping_info
    client_cls.google_play_store_information = google_play_store_information
    client_cls.google_play_store_reviews = google_play_store_reviews
