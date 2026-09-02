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

def reddit_comment_by_url(comment_limit: str = '', days_back: str = '', file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Reddit 帖子评论、Reddit 评论、Reddit post comments、Reddit 回复信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Reddit 帖子评论采集 Builder 任务，采集器标识固定为 reddit_comment_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: reddit.com
    spider_id: reddit_comment_by-url

    Parameters
    ----------
    url: Reddit URL，该参数用于指定采集 Reddit 帖子的 URL。用于 reddit_comment_by-url，默认值为 https://www.reddit.com/r/datascience/comments/1cmnf0m/comment/l32204i/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button。  [默认: (空)]
    days_back: 发布天数限制，该参数用于指定采集您输入的天数内发布的所有评论。默认值为 10。  [默认: (空)]
    comment_limit: 回复数量限制，该参数用于指定采集评论时返回的回复评论数量。默认值为 5。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "days_back": days_back,
        "comment_limit": comment_limit,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='reddit.com',
        spider_id='reddit_comment_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

