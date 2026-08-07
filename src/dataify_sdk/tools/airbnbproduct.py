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

def airbnb_product_by_searchurl(country: str = '', file_name: str = '{{TasksID}}', searchurl: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Airbnb房产信息、Airbnb房源信息、Airbnb房源搜索、Airbnb product、Airbnb homes，与采集、抓取、爬取、获取、提取等动词组合时触发。提交 Airbnb房产信息采集 Builder 任务，采集器标识固定为 airbnb_product_by-searchurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: airbnb.com
    spider_id: airbnb_product_by-searchurl

    Parameters
    ----------
    searchurl: 网址，该参数用于指定采集 Airbnb 中的房源搜索网址。用于 airbnb_product_by-searchurl，默认值为 https://www.airbnb.com/s/Greece/homes?query=Greece&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJY2xxEcdKWxMRHS2a3HUXOjY&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2025-03-01&monthly_length=3&monthly_end_date=2025-06-01&search_mode=regular_search&price_filter_input_type=0&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=5&flexible_date_search_filter_type=1。  [默认: (空)]
    country: 国家，该参数用于指定采集 Airbnb 中的房源所属国家。非必填，默认值为 HK，参数值取国家列表中的 typeValue 列。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "searchurl": searchurl,
        "country": country,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='airbnb.com',
        spider_id='airbnb_product_by-searchurl',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

