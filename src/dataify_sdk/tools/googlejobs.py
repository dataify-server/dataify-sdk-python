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

def google_jobs(q: str, chips: str = '', gl: str = '', google_domain: str = 'google.com', hl: str = '', json_: str = '1', location: str = '', lrad: str = '', ltype: str = '', next_page_token: str = '', no_cache: str = 'false', uds: str = '', uule: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义想要搜索的查询内容。

    上游接口: Search Engine (POST /request)
    engine: google_jobs

    Parameters
    ----------
    q: 定义想要搜索的查询内容。  [必填]
    json_: 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。  [默认: 1] (上游字段: json)
    google_domain: 定义要使用的 Google 域名。默认为 google.com。  [默认: google.com]
    gl: 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。  [默认: (空)]
    hl: 定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    location: 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。  [默认: (空)]
    uule: 希望用于搜索的 Google 编码位置。uule 和 location 参数不能同时使用。  [默认: (空)]
    next_page_token: 定义下一页令牌，用于检索下一页结果。每页最多返回 10 条结果。  [默认: (空)]
    chips: 定义额外的查询条件。职位搜索页面顶部包含称为 chips 的元素，提取其值以传递给 chips 参数。  [默认: (空)]
    lrad: 定义以公里为单位的搜索半径。不严格限制半径范围。  [默认: (空)]
    ltype: 按居家办公过滤结果。此参数已被 Google 弃用，可设置为 true 或 1。  [默认: (空)]
    uds: 启用搜索过滤。它是 Google 提供的一个字符串作为过滤器。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "google_domain": google_domain,
        "gl": gl,
        "hl": hl,
        "location": location,
        "uule": uule,
        "next_page_token": next_page_token,
        "chips": chips,
        "lrad": lrad,
        "ltype": ltype,
        "uds": uds,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_jobs', fields=form)

