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

def facebook_profile_by_profiles_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Facebook 个人主页、Facebook 个人资料、Facebook profile、个人主页信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Facebook 个人主页采集 Builder 任务，采集器标识固定为 facebook_profile_by-profiles-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: facebook.com
    spider_id: facebook_profile_by-profiles-url

    Parameters
    ----------
    url: 个人主页 URL，该参数用于指定要采集的个人主页 URL。用于 facebook_profile_by-profiles-url，默认值为 https://www.facebook.com/MayeMusk。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='facebook.com',
        spider_id='facebook_profile_by-profiles-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

