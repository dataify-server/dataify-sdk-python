"""Indeed scraper tools.

Wraps Indeed MCP tools: companies info and job listings.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _IndeedBase(BaseModel):
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


class ScrapeIndeedCompaniesInfoParams(_IndeedBase):
    """Parameters for ``scrape_indeed_companies_info`` — Indeed 公司信息采集。"""
    url: str = Field(..., description="Indeed 公司页面 URL")


class ScrapeIndeedJobListingsParams(_IndeedBase):
    """Parameters for ``scrape_indeed_job_listings`` — Indeed 职位列表采集。"""
    url: str = Field(..., description="Indeed 职位搜索 URL")


async def scrape_indeed_companies_info(self, params: ScrapeIndeedCompaniesInfoParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_indeed_companies_info", arguments)


async def scrape_indeed_job_listings(self, params: ScrapeIndeedJobListingsParams | None = None) -> Any:
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_indeed_job_listings", arguments)


def _attach(client_cls: type) -> None:
    client_cls.scrape_indeed_companies_info = scrape_indeed_companies_info
    client_cls.scrape_indeed_job_listings = scrape_indeed_job_listings
