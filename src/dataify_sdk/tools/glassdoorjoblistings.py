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

def glassdoor_joblistings_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Glassdoor 招聘信息、Glassdoor 职位信息、Glassdoor job listings、Glassdoor 招聘搜索链接，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 招聘信息采集 Builder 任务，支持 glassdoor_joblistings_by-url、glassdoor_joblistings_by-keywords 和 glassdoor_joblistings_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: glassdoor.com
    spider_id: glassdoor_joblistings_by-url

    Parameters
    ----------
    url: 列表网址或招聘搜索链接，该参数用于指定采集 Glassdoor 职位列表网址或 Glassdoor 招聘信息的搜索链接。用于 glassdoor_joblistings_by-url 和 glassdoor_joblistings_by-listurl，默认值按文档为同一个 Glassdoor 职位 URL。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='glassdoor.com',
        spider_id='glassdoor_joblistings_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def glassdoor_joblistings_by_keywords(country: str = 'US', file_name: str = '{{TasksID}}', keyword: str = 'data analyst', location: str = 'New York', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Glassdoor 招聘信息、Glassdoor 职位信息、Glassdoor job listings、Glassdoor 招聘搜索链接，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 招聘信息采集 Builder 任务，支持 glassdoor_joblistings_by-url、glassdoor_joblistings_by-keywords 和 glassdoor_joblistings_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: glassdoor.com
    spider_id: glassdoor_joblistings_by-keywords

    Parameters
    ----------
    keyword: 关键词，该参数是通过职位名称等关键字搜索进行采集招聘信息。用于 glassdoor_joblistings_by-keywords，默认值为 data analyst。  [默认: data analyst]
    location: 地点，该参数用于指定采集特定位置的招聘信息。用于 glassdoor_joblistings_by-keywords，默认值为 New York。  [默认: New York]
    country: 国家，该参数用于指定采集招聘信息的国家。接口取 country 选项的 typeValue，默认按确认使用 US。  [默认: US]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "location": location,
        "country": country,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='glassdoor.com',
        spider_id='glassdoor_joblistings_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def glassdoor_joblistings_by_listurl(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Glassdoor 招聘信息、Glassdoor 职位信息、Glassdoor job listings、Glassdoor 招聘搜索链接，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Glassdoor 招聘信息采集 Builder 任务，支持 glassdoor_joblistings_by-url、glassdoor_joblistings_by-keywords 和 glassdoor_joblistings_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: glassdoor.com
    spider_id: glassdoor_joblistings_by-listurl

    Parameters
    ----------
    url: 列表网址或招聘搜索链接，该参数用于指定采集 Glassdoor 职位列表网址或 Glassdoor 招聘信息的搜索链接。用于 glassdoor_joblistings_by-url 和 glassdoor_joblistings_by-listurl，默认值按文档为同一个 Glassdoor 职位 URL。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='glassdoor.com',
        spider_id='glassdoor_joblistings_by-listurl',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

