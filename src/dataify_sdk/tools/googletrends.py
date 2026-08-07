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

def google_trends(cat: str = '0', csv: str = '', data_type: str = '', date: str = '', geo: str = '', gprop: str = '', hl: str = '', include_low_search_volume: str = '', json_: str = '1', no_cache: str = 'false', q: str = 'pizza', region: str = '', tz: str = '420', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义搜索的查询内容，默认值为 pizza。

    上游接口: Search Engine (POST /request)
    engine: google_trends

    Parameters
    ----------
    q: 定义搜索的查询内容，默认值为 pizza。  [默认: pizza]
    json_: 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。  [默认: 1] (上游字段: json)
    hl: 定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    geo: 定义搜索发起的地理位置。默认为全球，当 geo 参数值未设置或为空时激活。  [默认: (空)]
    region: 用于在使用“按细分区域的比较”和“按区域的兴趣”数据类型图表时获取更具体的结果。其他数据类型图表不接受 region 参数。默认值取决于设置的 geo 位置。可用值包括 COUNTRY、REGION、DMA、CITY。  [默认: (空)]
    data_type: 定义想要执行的搜索类型。可用值包括 TIMESERIES（时间趋势分析）、GEO_MAP（区域对比分析）、GEO_MAP_0（区域兴趣分布）、RELATED_TOPICS（相关主题推荐）、RELATED_QUERIES（相关查询推荐）。  [默认: (空)]
    tz: 定义时区偏移量。默认值为 420（太平洋夏令时间 PDT: -07:00）。值以分钟为单位，范围从 -1439 到 1439。  [默认: 420]
    cat: 定义搜索类别。默认值为 0（所有类别）。可以在 Google 趋势类别列表中找到或下载所有支持的值。示例值包括 0、3、5、7、8、11、12、13、14、16。  [默认: 0]
    gprop: 按属性对结果进行排序。默认属性为网页搜索，当 gprop 参数值未设置或为空时激活。可用值包括 images（图像搜索）、news（新闻搜索）、froogle（Google 购物）、youtube（YouTube 搜索）。  [默认: (空)]
    date: 定义日期。  [默认: (空)]
    csv: 用于检索 CSV 结果。设置为 true 可将 CSV 结果作为数组检索。可用值为 true 或 false。  [默认: (空)]
    include_low_search_volume: 用于在结果中包含低搜索量区域。设置为 true 以在结果中包含低搜索量区域。可用值为 true 或 false。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "hl": hl,
        "geo": geo,
        "region": region,
        "data_type": data_type,
        "tz": tz,
        "cat": cat,
        "gprop": gprop,
        "date": date,
        "csv": csv,
        "include_low_search_volume": include_low_search_volume,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_trends', fields=form)

