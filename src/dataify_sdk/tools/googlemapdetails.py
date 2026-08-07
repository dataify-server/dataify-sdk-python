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

def google_map_details_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Google 地图信息、Google 地图详细信息、Google Maps details、Google 商家信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Google 地图详细信息采集 Builder 任务，支持 google_map-details_by-url、google_map-details_by-cid、google_map-details_by-location 和 google_map-details_by-placeid。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: google.com
    spider_id: google_map-details_by-url

    Parameters
    ----------
    url: Google 地图 URL，该参数用于指定待采集的 Google 地图访问链接信息。用于 google_map-details_by-url，默认值为 https://www.google.com/maps/place/Pizza+Inn+Magdeburg/data=!4m7!3m6!1s0x47a5f50c083530a3:0xfdba8746b538141!8m2!3d52.1263086!4d11.6094743!16s%2Fg%2F11kqmtk3dt!19sChIJozA1CAz1pUcRQYFTa3So2w8?authuser=0&hl=en&rclk=1。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='google.com',
        spider_id='google_map-details_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def google_map_details_by_cid(CID: str = '', file_name: str = '{{TasksID}}', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Google 地图信息、Google 地图详细信息、Google Maps details、Google 商家信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Google 地图详细信息采集 Builder 任务，支持 google_map-details_by-url、google_map-details_by-cid、google_map-details_by-location 和 google_map-details_by-placeid。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: google.com
    spider_id: google_map-details_by-cid

    Parameters
    ----------
    CID: CID，该参数用于指定待采集的 CID 信息。用于 google_map-details_by-cid，默认值为 2476046430038551731。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "CID": CID,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='google.com',
        spider_id='google_map-details_by-cid',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def google_map_details_by_location(country: str = '', file_name: str = '{{TasksID}}', keyword: str = '', lat: str = '', long: str = '', zoom_level: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Google 地图信息、Google 地图详细信息、Google Maps details、Google 商家信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Google 地图详细信息采集 Builder 任务，支持 google_map-details_by-url、google_map-details_by-cid、google_map-details_by-location 和 google_map-details_by-placeid。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: google.com
    spider_id: google_map-details_by-location

    Parameters
    ----------
    keyword: Google 关键词，该参数用于指定通过特定关键词搜索地图信息，可以是位置、邮政编码或类别。用于 google_map-details_by-location，默认值为 pizza。  [默认: (空)]
    country: Google 国家，该参数用于指定要搜索的国家。用于 google_map-details_by-location，默认值为 United States。  [默认: (空)]
    lat: 纬度，该参数用于指定要搜索的位置的纬度。用于 google_map-details_by-location，默认值为 38。  [默认: (空)]
    long: 经度，该参数用于指定要搜索的位置的经度。用于 google_map-details_by-location，默认值为 77。  [默认: (空)]
    zoom_level: 缩放级别，该参数用于指示要搜索的缩放级别。用于 google_map-details_by-location，默认值为 20。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "country": country,
        "lat": lat,
        "long": long,
        "zoom_level": zoom_level,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='google.com',
        spider_id='google_map-details_by-location',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def google_map_details_by_placeid(file_name: str = '{{TasksID}}', place_id: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Google 地图信息、Google 地图详细信息、Google Maps details、Google 商家信息，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Google 地图详细信息采集 Builder 任务，支持 google_map-details_by-url、google_map-details_by-cid、google_map-details_by-location 和 google_map-details_by-placeid。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: google.com
    spider_id: google_map-details_by-placeid

    Parameters
    ----------
    place_id: 商家ID，该参数用于指定 Google 地图的商家 ID。用于 google_map-details_by-placeid，默认值为 ChIJ3S-JXmauEmsRUcIaWtf4MzE。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "place_id": place_id,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='google.com',
        spider_id='google_map-details_by-placeid',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

