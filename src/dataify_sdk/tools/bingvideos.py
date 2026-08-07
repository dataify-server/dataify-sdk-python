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

def bing_videos(cc: str = '', date: str = '', first: str = '0', json_: str = '1', length: str = '', mkt: str = '', no_cache: str = 'false', price: str = '', q: str = 'Pizza', resolution: str = '', setlang: str = '', source_site: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。

    上游接口: Search Engine (POST /request)
    engine: bing_videos

    Parameters
    ----------
    q: 该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。  [默认: Pizza]
    json_: 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML。  [默认: 1] (上游字段: json)
    mkt: 参数定义了爬取时搜索结果的界面显示语言。该参数采用 <语言代码>-<国家/地区代码> 的形式。例如：en-US。  [默认: (空)]
    cc: 该参数定义了爬取时可以指定搜索结果按照国家/地区用户的习惯展示。它是一个由两个字母组成的国家/地区代码，例如：us、ru、uk。  [默认: (空)]
    setlang: 该参数定义搜索使用的语言。它遵循 2 字符的 ISO_3166-1 格式，例如：us 代表美国，de 代表德国，gb 代表英国。  [默认: (空)]
    first: 该参数控制自然结果的偏移量。此参数默认 0。例如 first=10 会将第 10 个自然结果移动到第一个位置。  [默认: 0]
    length: 该参数用于按时长过滤视频。可用值：short（少于 5 分钟）、medium（5-20 分钟）、long（超过 20 分钟）。  [默认: (空)]
    date: 该参数用于按日期过滤视频。可用值：lt1440（过去 24 小时）、lt10080（过去一周）、lt43200（过去一个月）、lt525600（过去一年）。  [默认: (空)]
    resolution: 该参数用于按分辨率类型过滤视频。可用值：lowerthan_360p、360p、480p、720p、1080p。  [默认: (空)]
    source_site: 该参数用于按来源过滤视频。可用值包括：dailymotion.com、vimeo.com、metacafe.com、hulu.com、vevo.com、myspace.com、mtv.com、cbsnews.com、foxnews.com、cnn.com、msn.com。  [默认: (空)]
    price: 该参数用于按价格过滤视频。可用值：free（免费）、paid（付费）。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "mkt": mkt,
        "cc": cc,
        "setlang": setlang,
        "first": first,
        "length": length,
        "date": date,
        "resolution": resolution,
        "source_site": source_site,
        "price": price,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='bing_videos', fields=form)

