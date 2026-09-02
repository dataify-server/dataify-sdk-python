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

def amazon_product_list_by_keywords_domain(domain: str = 'https://www.amazon.com/', file_name: str = '{{TasksID}}', keyword: str = 'X-box', page_turning: str = '1', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 产品列表、Amazon 商品列表、Amazon 搜索结果列表、Amazon 关键词商品列表，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Amazon 产品列表采集 Builder 任务，采集器标识固定为 amazon_product-list_by-keywords-domain。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_product-list_by-keywords-domain

    Parameters
    ----------
    keyword: 关键词，搜索产品的关键词。用于 amazon_product-list_by-keywords-domain，默认值为 X-box。  [默认: X-box]
    domain: 域名，请输入需要搜索关键词的主域名，例如：https://www.amazon.com。用于 amazon_product-list_by-keywords-domain，默认值为 https://www.amazon.com/。  [默认: https://www.amazon.com/]
    page_turning: 采集页数，请输入要采集多少页的产品。即如果输入 2，就是需要把搜索结果页的第一页、第二页的所有产品都采集过来。默认值为 1。  [默认: 1]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "domain": domain,
        "page_turning": page_turning,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_product-list_by-keywords-domain',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

