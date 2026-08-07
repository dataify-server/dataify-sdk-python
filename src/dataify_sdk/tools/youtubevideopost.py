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

def youtube_video_post_by_url(file_name: str = '{{TasksID}}', num_of_posts: str = '', order_by: str = 'Latest', start_index: str = '1', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_video-post_by-url

    Parameters
    ----------
    url: URL。用于频道 Video URL、播客 URL 或探索 URL；不同采集器未传时按文档默认 URL 提交。  [默认: (空)]
    order_by: 排序方式。用于 youtube_video-post_by-url，可传 最新、热门、最旧，提交值为 Latest、Popular、Oldest；默认 Latest。  [默认: Latest]
    start_index: 起始条数，该参数用于指定从第几条视频开始采集信息。用于 youtube_video-post_by-url，默认值为 1。  [默认: 1]
    num_of_posts: 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "order_by": order_by,
        "start_index": start_index,
        "num_of_posts": num_of_posts,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_video-post_by-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def youtube_video_post_by_search_filters(duration: str = 'Under 3 minutes', features: str = 'All', file_name: str = '{{TasksID}}', keyword_search: str = 'popular music', num_of_posts: str = '', type_: str = 'Video', upload_date: str = '上一小时', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_video-post_by-search-filters

    Parameters
    ----------
    keyword_search: 搜索关键词。用于 youtube_video-post_by-search-filters，默认值为 popular music。  [默认: popular music]
    features: 特征。用于 youtube_video-post_by-search-filters，可传 All、全部、Live、4K、HD、Subtitles/CC、Creative Commons、360°、VR180、3D、HDR；默认 All。  [默认: All]
    type_: 类型。用于 youtube_video-post_by-search-filters，可选 Video、Movie，默认值为 Video。  [默认: Video] (上游字段: type)
    duration: 持续时间。用于 youtube_video-post_by-search-filters，可传 Under 3 minutes、4 分钟以内、4-20 分钟、20 分钟以上、全部；默认 Under 3 minutes。  [默认: Under 3 minutes]
    upload_date: 上传日期。用于 youtube_video-post_by-search-filters，可传 上一小时、今天、本周、本月、今年、全部；默认 上一小时。  [默认: 上一小时]
    num_of_posts: 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword_search": keyword_search,
        "features": features,
        "type": type_,
        "duration": duration,
        "upload_date": upload_date,
        "num_of_posts": num_of_posts,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_video-post_by-search-filters',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def youtube_video_post_by_hashtag(file_name: str = '{{TasksID}}', hashtag: str = 'shopping', num_of_posts: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_video-post_by-hashtag

    Parameters
    ----------
    hashtag: 话题标签，按标签筛选视频，请参考 https://www.youtube.com/hashtag。用于 youtube_video-post_by-hashtag，默认值为 shopping。  [默认: shopping]
    num_of_posts: 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "hashtag": hashtag,
        "num_of_posts": num_of_posts,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_video-post_by-hashtag',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def youtube_video_post_by_podcast_url(file_name: str = '{{TasksID}}', num_of_posts: str = '', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_video-post_by-podcast-url

    Parameters
    ----------
    url: URL。用于频道 Video URL、播客 URL 或探索 URL；不同采集器未传时按文档默认 URL 提交。  [默认: (空)]
    num_of_posts: 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "num_of_posts": num_of_posts,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_video-post_by-podcast-url',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def youtube_video_post_by_keyword(file_name: str = '{{TasksID}}', keyword: str = 'top videos', num_of_posts: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_video-post_by-keyword

    Parameters
    ----------
    keyword: 关键词。用于 youtube_video-post_by-keyword，默认值为 top videos。  [默认: top videos]
    num_of_posts: 帖子数量，此参数用于指定要采集的帖子数量。不同采集器按文档默认值提交。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "keyword": keyword,
        "num_of_posts": num_of_posts,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_video-post_by-keyword',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )


def youtube_video_post_by_explore(all_tabs: str = '', file_name: str = '{{TasksID}}', url: str = '', client: DataifyClient | None = None) -> dict[str, Any]:
    """当用户需要 YouTube 视频帖子、YouTube 视频列表、YouTube 频道视频、YouTube 搜索视频、YouTube 话题标签视频、YouTube 播客视频、YouTube 探索视频，与采集、抓取、爬取、获取、提取等动词组合时触发。复用一个工具提交 YouTube 视频帖子采集 Builder 任务，支持 youtube_video-post_by-url、youtube_video-post_by-search-filters、youtube_video-post_by-hashtag、youtube_video-post_by-podcast-url、youtube_video-post_by-keyword、youtube_video-post_by-explore。

    上游接口: Scraper Builder (POST /builder?platform=1)
    spider_name: youtube.com
    spider_id: youtube_video-post_by-explore

    Parameters
    ----------
    url: URL。用于频道 Video URL、播客 URL 或探索 URL；不同采集器未传时按文档默认 URL 提交。  [默认: (空)]
    all_tabs: 所有标签页。用于 youtube_video-post_by-explore，参数值为 true 或 false，默认 true。  [默认: (空)]
    file_name: Builder file_name 字段。不传默认为 {{TasksID}}。  [默认: {{TasksID}}]
    client: 可选 DataifyClient 实例;不传则使用默认 client(读取 DATAIFY_TOKEN)。
    """
    params_obj = {
        "url": url,
        "all_tabs": all_tabs,
    }
    spider_parameters = json.dumps([params_obj], ensure_ascii=False)
    return _client(client).request_scraper(
        spider_name='youtube.com',
        spider_id='youtube_video-post_by-explore',
        spider_parameters=spider_parameters,
        file_name=file_name,
    )

