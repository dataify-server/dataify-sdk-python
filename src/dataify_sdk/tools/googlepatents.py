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

def google_patents(after: str = '', assignee: str = '', before: str = '', clustered: str = '', country: str = '', dups: str = 'family', inventor: str = '', json_: str = '1', language: str = '', litigation: str = '', no_cache: str = 'false', num: str = '', page: str = '1', patents: str = 'true', q: str = '', scholar: str = 'false', sort: str = '', status: str = '', type_: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义您想要搜索的查询内容。您可以使用分号 ; 分隔多个搜索词。例如：(Coffee) OR (Tea);(A47J)。

    上游接口: Search Engine (POST /request)
    engine: google_patents

    Parameters
    ----------
    q: 该参数定义您想要搜索的查询内容。您可以使用分号 ; 分隔多个搜索词。例如：(Coffee) OR (Tea);(A47J)。  [默认: (空)]
    json_: 该参数定义采集结果的输出格式；可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    page: 该参数定义页码，用于分页。1（默认）是第一页结果，2 是第二页结果，依此类推。  [默认: 1]
    num: 该参数控制每页的结果数量。最小值：10，最大值：100。  [默认: (空)]
    sort: 该参数定义排序方法。默认按相关性排序。可用值：new - Newest，old - Oldest。  [默认: (空)]
    clustered: 该参数定义结果的分组方式。支持的值：true - 按分类分组。  [默认: (空)]
    dups: 该参数定义去重方法。可选 family（Family，默认）或 language（Publication）。  [默认: family]
    patents: 该参数控制是否包含 Google 专利结果，默认为 true。参数值：true。  [默认: true]
    scholar: 该参数控制是否包含 Google 学术结果，默认为 false。参数值：true。  [默认: false]
    before: 该参数定义结果的最大日期。格式为 type:YYYYMMDD，type 可以是 priority、filing、publication 之一。例如：priority:20221231、publication:20230101。  [默认: (空)]
    after: 该参数定义结果的最小日期。格式为 type:YYYYMMDD，type 可以是 priority、filing、publication 之一。例如：priority:20221231、publication:20230101。  [默认: (空)]
    inventor: 该参数定义专利的发明人。使用逗号 , 分隔多个发明人。将包含逗号的名称括在括号中，例如：(Doe, John)。  [默认: (空)]
    assignee: 该参数定义专利的受让人。使用逗号 , 分隔多个受让人。将包含逗号的名称括在括号中，例如：(Tesla, Inc)。  [默认: (空)]
    country: 该参数按国家/地区过滤专利结果。使用逗号 , 分隔多个国家/地区代码。例如：WO,US。  [默认: (空)]
    language: 该参数按语言过滤专利结果。使用逗号 , 分隔多个语言。  [默认: (空)]
    status: 该参数按状态过滤专利结果。支持的值：GRANT - 授权专利，APPLICATION - 专利申请。  [默认: (空)]
    type_: 该参数按类型过滤专利结果。支持的值：PATENT - 专利，DESIGN - 外观设计。  [默认: (空)] (上游字段: type)
    litigation: 该参数按诉讼状态过滤专利结果。支持的值：YES - 有相关诉讼，NO - 无已知诉讼。  [默认: (空)]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果；将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果；缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "page": page,
        "num": num,
        "sort": sort,
        "clustered": clustered,
        "dups": dups,
        "patents": patents,
        "scholar": scholar,
        "before": before,
        "after": after,
        "inventor": inventor,
        "assignee": assignee,
        "country": country,
        "language": language,
        "status": status,
        "type": type_,
        "litigation": litigation,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_patents', fields=form)

