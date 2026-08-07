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

def youtube_comment_by_id(file_name: str = '{{TasksID}}', load_replies: str = '10', num_of_comments: str = '10', sort_by: str = 'Top comments', video_id: str = '8RePenzQH80', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 评论信息、YouTube 视频评论、YouTube 评论列表、YouTube comment、视频评论信息，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 YouTube 评论信息采集 Builder 任务，采集器标识固定为 youtube_comment_by-id。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_comment_by-id

    Parameters
    ----------
    video_id: 视频唯一 ID，该参数用于指定待采集的 YouTube 视频的唯一 ID。用于 youtube_comment_by-id，默认值为 8RePenzQH80。  [默认: 8RePenzQH80]
    load_replies: 加载回复，该参数用于指定页面加载回复时用到的时间。用于 youtube_comment_by-id，默认值为 10。  [默认: 10]
    num_of_comments: 评论数量，该参数用于指定需要采集的评论数量。用于 youtube_comment_by-id，默认值为 10。  [默认: 10]
    sort_by: 评论排序方式，该参数用于指定 YouTube 评论排序。用于 youtube_comment_by-id，可选值：Top comments、Newest first，默认值为 Top comments。  [默认: Top comments]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "video_id": video_id,
        "load_replies": load_replies,
        "num_of_comments": num_of_comments,
        "sort_by": sort_by,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_comment_by-id',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

