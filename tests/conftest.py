"""Shared fixtures for the Dataify SDK tests."""

from __future__ import annotations

import io
import urllib.error
import urllib.parse
import urllib.request
from typing import Any
from unittest import mock

import pytest


class _FakeResponse:
    def __init__(self, body: str | bytes) -> None:
        self._body = body.encode() if isinstance(body, str) else body

    def read(self) -> bytes:
        return self._body

    def __enter__(self) -> "_FakeResponse":
        return self

    def __exit__(self, *exc: Any) -> bool:
        return False


@pytest.fixture
def captured_request():
    """Patch ``urllib.request.urlopen`` and expose the last Request object.

    The real client logic (form encoding, empty-value dropping, auth header)
    runs; only the socket round-trip is stubbed.
    """
    holder: dict[str, urllib.request.Request] = {}

    def _fake(req: urllib.request.Request, timeout: int | None = None):
        holder["req"] = req
        return _FakeResponse('{"ok": true}')

    with mock.patch("urllib.request.urlopen", side_effect=_fake):
        yield holder


@pytest.fixture
def api_token() -> str:
    return "test-token-12345"


def decode_form(req: urllib.request.Request) -> dict[str, str]:
    """Decode a urlencoded request body into a dict."""
    return dict(urllib.parse.parse_qsl(req.data.decode("utf-8")))


def raise_http_error(req: urllib.request.Request, timeout: int | None = None):
    raise urllib.error.HTTPError(
        req.full_url, 400, "Bad Request", {}, io.BytesIO(b'{"error":"bad"}')
    )
