"""Enums for common Dataify parameter values.

These provide type-safe alternatives to raw string literals when
constructing tool parameters.
"""

from __future__ import annotations

from enum import Enum


# ---------------------------------------------------------------------------
# Web Unlocker
# ---------------------------------------------------------------------------


class UnlockerOutputType(str, Enum):
    """Output format for request_web_unlocker 'type' parameter."""

    HTML = "html"
    PNG = "png"
    HTML_PNG = "html,png"


# ---------------------------------------------------------------------------
# Google / Bing / Search Engine
# ---------------------------------------------------------------------------


class JSONOutputFormat(str, Enum):
    """JSON output format for search engine results."""

    JSON = "1"
    JSON_HTML = "2"
    HTML = "3"
    LIGHT_JSON = "4"


class Device(str, Enum):
    """Device type for search engine emulation."""

    DESKTOP = "desktop"
    TABLET = "tablet"
    MOBILE = "mobile"


class SafeSearch(str, Enum):
    """SafeSearch / adult content filtering."""

    ACTIVE = "active"
    OFF = "off"


class BingSafeSearch(str, Enum):
    """Bing SafeSearch levels."""

    OFF = "Off"
    MODERATE = "Moderate"
    STRICT = "Strict"


class DuckDuckGoSafeSearch(str, Enum):
    """DuckDuckGo SafeSearch levels."""

    STRICT = "1"
    MODERATE = "-1"
    OFF = "-2"


class DateFilter(str, Enum):
    """Date filter shortcuts for search results."""

    PAST_DAY = "d"
    PAST_WEEK = "w"
    PAST_MONTH = "m"
    PAST_YEAR = "y"


class TaskStatus(str, Enum):
    """Generic task status codes."""

    ALL = "-1"
    PROCESSING = "-1"
    SUCCESS = "0"
    FAILED = "1"


class ScraperTaskStatus(str, Enum):
    """Scraper task status codes."""

    ALL = "0"
    PROCESSING = "-1"
    SUCCESS = "200"
    FAILED = "400"


class ScraperType(str, Enum):
    """Scraper product type."""

    ALL = "-1"
    WEB_SCRAPER = "0"
    SERP = "1"


class TaskType(str, Enum):
    """Scraper task type."""

    ALL = "0"
    SERP = "1"
    WEB_SCRAPER = "2"


# ---------------------------------------------------------------------------
# Yandex
# ---------------------------------------------------------------------------


class YandexFamilyMode(str, Enum):
    """Yandex SafeSearch / family filter."""

    OFF = "0"
    MODERATE = "1"
    STRICT = "2"


# ---------------------------------------------------------------------------
# Amazon
# ---------------------------------------------------------------------------


class AmazonSpiderID(str, Enum):
    """Amazon product spider identifiers."""

    BY_ASIN = "amazon_product_by-asin"
    BY_URL = "amazon_product_by-url"
    BY_KEYWORDS = "amazon_product_by-keywords"
    BY_CATEGORY_URL = "amazon_product_by-category-url"
    BY_BEST_SELLERS = "amazon_product_by-best-sellers"


class AmazonDomain(str, Enum):
    """Amazon marketplace domains."""

    COM = "amazon.com"
    JP = "amazon.co.jp"
    DE = "amazon.de"
    UK = "amazon.co.uk"
    FR = "amazon.fr"
    IT = "amazon.it"
    ES = "amazon.es"
    CA = "amazon.ca"
    IN = "amazon.in"
    BR = "amazon.com.br"
    MX = "amazon.com.mx"
    AU = "amazon.com.au"


class AmazonSortBy(str, Enum):
    """Amazon product sorting options (Chinese)."""

    BEST_SELLERS = "畅销排行"
    NEWEST_ARRIVALS = "最新上架"
    AVG_CUSTOMER_REVIEW = "平均评价"
    PRICE_HIGH_TO_LOW = "价格：从高到低"
    PRICE_LOW_TO_HIGH = "价格：从低到高"
    FEATURED = "精选推荐"


# ---------------------------------------------------------------------------
# YouTube
# ---------------------------------------------------------------------------


class YouTubeVideoCodec(str, Enum):
    """YouTube video codec options."""

    VP9 = "vp9"
    AVC1 = "avc1"  # Also: h264, avc
    AV01 = "av01"  # Also: av1


class YouTubeAudioFormat(str, Enum):
    """YouTube audio format options."""

    OPUS = "opus"
    M4A = "m4a"  # Also: aac


class YouTubeResolution(str, Enum):
    """YouTube video resolution options (bare value, no operator)."""

    P360 = "360p"
    P480 = "480p"
    P720 = "720p"
    P1080 = "1080p"
    P1440 = "1440p"
    P2160 = "2160p"


class YouTubeBitrate(str, Enum):
    """YouTube audio bitrate options (bare value, no operator)."""

    K48 = "48"
    K64 = "64"
    K128 = "128"
    K160 = "160"
    K256 = "256"
    K320 = "320"


# ---------------------------------------------------------------------------
# Comparison operators
# ---------------------------------------------------------------------------


class ComparisonOp(str, Enum):
    """Comparison operators used in YouTube resolution/bitrate."""

    LE = "<="
    GE = ">="
