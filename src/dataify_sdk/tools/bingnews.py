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

def bing_news(cc: str = '', count: str = '', first: str = '0', json_: str = '1', mkt: str = '', no_cache: str = 'false', q: str = 'Pizza', qft: str = '', safeSearch: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。

    上游接口: Search Engine (POST /request)
    engine: bing_news

    Parameters
    ----------
    q: 该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。  [默认: Pizza]
    json_: 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    mkt: 参数定义了爬取时搜索结果的界面显示语言。该参数采用 <语言代码>-<国家/地区代码> 的形式。例如：en-US。  [默认: (空)]
    cc: 该参数定义了爬取时可以指定搜索结果按照国家/地区用户的习惯展示。它是一个由两个字母组成的国家/地区代码，例如：us、ru、uk。  [默认: (空)]
    first: 该参数控制自然结果的偏移量。此参数默认为 0。例如 first=10 会将第 10 个自然结果移动到第一个位置。  [默认: 0]
    count: 该参数控制每页的结果数量。此参数仅为建议值，可能无法反映返回的结果数。  [默认: (空)]
    qft: 该参数定义按日期排序的结果。  [默认: (空)]
    safeSearch: 该参数定义成人内容的过滤级别。可用值：Off、Moderate、Strict。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "mkt": mkt,
        "cc": cc,
        "first": first,
        "count": count,
        "qft": qft,
        "safeSearch": safeSearch,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='bing_news', fields=form)

