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

def google_news(gl: str = 'us', hl: str = '', json_: str = '1', kgmid: str = '', no_cache: str = 'false', publication_token: str = '', q: str = 'pizza', section_token: str = '', so: str = '0', story_token: str = '', topic_token: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """定义搜索的查询内容，默认值为 pizza。

    上游接口: Search Engine (POST /request)
    engine: google_news

    Parameters
    ----------
    q: 定义搜索的查询内容，默认值为 pizza。  [默认: pizza]
    json_: 定义采集结果的输出格式。1 返回 JSON 格式数据，2 返回 JSON+HTML 格式数据，3 返回 HTML 格式数据，4 返回 Light JSON。默认值为 1。  [默认: 1] (上游字段: json)
    no_cache: 默认情况下，5 分钟内缓存相同参数的搜索结果。设为 true 可跳过缓存，设为 false（默认）则使用缓存结果。缓存搜索免费，且不计入搜索统计。  [默认: false]
    gl: 定义 Google 搜索要使用的国家/地区。它是一个两位数的国家/地区代码。例如 us 代表美国，uk 代表英国，fr 代表法国。默认值 us  [默认: us]
    hl: 定义 Google 搜索要使用的语言。它是一个两位数的语言代码。例如 en 代表英语，es 代表西班牙语，fr 代表法语。  [默认: (空)]
    topic_token: 定义 Google 新闻主题令牌。用于访问特定主题，例如世界、商业、科技。  [默认: (空)]
    kgmid: 定义 Google 新闻结果中主题或地点的知识图谱 ID（KGMID）。它是一个以 /m/ 或 /g/ 开头的字符串。例如 /m/0vzm 是德克萨斯州奥斯汀的 kgmid。  [默认: (空)]
    publication_token: 定义 Google 新闻出版物令牌。用于访问来自特定发布者，例如 CNN、BBC、卫报的新闻结果。  [默认: (空)]
    section_token: 定义 Google 新闻版块令牌。用于访问特定主题的子版块，例如“商业 -> 经济”。  [默认: (空)]
    story_token: 定义 Google 新闻报道令牌。用于访问特定报道的完整报道新闻结果。  [默认: (空)]
    so: 定义排序方法。结果可以按相关性或日期排序，默认按相关性排序。0 表示相关性，1 表示日期。  [默认: 0]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    form = {
        "q": q,
        "json": json_,
        "no_cache": no_cache,
        "gl": gl,
        "hl": hl,
        "topic_token": topic_token,
        "kgmid": kgmid,
        "publication_token": publication_token,
        "section_token": section_token,
        "story_token": story_token,
        "so": so,
    }
    return _client(client).request_serp(engine='google_news', fields=form)

