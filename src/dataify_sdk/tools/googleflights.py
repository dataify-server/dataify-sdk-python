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

def google_flights(adults: str = '1', arrival_id: str = '', bags: str = '0', children: str = '0', currency: str = 'USD', deep_search: str = 'false', departure_id: str = '', departure_token: str = '', emissions: str = '', exclude_airlines: str = '', exclude_basic: str = 'false', exclude_conns: str = '', gl: str = '', hl: str = '', include_airlines: str = '', infants_in_seat: str = '0', infants_on_lap: str = '0', json_: str = '1', layover_duration: str = '', max_duration: str = '', max_price: str = '', multi_city_json: str = '', no_cache: str = 'false', outbound_date: str = '', outbound_times: str = '', return_date: str = '', return_times: str = '', show_hidden: str = 'false', sort_by: str = '1', stops: str = '0', travel_class: str = '1', type_: str = '1', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义出发机场代码或地点 kgmid。可以通过逗号分隔指定多个出发机场。例如 CDG,ORY,/m/04jpl。

    上游接口: Search Engine (POST /request)
    engine: google_flights

    Parameters
    ----------
    departure_id: 定义出发机场代码或地点 kgmid。可以通过逗号分隔指定多个出发机场。例如 CDG,ORY,/m/04jpl。  [默认: (空)]
    arrival_id: 定义到达机场代码或地点 kgmid。例如 /m/0vzm 是德克萨斯州奥斯汀的地点 kgmid。可以通过逗号分隔指定多个到达机场。例如 CDG,ORY,/m/04jpl。  [默认: (空)]
    json_: 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。  [默认: 1] (上游字段: json)
    gl: 定义 Google Flights 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。  [默认: (空)]
    hl: 定义 Google Flights 搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    currency: 定义返回价格的货币。默认为 USD。  [默认: USD]
    type_: 定义航班类型。1 为往返（默认），2 为单程，3 为多城市。当此参数设置为 3 时，使用 multi_city_json 设置航班信息。  [默认: 1] (上游字段: type)
    outbound_date: 定义出发日期，格式为 YYYY-MM-DD。例如 2026-03-13。  [默认: (空)]
    return_date: 定义返程日期，格式为 YYYY-MM-DD。例如 2026-03-19。如果 type 参数设置为 1（往返），则此参数为必填。  [默认: (空)]
    travel_class: 定义旅行舱位。1 为经济舱（默认），2 为高级经济舱，3 为商务舱，4 为头等舱。  [默认: 1]
    multi_city_json: 定义多城市航班的航班信息。它是一个包含多个航班信息对象的 JSON 字符串。  [默认: (空)]
    show_hidden: 设置为 true 以包含隐藏的航班结果。默认为 false。  [默认: false]
    exclude_basic: 设置为 true 以排除基础经济舱结果。得到的票价将包含免费选座和随身行李。默认为 false。目前，此过滤器仅适用于美国国内航班，且只能在 gl 为 us 且 travel_class 为 1 时使用。  [默认: false]
    deep_search: 设置为 true 以启用深度搜索，这可能会产生更好的结果，但响应时间更长。深度搜索结果与浏览器中 Google Flights 页面上找到的结果相同。出于性能考虑，默认情况下此选项设置为 false。  [默认: false]
    adults: 定义成人数量。默认为 1。  [默认: 1]
    children: 定义儿童数量。默认为 0。  [默认: 0]
    infants_in_seat: 定义占座婴儿数量。默认为 0。  [默认: 0]
    infants_on_lap: 定义不占座婴儿数量。默认为 0。  [默认: 0]
    sort_by: 定义结果的排序顺序。1 为优选航班（默认），2 为价格，3 为起飞时间，4 为到达时间，5 为飞行时长，6 为排放量。  [默认: 1]
    stops: 定义航班经停次数。0 为任何经停次数（默认），1 为仅直飞，2 为 1 次或更少经停，3 为 2 次或更少经停。  [默认: 0]
    exclude_airlines: 定义要排除的航空公司代码。多个航空公司用逗号分隔。不能与 include_airlines 一起使用。  [默认: (空)]
    include_airlines: 定义要包含的航空公司代码。多个航空公司用逗号分隔。不能与 exclude_airlines 一起使用。  [默认: (空)]
    bags: 定义随身行李数量。默认为 0。此参数不应超过允许携带随身行李的乘客总数（成人、儿童和占座婴儿）。  [默认: 0]
    max_price: 定义最高机票价格。默认为无限制。  [默认: (空)]
    outbound_times: 定义出发时间范围。它是一个包含两个（仅起飞）或四个（起飞和到达）逗号分隔数字的字符串。  [默认: (空)]
    return_times: 定义返程时间范围。它是一个包含两个（仅起飞）或四个（起飞和到达）逗号分隔数字的字符串。每个数字代表一个小时的开始。  [默认: (空)]
    emissions: 定义航班的排放水平。1 表示仅选择低碳排放航班。  [默认: (空)]
    layover_duration: 定义中转时长（以分钟为单位）。它是一个包含两个逗号分隔数字的字符串。例如 90,330 表示 1 小时 30 分钟到 5 小时 30 分钟。  [默认: (空)]
    exclude_conns: 定义要排除的中转机场代码。机场 ID 为大写 3 字母代码，可以在 Google Flights 或 IATA 上搜索。  [默认: (空)]
    max_duration: 定义最长飞行时长（以分钟为单位）。例如 1500 表示 25 小时。  [默认: (空)]
    departure_token: 用于选择航班并获取返程航班（对于往返航班）或行程下一段的航班（对于多城市航班）。在出发航班结果中找到此令牌。它不能与 booking_token 一起使用。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "json": json_,
        "gl": gl,
        "hl": hl,
        "currency": currency,
        "type": type_,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "travel_class": travel_class,
        "multi_city_json": multi_city_json,
        "show_hidden": show_hidden,
        "exclude_basic": exclude_basic,
        "deep_search": deep_search,
        "adults": adults,
        "children": children,
        "infants_in_seat": infants_in_seat,
        "infants_on_lap": infants_on_lap,
        "sort_by": sort_by,
        "stops": stops,
        "exclude_airlines": exclude_airlines,
        "include_airlines": include_airlines,
        "bags": bags,
        "max_price": max_price,
        "outbound_times": outbound_times,
        "return_times": return_times,
        "emissions": emissions,
        "layover_duration": layover_duration,
        "exclude_conns": exclude_conns,
        "max_duration": max_duration,
        "departure_token": departure_token,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_flights', fields=form)

