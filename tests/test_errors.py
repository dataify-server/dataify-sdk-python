"""Tests for SDK exception formatting."""

from __future__ import annotations

import pytest

from dataify_sdk import (
    DataifyAPIError,
    DataifyConnectionError,
    DataifyError,
    DataifyMissingAIWebBaseUrlError,
    DataifyTimeoutError,
)


def test_dataify_api_error_str_includes_message_and_status():
    error = DataifyAPIError("boom", 401, '{"message": "invalid"}')

    assert error.message == "boom"
    assert str(error) == "boom (HTTP 401)"


def test_dataify_api_error_str_without_status():
    error = DataifyAPIError("boom")

    assert str(error) == "boom"


@pytest.mark.parametrize(
    "error",
    [
        DataifyError("boom"),
        DataifyAPIError("boom"),
        DataifyConnectionError("boom"),
        DataifyTimeoutError("boom"),
        DataifyMissingAIWebBaseUrlError(),
    ],
)
def test_every_dataify_error_can_be_printed(error):
    rendered = str(error)

    assert isinstance(rendered, str)
    assert rendered
