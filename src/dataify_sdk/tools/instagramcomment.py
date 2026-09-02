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

def ins_comment_by_posturl(file_name: str = '{{TasksID}}', posturl: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Instagram 帖子评论、Instagram 评论、Instagram post comments、IG 帖子评论信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Instagram 帖子评论采集 Builder 任务，采集器标识固定为 ins_comment_by-posturl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: instagram.com
    spider_id: ins_comment_by-posturl

    Parameters
    ----------
    posturl: 帖子 URL，该参数用于指定待采集的 Instagram 的帖子 URL。用于 ins_comment_by-posturl，默认值为 https://www.instagram.com/cats_of_instagram/reel/C4GLo_eLO2e/。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "posturl": posturl,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='instagram.com',
        spider_id='ins_comment_by-posturl',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

