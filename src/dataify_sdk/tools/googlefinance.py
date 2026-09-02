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

def google_finance(hl: str = '', json_: str = '1', no_cache: str = 'false', q: str = '', window: str = '1D', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义您想要搜索的查询内容。可以是股票、指数、共同基金、货币或期货。

    上游接口: Search Engine (POST /request)
    engine: google_finance

    Parameters
    ----------
    q: 该参数定义您想要搜索的查询内容。可以是股票、指数、共同基金、货币或期货。  [默认: (空)]
    json_: 该参数定义采集结果的输出格式。可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    hl: 该参数定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码，例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    window: 该参数用于设置图表的时间范围。可设置为 1D - 1 天（默认），5D - 5 天，1M - 1 个月，6M - 6 个月，YTD - 年初至今，1Y - 1 年，5Y - 5 年，MAX - 最大值。  [默认: 1D]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "hl": hl,
        "window": window,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_finance', fields=form)

