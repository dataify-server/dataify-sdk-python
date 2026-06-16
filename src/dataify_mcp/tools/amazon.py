"""Amazon scraper tools.

Wraps all Amazon-related MCP tools: product (5 spider IDs), comment,
seller, product list, and global product.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# scrape_amazon_product
# ---------------------------------------------------------------------------


class ScrapeAmazonProductParams(BaseModel):
    """Parameters for ``scrape_amazon_product``.

    采集 Amazon 产品详情。支持 5 种采集方式: by-asin, by-url,
    by-keywords, by-category-url, by-best-sellers。
    """

    spider_id: str = Field(
        default="amazon_product_by-asin",
        description="采集器标识: amazon_product_by-asin / by-url / by-keywords / by-category-url / by-best-sellers",
    )
    asin: str | None = Field(default="B0BZYCJK89", description="ASIN (用于 by-asin)")
    url: str | None = Field(default="", description="产品/类别/畅销商品 URL (用于 by-url/by-category-url/by-best-sellers)")
    category_url: str | None = Field(default="", description="畅销类别 URL (用于 by-best-sellers)")
    keyword: str | None = Field(default="coffee", description="搜索关键词 (用于 by-keywords)")
    page_turning: str | None = Field(default="", description="采集页数 (用于 by-keywords/by-category-url/by-best-sellers)")
    lowest_price: str | None = Field(default="20", description="最低价格 (用于 by-keywords)")
    highest_price: str | None = Field(default="50", description="最高价格 (用于 by-keywords)")
    sort_by: str | None = Field(default="畅销排行", description="排序方式 (用于 by-category-url)")
    collect_subcategories: str | None = Field(default="", description="收集子类别 (用于 by-category-url)")
    zip_code: str | None = Field(default="94107", description="邮政编码 (用于 by-url)")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


async def scrape_amazon_product(self, params: ScrapeAmazonProductParams | None = None) -> Any:
    """Call ``scrape_amazon_product`` — Amazon 产品详情采集。

    通过 ASIN、URL、关键词、类别 URL 或畅销排行榜采集 Amazon 产品详情。
    """
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_amazon_product", arguments)


# ---------------------------------------------------------------------------
# scrape_amazon_comment
# ---------------------------------------------------------------------------


class ScrapeAmazonCommentParams(BaseModel):
    """Parameters for ``scrape_amazon_comment`` — Amazon 评论采集。"""

    url: str = Field(..., description="Amazon 产品评论页面 URL")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


async def scrape_amazon_comment(self, params: ScrapeAmazonCommentParams | None = None) -> Any:
    """Call ``scrape_amazon_comment`` — Amazon 评论采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_amazon_comment", arguments)


# ---------------------------------------------------------------------------
# scrape_amazon_seller
# ---------------------------------------------------------------------------


class ScrapeAmazonSellerParams(BaseModel):
    """Parameters for ``scrape_amazon_seller`` — Amazon 卖家信息采集。"""

    url: str = Field(..., description="Amazon 卖家页面 URL")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


async def scrape_amazon_seller(self, params: ScrapeAmazonSellerParams | None = None) -> Any:
    """Call ``scrape_amazon_seller`` — Amazon 卖家信息采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_amazon_seller", arguments)


# ---------------------------------------------------------------------------
# scrape_amazon_product_list
# ---------------------------------------------------------------------------


class ScrapeAmazonProductListParams(BaseModel):
    """Parameters for ``scrape_amazon_product_list`` — Amazon 产品列表采集。"""

    url: str = Field(..., description="Amazon 产品列表/搜索结果 URL")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


async def scrape_amazon_product_list(self, params: ScrapeAmazonProductListParams | None = None) -> Any:
    """Call ``scrape_amazon_product_list`` — Amazon 产品列表采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_amazon_product_list", arguments)


# ---------------------------------------------------------------------------
# scrape_amazon_global_product
# ---------------------------------------------------------------------------


class ScrapeAmazonGlobalProductParams(BaseModel):
    """Parameters for ``scrape_amazon_global_product`` — Amazon 全球产品采集。"""

    url: str = Field(..., description="Amazon 全球站点产品 URL")
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


async def scrape_amazon_global_product(self, params: ScrapeAmazonGlobalProductParams | None = None) -> Any:
    """Call ``scrape_amazon_global_product`` — Amazon 全球产品采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_amazon_global_product", arguments)


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all Amazon scraper methods to the client class."""
    client_cls.scrape_amazon_product = scrape_amazon_product
    client_cls.scrape_amazon_comment = scrape_amazon_comment
    client_cls.scrape_amazon_seller = scrape_amazon_seller
    client_cls.scrape_amazon_product_list = scrape_amazon_product_list
    client_cls.scrape_amazon_global_product = scrape_amazon_global_product
