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

def bing_images(age: str = '', aspect: str = '', cc: str = '', color2: str = '', count: str = '', face: str = '', first: str = '0', imagesize: str = '', json_: str = '1', license: str = '', mkt: str = '', no_cache: str = 'false', photo: str = '', q: str = 'Pizza', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。

    上游接口: Search Engine (POST /request)
    engine: bing_images

    Parameters
    ----------
    q: 该参数定义爬取时的搜索结果，默认值为 Pizza。您可以输入任意想要查询的关键词，也可以是任意语言。  [默认: Pizza]
    json_: 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    mkt: 参数定义了爬取时搜索结果的界面显示语言。该参数采用 <语言代码>-<国家/地区代码> 的形式。例如：en-US。  [默认: (空)]
    cc: 该参数定义了爬取时可以指定搜索结果按照国家/地区用户的习惯展示。它是一个由两个字母组成的国家/地区代码，例如：us、ru、uk。  [默认: (空)]
    first: 该参数控制自然结果的偏移量。此参数默认为 0。例如 first=10 会将第 10 个自然结果移动到第一个位置。  [默认: 0]
    count: 该参数控制每页的结果数量。此参数仅为建议值，可能无法反映返回的结果数。  [默认: (空)]
    imagesize: 该参数用于按尺寸过滤图片。可用值：small - 小，medium - 中，large - 大，wallpaper - 超大。  [默认: (空)]
    color2: 该参数用于按颜色过滤图片。可用值：color - 仅彩色，bw - 黑白，FGcls_RED - 红色，FGcls_ORGANGE - 橙色，FGcls_YELLOW - 黄色，FGcls_GREEN - 绿色，FGcls_TEAL - 青色，FGcls_BLUE - 蓝色，FGcls_PURPLE - 紫色，FGcls_PINK - 粉色，FGcls_BROWN - 棕色，FGcls_BLACK - 黑色，FGcls_GRAY - 灰色，FGcls_WHITE - 白色。  [默认: (空)]
    photo: 该参数用于按图片类型过滤图片。可用值：photo - 照片，clipart - 剪贴画，linedrawing - 线条画，animatedgif - 动图，animatedgifhttps - HTTPS 动图，transparent - 透明，shopping - 购物。  [默认: (空)]
    aspect: 该参数用于按布局过滤图片。可用值：square - 方形，wide - 宽，tall - 高。  [默认: (空)]
    face: 该参数用于按人物类型过滤图片。可用值：face - 仅限面部，portrait - 头肩。  [默认: (空)]
    age: 该参数用于按日期过滤图片。可用值：lt1440 - 过去 24 小时，lt10080 - 过去一周，lt43200 - 过去一个月，lt525600 - 过去一年。  [默认: (空)]
    license: 该参数用于按使用许可过滤图片。可用值：Type-Any - 所有 Creative Commons，L1 - Public Domain，L2_L3_L4_L5_L6_L7 - 免费共享和使用，L2_L3_L4 - 免费共享和商业使用，L2_L3_L5_L6 - 免费修改、共享和使用，L2_L3 - 免费修改、共享和商业使用。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "mkt": mkt,
        "cc": cc,
        "first": first,
        "count": count,
        "imagesize": imagesize,
        "color2": color2,
        "photo": photo,
        "aspect": aspect,
        "face": face,
        "age": age,
        "license": license,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='bing_images', fields=form)

