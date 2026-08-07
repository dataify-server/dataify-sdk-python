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

def duckduckgo_search(df: str = '', json_: str = '1', kl: str = '', m: str = '10', no_cache: str = 'false', q: str = 'pizza', safe: str = '-1', search_assist: str = 'false', start: str = '0', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义爬取时的搜索结果，默认值为 pizza。您可以输入任意想要查询的关键词，也可以是任意语言。

    上游接口: Search Engine (POST /request)
    engine: duckduckgo

    Parameters
    ----------
    q: 该参数定义爬取时的搜索结果，默认值为 pizza。您可以输入任意想要查询的关键词，也可以是任意语言。  [默认: pizza]
    json_: 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    kl: 该参数定义 DuckDuckGo 搜索要使用的地区。地区代码示例：us-en 代表美国，uk-en 代表英国，fr-fr 代表法国。请访问 DuckDuckGo 地区页面查看支持的地区完整列表。  [默认: (空)]
    search_assist: 该参数决定是否在响应中返回 DuckDuckGo 的 AI 搜索辅助。可设置为 true 或 false（默认）。search_assist 和 m 不能一起使用。  [默认: false]
    safe: 该参数定义成人内容的过滤级别。可设置为：1 - 严格，-1 - 中等（默认），-2 - 关闭。  [默认: -1]
    df: 该参数定义按日期过滤的结果。可设置为：d - 过去一天，w - 过去一周，m - 过去一月，y - 过去一年；也可以按 start_date..end_date 格式传递自定义日期，例如：2021-06-15..2024-06-16。  [默认: (空)]
    start: 该参数定义结果偏移量，它跳过指定数量的结果。当 start 设置为 0 或留空时，最多可返回 25 个自然结果；当 start 大于 0 时，最多可返回 10 个自然结果。DuckDuckGo 可能返回重复结果或数量可变的结果，这在使用较大的 start 和 m 参数时更可能发生。  [默认: 0]
    m: 该参数定义要返回的最大结果数量。默认值：10，最小值：1，最大值：50。当 start 设置为 0 或留空时，最多可返回 25 个自然结果。DuckDuckGo 可能返回重复结果或数量可变的结果，这在使用较大的 start 和 m 参数时更可能发生。m 和 search_assist 不能一起使用。  [默认: 10]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "kl": kl,
        "search_assist": search_assist,
        "safe": safe,
        "df": df,
        "start": start,
        "m": m,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='duckduckgo', fields=form)

