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

def google_lens(country: str = '', hl: str = '', json_: str = '1', no_cache: str = 'false', q: str = '', safe: str = '', type_: str = 'all', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义要执行 Google Lens 搜索的图片 URL。

    上游接口: Search Engine (POST /request)
    engine: google_lens

    Parameters
    ----------
    url: 该参数定义要执行 Google Lens 搜索的图片 URL。  [默认: (空)]
    json_: 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON。1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    hl: 该参数定义 Google Lens 搜索要使用的语言。它是一个两位数的语言代码。例如：en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    country: 该参数定义 Google Lens 搜索要使用的特定国家/地区位置。它是一个两位数的国家/地区代码。例如：us 代表美国，fr 代表法国，de 代表德国。  [默认: (空)]
    type_: 该参数定义要执行的搜索类型，默认值为 all。可用值：all、products、about_this_image、exact_matches、visual_matches。  [默认: all] (上游字段: type)
    q: 该参数定义在 Google Lens 搜索中一并使用的搜索查询。仅当 type 为 all、visual_matches 或 products 时适用。  [默认: (空)]
    safe: 该参数定义成人内容的过滤级别。可设置为 active 或 off。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设置为 true 可跳过缓存，设置为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "url": url,
        "json": json_,
        "hl": hl,
        "country": country,
        "type": type_,
        "q": q,
        "safe": safe,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_lens', fields=form)

