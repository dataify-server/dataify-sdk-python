"""Miscellaneous platform scraper tools.

Wraps Airbnb, Booking, Crunchbase, eBay, GitHub, Walmart, and Zillow MCP tools.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _ScraperBase(BaseModel):
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


# ---------------------------------------------------------------------------
# scrape_airbnb_product
# ---------------------------------------------------------------------------


class ScrapeAirbnbProductParams(_ScraperBase):
    """Parameters for ``scrape_airbnb_product`` — Airbnb 房源采集。"""
    url: str = Field(..., description="Airbnb 房源 URL")


async def scrape_airbnb_product(self, params: ScrapeAirbnbProductParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_airbnb_product", arguments)


# ---------------------------------------------------------------------------
# scrape_booking_hotel_list
# ---------------------------------------------------------------------------


class ScrapeBookingHotelListParams(_ScraperBase):
    """Parameters for ``scrape_booking_hotel_list`` — Booking 酒店列表采集。"""
    url: str = Field(..., description="Booking 酒店搜索 URL")


async def scrape_booking_hotel_list(self, params: ScrapeBookingHotelListParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_booking_hotel_list", arguments)


# ---------------------------------------------------------------------------
# scrape_crunchbase_company
# ---------------------------------------------------------------------------


class ScrapeCrunchbaseCompanyParams(_ScraperBase):
    """Parameters for ``scrape_crunchbase_company`` — Crunchbase 公司采集。"""
    url: str = Field(..., description="Crunchbase 公司页面 URL")


async def scrape_crunchbase_company(self, params: ScrapeCrunchbaseCompanyParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_crunchbase_company", arguments)


# ---------------------------------------------------------------------------
# scrape_ebay_info
# ---------------------------------------------------------------------------


class ScrapeEbayInfoParams(_ScraperBase):
    """Parameters for ``scrape_ebay_info`` — eBay 商品信息采集。"""
    url: str = Field(..., description="eBay 商品页面 URL")


async def scrape_ebay_info(self, params: ScrapeEbayInfoParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_ebay_info", arguments)


# ---------------------------------------------------------------------------
# scrape_github_repository
# ---------------------------------------------------------------------------


class ScrapeGithubRepositoryParams(_ScraperBase):
    """Parameters for ``scrape_github_repository`` — GitHub 仓库信息采集。"""
    url: str = Field(..., description="GitHub 仓库 URL")


async def scrape_github_repository(self, params: ScrapeGithubRepositoryParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_github_repository", arguments)


# ---------------------------------------------------------------------------
# scrape_walmart_product
# ---------------------------------------------------------------------------


class ScrapeWalmartProductParams(_ScraperBase):
    """Parameters for ``scrape_walmart_product`` — Walmart 商品采集。"""
    url: str = Field(..., description="Walmart 商品页面 URL")


async def scrape_walmart_product(self, params: ScrapeWalmartProductParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_walmart_product", arguments)


# ---------------------------------------------------------------------------
# scrape_zillow_product
# ---------------------------------------------------------------------------


class ScrapeZillowProductParams(_ScraperBase):
    """Parameters for ``scrape_zillow_product`` — Zillow 房产采集。"""
    url: str = Field(..., description="Zillow 房产页面 URL")


async def scrape_zillow_product(self, params: ScrapeZillowProductParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_zillow_product", arguments)


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all miscellaneous scraper methods to the client class."""
    client_cls.scrape_airbnb_product = scrape_airbnb_product
    client_cls.scrape_booking_hotel_list = scrape_booking_hotel_list
    client_cls.scrape_crunchbase_company = scrape_crunchbase_company
    client_cls.scrape_ebay_info = scrape_ebay_info
    client_cls.scrape_github_repository = scrape_github_repository
    client_cls.scrape_walmart_product = scrape_walmart_product
    client_cls.scrape_zillow_product = scrape_zillow_product
