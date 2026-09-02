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

def youtube_product_by_id(file_name: str = '{{TasksID}}', video_id: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 视频基本信息、YouTube 视频信息、YouTube 视频详情、YouTube product、视频基础资料，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 YouTube 视频基本信息采集 Builder 任务，采集器标识固定为 youtube_product_by-id。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_product_by-id

    Parameters
    ----------
    video_id: 视频唯一 ID，该参数用于指定待采集的 YouTube 视频的唯一 ID。用于 youtube_product_by-id，默认值为 8RePenzQH80。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "video_id": video_id,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_product_by-id',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

