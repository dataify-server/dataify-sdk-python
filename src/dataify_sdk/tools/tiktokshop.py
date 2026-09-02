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

def tiktok_shop_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 TikTok 商店信息、Tiktok 商店信息、TikTok Shop 信息、TikTok 店铺信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 TikTok 商店信息采集 Builder 任务，采集器标识固定为 tiktok_shop_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: tiktok.com
    spider_id: tiktok_shop_by-url

    Parameters
    ----------
    url: TikTok商店URL，该参数用于指定待采集的 TikTok 商店网址。用于 tiktok_shop_by-url，默认值为 https://www.tiktok.com/shop/pdp/long-sleeve-crew-neck-tee-3-pack-by-galaxy-by-harvic-cotton-blend/1729461570693075200。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='tiktok.com',
        spider_id='tiktok_shop_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

