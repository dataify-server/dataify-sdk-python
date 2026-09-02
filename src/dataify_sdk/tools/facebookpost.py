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

def facebook_post_by_posts_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Facebook 帖子、Facebook 帖子信息、Facebook post、帖子内容，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Facebook 帖子采集 Builder 任务，采集器标识固定为 facebook_post_by-posts-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: facebook.com
    spider_id: facebook_post_by-posts-url

    Parameters
    ----------
    url: 帖子 URL，该参数用于指定要采集的 Facebook 帖子 URL。用于 facebook_post_by-posts-url，默认值为 https://www.facebook.com/permalink.php?story_fbid=pfbid0gNjZBhqCxSqj9xJS5aygNwqFqNEM2fYbTFKKbsvvGdEfTgFyAYWSckvkEHPqAE7gl&id=61574926580533&rdid=86oaujwNGCCdPLfj#。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='facebook.com',
        spider_id='facebook_post_by-posts-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

