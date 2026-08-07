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

def yandex_search(family_mode: str = '1', fix_typo: str = 'true', groups_on_page: str = '10', json_: str = '1', lang: str = 'en', lr: str = '', no_cache: str = 'false', p: str = '0', text: str = 'pizza', yandex_domain: str = 'yandex.com', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义搜索查询，默认值为 pizza。您可以使用常规 Yandex 搜索中使用的任何内容。

    上游接口: Search Engine (POST /request)
    engine: yandex

    Parameters
    ----------
    text: 该参数定义搜索查询，默认值为 pizza。您可以使用常规 Yandex 搜索中使用的任何内容。  [默认: pizza]
    json_: 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    yandex_domain: 该参数定义要使用的 Yandex 域名。默认为 yandex.com。可用值：yandex.com、yandex.ru、ya.ru、yandex.by、yandex.kz、yandex.uz、yandex.com.tr、yandex.az、yandex.com.ge、yandex.com.am、yandex.co.il、yandex.md、yandex.tm、yandex.tj、yandex.eu。  [默认: yandex.com]
    lang: 该参数定义 Yandex 搜索要使用的语言。当 yandex_domain 为 yandex.com 时，默认为 en。  [默认: en]
    lr: 该参数定义将搜索结果限制在的国家或地区 ID。  [默认: (空)]
    p: 该参数定义页码。分页从 0 开始。  [默认: 0]
    family_mode: 该参数启用或禁用家庭模式（安全搜索）。可设置为：0 - 关闭，1 - 中等，2 - 严格。默认为 1（中等）。  [默认: 1]
    fix_typo: 该参数启用或禁用自动拼写纠正。可设置为 true 或 false。默认为 true。  [默认: true]
    groups_on_page: 该参数定义单页结果上显示的最大群组数。默认为 10。  [默认: 10]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "text": text,
        "json": json_,
        "yandex_domain": yandex_domain,
        "lang": lang,
        "lr": lr,
        "p": p,
        "family_mode": family_mode,
        "fix_typo": fix_typo,
        "groups_on_page": groups_on_page,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='yandex', fields=form)

