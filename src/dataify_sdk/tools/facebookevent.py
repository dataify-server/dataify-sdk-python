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

def facebook_event_by_eventlist_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Facebook 活动、Facebook 活动信息、Facebook event、活动列表、活动搜索结果，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Facebook 活动采集 Builder 任务，支持 facebook_event_by-eventlist-url 和 facebook_event_by-search-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: facebook.com
    spider_id: facebook_event_by-eventlist-url

    Parameters
    ----------
    url: 活动列表 URL 或活动搜索 URL。用于 facebook_event_by-eventlist-url 时默认值为 https://www.facebook.com/nohoclub/events；用于 facebook_event_by-search-url 时默认值为 https://www.facebook.com/events/explore/us-atlanta/107991659233606。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='facebook.com',
        spider_id='facebook_event_by-eventlist-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def facebook_event_by_search_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Facebook 活动、Facebook 活动信息、Facebook event、活动列表、活动搜索结果，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Facebook 活动采集 Builder 任务，支持 facebook_event_by-eventlist-url 和 facebook_event_by-search-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: facebook.com
    spider_id: facebook_event_by-search-url

    Parameters
    ----------
    url: 活动列表 URL 或活动搜索 URL。用于 facebook_event_by-eventlist-url 时默认值为 https://www.facebook.com/nohoclub/events；用于 facebook_event_by-search-url 时默认值为 https://www.facebook.com/events/explore/us-atlanta/107991659233606。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='facebook.com',
        spider_id='facebook_event_by-search-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

