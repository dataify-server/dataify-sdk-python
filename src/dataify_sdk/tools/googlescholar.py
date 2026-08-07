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

def google_scholar(as_rr: str = '0', as_sdt: str = '0', as_vis: str = '0', as_yhi: str = '', as_ylo: str = '', cites: str = '', cluster: str = '', filter: str = '1', hl: str = '', json_: str = '1', lr: str = '', no_cache: str = 'false', num: str = '10', q: str = '', safe: str = '', scisbd: str = '0', start: str = '0', client: DataifyClient | None = None) -> dict[str, Any]:
    """该参数定义您想要搜索的查询内容。

    上游接口: Search Engine (POST /request)
    engine: google_scholar

    Parameters
    ----------
    q: 该参数定义您想要搜索的查询内容。  [默认: (空)]
    json_: 该参数定义采集结果的输出格式。可选择 JSON、HTML（支持下载）格式，默认为 JSON；1 返回 JSON，2 返回 JSON+HTML，3 返回 HTML，4 返回 Light JSON。  [默认: 1] (上游字段: json)
    hl: 该参数定义 Google 职位搜索要使用的语言。它是一个两位数的语言代码，例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    lr: 该参数定义一个或多个将搜索限制在的语言。它使用 lang_{两位语言代码} 指定语言，并使用 | 作为分隔符，例如 lang_fr|lang_de 将仅搜索法语和德语的页面。  [默认: (空)]
    start: 该参数定义结果偏移量。它跳过指定数量的结果，用于分页。例如 0（默认）是第一页结果，10 是第二页结果，20 是第三页结果，依此类推。  [默认: 0]
    num: 该参数定义返回的最大结果数量，范围为 1 到 20，默认为 10。  [默认: 10]
    cites: 该参数定义用于触发“被引”搜索的文章唯一 ID。使用 cites 将显示 Google 学术中引用该文献的列表。示例值：cites=1275980731835430123。cites 和 q 参数同时使用会触发在引用文献中的搜索。  [默认: (空)]
    as_ylo: 该参数定义您希望包含结果的起始年份。例如将 as_ylo 设置为 2018 年，则该年份之前的结果将被省略。此参数可与 as_yhi 参数结合使用。  [默认: (空)]
    as_yhi: 该参数定义您希望包含结果的结束年份。例如将 as_yhi 设置为 2018 年，则该年份之后的结果将被省略。此参数可与 as_ylo 参数结合使用。  [默认: (空)]
    scisbd: 该参数定义过去一年添加的文献，按日期排序。可设置为 1 以仅包含摘要，或设置为 2 以包含全部内容。默认值为 0，表示文献按相关性排序。  [默认: 0]
    cluster: 该参数定义用于触发“所有版本”搜索的文章唯一 ID。示例值：cluster=1275980731835430123。禁止将 cluster 与 q 和 cites 参数一起使用。请仅使用 cluster 参数。  [默认: (空)]
    as_sdt: 该参数既可用作搜索类型，也可用作过滤器。作为过滤器（仅在搜索文章时有效）：0 排除专利（默认），7 包含专利。作为搜索类型：4 选择判例法（仅限美国法院）。  [默认: 0]
    safe: 该参数定义成人内容的过滤级别。可以设置为 active 或 off，默认情况下 Google 会模糊处理露骨内容。  [默认: (空)]
    filter: 该参数定义“类似结果”和“省略结果”的过滤器是开启还是关闭。可以设置为 1（默认）以启用这些过滤器，或设置为 0 以禁用这些过滤器。  [默认: 1]
    as_vis: 该参数定义是否希望包含引用。可以设置为 1 以排除这些结果，或设置为 0（默认）以包含它们。  [默认: 0]
    as_rr: 该参数定义是否仅显示综述文章（这些文章包括主题综述，或讨论您搜索的作品或作者）。可以设置为 1 以启用此过滤器，或设置为 0（默认）以显示所有结果。  [默认: 0]
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。将 no_cache 设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "hl": hl,
        "lr": lr,
        "start": start,
        "num": num,
        "cites": cites,
        "as_ylo": as_ylo,
        "as_yhi": as_yhi,
        "scisbd": scisbd,
        "cluster": cluster,
        "as_sdt": as_sdt,
        "safe": safe,
        "filter": filter,
        "as_vis": as_vis,
        "as_rr": as_rr,
        "no_cache": no_cache,
    }
    return _client(client).request_serp(engine='google_scholar', fields=form)

