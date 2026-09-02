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

def google_ai_mode(gl: str = '', hl: str = '', json_: str = '1', location: str = '', no_cache: str = 'false', q: str = 'pizza', uule: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义搜索的查询内容，默认值为 pizza。

    上游接口: Search Engine (POST /request)
    engine: google_ai_mode

    Parameters
    ----------
    q: 定义搜索的查询内容，默认值为 pizza。  [默认: pizza]
    json_: 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。  [默认: 1] (上游字段: json)
    location: 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。此参数不能与 uule、lat 和 lon 参数一起使用。  [默认: (空)]
    uule: 希望用于搜索的 Google 编码位置。此参数不能与 location、lat、lon 和 radius 参数一起使用。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    gl: 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。  [默认: (空)]
    hl: 定义 Google 搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "location": location,
        "uule": uule,
        "no_cache": no_cache,
        "gl": gl,
        "hl": hl,
    }
    return _client(client).request_serp(engine='google_ai_mode', fields=form)

