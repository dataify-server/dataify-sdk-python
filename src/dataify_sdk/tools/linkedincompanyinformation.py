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

def linkedin_company_information_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 LinkedIn 公司信息、领英公司信息、LinkedIn company information、LinkedIn 公司 URL，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 LinkedIn 公司信息采集 Builder 任务，采集器标识固定为 linkedin_company_information_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: linkedin.com
    spider_id: linkedin_company_information_by-url

    Parameters
    ----------
    url: 公司URL，该参数用于指定要采集的公司URL。用于 linkedin_company_information_by-url，默认值为 https://www.linkedin.com/company/dynamo-software。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='linkedin.com',
        spider_id='linkedin_company_information_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

