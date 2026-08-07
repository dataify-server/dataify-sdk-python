"""Tests for the synchronous Dataify REST client (no MCP layer)."""

from __future__ import annotations

import pytest
import urllib.error
from unittest import mock

from dataify_sdk import DataifyClient
from dataify_sdk.errors import DataifyAPIError
from tests.conftest import decode_form, raise_http_error


def test_token_required(monkeypatch):
    monkeypatch.delenv("DATAIFY_TOKEN", raising=False)
    with pytest.raises(ValueError):
        DataifyClient()


def test_token_from_env(monkeypatch):
    monkeypatch.setenv("DATAIFY_TOKEN", "env-token")
    assert DataifyClient().token == "env-token"


def test_token_from_constructor(monkeypatch):
    monkeypatch.delenv("DATAIFY_TOKEN", raising=False)
    assert DataifyClient(token="ctor-token").token == "ctor-token"


def test_request_scraper_builds_body(captured_request):
    client = DataifyClient(token="t")
    client.request_scraper(
        spider_name="amazon.com",
        spider_id="amazon_product_by-asin",
        spider_parameters='[{"asin": "B0X"}]',
    )
    req = captured_request["req"]
    assert req.full_url.endswith("/builder?platform=1")
    form = decode_form(req)
    assert form["spider_name"] == "amazon.com"
    assert form["spider_id"] == "amazon_product_by-asin"
    assert form["spider_parameters"] == '[{"asin": "B0X"}]'
    assert form["spider_errors"] == "true"
    assert req.get_header("Authorization") == "Bearer t"


def test_request_serp_skips_empty(captured_request):
    client = DataifyClient(token="t")
    client.request_serp("google", {"q": "pizza", "gl": "", "hl": "en"})
    req = captured_request["req"]
    assert req.full_url.endswith("/request")
    form = decode_form(req)
    assert form["engine"] == "google"
    assert form["q"] == "pizza"
    assert form["hl"] == "en"
    assert "gl" not in form  # empty values are dropped


def test_api_error_propagates():
    with mock.patch("urllib.request.urlopen", side_effect=raise_http_error):
        client = DataifyClient(token="t")
        with pytest.raises(DataifyAPIError) as exc:
            client.request_serp("google", {"q": "x"})
    assert exc.value.status_code == 400
