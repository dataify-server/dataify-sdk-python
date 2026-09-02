"""Tests for the synchronous Dataify REST client (no MCP layer)."""

from __future__ import annotations

import pytest
import urllib.error
import urllib.parse
from unittest import mock

from dataify_sdk import DataifyClient
from dataify_sdk.errors import DataifyAPIError
from tests.conftest import decode_form, raise_http_error


def test_token_required(monkeypatch):
    monkeypatch.delenv("DATAIFY_API_TOKEN", raising=False)
    monkeypatch.delenv("DATAIFY_TOKEN", raising=False)
    with pytest.raises(ValueError):
        DataifyClient()


def test_token_from_env(monkeypatch):
    monkeypatch.setenv("DATAIFY_API_TOKEN", "env-token")
    assert DataifyClient().token == "env-token"


def test_legacy_token_from_env(monkeypatch):
    monkeypatch.delenv("DATAIFY_API_TOKEN", raising=False)
    monkeypatch.setenv("DATAIFY_TOKEN", "legacy-token")
    assert DataifyClient().token == "legacy-token"


def test_api_token_takes_precedence(monkeypatch):
    monkeypatch.setenv("DATAIFY_API_TOKEN", "api-token")
    monkeypatch.setenv("DATAIFY_TOKEN", "legacy-token")
    assert DataifyClient().token == "api-token"


def test_token_from_constructor(monkeypatch):
    monkeypatch.delenv("DATAIFY_API_TOKEN", raising=False)
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


def test_query_scraper_task_status_builds_query(captured_request):
    client = DataifyClient(token="t")
    response = client.query_scraper_task_status("task-1")

    req = captured_request["req"]
    assert req.full_url.startswith("https://scraperapi.dataify.com/task_status")
    query = urllib.parse.parse_qs(urllib.parse.urlparse(req.full_url).query)
    assert query["api_key"] == ["t"]
    assert query["task_id"] == ["task-1"]
    assert response == {"ok": True}


def test_download_scraper_task_result_json_builds_query(captured_request):
    client = DataifyClient(token="t")
    response = client.download_scraper_task_result("task-1")

    req = captured_request["req"]
    assert req.full_url.startswith("https://scraperapi.dataify.com/download")
    query = urllib.parse.parse_qs(urllib.parse.urlparse(req.full_url).query)
    assert query["api_key"] == ["t"]
    assert query["task_id"] == ["task-1"]
    assert query["type"] == ["json"]
    assert response == {"ok": True}


def test_download_scraper_task_result_csv_returns_text(captured_request):
    client = DataifyClient(token="t")
    response = client.download_scraper_task_result("task-1", result_type="csv")

    req = captured_request["req"]
    query = urllib.parse.parse_qs(urllib.parse.urlparse(req.full_url).query)
    assert query["type"] == ["csv"]
    assert response == '{"ok": true}'


def test_download_scraper_task_result_xlsx_returns_bytes(captured_request):
    client = DataifyClient(token="t")
    response = client.download_scraper_task_result("task-1", result_type="xlsx")

    req = captured_request["req"]
    query = urllib.parse.parse_qs(urllib.parse.urlparse(req.full_url).query)
    assert query["type"] == ["xlsx"]
    assert response == b'{"ok": true}'


def test_download_scraper_task_result_rejects_unknown_type():
    client = DataifyClient(token="t")
    with pytest.raises(ValueError):
        client.download_scraper_task_result("task-1", result_type="pdf")


def test_api_error_propagates():
    with mock.patch("urllib.request.urlopen", side_effect=raise_http_error):
        client = DataifyClient(token="t")
        with pytest.raises(DataifyAPIError) as exc:
            client.request_serp("google", {"q": "x"})
    assert exc.value.status_code == 400
