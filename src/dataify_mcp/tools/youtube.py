"""YouTube scraper tools.

Wraps all YouTube-related MCP tools: video, video_post, profiles,
comment, transcript, product, and audio.

Auto-generated.  Regenerate with: python scripts/codegen.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class _YouTubeFileParams(BaseModel):
    """Base params for YouTube tools with file_name."""

    file_name: str | None = Field(default="{{TasksID}}", description="Builder file_name")


# ---------------------------------------------------------------------------
# scrape_youtube_video
# ---------------------------------------------------------------------------


class ScrapeYouTubeVideoParams(_YouTubeFileParams):
    """Parameters for ``scrape_youtube_video`` — YouTube 视频文件下载。

    下载 YouTube 视频文件，支持字幕、分辨率、视频编码、音频格式等配置。
    """

    url: str = Field(default="https://www.youtube.com/watch?v=_SdpvpvVrLY", description="YouTube 视频 URL")
    subtitles_language: str | None = Field(default="ab", description="字幕语言代码")
    selected_only: str | None = Field(default="false", description="仅下载已选规格: true/false")
    resolution: str | None = Field(default="<=360p", description="分辨率，如 <=1080p")
    video_codec: str | None = Field(default="vp9", description="视频编码: vp9, avc1, av01")
    audio_format: str | None = Field(default="opus", description="音频格式: opus, m4a")
    bitrate: str | None = Field(default="<=320", description="比特率，如 <=320")


async def scrape_youtube_video(self, params: ScrapeYouTubeVideoParams | None = None) -> Any:
    """Call ``scrape_youtube_video`` — YouTube 视频文件下载。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_youtube_video", arguments)


# ---------------------------------------------------------------------------
# scrape_youtube_video_post
# ---------------------------------------------------------------------------


class ScrapeYouTubeVideoPostParams(_YouTubeFileParams):
    """Parameters for ``scrape_youtube_video_post`` — YouTube 视频帖子采集。"""

    url: str = Field(..., description="YouTube 视频 URL")


async def scrape_youtube_video_post(self, params: ScrapeYouTubeVideoPostParams | None = None) -> Any:
    """Call ``scrape_youtube_video_post`` — YouTube 视频帖子采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_youtube_video_post", arguments)


# ---------------------------------------------------------------------------
# scrape_youtube_profiles
# ---------------------------------------------------------------------------


class ScrapeYouTubeProfilesParams(_YouTubeFileParams):
    """Parameters for ``scrape_youtube_profiles`` — YouTube 频道信息采集。"""

    url: str = Field(..., description="YouTube 频道 URL")


async def scrape_youtube_profiles(self, params: ScrapeYouTubeProfilesParams | None = None) -> Any:
    """Call ``scrape_youtube_profiles`` — YouTube 频道信息采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_youtube_profiles", arguments)


# ---------------------------------------------------------------------------
# scrape_youtube_comment
# ---------------------------------------------------------------------------


class ScrapeYouTubeCommentParams(_YouTubeFileParams):
    """Parameters for ``scrape_youtube_comment`` — YouTube 评论采集。"""

    url: str = Field(..., description="YouTube 视频 URL")


async def scrape_youtube_comment(self, params: ScrapeYouTubeCommentParams | None = None) -> Any:
    """Call ``scrape_youtube_comment`` — YouTube 评论采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_youtube_comment", arguments)


# ---------------------------------------------------------------------------
# scrape_youtube_transcript
# ---------------------------------------------------------------------------


class ScrapeYouTubeTranscriptParams(_YouTubeFileParams):
    """Parameters for ``scrape_youtube_transcript`` — YouTube 字幕采集。"""

    url: str = Field(..., description="YouTube 视频 URL")


async def scrape_youtube_transcript(self, params: ScrapeYouTubeTranscriptParams | None = None) -> Any:
    """Call ``scrape_youtube_transcript`` — YouTube 字幕采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_youtube_transcript", arguments)


# ---------------------------------------------------------------------------
# scrape_youtube_product
# ---------------------------------------------------------------------------


class ScrapeYouTubeProductParams(_YouTubeFileParams):
    """Parameters for ``scrape_youtube_product`` — YouTube 商品采集。"""

    url: str = Field(..., description="YouTube 商品相关 URL")


async def scrape_youtube_product(self, params: ScrapeYouTubeProductParams | None = None) -> Any:
    """Call ``scrape_youtube_product`` — YouTube 商品采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_youtube_product", arguments)


# ---------------------------------------------------------------------------
# scrape_youtube_audio
# ---------------------------------------------------------------------------


class ScrapeYouTubeAudioParams(_YouTubeFileParams):
    """Parameters for ``scrape_youtube_audio`` — YouTube 音频采集。"""

    url: str = Field(..., description="YouTube 视频 URL")


async def scrape_youtube_audio(self, params: ScrapeYouTubeAudioParams | None = None) -> Any:
    """Call ``scrape_youtube_audio`` — YouTube 音频采集。"""
    arguments = params.model_dump(exclude_none=True) if params else {}
    return await self.call_tool("scrape_youtube_audio", arguments)


# ---------------------------------------------------------------------------
# Attach methods to DataifyClient
# ---------------------------------------------------------------------------


def _attach(client_cls: type) -> None:
    """Attach all YouTube scraper methods to the client class."""
    client_cls.scrape_youtube_video = scrape_youtube_video
    client_cls.scrape_youtube_video_post = scrape_youtube_video_post
    client_cls.scrape_youtube_profiles = scrape_youtube_profiles
    client_cls.scrape_youtube_comment = scrape_youtube_comment
    client_cls.scrape_youtube_transcript = scrape_youtube_transcript
    client_cls.scrape_youtube_product = scrape_youtube_product
    client_cls.scrape_youtube_audio = scrape_youtube_audio
