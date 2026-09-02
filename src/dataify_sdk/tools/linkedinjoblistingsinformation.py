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

def linkedin_job_listings_information_by_job_listing_url(file_name: str = '{{TasksID}}', job_listing_url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 LinkedIn 职位列表、领英职位列表、LinkedIn 招聘信息、领英招聘信息、LinkedIn job listings，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 LinkedIn 职位列表采集 Builder 任务，支持 linkedin_job_listings_information_by-job-listing-url、linkedin_job_listings_information_by-job-url 和 linkedin_job_listings_information_by-keyword。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: linkedin.com
    spider_id: linkedin_job_listings_information_by-job-listing-url

    Parameters
    ----------
    job_listing_url: 职位列表URL，该参数用于指定要采集的职位列表URL。用于 linkedin_job_listings_information_by-job-listing-url，默认值为 https://www.linkedin.com/jobs/reddit-inc.-jobs-worldwide?f_C=150573。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "job_listing_url": job_listing_url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='linkedin.com',
        spider_id='linkedin_job_listings_information_by-job-listing-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def linkedin_job_listings_information_by_job_url(file_name: str = '{{TasksID}}', job_url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 LinkedIn 职位列表、领英职位列表、LinkedIn 招聘信息、领英招聘信息、LinkedIn job listings，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 LinkedIn 职位列表采集 Builder 任务，支持 linkedin_job_listings_information_by-job-listing-url、linkedin_job_listings_information_by-job-url 和 linkedin_job_listings_information_by-keyword。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: linkedin.com
    spider_id: linkedin_job_listings_information_by-job-url

    Parameters
    ----------
    job_url: 职位URL，该参数用于指定要采集的职位URL。用于 linkedin_job_listings_information_by-job-url，默认值为文档提供的 LinkedIn 职位 URL。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "job_url": job_url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='linkedin.com',
        spider_id='linkedin_job_listings_information_by-job-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def linkedin_job_listings_information_by_keyword(file_name: str = '{{TasksID}}', keyword: str = 'product manager', location: str = 'New York', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 LinkedIn 职位列表、领英职位列表、LinkedIn 招聘信息、领英招聘信息、LinkedIn job listings，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 LinkedIn 职位列表采集 Builder 任务，支持 linkedin_job_listings_information_by-job-listing-url、linkedin_job_listings_information_by-job-url 和 linkedin_job_listings_information_by-keyword。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: linkedin.com
    spider_id: linkedin_job_listings_information_by-keyword

    Parameters
    ----------
    location: 职位位置，该参数用于指定通过特定位置搜索职位。用于 linkedin_job_listings_information_by-keyword，默认值为 New York。  [默认: New York]
    keyword: 关键词，该参数用于指定通过特定关键词搜索职位。用于 linkedin_job_listings_information_by-keyword，非必填，默认值为 product manager。  [默认: product manager]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "location": location,
        "keyword": keyword,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='linkedin.com',
        spider_id='linkedin_job_listings_information_by-keyword',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

