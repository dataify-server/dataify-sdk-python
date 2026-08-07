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

def amazon_global_product_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 全球产品详情、Amazon 全球商品详情、Amazon 全球产品信息、全球商品信息、Amazon 全球产品 URL、类别 URL、关键词搜索、关键词品牌搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Amazon 全球产品详情采集 Builder 任务，支持 amazon_global-product_by-url、amazon_global-product_by-category-url、amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_global-product_by-url

    Parameters
    ----------
    url: URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_global-product_by-url、amazon_global-product_by-category-url；未传时按采集器使用文档默认 URL。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_global-product_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def amazon_global_product_by_category_url(file_name: str = '{{TasksID}}', get_sponsored: str = '', maximum: str = '5', sort_by: str = '畅销排行', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 全球产品详情、Amazon 全球商品详情、Amazon 全球产品信息、全球商品信息、Amazon 全球产品 URL、类别 URL、关键词搜索、关键词品牌搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Amazon 全球产品详情采集 Builder 任务，支持 amazon_global-product_by-url、amazon_global-product_by-category-url、amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_global-product_by-category-url

    Parameters
    ----------
    url: URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_global-product_by-url、amazon_global-product_by-category-url；未传时按采集器使用文档默认 URL。  [默认: (空)]
    maximum: 最大数量，该参数用于指定采集的最大数量。用于 amazon_global-product_by-category-url，默认值为 5。  [默认: 5]
    sort_by: 排序方式。用于 amazon_global-product_by-category-url，仅传 cn 列：畅销排行、最新上架、平均评价、价格：从高到低、价格：从低到高、精选推荐。默认畅销排行。  [默认: 畅销排行]
    get_sponsored: 获取赞助商品。用于 amazon_global-product_by-category-url，参数值为 true 或 false，默认值为 true。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "maximum": maximum,
        "sort_by": sort_by,
        "get_sponsored": get_sponsored,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_global-product_by-category-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def amazon_global_product_by_keywords(domain: str = 'https://www.amazon.com', file_name: str = '{{TasksID}}', highest_price: str = '50', keyword: str = '', lowest_price: str = '20', page_turning: str = '2', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 全球产品详情、Amazon 全球商品详情、Amazon 全球产品信息、全球商品信息、Amazon 全球产品 URL、类别 URL、关键词搜索、关键词品牌搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Amazon 全球产品详情采集 Builder 任务，支持 amazon_global-product_by-url、amazon_global-product_by-category-url、amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_global-product_by-keywords

    Parameters
    ----------
    keyword: 关键词，搜索产品的关键词。amazon_global-product_by-keywords 默认 coffee；amazon_global-product_by-keywords-brand 默认 shirts。  [默认: (空)]
    domain: 域名，请输入需要搜索关键词的主域名，例如：https://www.amazon.com。用于 amazon_global-product_by-keywords，默认值为 https://www.amazon.com。  [默认: https://www.amazon.com]
    lowest_price: 最低价格，该参数用于指定要筛选的最低商品价格。用于 amazon_global-product_by-keywords，默认值为 20。  [默认: 20]
    highest_price: 最高价格，该参数用于指定要筛选的最高商品价格。用于 amazon_global-product_by-keywords，默认值为 50。  [默认: 50]
    page_turning: 采集页数，请输入要采集多少页的产品。用于 amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand，默认值为 2。  [默认: 2]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "domain": domain,
        "lowest_price": lowest_price,
        "highest_price": highest_price,
        "page_turning": page_turning,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_global-product_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def amazon_global_product_by_keywords_brand(brands: str = 'Adidas', file_name: str = '{{TasksID}}', keyword: str = '', page_turning: str = '2', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 全球产品详情、Amazon 全球商品详情、Amazon 全球产品信息、全球商品信息、Amazon 全球产品 URL、类别 URL、关键词搜索、关键词品牌搜索，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Amazon 全球产品详情采集 Builder 任务，支持 amazon_global-product_by-url、amazon_global-product_by-category-url、amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_global-product_by-keywords-brand

    Parameters
    ----------
    keyword: 关键词，搜索产品的关键词。amazon_global-product_by-keywords 默认 coffee；amazon_global-product_by-keywords-brand 默认 shirts。  [默认: (空)]
    brands: 品牌，该参数用于指定采集的品牌信息，请输入 Amazon 平台有的品牌名称，如果找不到该品牌选项，则采集字段将为空。用于 amazon_global-product_by-keywords-brand，默认值为 Adidas。  [默认: Adidas]
    page_turning: 采集页数，请输入要采集多少页的产品。用于 amazon_global-product_by-keywords、amazon_global-product_by-keywords-brand，默认值为 2。  [默认: 2]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "brands": brands,
        "page_turning": page_turning,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_global-product_by-keywords-brand',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

