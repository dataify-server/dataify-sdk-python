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

def zillow_product_by_filter(HomeType: str = '', days_on_zillow: str = '', file_name: str = '{{TasksID}}', keywords_location: str = '', listingCategory: str = '', maximum: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Zillow 房产信息、Zillow 房产详细信息、Zillow 房源信息、Zillow property details，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Zillow 房产详细信息采集 Builder 任务，采集器标识固定为 zillow_product_by-filter。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: zillow.com
    spider_id: zillow_product_by-filter

    Parameters
    ----------
    keywords_location: 地点关键词，该参数用于指定 Zillow 搜索页面的搜索地址信息，可以是邮政编码、具体城市或地址。用于 zillow_product_by-filter，默认值为 South Bend。  [默认: (空)] (上游字段: keywords-location)
    listingCategory: 列表类别，该参数用于指定 Zillow 搜索房产类别的参数。可选值：Sold、For Rent、For Sale。默认值为 For Rent。  [默认: (空)]
    HomeType: 主页类型，该参数用于指定 Zillow 搜索房产主页类型的参数。可选值：Houses、Townhomes、Multi-family、Condos/Co-ops、Lots/Land、Apartments、Manufactured。默认值为 Houses。  [默认: (空)]
    days_on_zillow: 在zillow上的日子，该参数用于指定采集发布在 Zillow 网站多久时长的房屋。可选值：Any、1 day、7 days、14 days、30 days、90 days、6 months、12 months、24 months、36 months。默认值为 Any。  [默认: (空)]
    maximum: 最大数量，该参数用于指定采集的最大数量。默认值为 10。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keywords-location": keywords_location,
        "listingCategory": listingCategory,
        "HomeType": HomeType,
        "days_on_zillow": days_on_zillow,
        "maximum": maximum,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='zillow.com',
        spider_id='zillow_product_by-filter',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

