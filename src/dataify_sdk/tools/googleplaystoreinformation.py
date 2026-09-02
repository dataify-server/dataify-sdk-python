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

def google_play_store_information_by_url(app_url: str = '', file_name: str = '{{TasksID}}', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Google Play 商店信息、Google Play App 信息、Google Play 应用信息、Play Store information、Google Play store information，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Google Play商店信息采集 Builder 任务，采集器标识固定为 google-play-store_information_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: play.google.com
    spider_id: google-play-store_information_by-url

    Parameters
    ----------
    app_url: App URL，Google Play 网站上的 App URL。用于 google-play-store_information_by-url，默认值为 https://play.google.com/store/apps/details?id=com.linkedin.android。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "app_url": app_url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='play.google.com',
        spider_id='google-play-store_information_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

