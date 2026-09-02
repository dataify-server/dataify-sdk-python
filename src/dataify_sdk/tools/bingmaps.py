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

def bing_maps(count: str = '', cp: str = '', first: str = '0', json_: str = '1', no_cache: str = 'false', place_id: str = '', q: str = '', setlang: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义搜索查询。您可以使用常规必应地图搜索中使用的任何内容。

    上游接口: Search Engine (POST /request)
    engine: bing_maps

    Parameters
    ----------
    q: 该参数定义搜索查询。您可以使用常规必应地图搜索中使用的任何内容。  [默认: (空)]
    json_: 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    cp: 该参数定义您希望 q（查询）应用到的位置的 GPS 坐标。它必须按纬度 + ~ + 经度的顺序构建。例如：40.7455096~-74.0083012。  [默认: (空)]
    setlang: 该参数定义搜索使用的语言。它遵循 ISO_3166-1 格式，例如 us 代表美国，de 代表德国，gb 代表英国等。  [默认: (空)]
    place_id: 该参数定义必应地图上地点的唯一引用。  [默认: (空)]
    first: 该参数控制本地结果的偏移量。此参数默认为 0。例如，当 count=10 时，第二页结果从 first=10 开始。  [默认: 0]
    count: 该参数控制每页的结果数量。此参数仅为建议值，可能无法反映返回的结果数。每页最大结果为 10。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "cp": cp,
        "setlang": setlang,
        "place_id": place_id,
        "first": first,
        "count": count,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='bing_maps', fields=form)

