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

def google_search(ai_overview: str = '', cr: str = '', device: str = 'desktop', filter: str = '1', gl: str = '', google_domain: str = 'google.com', hl: str = '', json_: str = '1', location: str = '', lr: str = '', nfpr: str = '', no_cache: str = 'false', q: str = 'pizza', render_js: str = '', safe: str = '', start: str = '0', tbs: str = '', uule: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义搜索的查询内容，默认值为 pizza。

    上游接口: Search Engine (POST /request)
    engine: google

    Parameters
    ----------
    q: 定义搜索的查询内容，默认值为 pizza。  [默认: pizza]
    json_: 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。  [默认: 1] (上游字段: json)
    google_domain: 定义要使用的 Google 域名。默认为 google.com。  [默认: google.com]
    gl: 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。  [默认: (空)]
    hl: 定义 Google 搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    cr: 定义一个或多个将搜索限制在的国家/地区。它使用 country{两位大写国家/地区代码} 指定国家/地区，并使用 I 作为分隔符。例如 countryFRIcountryDE 将仅搜索法国和德国的页面。  [默认: (空)]
    lr: 定义一个或多个将搜索限制在的语言。它使用 lang_{两位语言代码} 指定语言，并使用 I 作为分隔符。例如 lang_frIlang_de 将仅搜索法语和德语的页面。  [默认: (空)]
    location: 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。此参数不能与 uule、lat 和 lon 参数一起使用。  [默认: (空)]
    uule: 希望用于搜索的 Google 编码位置。此参数不能与 location、lat、lon 和 radius 参数一起使用。  [默认: (空)]
    start: 定义结果偏移量。它跳过指定数量的结果，用于分页。例如 0 默认是第一页结果，10 是第二页结果，20 是第三页结果，以此类推。  [默认: 0]
    tbs: 定义常规查询字段中无法实现的高级搜索参数。例如专利、日期、新闻、视频、图片、应用或文本内容的高级搜索。  [默认: (空)]
    safe: 定义成人内容的过滤级别。可以设置为 active 或 off，默认情况下 Google 会模糊处理露骨内容。  [默认: (空)]
    nfpr: 当原始查询拼写错误时，定义是否排除来自自动更正查询的结果。设置为 1 排除这些结果，设置为 0 包含它们（默认）。  [默认: (空)]
    filter: 定义“类似结果”和“省略结果”的过滤器是开启还是关闭。设置为 1（默认）启用这些过滤器，设置为 0 禁用这些过滤器。  [默认: 1]
    device: 定义用于获取结果的设备。可设置为 desktop（默认值）使用常规浏览器，tablet 使用平板浏览器（目前使用 iPad），或 mobile 使用移动浏览器。  [默认: desktop]
    render_js: 如果为 true，系统将使用浏览器执行页面脚本并返回完整渲染后的 HTML。开启后会显著增加采集耗时，请按需使用。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    ai_overview: 控制是否获取 Google 搜索结果中的 AI 概览（AI Overview）内容。成功获取 AI 概览通常计为 1 次响应；当首次请求仅返回 page_token 时，系统自动进行的第二次请求将额外计费，总共消耗 2 次响应。  [默认: (空)]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "google_domain": google_domain,
        "gl": gl,
        "hl": hl,
        "cr": cr,
        "lr": lr,
        "location": location,
        "uule": uule,
        "start": start,
        "tbs": tbs,
        "safe": safe,
        "nfpr": nfpr,
        "filter": filter,
        "device": device,
        "render_js": render_js,
        "no_cache": no_cache,
        "ai_overview": ai_overview,
    }
    return _client(client).request_serp(engine='google', fields=form)

