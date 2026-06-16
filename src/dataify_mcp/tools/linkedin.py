"""LinkedIn scraper tools.

Wraps LinkedIn MCP tools: company information and job listings.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _LinkedInBase(BaseModel):
    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


class ScrapeLinkedinCompanyInformationParams(_LinkedInBase):
    """Parameters for ``scrape_linkedin_company_information`` — LinkedIn 公司信息采集。"""
    url: str = Field(..., description="LinkedIn 公司页面 URL")


class ScrapeLinkedinJobListingsInformationParams(_LinkedInBase):
    """Parameters for ``scrape_linkedin_job_listings_information`` — LinkedIn 职位列表采集。"""
    url: str = Field(..., description="LinkedIn 职位搜索 URL")


async def scrape_linkedin_company_information(self, params: ScrapeLinkedinCompanyInformationParams | None = None) -> Any:  # noqa: E501
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_linkedin_company_information", arguments)


async def scrape_linkedin_job_listings_information(self, params: ScrapeLinkedinJobListingsInformationParams | None = None) -> Any:  # noqa: E501
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_linkedin_job_listings_information", arguments)


def _attach(client_cls: type) -> None:
    client_cls.scrape_linkedin_company_information = scrape_linkedin_company_information
    client_cls.scrape_linkedin_job_listings_information = scrape_linkedin_job_listings_information
