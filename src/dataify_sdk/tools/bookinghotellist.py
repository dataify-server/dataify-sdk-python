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

def booking_hotellist_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Booking 酒店信息、Booking 酒店详情、Booking hotel information、Booking hotel list，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Booking 酒店信息采集 Builder 任务，采集器标识固定为 booking_hotellist_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: booking.com
    spider_id: booking_hotellist_by-url

    Parameters
    ----------
    url: Booking URL，该参数用于指定采集 Booking 酒店信息链接。用于 booking_hotellist_by-url，默认值为 https://www.booking.com/hotel/gb/westlands-of-pitlochry.en-gb.html#tab-main。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='booking.com',
        spider_id='booking_hotellist_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

