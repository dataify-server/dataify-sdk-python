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

def google_comment_by_url(days_limit: str = '', file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Google 地图评论信息、Google 地图评论、Google Maps reviews、Google 商家评论，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Google 地图评论信息采集 Builder 任务，采集器标识固定为 google_comment_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: google.com
    spider_id: google_comment_by-url

    Parameters
    ----------
    url: Google 地图 URL，该参数用于指定待采集的 Google 地图访问链接信息。用于 google_comment_by-url，默认值为 https://www.google.com/maps/place/Waterfront+Botanical+Gardens/@38.2630366,-85.7288454,15z/data=!4m8!3m7!1s0x8869731e16a7bdbd:0x2f5d238fefed7ca1!8m2!3d38.2632837!4d-85.7239738!9m1!1b1!16s%2Fg%2F11c709xzzx?hl=en&entry=ttu。  [默认: (空)]
    days_limit: 天数限制，该参数用于指定待采集的 Google 地图评论发布天数限制，即从当前日期开始向前检索评论的天数。默认值为 20。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "days_limit": days_limit,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='google.com',
        spider_id='google_comment_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

