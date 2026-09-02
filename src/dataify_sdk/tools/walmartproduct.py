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

def walmart_product_by_url(all_variations: str = '', file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Walmart 产品信息、Walmart 商品信息、Walmart 产品详情、Walmart 商品列表、Walmart product，与采集、抓取、爬取、获取、提取等动词组合时触发。从 walmart.com 提取商品列表、售价区间、品类分类、库存状态、配送方式、用户评价等数据。复用一个工具提交 Walmart 产品信息采集 Builder 任务，支持 walmart_product_by-url、walmart_product_by-category-url、walmart_product_by-sku 和 walmart_product_by-keywords。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: walmart.com
    spider_id: walmart_product_by-url

    Parameters
    ----------
    url: Walmart URL，该参数用于指定待采集的 Walmart 产品 URL。用于 walmart_product_by-url，默认值为 https://www.walmart.com/ip/HI-CHEW-Stand-Up-Pouch-Getaway-Mix-11-65oz/12284762931?athAsset=eyJhdGhjcGlkIjoiMTIyODQ3NjI5MzEiLCJhdGhzdGlkIjoiQ1MwNTV+Q1MwMDR+Q1MwOTgiLCJhdGhlZSI6eyJhIjoyNy44NCwiYiI6Mjk1MS40MSwidyI6MC4wMDk0MjcxMjc3OTA0NzcxMjMsImwiOjAuNX0sImF0aHBvc2IiOiI4IiwiYXRoYW5jaWQiOiIxMDE2NDUwNzU1IiwiYXRocmsiOjAuMH0%3D&athena=true&adsRedirect=true。  [默认: (空)]
    all_variations: 所有变体，该参数用于指定是否收集所有产品变量，设置为 true 为收集。参数值为 true 或 false；walmart_product_by-url 默认 true，其余采集器默认 false。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "all_variations": all_variations,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='walmart.com',
        spider_id='walmart_product_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def walmart_product_by_category_url(all_variations: str = '', category_url: str = '', file_name: str = '{{TasksID}}', page_turning: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Walmart 产品信息、Walmart 商品信息、Walmart 产品详情、Walmart 商品列表、Walmart product，与采集、抓取、爬取、获取、提取等动词组合时触发。从 walmart.com 提取商品列表、售价区间、品类分类、库存状态、配送方式、用户评价等数据。复用一个工具提交 Walmart 产品信息采集 Builder 任务，支持 walmart_product_by-url、walmart_product_by-category-url、walmart_product_by-sku 和 walmart_product_by-keywords。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: walmart.com
    spider_id: walmart_product_by-category-url

    Parameters
    ----------
    category_url: 类别URL，该参数用于指定 Walmart 的特定类别网址来查找新产品。用于 walmart_product_by-category-url，默认值为 https://www.walmart.com/shop/deals/food/。  [默认: (空)]
    all_variations: 所有变体，该参数用于指定是否收集所有产品变量，设置为 true 为收集。参数值为 true 或 false；walmart_product_by-url 默认 true，其余采集器默认 false。  [默认: (空)]
    page_turning: 页数限制，该参数用于指定采集结果数量的限制（请输入页数）。walmart_product_by-category-url 默认 1；walmart_product_by-keywords 默认 2。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "category_url": category_url,
        "all_variations": all_variations,
        "page_turning": page_turning,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='walmart.com',
        spider_id='walmart_product_by-category-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def walmart_product_by_sku(all_variations: str = '', file_name: str = '{{TasksID}}', sku: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Walmart 产品信息、Walmart 商品信息、Walmart 产品详情、Walmart 商品列表、Walmart product，与采集、抓取、爬取、获取、提取等动词组合时触发。从 walmart.com 提取商品列表、售价区间、品类分类、库存状态、配送方式、用户评价等数据。复用一个工具提交 Walmart 产品信息采集 Builder 任务，支持 walmart_product_by-url、walmart_product_by-category-url、walmart_product_by-sku 和 walmart_product_by-keywords。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: walmart.com
    spider_id: walmart_product_by-sku

    Parameters
    ----------
    sku: SKU，该参数用于指定待采集的 SKU 产品唯一代码。用于 walmart_product_by-sku，默认值为 439179861。  [默认: (空)]
    all_variations: 所有变体，该参数用于指定是否收集所有产品变量，设置为 true 为收集。参数值为 true 或 false；walmart_product_by-url 默认 true，其余采集器默认 false。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "sku": sku,
        "all_variations": all_variations,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='walmart.com',
        spider_id='walmart_product_by-sku',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def walmart_product_by_keywords(all_variations: str = '', domain: str = '', file_name: str = '{{TasksID}}', keyword: str = '', page_turning: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Walmart 产品信息、Walmart 商品信息、Walmart 产品详情、Walmart 商品列表、Walmart product，与采集、抓取、爬取、获取、提取等动词组合时触发。从 walmart.com 提取商品列表、售价区间、品类分类、库存状态、配送方式、用户评价等数据。复用一个工具提交 Walmart 产品信息采集 Builder 任务，支持 walmart_product_by-url、walmart_product_by-category-url、walmart_product_by-sku 和 walmart_product_by-keywords。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: walmart.com
    spider_id: walmart_product_by-keywords

    Parameters
    ----------
    keyword: 关键词，该参数用于指定采集的搜索关键词。用于 walmart_product_by-keywords，默认值为 leggins。  [默认: (空)]
    domain: 主域名，该参数用于指定采集 Walmart 产品信息的主域名。用于 walmart_product_by-keywords，默认值为 https://www.walmart.com/。  [默认: (空)]
    all_variations: 所有变体，该参数用于指定是否收集所有产品变量，设置为 true 为收集。参数值为 true 或 false；walmart_product_by-url 默认 true，其余采集器默认 false。  [默认: (空)]
    page_turning: 页数限制，该参数用于指定采集结果数量的限制（请输入页数）。walmart_product_by-category-url 默认 1；walmart_product_by-keywords 默认 2。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "domain": domain,
        "all_variations": all_variations,
        "page_turning": page_turning,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='walmart.com',
        spider_id='walmart_product_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

