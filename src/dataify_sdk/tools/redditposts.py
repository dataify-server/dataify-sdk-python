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

def reddit_posts_by_url(file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Reddit 帖子信息、Reddit 帖子、Reddit posts、subreddit 帖子，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Reddit 帖子信息采集 Builder 任务，支持 reddit_posts_by-url、reddit_posts_by-keywords 和 reddit_posts_by-subredditurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: reddit.com
    spider_id: reddit_posts_by-url

    Parameters
    ----------
    url: Reddit URL 或 subreddit URL。reddit_posts_by-url 默认值为 https://www.reddit.com/r/battlefield2042/comments/1cmqs1d/official_update_on_the_next_battlefield_game/；reddit_posts_by-subredditurl 默认值为 https://www.reddit.com/r/battlefield2042。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='reddit.com',
        spider_id='reddit_posts_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def reddit_posts_by_keywords(file_name: str = '{{TasksID}}', keyword: str = '', num_of_posts: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Reddit 帖子信息、Reddit 帖子、Reddit posts、subreddit 帖子，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Reddit 帖子信息采集 Builder 任务，支持 reddit_posts_by-url、reddit_posts_by-keywords 和 reddit_posts_by-subredditurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: reddit.com
    spider_id: reddit_posts_by-keywords

    Parameters
    ----------
    keyword: Reddit 关键词，该参数用于指定采集 Reddit 帖子的搜索关键词。用于 reddit_posts_by-keywords，默认值为 datascience。  [默认: (空)]
    num_of_posts: 最大帖子数，该参数用于指定采集帖子的最大数量。用于 reddit_posts_by-keywords 和 reddit_posts_by-subredditurl，默认值为 10。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "num_of_posts": num_of_posts,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='reddit.com',
        spider_id='reddit_posts_by-keywords',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def reddit_posts_by_subredditurl(file_name: str = '{{TasksID}}', num_of_posts: str = '', sort_by: str = '', sort_by_time: str = '', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 Reddit 帖子信息、Reddit 帖子、Reddit posts、subreddit 帖子，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 Reddit 帖子信息采集 Builder 任务，支持 reddit_posts_by-url、reddit_posts_by-keywords 和 reddit_posts_by-subredditurl。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: reddit.com
    spider_id: reddit_posts_by-subredditurl

    Parameters
    ----------
    url: Reddit URL 或 subreddit URL。reddit_posts_by-url 默认值为 https://www.reddit.com/r/battlefield2042/comments/1cmqs1d/official_update_on_the_next_battlefield_game/；reddit_posts_by-subredditurl 默认值为 https://www.reddit.com/r/battlefield2042。  [默认: (空)]
    sort_by: 排序方式，该参数用于指定采集帖子的排序方式。用于 reddit_posts_by-subredditurl，可选值：Hot、Top、New、Rising，默认值为 Rising。  [默认: (空)]
    num_of_posts: 最大帖子数，该参数用于指定采集帖子的最大数量。用于 reddit_posts_by-keywords 和 reddit_posts_by-subredditurl，默认值为 10。  [默认: (空)]
    sort_by_time: 时间排序，该参数用于指定采集帖子的时间排序方式。用于 reddit_posts_by-subredditurl，可选值：Now、Today、This Week、This Month、This Year、All Time，默认值为 Now。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(优先读取 DATAIFY_API_TOKEN, 兼容 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "sort_by": sort_by,
        "num_of_posts": num_of_posts,
        "sort_by_time": sort_by_time,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='reddit.com',
        spider_id='reddit_posts_by-subredditurl',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

