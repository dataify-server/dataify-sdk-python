"""Glassdoor scraper tools.

Wraps Glassdoor MCP tools: company and job listings.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _GlassdoorBase(BaseModel):
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


class ScrapeGlassdoorCompanyParams(_GlassdoorBase):
    """Parameters for ``scrape_glassdoor_company`` — Glassdoor 公司信息采集。"""
    url: str = Field(..., description="Glassdoor 公司页面 URL")


class ScrapeGlassdoorJobListingsParams(_GlassdoorBase):
    """Parameters for ``scrape_glassdoor_job_listings`` — Glassdoor 职位列表采集。"""
    url: str = Field(..., description="Glassdoor 职位搜索 URL")


async def scrape_glassdoor_company(self, params: ScrapeGlassdoorCompanyParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_glassdoor_company", arguments)


async def scrape_glassdoor_job_listings(self, params: ScrapeGlassdoorJobListingsParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_glassdoor_job_listings", arguments)


def _attach(client_cls: type) -> None:
    client_cls.scrape_glassdoor_company = scrape_glassdoor_company
    client_cls.scrape_glassdoor_job_listings = scrape_glassdoor_job_listings
