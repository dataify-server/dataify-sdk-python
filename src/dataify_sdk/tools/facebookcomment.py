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

def facebook_comment_by_comments_url(comments_sort: str = '', file_name: str = '{{TasksID}}', get_all_replies: str = '', limit_records: str = '', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Facebook 帖子评论、Facebook 评论、Facebook post comments、帖子回复信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Facebook 帖子评论采集 Builder 任务，采集器标识固定为 facebook_comment_by-comments-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: facebook.com
    spider_id: facebook_comment_by-comments-url

    Parameters
    ----------
    url: 帖子 URL，该参数用于指定要采集的 Facebook 帖子 URL。用于 facebook_comment_by-comments-url，默认值为 https://www.facebook.com/share/p/1K6xfHFkrK/。  [默认: (空)]
    get_all_replies: 全部回复，该参数用于指定是否要采集全部回复。选择 True 则采集全部回复，优先级高于 limit_records。可选值：True、False，默认值为 True。  [默认: (空)]
    limit_records: 回复数量上限，该参数用于指定采集的最多回复数量。当值为空时，采集数量默认 1 页（最多 10 条）。默认值为 10。  [默认: (空)]
    comments_sort: 评论排序方式。可选值：All comments、Most Relevent、Newest；默认值为 All comments。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "get_all_replies": get_all_replies,
        "limit_records": limit_records,
        "comments_sort": comments_sort,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='facebook.com',
        spider_id='facebook_comment_by-comments-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

