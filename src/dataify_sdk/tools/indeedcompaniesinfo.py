"""Auto-generated Dataify tool functions.  Do not edit by hand.

Generated from the Go reference project by ``dataify_sdk._codegen.generate``.
Each function calls the Dataify upstream REST API directly (no MCP layer).
"""

from __future__ import annotations

import json
from typing import Any

from dataify_sdk.client import DataifyClient, get_default_client


def _client(client: DataifyClient | None) -> DataifyClient:
    return client if client is not None else get_default_client()

def indeed_companies_info_by_company_list_url(company_list_url: str = '', file_name: str = '{{TasksID}}', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Indeed 公司信息、Indeed companies info、Indeed 公司列表、Indeed 公司关键词、Indeed 行业地区公司，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Indeed 公司信息采集 Builder 任务，支持 indeed_companies-info_by-company-list-url、indeed_companies-info_by-keyword、indeed_companies-info_by-industry-and-state 和 indeed_companies-info_by-company-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: indeed.com
    spider_id: indeed_companies-info_by-company-list-url

    Parameters
    ----------
    company_list_url: Indeed公司列表URL，该参数用于指定采集公司列表的URL。用于 indeed_companies-info_by-company-list-url，默认值为 https://www.indeed.com/companies/browse-companies。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "company_list_url": company_list_url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='indeed.com',
        spider_id='indeed_companies-info_by-company-list-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def indeed_companies_info_by_keyword(file_name: str = '{{TasksID}}', keyword: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Indeed 公司信息、Indeed companies info、Indeed 公司列表、Indeed 公司关键词、Indeed 行业地区公司，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Indeed 公司信息采集 Builder 任务，支持 indeed_companies-info_by-company-list-url、indeed_companies-info_by-keyword、indeed_companies-info_by-industry-and-state 和 indeed_companies-info_by-company-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: indeed.com
    spider_id: indeed_companies-info_by-keyword

    Parameters
    ----------
    keyword: 公司关键词，该参数用于指定采集公司的关键词。用于 indeed_companies-info_by-keyword，默认值为 openai。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='indeed.com',
        spider_id='indeed_companies-info_by-keyword',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def indeed_companies_info_by_industry_and_state(file_name: str = '{{TasksID}}', industry: str = '', state: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Indeed 公司信息、Indeed companies info、Indeed 公司列表、Indeed 公司关键词、Indeed 行业地区公司，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Indeed 公司信息采集 Builder 任务，支持 indeed_companies-info_by-company-list-url、indeed_companies-info_by-keyword、indeed_companies-info_by-industry-and-state 和 indeed_companies-info_by-company-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: indeed.com
    spider_id: indeed_companies-info_by-industry-and-state

    Parameters
    ----------
    industry: Indeed行业，该参数用于指定采集公司所属行业。用于 indeed_companies-info_by-industry-and-state，默认值为 Accounting & Tax。  [默认: (空)]
    state: Indeed 地区，该参数用于指定采集公司所在地区。用于 indeed_companies-info_by-industry-and-state，默认值为 Alabama - 60 companies。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "industry": industry,
        "state": state,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='indeed.com',
        spider_id='indeed_companies-info_by-industry-and-state',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def indeed_companies_info_by_company_url(company_url: str = '', file_name: str = '{{TasksID}}', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Indeed 公司信息、Indeed companies info、Indeed 公司列表、Indeed 公司关键词、Indeed 行业地区公司，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Indeed 公司信息采集 Builder 任务，支持 indeed_companies-info_by-company-list-url、indeed_companies-info_by-keyword、indeed_companies-info_by-industry-and-state 和 indeed_companies-info_by-company-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: indeed.com
    spider_id: indeed_companies-info_by-company-url

    Parameters
    ----------
    company_url: Indeed公司URL，该参数用于指定要采集的公司URL。用于 indeed_companies-info_by-company-url，默认值为 https://www.indeed.com/cmp/Allstate-Insurance。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "company_url": company_url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='indeed.com',
        spider_id='indeed_companies-info_by-company-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

