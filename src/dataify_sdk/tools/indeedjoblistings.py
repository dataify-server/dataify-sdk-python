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

def indeed_job_listings_by_job_url(file_name: str = '{{TasksID}}', job_url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Indeed 职位列表、Indeed 职位信息、Indeed job listings、Indeed job URL，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Indeed 职位列表采集 Builder 任务，采集器标识固定为 indeed_job-listings_by-job-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: indeed.com
    spider_id: indeed_job-listings_by-job-url

    Parameters
    ----------
    job_url: Indeed职位URL，该参数用于指定采集的 Indeed 职位 URL。用于 indeed_job-listings_by-job-url，默认值为 https://fr.indeed.com/viewjob?jk=55b3e5dfa0c2ff66。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "job_url": job_url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='indeed.com',
        spider_id='indeed_job-listings_by-job-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

