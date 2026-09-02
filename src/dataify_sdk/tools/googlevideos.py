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

def google_videos(q: str, filter: str = '1', gl: str = '', google_domain: str = 'google.com', hl: str = '', json_: str = '1', location: str = '', lr: str = '', nfpr: str = '', no_cache: str = 'false', safe: str = '', start: str = '', tbs: str = '', uule: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义想要搜索的查询内容。

    上游接口: Search Engine (POST /request)
    engine: google_videos

    Parameters
    ----------
    q: 定义想要搜索的查询内容。  [必填]
    json_: 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。  [默认: 1] (上游字段: json)
    google_domain: 定义要使用的 Google 域名。默认为 google.com。  [默认: google.com]
    gl: 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。  [默认: (空)]
    hl: 定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    location: 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。  [默认: (空)]
    uule: 希望用于搜索的 Google 编码位置。uule 和 location 参数不能同时使用。  [默认: (空)]
    start: 定义结果偏移量。它跳过指定数量的结果，用于分页。该值取决于返回的结果数量，可以是 10 或 20。例如，移动端返回 10 条结果时，start 应为 10、20、30。  [默认: (空)]
    tbs: 定义常规查询字段中无法实现的高级搜索参数。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    lr: 定义一个或多个将搜索限制在的语言。它使用 lang_{两位语言代码} 指定语言，并使用 | 作为分隔符。例如 lang_fr|lang_de 将仅搜索法语和德语的页面。  [默认: (空)]
    safe: 定义成人内容的过滤级别。可以设置为 active 或 off，默认情况下 Google 会模糊处理露骨内容。  [默认: (空)]
    nfpr: 当原始查询拼写错误时，定义是否排除来自自动更正查询的结果。可以设置为 1 以排除这些结果，或设置为 0 以包含它们（默认）。  [默认: (空)]
    filter: 定义“类似结果”和“省略结果”的过滤器是开启还是关闭。可以设置为 1（默认）以启用这些过滤器，或设置为 0 以禁用这些过滤器。  [默认: 1]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "google_domain": google_domain,
        "gl": gl,
        "hl": hl,
        "location": location,
        "uule": uule,
        "start": start,
        "tbs": tbs,
        "no_cache": no_cache,
        "lr": lr,
        "safe": safe,
        "nfpr": nfpr,
        "filter": filter,
    }
    return _client(client).request_serp(engine='google_videos', fields=form)

