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

def tiktok_comment_by_url(file_name: str = '{{TasksID}}', page_turning: str = '', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 TikTok 评论信息、Tiktok 评论信息、TikTok 帖子评论、Tiktok 视频评论、TikTok comment，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 TikTok 评论信息采集 Builder 任务，采集器标识固定为 tiktok_comment_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: tiktok.com
    spider_id: tiktok_comment_by-url

    Parameters
    ----------
    url: TikTok 帖子 URL，该参数用于指定待采集的 TikTok 具体帖子网址。用于 tiktok_comment_by-url，默认值为 https://www.tiktok.com/@heymrcat/video/7216019547806092550。  [默认: (空)]
    page_turning: 页数限制，该参数用于指定采集结果数量的限制（请输入页数）。用于 tiktok_comment_by-url，可选参数，默认值为 1。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "page_turning": page_turning,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='tiktok.com',
        spider_id='tiktok_comment_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

