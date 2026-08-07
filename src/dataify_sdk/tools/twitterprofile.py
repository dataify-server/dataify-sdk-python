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

def twitter_profile_by_profileurl(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Twitter 个人资料、Twitter(X) 个人资料、X 个人资料、X 用户资料，与采集、抓取、爬取、获取、提取等动词组合时触发。Twitter 已更名为 X。复用一个工具提交 Twitter(X) 个人资料采集 Builder 任务，支持 twitter_profile_by-profileurl 和 twitter_profile_by-username。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: x.com
    spider_id: twitter_profile_by-profileurl

    Parameters
    ----------
    url: Twitter 个人资料 URL，该参数用于指定采集 Twitter 个人资料的 URL。用于 twitter_profile_by-profileurl，默认值为 https://x.com/elonmusk。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='x.com',
        spider_id='twitter_profile_by-profileurl',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def twitter_profile_by_username(file_name: str = '{{TasksID}}', user_name: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Twitter 个人资料、Twitter(X) 个人资料、X 个人资料、X 用户资料，与采集、抓取、爬取、获取、提取等动词组合时触发。Twitter 已更名为 X。复用一个工具提交 Twitter(X) 个人资料采集 Builder 任务，支持 twitter_profile_by-profileurl 和 twitter_profile_by-username。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: x.com
    spider_id: twitter_profile_by-username

    Parameters
    ----------
    user_name: Twitter 用户名，该参数用于指定待采集的 Twitter 的个人资料用户名。用于 twitter_profile_by-username，默认值为 elonmusk。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "user_name": user_name,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='x.com',
        spider_id='twitter_profile_by-username',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

