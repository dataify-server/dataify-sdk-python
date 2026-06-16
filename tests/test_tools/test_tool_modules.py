"""Tests for typed tool wrapper modules."""

from __future__ import annotations

import pytest

from dataify_mcp.tools.task_status import (
    ScraperSerpProductsParams,
    ScraperSerpToolsParams,
    ScraperStatisticsParams,
    ScraperTaskListParams,
    WebUnlockStatisticsParams,
    WebUnlockTaskParams,
)
from dataify_mcp.tools.web_unlocker import RequestWebUnlockerParams
from dataify_mcp.tools.google_serp import (
    GoogleAiModeParams,
    GoogleImagesParams,
    GoogleMapsParams,
    GoogleNewsParams,
    GoogleSearchParams,
)
from dataify_mcp.tools.bing import BingSearchParams
from dataify_mcp.tools.other_search import DuckDuckGoSearchParams, YandexSearchParams
from dataify_mcp.tools.amazon import ScrapeAmazonProductParams
from dataify_mcp.tools.youtube import ScrapeYouTubeVideoParams
from dataify_mcp.tools.tiktok import ScrapeTikTokPostsParams


class TestTaskStatusModels:
    """Verify task status parameter models."""

    def test_web_unlock_task_defaults(self):
        p = WebUnlockTaskParams()
        assert p.status == -1
        assert p.page == 1
        assert p.page_size == 10
        assert p.keyword == ""

    def test_web_unlock_task_custom(self):
        p = WebUnlockTaskParams(status=0, page=2, page_size=20)
        assert p.status == 0
        assert p.page == 2
        assert p.page_size == 20

    def test_web_unlock_statistics_defaults(self):
        p = WebUnlockStatisticsParams()
        assert p.start is None
        assert p.end is None

    def test_scraper_task_list_defaults(self):
        p = ScraperTaskListParams()
        assert p.type == 0
        assert p.status == 0
        assert p.page == 1
        assert p.page_size == 10

    def test_scraper_serp_products_required(self):
        # scraper_type has default, so no args needed
        p = ScraperSerpProductsParams()
        assert p.scraper_type == -1

    def test_scraper_serp_tools_required(self):
        p = ScraperSerpToolsParams(product_id=42)
        assert p.product_id == 42

    def test_scraper_statistics(self):
        p = ScraperStatisticsParams(start=1700000000, end=1700100000)
        assert p.start == 1700000000


class TestWebUnlockerModel:
    """Verify web unlocker parameter model."""

    def test_required_url(self):
        p = RequestWebUnlockerParams(url="https://example.com")
        assert p.url == "https://example.com"
        assert p.type == "html"
        assert p.js_render == "True"
        assert p.country == "us"
        assert p.follow_redirect == "True"

    def test_custom_options(self):
        p = RequestWebUnlockerParams(
            url="https://example.com",
            type="png",
            js_render="True",
            country="cn",
            wait="3000",
        )
        assert p.type == "png"
        assert p.country == "cn"
        assert p.wait == "3000"


class TestGoogleModels:
    """Verify Google SERP parameter models."""

    def test_search_defaults(self):
        p = GoogleSearchParams()
        d = p.model_dump(exclude_none=True)
        assert d.get("q") == "pizza"
        assert d.get("json") == "1"
        assert d.get("device") == "desktop"

    def test_news_params(self):
        p = GoogleNewsParams(q="Python", so="1")
        assert p.q == "Python"
        assert p.so == "1"

    def test_images_params(self):
        p = GoogleImagesParams(q="cats", tbm="isch")
        assert p.q == "cats"
        assert p.tbm == "isch"

    def test_maps_required_q(self):
        p = GoogleMapsParams(q="restaurants near me")
        assert p.q == "restaurants near me"

    def test_ai_mode_params(self):
        p = GoogleAiModeParams(q="AI news", gl="us")
        assert p.q == "AI news"
        assert p.gl == "us"


class TestOtherSearchModels:
    """Verify other search engine parameter models."""

    def test_bing_search_defaults(self):
        p = BingSearchParams()
        assert p.q == "Pizza"
        assert p.json == "1"

    def test_yandex_search_defaults(self):
        p = YandexSearchParams()
        assert p.yandex_domain == "yandex.com"
        assert p.lang == "en"
        assert p.family_mode == "1"

    def test_duckduckgo_search_defaults(self):
        p = DuckDuckGoSearchParams()
        assert p.q == "Pizza"
        assert p.safe == "-1"
        assert p.m == "10"


class TestScraperModels:
    """Verify scraper parameter models."""

    def test_amazon_product_defaults(self):
        p = ScrapeAmazonProductParams()
        assert p.spider_id == "amazon_product_by-asin"
        assert p.asin == "B0BZYCJK89"

    def test_amazon_product_keywords_mode(self):
        p = ScrapeAmazonProductParams(
            spider_id="amazon_product_by-keywords",
            keyword="laptop",
            lowest_price="100",
            highest_price="500",
            page_turning="3",
        )
        assert p.spider_id == "amazon_product_by-keywords"
        assert p.keyword == "laptop"

    def test_youtube_video_defaults(self):
        p = ScrapeYouTubeVideoParams()
        assert p.url == "https://www.youtube.com/watch?v=_SdpvpvVrLY"
        assert p.resolution == "<=360p"
        assert p.video_codec == "vp9"
        assert p.audio_format == "opus"

    def test_tiktok_posts_defaults(self):
        p = ScrapeTikTokPostsParams()
        assert p.url == "https://www.tiktok.com/discover/dog"
        assert p.num_of_posts == "5"


class TestModelSerialization:
    """Verify model_dump produces correct MCP arguments."""

    def test_exclude_none_works(self):
        """model_dump(exclude_none=True) should skip None fields."""
        p = GoogleSearchParams(q="test")
        d = p.model_dump(exclude_none=True)
        # ai_overview has default="" (not None), so it IS included
        assert d.get("ai_overview") == ""
        # cr has default="" as well
        assert d.get("cr") == ""
        assert d["q"] == "test"

    def test_explicit_none_excluded(self):
        """Explicitly passing None should be treated as unset."""
        p = WebUnlockTaskParams(keyword=None)
        d = p.model_dump(exclude_none=True)
        assert "keyword" not in d

    def test_empty_string_kept(self):
        """Empty string default should be preserved."""
        p = WebUnlockTaskParams(keyword="")
        d = p.model_dump(exclude_none=True)
        # "" is not None, so it should be included
        assert d.get("keyword") == ""
