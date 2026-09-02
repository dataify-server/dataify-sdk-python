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

def ebay_ebay_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 ebay 信息、eBay 商品信息、eBay 产品信息、eBay 类别商品、eBay 店铺商品，与采集、抓取、爬取、获取、提取等动词组合时触发。从 ebay.com 提取商品列表、售价区间、卖家详情、拍卖记录、库存状态、用户评价、物流配送信息等数据。复用一个工具提交 eBay 信息采集 Builder 任务，支持 ebay_ebay_by-url、ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: ebay.com
    spider_id: ebay_ebay_by-url

    Parameters
    ----------
    url: eBay URL 或 Category URL。用于 ebay_ebay_by-url 时默认值为 https://www.ebay.com/itm/296197468977?itmmeta=01HRWJ04NFHYT9AX0XZB8F18G1&hash=item44f6beb331%3Ag%3ADEQAAOSw3CxlhTJ%7E&_trkparms=%2526rpp_cid%253D6523c97b0b7882040b9472b6；用于 ebay_ebay_by-category-url 时默认值为 https://www.ebay.com/b/Collectible-Japanese-Bells-1900-Now/165467/bn_3104829；用于 ebay_ebay_by-listurl 时默认值为 https://www.ebay.com/str/kptradingdeals?_trksid=p4429486.m145687.l149086。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='ebay.com',
        spider_id='ebay_ebay_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def ebay_ebay_by_category_url(count: str = '', file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 ebay 信息、eBay 商品信息、eBay 产品信息、eBay 类别商品、eBay 店铺商品，与采集、抓取、爬取、获取、提取等动词组合时触发。从 ebay.com 提取商品列表、售价区间、卖家详情、拍卖记录、库存状态、用户评价、物流配送信息等数据。复用一个工具提交 eBay 信息采集 Builder 任务，支持 ebay_ebay_by-url、ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: ebay.com
    spider_id: ebay_ebay_by-category-url

    Parameters
    ----------
    url: eBay URL 或 Category URL。用于 ebay_ebay_by-url 时默认值为 https://www.ebay.com/itm/296197468977?itmmeta=01HRWJ04NFHYT9AX0XZB8F18G1&hash=item44f6beb331%3Ag%3ADEQAAOSw3CxlhTJ%7E&_trkparms=%2526rpp_cid%253D6523c97b0b7882040b9472b6；用于 ebay_ebay_by-category-url 时默认值为 https://www.ebay.com/b/Collectible-Japanese-Bells-1900-Now/165467/bn_3104829；用于 ebay_ebay_by-listurl 时默认值为 https://www.ebay.com/str/kptradingdeals?_trksid=p4429486.m145687.l149086。  [默认: (空)]
    count: 数量，该参数用于指定采集结果的最大数量。用于 ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl，默认值为 60。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "count": count,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='ebay.com',
        spider_id='ebay_ebay_by-category-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def ebay_ebay_by_keywords(count: str = '', file_name: str = '{{TasksID}}', keywords: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 ebay 信息、eBay 商品信息、eBay 产品信息、eBay 类别商品、eBay 店铺商品，与采集、抓取、爬取、获取、提取等动词组合时触发。从 ebay.com 提取商品列表、售价区间、卖家详情、拍卖记录、库存状态、用户评价、物流配送信息等数据。复用一个工具提交 eBay 信息采集 Builder 任务，支持 ebay_ebay_by-url、ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: ebay.com
    spider_id: ebay_ebay_by-keywords

    Parameters
    ----------
    keywords: 关键词，该参数用于指定采集 eBay 产品的搜索关键词。用于 ebay_ebay_by-keywords，默认值为 baby toys。  [默认: (空)]
    count: 数量，该参数用于指定采集结果的最大数量。用于 ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl，默认值为 60。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keywords": keywords,
        "count": count,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='ebay.com',
        spider_id='ebay_ebay_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def ebay_ebay_by_listurl(count: str = '', file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 ebay 信息、eBay 商品信息、eBay 产品信息、eBay 类别商品、eBay 店铺商品，与采集、抓取、爬取、获取、提取等动词组合时触发。从 ebay.com 提取商品列表、售价区间、卖家详情、拍卖记录、库存状态、用户评价、物流配送信息等数据。复用一个工具提交 eBay 信息采集 Builder 任务，支持 ebay_ebay_by-url、ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: ebay.com
    spider_id: ebay_ebay_by-listurl

    Parameters
    ----------
    url: eBay URL 或 Category URL。用于 ebay_ebay_by-url 时默认值为 https://www.ebay.com/itm/296197468977?itmmeta=01HRWJ04NFHYT9AX0XZB8F18G1&hash=item44f6beb331%3Ag%3ADEQAAOSw3CxlhTJ%7E&_trkparms=%2526rpp_cid%253D6523c97b0b7882040b9472b6；用于 ebay_ebay_by-category-url 时默认值为 https://www.ebay.com/b/Collectible-Japanese-Bells-1900-Now/165467/bn_3104829；用于 ebay_ebay_by-listurl 时默认值为 https://www.ebay.com/str/kptradingdeals?_trksid=p4429486.m145687.l149086。  [默认: (空)]
    count: 数量，该参数用于指定采集结果的最大数量。用于 ebay_ebay_by-category-url、ebay_ebay_by-keywords 和 ebay_ebay_by-listurl，默认值为 60。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "count": count,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='ebay.com',
        spider_id='ebay_ebay_by-listurl',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

