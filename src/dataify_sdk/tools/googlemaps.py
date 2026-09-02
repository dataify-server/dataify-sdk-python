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

def google_maps(q: str, data: str = '', data_cid: str = '', gl: str = '', google_domain: str = 'google.com', hl: str = '', json_: str = '1', lat: str = '', ll: str = '', location: str = '', lon: str = '', m: str = '', nearby: str = '', no_cache: str = 'false', place_id: str = '', start: str = '0', type_: str = '', z: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义想要搜索的查询内容。

    上游接口: Search Engine (POST /request)
    engine: google_maps

    Parameters
    ----------
    q: 定义想要搜索的查询内容。  [必填]
    json_: 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。  [默认: 1] (上游字段: json)
    ll: 定义搜索起点的 GPS 坐标。其值必须符合 @ + 纬度 + , + 经度 + , + 缩放级别/地图高度格式，例如 @40.7455096,-74.0083012,14z 或 @43.8521864,11.2168835,10410m。此参数不能与 location、lat、lon、z 或 m 参数一起使用。  [默认: (空)]
    location: 定义地点，其 GPS 坐标用作搜索起点，最终会被编码为 ll 参数的一部分。此参数应与 z 或 m 参数一起使用，不能与 ll、lat 或 lon 参数一起使用。  [默认: (空)]
    lat: 定义搜索起点的 GPS 纬度，最终会被编码为 ll 参数的一部分。使用 lon 参数时必须同时提供此参数。此参数应与 z 或 m 参数一起使用，不能与 ll 或 location 参数一起使用。  [默认: (空)]
    lon: 定义搜索起点的 GPS 经度，最终会被编码为 ll 参数的一部分。使用 lat 参数时必须同时提供此参数。此参数应与 z 或 m 参数一起使用，不能与 ll 或 location 参数一起使用。  [默认: (空)]
    z: 定义地图缩放级别。最小值为 3（地图完全缩小），最大有效值取决于位置，范围从 18 到 23。使用 location 或 lat/lon 参数时，必须指定 z 或 m。  [默认: (空)]
    m: 定义以米为单位的地图高度。最小值为 1，最大值为 15028132，大致相当于赤道上的 3z。最终会被编码为 ll 参数的一部分。使用 location 或 lat/lon 参数时，必须指定 m 或 z。  [默认: (空)]
    nearby: 强制返回更接近指定位置的搜索结果。当 q 参数包含 near me 关键词时，强烈建议使用此参数；当 q 参数包含地点时，不建议使用。此参数应与 ll、location 或 lat/lon 参数一起使用。可设置为 true 或 false。  [默认: (空)]
    google_domain: 定义要使用的 Google 域名。默认为 google.com。  [默认: google.com]
    hl: 定义 Google 地图搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    gl: 定义 Google 地图搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。  [默认: (空)]
    start: 定义结果偏移量。它跳过指定数量的结果，用于分页。例如 0 默认是第一页结果，20 是第二页结果，40 是第三页结果，依此类推。  [默认: 0]
    type_: 定义要执行的搜索类型。search 返回 q 参数列出的结果列表；place 在设置 data 参数时返回特定地点结果。使用 place_id 或 data_cid 时不需要此参数。  [默认: (空)] (上游字段: type)
    data: 此参数已弃用，请改用 place_id 或 data_cid。该参数可用于过滤搜索结果。  [默认: (空)]
    place_id: 定义 Google 地图中地点的唯一引用。地点 ID 可用于大多数地点，包括企业、地标、公园和交叉路口。  [默认: (空)]
    data_cid: 定义地点的 Google CID（客户标识符）。data_cid 和 place_id 不能同时使用。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "ll": ll,
        "location": location,
        "lat": lat,
        "lon": lon,
        "z": z,
        "m": m,
        "nearby": nearby,
        "google_domain": google_domain,
        "hl": hl,
        "gl": gl,
        "start": start,
        "type": type_,
        "data": data,
        "place_id": place_id,
        "data_cid": data_cid,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_maps', fields=form)

