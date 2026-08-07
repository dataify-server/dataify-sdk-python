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

def tiktok_profiles_by_url(country: str = '', file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 TikTok 个人资料信息、Tiktok 个人资料信息、TikTok 用户资料、Tiktok 创作者资料、TikTok profiles，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 TikTok 个人资料信息采集 Builder 任务，支持 tiktok_profiles_by-url 和 tiktok_profiles_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: tiktok.com
    spider_id: tiktok_profiles_by-url

    Parameters
    ----------
    url: TikTok 个人资料URL，该参数用于指定待采集的 TikTok 个人资料网址。用于 tiktok_profiles_by-url，默认值为 https://www.tiktok.com/@fofimdmell。  [默认: (空)]
    country: 国家，该参数用于指定要搜索的国家。接口按文档示例取值，默认值为 us。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "country": country,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='tiktok.com',
        spider_id='tiktok_profiles_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def tiktok_profiles_by_listurl(country: str = '', file_name: str = '{{TasksID}}', page_turning: str = '', search_url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 TikTok 个人资料信息、Tiktok 个人资料信息、TikTok 用户资料、Tiktok 创作者资料、TikTok profiles，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 TikTok 个人资料信息采集 Builder 任务，支持 tiktok_profiles_by-url 和 tiktok_profiles_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: tiktok.com
    spider_id: tiktok_profiles_by-listurl

    Parameters
    ----------
    search_url: TikTok搜索URL，该参数用于指定待采集的 TikTok 搜索结果网址。用于 tiktok_profiles_by-listurl，默认值为 https://www.tiktok.com/explore?lang=en。  [默认: (空)]
    country: 国家，该参数用于指定要搜索的国家。接口按文档示例取值，默认值为 us。  [默认: (空)]
    page_turning: 页数限制，该参数用于指定采集结果数量的限制（请输入页数）。用于 tiktok_profiles_by-listurl，默认值为 1。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "search_url": search_url,
        "country": country,
        "page_turning": page_turning,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='tiktok.com',
        spider_id='tiktok_profiles_by-listurl',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

