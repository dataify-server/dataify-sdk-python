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

def bing_search(cc: str = '', filters: str = '', first: str = '0', json_: str = '1', lat: str = '', location: str = '', lon: str = '', mkt: str = '', no_cache: str = 'false', q: str = 'pizza', safeSearch: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义爬取时的搜索结果，默认值为 pizza。您可以输入任意想要查询的关键词，也可以是任意语言。

    上游接口: Search Engine (POST /request)
    engine: bing

    Parameters
    ----------
    q: 该参数定义爬取时的搜索结果，默认值为 pizza。您可以输入任意想要查询的关键词，也可以是任意语言。  [默认: pizza]
    json_: 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    location: 该参数定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。  [默认: (空)]
    lat: 定义搜索起点的 GPS 纬度。  [默认: (空)]
    lon: 定义搜索起点的 GPS 经度。  [默认: (空)]
    mkt: 该参数定义爬取时搜索结果的界面显示语言。该参数采用 <语言代码>-<国家/地区代码> 的形式。例如：en-US。该字符串不区分大小写。  [默认: (空)]
    cc: 该参数定义爬取时可以指定搜索结果按照国家/地区用户的习惯展示。它是一个由两个字母组成的国家/地区代码，例如：us、ru、uk。  [默认: (空)]
    first: 该参数控制自然结果的偏移量。此参数默认为 0。例如 first=10 会将第 10 个自然结果移动到第一个位置。  [默认: 0]
    safeSearch: 该参数定义成人内容的过滤级别。可设置为：Off - 返回包含成人文本、图片或视频的网页；Moderate - 返回包含成人文本但不包含成人图片或视频的网页；Strict - 不返回包含成人文本、图片或视频的网页。  [默认: (空)]
    filters: 该参数允许使用更复杂的过滤选项，例如按日期范围过滤（例如：ez5_18169_18230）或使用特定的显示过滤器（例如：ufn:\"Wunderman+Thompson\"+sid:\"5bede9a2-1bda-9887-e6eb-30b1b8b6b513\"+catguid:\"5bede9a2-1bda-9887-e6eb-30b1b8b6b513_cfb02057\"+segment:\"generic.carousel\"+entitysegment:\"Organization\"）。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "location": location,
        "lat": lat,
        "lon": lon,
        "mkt": mkt,
        "cc": cc,
        "first": first,
        "safeSearch": safeSearch,
        "filters": filters,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='bing', fields=form)

