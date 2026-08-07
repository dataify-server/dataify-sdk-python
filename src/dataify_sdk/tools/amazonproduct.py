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

def amazon_product_by_asin(asin: str = 'B0BZYCJK89', file_name: str = '{{TasksID}}', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_product_by-asin

    Parameters
    ----------
    asin: ASIN，该参数用于指定采集 Amazon 产品的唯一标识符。ASIN 通常是一个 10 位字母和数字的组合，比如 B0BZYCJK89。用于 amazon_product_by-asin。  [默认: B0BZYCJK89]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "asin": asin,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_product_by-asin',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def amazon_product_by_url(file_name: str = '{{TasksID}}', url: str = '', zip_code: str = '94107', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_product_by-url

    Parameters
    ----------
    url: URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_product_by-url、amazon_product_by-category-url；也可用于 amazon_product_by-best-sellers。  [默认: (空)]
    zip_code: 邮政编码，该参数用于指定采集页面中配送区域的邮政编码。用于 amazon_product_by-url，默认 94107。  [默认: 94107]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "zip_code": zip_code,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_product_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def amazon_product_by_keywords(file_name: str = '{{TasksID}}', highest_price: str = '50', keyword: str = 'coffee', lowest_price: str = '20', page_turning: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_product_by-keywords

    Parameters
    ----------
    keyword: 关键词，搜索产品的关键词。用于 amazon_product_by-keywords。  [默认: coffee]
    page_turning: 采集页数，请输入要采集多少页的产品。用于 amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。关键词采集默认 2，其它列表采集默认 1。  [默认: (空)]
    lowest_price: 最低价格，该参数用于指定要筛选的最低商品价格。用于 amazon_product_by-keywords。  [默认: 20]
    highest_price: 最高价格，该参数用于指定要筛选的最高商品价格。用于 amazon_product_by-keywords。  [默认: 50]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "page_turning": page_turning,
        "lowest_price": lowest_price,
        "highest_price": highest_price,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_product_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def amazon_product_by_category_url(collect_subcategories: str = '', file_name: str = '{{TasksID}}', page_turning: str = '', sort_by: str = '畅销排行', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_product_by-category-url

    Parameters
    ----------
    url: URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_product_by-url、amazon_product_by-category-url；也可用于 amazon_product_by-best-sellers。  [默认: (空)]
    page_turning: 采集页数，请输入要采集多少页的产品。用于 amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。关键词采集默认 2，其它列表采集默认 1。  [默认: (空)]
    sort_by: 排序方式。用于 amazon_product_by-category-url，仅传 cn 列：畅销排行、最新上架、平均评价、价格：从高到低、价格：从低到高、精选推荐。默认畅销排行。  [默认: 畅销排行]
    collect_subcategories: 收集子类别，该参数用于指定在主类别下要采集的子类别商品范围。仅在传入非空值时提交。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "page_turning": page_turning,
        "sort_by": sort_by,
        "collect_subcategories": collect_subcategories,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_product_by-category-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def amazon_product_by_best_sellers(file_name: str = '{{TasksID}}', page_turning: str = '', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Amazon 产品详情、商品详情、商品信息、产品信息、ASIN、产品 URL、关键词搜索、类别 URL 或畅销商品 URL 加采集、抓取、爬取、获取、提取时触发。复用一个工具提交 Amazon 产品详情采集 Builder 任务，支持 amazon_product_by-asin、amazon_product_by-url、amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: amazon.com
    spider_id: amazon_product_by-best-sellers

    Parameters
    ----------
    url: URLs，该参数用于指定待采集的访问 URL 地址。用于 amazon_product_by-url、amazon_product_by-category-url；也可用于 amazon_product_by-best-sellers。  [默认: (空)]
    page_turning: 采集页数，请输入要采集多少页的产品。用于 amazon_product_by-keywords、amazon_product_by-category-url、amazon_product_by-best-sellers。关键词采集默认 2，其它列表采集默认 1。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "page_turning": page_turning,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='amazon.com',
        spider_id='amazon_product_by-best-sellers',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

