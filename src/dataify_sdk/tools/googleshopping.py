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

def google_shopping(free_shipping: str = '', gl: str = '', google_domain: str = 'google.com', hl: str = '', json_: str = '1', location: str = '', max_price: str = '', min_price: str = '', no_cache: str = 'false', on_sale: str = '', q: str = '', shoprs: str = '', small_business: str = '', sort_by: str = '', start: str = '', uule: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义想要搜索的查询内容。提供 shoprs 参数时不需要同时提供 q 参数。

    上游接口: Search Engine (POST /request)
    engine: google_shopping

    Parameters
    ----------
    q: 定义想要搜索的查询内容。提供 shoprs 参数时不需要同时提供 q 参数。  [默认: (空)]
    json_: 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。  [默认: 1] (上游字段: json)
    google_domain: 定义要使用的 Google 域名。默认为 google.com。  [默认: google.com]
    gl: 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。  [默认: (空)]
    hl: 定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    location: 定义搜索发起的地理位置。如果有多个位置与请求的位置匹配，将选择最受欢迎的一个。  [默认: (空)]
    uule: 希望用于搜索的 Google 编码位置。uule 和 location 参数不能同时使用。  [默认: (空)]
    start: 定义结果偏移量。它跳过指定数量的结果，用于分页。该值取决于返回的结果数量，可以是 10 或 20。例如，移动端返回 10 条结果时，start 应为 10、20、30。  [默认: (空)]
    shoprs: 定义包含关于查询和搜索过滤器元数据的令牌。提供 shoprs 参数时不需要同时提供 q 参数。要应用多个过滤器，请使用 || 分隔符连接它们，例如 shoprs_1||shoprs_2||shoprs_3。  [默认: (空)]
    min_price: 价格范围查询的下限。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。  [默认: (空)]
    max_price: 价格范围查询的上限。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。  [默认: (空)]
    sort_by: 定义结果的排序顺序。1 为价格从低到高，2 为价格从高到低。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。  [默认: (空)]
    free_shipping: 仅显示包邮产品。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。  [默认: (空)]
    on_sale: 仅显示促销产品。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。  [默认: (空)]
    small_business: 仅显示来自小企业的产品。该参数会覆盖嵌入到 shoprs 参数中的相应过滤器。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
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
        "shoprs": shoprs,
        "min_price": min_price,
        "max_price": max_price,
        "sort_by": sort_by,
        "free_shipping": free_shipping,
        "on_sale": on_sale,
        "small_business": small_business,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_shopping', fields=form)

