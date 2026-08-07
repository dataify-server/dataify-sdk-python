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

def crunchbase_company_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Crunchbase 信息、Crunchbase 公司信息、Crunchbase 企业信息、Crunchbase company，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Crunchbase 公司信息采集 Builder 任务，支持 crunchbase_company_by-url 和 crunchbase_company_by-keywords。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: crunchbase.com
    spider_id: crunchbase_company_by-url

    Parameters
    ----------
    url: Crunchbase URL，该参数用于指定采集 Crunchbase 中的公司 URL。用于 crunchbase_company_by-url，默认值为 https://www.crunchbase.com/organization/aisci。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='crunchbase.com',
        spider_id='crunchbase_company_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def crunchbase_company_by_keywords(file_name: str = '{{TasksID}}', keyword: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Crunchbase 信息、Crunchbase 公司信息、Crunchbase 企业信息、Crunchbase company，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Crunchbase 公司信息采集 Builder 任务，支持 crunchbase_company_by-url 和 crunchbase_company_by-keywords。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: crunchbase.com
    spider_id: crunchbase_company_by-keywords

    Parameters
    ----------
    keyword: 关键词，该参数用于指定采集 Crunchbase 中搜索公司的关键词。用于 crunchbase_company_by-keywords，默认值为 NetBooster。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='crunchbase.com',
        spider_id='crunchbase_company_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

