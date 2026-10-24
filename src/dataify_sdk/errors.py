"""Exceptions raised by the Dataify SDK."""

from __future__ import annotations


class DataifyError(Exception):
    """Base class for all Dataify SDK errors."""


class DataifyAPIError(DataifyError):
    """Raised when the Dataify upstream API returns an error.

    Attributes
    ----------
    message:
        Human-readable error message.
    status_code:
        HTTP status code returned by the upstream (``None`` for network errors).
    body:
        Raw response body (or error text) returned by the upstream.
    """



    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        body: str | None = None,
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.body = body
        super().__init__(message)



    def __str__(self) -> str:
        if self.status_code is not None:
            return f"{self.message} (HTTP {self.status_code})"
        return self.message


class DataifyConnectionError(DataifyError):
    """Raised when the HTTP request to the Dataify upstream cannot be completed."""


class DataifyTimeoutError(DataifyError):
    """Raised when the HTTP request to the Dataify upstream times out."""


class DataifyMissingAIWebBaseUrlError(DataifyError):
    """Raised when an AI Web request has no usable gateway base URL.

    The SDK defaults to ``https://aiwebapi.dataify.com``. This error only
    occurs when the client's AI Web base URL is explicitly cleared.
    """

    def __init__(self) -> None:
        super().__init__(
            "AI Web base URL is empty: pass ai_web_base_url=... "
            "or set AI_WEB_API_BASE_URL."
        )
