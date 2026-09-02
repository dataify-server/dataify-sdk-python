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

def github_repository_by_repo_url(file_name: str = '{{TasksID}}', repo_url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Github仓库信息、GitHub 仓库信息、Github repository、GitHub 代码 URL、GitHub 搜索仓库，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Github仓库信息采集 Builder 任务，支持 github_repository_by-repo-url、github_repository_by-search-url 和 github_repository_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: github.com
    spider_id: github_repository_by-repo-url

    Parameters
    ----------
    repo_url: 仓库URL，该参数用于指定要采集的仓库 URL。用于 github_repository_by-repo-url，默认值为 https://github.com/TheAlgorithms/Python。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "repo_url": repo_url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='github.com',
        spider_id='github_repository_by-repo-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def github_repository_by_search_url(file_name: str = '{{TasksID}}', max_num: str = '', page_turning: str = '', search_url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Github仓库信息、GitHub 仓库信息、Github repository、GitHub 代码 URL、GitHub 搜索仓库，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Github仓库信息采集 Builder 任务，支持 github_repository_by-repo-url、github_repository_by-search-url 和 github_repository_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: github.com
    spider_id: github_repository_by-search-url

    Parameters
    ----------
    search_url: 搜索URL，该参数用于指定要采集的 Search URL。用于 github_repository_by-search-url，默认值为 https://github.com/search?q=ML&type=repositories。  [默认: (空)]
    page_turning: 页数限制，该参数用于指定采集结果数量的限制。用于 github_repository_by-search-url，默认值为 1。  [默认: (空)]
    max_num: 最大仓库数量，该参数用于指定采集的最大仓库数量。用于 github_repository_by-search-url，默认值为 15。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "search_url": search_url,
        "page_turning": page_turning,
        "max_num": max_num,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='github.com',
        spider_id='github_repository_by-search-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def github_repository_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Github仓库信息、GitHub 仓库信息、Github repository、GitHub 代码 URL、GitHub 搜索仓库，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Github仓库信息采集 Builder 任务，支持 github_repository_by-repo-url、github_repository_by-search-url 和 github_repository_by-url。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: github.com
    spider_id: github_repository_by-url

    Parameters
    ----------
    url: URL，该参数用于指定要采集的代码URL。用于 github_repository_by-url，默认值为 https://github.com/TheAlgorithms/Python/blob/master/divide_and_conquer/power.py。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='github.com',
        spider_id='github_repository_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

