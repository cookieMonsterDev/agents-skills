"""Builder pattern in Python.

Note: for simple cases, keyword arguments with defaults are more idiomatic.
Use a builder when construction is multi-stage or needs validation.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class HttpRequest:
    """Immutable product."""

    method: str
    url: str
    headers: dict[str, str] = field(default_factory=dict)
    body: str | None = None
    timeout_seconds: float = 30.0


class HttpRequestBuilder:
    def __init__(self, method: str, url: str) -> None:
        self._method = method.upper()
        self._url = url
        self._headers: dict[str, str] = {}
        self._body: str | None = None
        self._timeout = 30.0

    def header(self, name: str, value: str) -> HttpRequestBuilder:
        self._headers[name] = value
        return self

    def body(self, body: str) -> HttpRequestBuilder:
        self._body = body
        return self

    def timeout(self, seconds: float) -> HttpRequestBuilder:
        self._timeout = seconds
        return self

    def build(self) -> HttpRequest:
        if self._body is not None and self._method in ("GET", "HEAD"):
            raise ValueError(f"{self._method} requests cannot have a body")
        return HttpRequest(
            method=self._method,
            url=self._url,
            headers=dict(self._headers),
            body=self._body,
            timeout_seconds=self._timeout,
        )


if __name__ == "__main__":
    request = (
        HttpRequestBuilder("POST", "https://api.example.com/users")
        .header("Content-Type", "application/json")
        .header("Authorization", "Bearer token123")
        .body('{"name": "Ada"}')
        .timeout(5.0)
        .build()
    )
    print(request)
