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

def glassdoor_company_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Glassdoor 公司概况信息、Glassdoor 公司信息、Glassdoor company overview、Glassdoor 公司 URL、Glassdoor 公司搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 公司概况信息采集 Builder 任务，支持 glassdoor_company_by-url、glassdoor_company_by-inputfilter、glassdoor_company_by-keywords 和 glassdoor_company_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: glassdoor.com
    spider_id: glassdoor_company_by-url

    Parameters
    ----------
    url: Glassdoor URL，该参数用于指定采集 Glassdoor 公司网址。用于 glassdoor_company_by-url 和 glassdoor_company_by-listurl；by-url 默认值为 https://www.glassdoor.co.uk/Overview/Working-at-Apple-EI_IE1138.11,16.htm，by-listurl 默认值为 https://www.glassdoor.com/Explore/browse-companies.htm?filterType=RATING_OVERALL&locId=1347&locType=S&locName=Texas%252C%2520US&occ=Manager&page=1&overall_rating_low=1。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='glassdoor.com',
        spider_id='glassdoor_company_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def glassdoor_company_by_inputfilter(Job_title: str = '', company_name: str = 'Tesla', file_name: str = '{{TasksID}}', industries: str = 'Information Technology', location: str = 'United States', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Glassdoor 公司概况信息、Glassdoor 公司信息、Glassdoor company overview、Glassdoor 公司 URL、Glassdoor 公司搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 公司概况信息采集 Builder 任务，支持 glassdoor_company_by-url、glassdoor_company_by-inputfilter、glassdoor_company_by-keywords 和 glassdoor_company_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: glassdoor.com
    spider_id: glassdoor_company_by-inputfilter

    Parameters
    ----------
    location: 地点，该参数用于指定采集公司的办公室位置搜索关键词。用于 glassdoor_company_by-inputfilter，默认值为 United States。  [默认: United States]
    company_name: 公司名称，此参数用于指定要采集的公司名称关键词。用于 glassdoor_company_by-inputfilter，默认值为 Tesla。  [默认: Tesla]
    industries: 行业，该参数用于指定采集公司的行业搜索关键词。用于 glassdoor_company_by-inputfilter，默认值为 Information Technology。  [默认: Information Technology]
    Job_title: 职位，该参数用于指定采集公司的含有的职位关键词。用于 glassdoor_company_by-inputfilter，严格按文档字段名 Job title 提交，默认值为 Data。  [默认: (空)] (上游字段: Job title)
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "location": location,
        "company_name": company_name,
        "industries": industries,
        "Job title": Job_title,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='glassdoor.com',
        spider_id='glassdoor_company_by-inputfilter',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def glassdoor_company_by_keywords(file_name: str = '{{TasksID}}', max_search_results: str = '', search_url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Glassdoor 公司概况信息、Glassdoor 公司信息、Glassdoor company overview、Glassdoor 公司 URL、Glassdoor 公司搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 公司概况信息采集 Builder 任务，支持 glassdoor_company_by-url、glassdoor_company_by-inputfilter、glassdoor_company_by-keywords 和 glassdoor_company_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: glassdoor.com
    spider_id: glassdoor_company_by-keywords

    Parameters
    ----------
    search_url: 搜索网址，该参数是您需要输入基于公司搜索词 URL。用于 glassdoor_company_by-keywords，默认值为 https://www.glassdoor.com/Search/results.htm?keyword=Apple。  [默认: (空)]
    max_search_results: 最大搜索结果数，该参数用于指定采集公司信息的最大数量。用于 glassdoor_company_by-keywords，默认值为 5。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "search_url": search_url,
        "max_search_results": max_search_results,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='glassdoor.com',
        spider_id='glassdoor_company_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def glassdoor_company_by_listurl(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Glassdoor 公司概况信息、Glassdoor 公司信息、Glassdoor company overview、Glassdoor 公司 URL、Glassdoor 公司搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 公司概况信息采集 Builder 任务，支持 glassdoor_company_by-url、glassdoor_company_by-inputfilter、glassdoor_company_by-keywords 和 glassdoor_company_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: glassdoor.com
    spider_id: glassdoor_company_by-listurl

    Parameters
    ----------
    url: Glassdoor URL，该参数用于指定采集 Glassdoor 公司网址。用于 glassdoor_company_by-url 和 glassdoor_company_by-listurl；by-url 默认值为 https://www.glassdoor.co.uk/Overview/Working-at-Apple-EI_IE1138.11,16.htm，by-listurl 默认值为 https://www.glassdoor.com/Explore/browse-companies.htm?filterType=RATING_OVERALL&locId=1347&locType=S&locName=Texas%252C%2520US&occ=Manager&page=1&overall_rating_low=1。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='glassdoor.com',
        spider_id='glassdoor_company_by-listurl',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

