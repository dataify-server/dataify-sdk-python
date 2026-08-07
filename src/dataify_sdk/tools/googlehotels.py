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

def google_hotels(adults: str = '2', amenities: str = '', bathrooms: str = '0', bedrooms: str = '0', brands: str = '', check_in_date: str = '', check_out_date: str = '', children: str = '0', children_ages: str = '', currency: str = 'USD', eco_certified: str = '', free_cancellation: str = '', gl: str = '', hl: str = '', hotel_class: str = '', json_: str = '1', max_price: str = '', min_price: str = '', next_page_token: str = '', no_cache: str = 'false', property_token: str = '', property_types: str = '', q: str = 'pizza', rating: str = '', sort_by: str = '', special_offers: str = '', vacation_rentals: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义搜索的查询内容，默认值为 pizza。

    上游接口: Search Engine (POST /request)
    engine: google_hotels

    Parameters
    ----------
    q: 定义搜索的查询内容，默认值为 pizza。  [默认: pizza]
    json_: 该参数定义采集结果的输出格式。可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    hl: 该参数定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码，例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    gl: 该参数定义 Google 酒店搜索要使用的国家/地区。它是一个两位数的国家/地区代码，例如 us 代表美国，uk 代表英国，fr 代表法国。  [默认: (空)]
    currency: 该参数定义返回价格的货币。默认为 USD。  [默认: USD]
    check_in_date: 该参数定义入住日期。格式为 YYYY-MM-DD。例如：2026-03-13。  [默认: (空)]
    check_out_date: 该参数定义退房日期。格式为 YYYY-MM-DD。例如：2026-03-14。  [默认: (空)]
    adults: 该参数定义成人数量。默认为 2。  [默认: 2]
    children: 该参数定义儿童数量。默认为 0。  [默认: 0]
    children_ages: 该参数定义儿童的年龄。年龄范围为 1 到 17，未满 1 岁的儿童视为 1 岁。单个儿童示例：5。多个儿童示例（用逗号 , 分隔）：5,8,10。指定的儿童年龄数量必须与 children 参数匹配。  [默认: (空)]
    sort_by: 该参数用于对结果进行排序。默认按相关性排序。可用选项：3 - 最低价格，8 - 最高评分，13 - 评论最多。  [默认: (空)]
    min_price: 该参数定义价格范围的下限。  [默认: (空)]
    max_price: 该参数定义价格范围的上限。  [默认: (空)]
    property_types: 该参数定义仅在结果中包含特定类型的住宿。单个类型示例：17。多个类型示例（用逗号 , 分隔）：17,12,18。  [默认: (空)]
    amenities: 该参数定义仅包含提供指定设施的结果。对于度假租赁，请访问 Google 度假租赁设施页面查看支持的度假租赁设施完整列表。单个设施示例：35。多个设施示例（用逗号 , 分隔）：35,9,19。  [默认: (空)]
    rating: 该参数用于将结果过滤到特定评分。可用选项：7 - 3.5+，8 - 4.0+，9 - 4.5+。  [默认: (空)]
    brands: 该参数定义您希望搜索结果集中的品牌，多个品牌示例用逗号 , 分隔。  [默认: (空)]
    hotel_class: 该参数定义仅在结果中包含特定酒店星级。多个星级示例用逗号 , 分隔。  [默认: (空)]
    free_cancellation: 该参数定义显示提供免费取消的结果。此参数不适用于度假租赁。可用值为 true 或 false。  [默认: (空)]
    special_offers: 该参数定义显示有特惠的结果。此参数不适用于度假租赁。可用值为 true 或 false。  [默认: (空)]
    eco_certified: 该参数定义显示获得生态认证的结果。此参数不适用于度假租赁。可用值为 true 或 false。  [默认: (空)]
    vacation_rentals: 该参数定义搜索度假租赁结果。默认搜索的是酒店。可用值为 true 或 false。  [默认: (空)]
    bedrooms: 该参数定义最小卧室数量。默认为 0。此参数仅适用于度假租赁。  [默认: 0]
    bathrooms: 该参数定义最小浴室数量。默认为 0。此参数仅适用于度假租赁。  [默认: 0]
    next_page_token: 该参数定义下一页令牌。它用于检索下一页结果。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    property_token: 该参数用于获取住宿详细信息，包括名称、地址、电话、价格、附近地点等。  [默认: (空)]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "hl": hl,
        "gl": gl,
        "currency": currency,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "adults": adults,
        "children": children,
        "children_ages": children_ages,
        "sort_by": sort_by,
        "min_price": min_price,
        "max_price": max_price,
        "property_types": property_types,
        "amenities": amenities,
        "rating": rating,
        "brands": brands,
        "hotel_class": hotel_class,
        "free_cancellation": free_cancellation,
        "special_offers": special_offers,
        "eco_certified": eco_certified,
        "vacation_rentals": vacation_rentals,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "next_page_token": next_page_token,
        "no_cache": no_cache,
        "property_token": property_token,
    }
    return _client(client).request_serp(engine='google_hotels', fields=form)

