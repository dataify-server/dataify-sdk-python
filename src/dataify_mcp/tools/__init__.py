"""Typed tool wrappers for Dataify MCP tools.

Each sub-module wraps a category of tools with Pydantic models for
type-safe parameter passing.  These modules are **auto-generated**
by ``scripts/codegen.py`` from a running Dataify MCP server.

Categories
----------
- ``task_status`` — web_unlock_task, web_unlock_statistics, scraper_task_list, etc.
- ``user`` — query_user_info, query_user_balance, query_user_api_keys, etc.
- ``web_unlocker`` — request_web_unlocker
- ``google_serp`` — google_search, google_news, google_images, google_maps, etc.
- ``google_scraper`` — google_map_details, google_map_comment, google_shopping_info, etc.
- ``bing`` — bing_search, bing_images, bing_maps, bing_news, etc.
- ``other_search`` — yandex_search, duckduckgo_search
- ``amazon`` — scrape_amazon_product, scrape_amazon_comment, etc.
- ``youtube`` — scrape_youtube_video, scrape_youtube_comment, etc.
- ``tiktok`` — scrape_tiktok_posts, scrape_tiktok_profiles, etc.
- ``facebook`` — scrape_facebook_post, scrape_facebook_profile, etc.
- ``instagram`` — scrape_instagram_profiles, etc.
- ``reddit`` — scrape_reddit_posts, etc.
- ``twitter`` — scrape_twitter_post, etc.
- ``linkedin`` — scrape_linkedin_company_information, etc.
- ``glassdoor`` — scrape_glassdoor_company, etc.
- ``indeed`` — scrape_indeed_companies_info, etc.
- ``other_scrapers`` — airbnb, booking, crunchbase, ebay, github, walmart, zillow

Regenerate with::

    python scripts/codegen.py --server http://localhost:7780 --token YOUR_TOKEN
"""

from __future__ import annotations

from dataify_mcp.tools import (
    amazon,
    bing,
    facebook,
    glassdoor,
    google_scraper,
    google_serp,
    indeed,
    instagram,
    linkedin,
    other_scrapers,
    other_search,
    reddit,
    task_status,
    tiktok,
    twitter,
    user,
    web_unlocker,
    youtube,
)

_ALL_MODULES = [
    task_status,
    user,
    web_unlocker,
    google_serp,
    google_scraper,
    bing,
    other_search,
    amazon,
    youtube,
    tiktok,
    facebook,
    instagram,
    reddit,
    twitter,
    linkedin,
    glassdoor,
    indeed,
    other_scrapers,
]


def attach_all(client_cls: type) -> None:
    """Attach all typed tool methods to a DataifyClient subclass or instance.

    Called automatically by ``DataifyClient.__init__`` so users don't
    need to invoke this manually.

    Parameters
    ----------
    client_cls:
        The ``DataifyClient`` class (not an instance).
    """
    for mod in _ALL_MODULES:
        mod._attach(client_cls)
