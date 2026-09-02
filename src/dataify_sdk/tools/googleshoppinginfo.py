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

def google_shopping_by_keywords(file_name: str = '{{TasksID}}', keyword: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Google 购物信息、Google Shopping 商品信息、Google 购物商品、Google 商品数据，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Google 购物信息采集 Builder 任务，采集器标识固定为 google_shopping_by-keywords。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: google.com
    spider_id: google_shopping_by-keywords

    Parameters
    ----------
    keyword: 产品关键词，该参数用于指定关键字来收集产品数据。用于 google_shopping_by-keywords，默认值为 iphone。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='google.com',
        spider_id='google_shopping_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

