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

def google_play(age: str = '', apps_category: str = '', chart: str = '', gl: str = 'us', hl: str = '', json_: str = '1', next_page_token: str = '', no_cache: str = 'false', q: str = '', section_page_token: str = '', see_more_token: str = '', store_device: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义您要在 Google Play 应用商店中搜索的查询内容。

    上游接口: Search Engine (POST /request)
    engine: google_play

    Parameters
    ----------
    q: 该参数定义您要在 Google Play 应用商店中搜索的查询内容。  [默认: (空)]
    json_: 该参数定义采集结果的输出格式。可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    hl: 该参数定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码，例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    gl: 该参数定义 Google Play 搜索要使用的国家/地区。它是一个两位数的国家/地区代码，例如 us（默认）代表美国，uk 代表英国，fr 代表法国。  [默认: us]
    apps_category: 该参数定义应用商店类别。  [默认: (空)]
    next_page_token: 该参数定义下一页令牌。它用于检索下一页结果。它不应与 section_page_token、see_more_token 和 chart 参数一起使用。  [默认: (空)]
    section_page_token: 该参数定义用于从各个版块检索分页结果的版块页面令牌。它不应与 next_page_token、see_more_token 和 chart 参数一起使用。  [默认: (空)]
    chart: 该参数用于显示热门排行榜。最多可返回 50 条结果。它不应与 section_page_token、see_more_token 和 next_page_token 参数一起使用。  [默认: (空)]
    see_more_token: 该参数定义用于从各个版块检索分页结果的“查看更多”令牌。它通常在下一页结果中找到。它不应与 section_page_token、next_page_token 和 chart 参数一起使用。  [默认: (空)]
    store_device: 该参数定义用于排序结果的设备。此参数不能与 apps_category 或 q 参数一起使用。可用值包括 phone、tablet、tv、chromebook、watch、car。  [默认: (空)]
    age: 该参数定义年龄段子类别。age 仅在 apps_category=FAMILY（儿童应用）时使用。可用值包括 AGE_RANGE1、AGE_RANGE2、AGE_RANGE3。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "hl": hl,
        "gl": gl,
        "apps_category": apps_category,
        "next_page_token": next_page_token,
        "section_page_token": section_page_token,
        "chart": chart,
        "see_more_token": see_more_token,
        "store_device": store_device,
        "age": age,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_play', fields=form)

