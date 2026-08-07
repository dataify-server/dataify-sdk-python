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

def youtube_profiles_by_keyword(file_name: str = '{{TasksID}}', keyword: str = 'MrBeast', page_turning: str = '1', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 个人资料、YouTube 频道资料、YouTube 频道信息、YouTube profile、YouTube 用户信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 个人资料采集 Builder 任务，支持 youtube_profiles_by-keyword 和 youtube_profiles_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_profiles_by-keyword

    Parameters
    ----------
    keyword: YouTube 关键词，该参数用于指定 YouTube 频道进行搜索的关键字。用于 youtube_profiles_by-keyword，默认值为 MrBeast。  [默认: MrBeast]
    page_turning: 采集页数，请输入要采集多少页的产品。用于 youtube_profiles_by-keyword，默认值为 1。  [默认: 1]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "page_turning": page_turning,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_profiles_by-keyword',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def youtube_profiles_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 个人资料、YouTube 频道资料、YouTube 频道信息、YouTube profile、YouTube 用户信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 个人资料采集 Builder 任务，支持 youtube_profiles_by-keyword 和 youtube_profiles_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_profiles_by-url

    Parameters
    ----------
    url: 频道 URL，该参数用于指定待采集的 YouTube 频道的访问 URL 地址。用于 youtube_profiles_by-url，默认值为 https://www.youtube.com/@mrbeast。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_profiles_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

