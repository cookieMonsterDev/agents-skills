"""Polite HTTP client: identify yourself, keep a session, stay under fair-access rates."""

from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any, Optional
from urllib.parse import urlparse

import requests

SEC_HOST_SUFFIX = "sec.gov"
SEC_MIN_INTERVAL = 0.12
DEFAULT_MIN_INTERVAL = 0.5
DEFAULT_TIMEOUT = 45


class HttpError(RuntimeError):
    def __init__(self, url: str, status: int, detail: str = ""):
        self.url = url
        self.status = status
        super().__init__(f"GET {url} -> {status} {detail}".strip())


class PoliteClient:
    def __init__(
        self,
        user_agent: str,
        *,
        timeout: int = DEFAULT_TIMEOUT,
        sec_interval: float = SEC_MIN_INTERVAL,
        default_interval: float = DEFAULT_MIN_INTERVAL,
        session: Optional[requests.Session] = None,
    ):
        if not user_agent or "@" not in user_agent:
            raise ValueError(
                "User-Agent must identify the client with a contact email "
                '(example: "finances-research you@example.com")'
            )
        self.user_agent = user_agent
        self.timeout = timeout
        self.sec_interval = sec_interval
        self.default_interval = default_interval
        self.session = session or requests.Session()
        self.session.headers.update(
            {
                "User-Agent": user_agent,
                "Accept-Encoding": "gzip, deflate",
                "Accept": "application/json, text/csv, text/html, application/xhtml+xml, */*;q=0.8",
            }
        )
        self._last_by_bucket: dict[str, float] = {}

    def _bucket(self, url: str) -> str:
        host = (urlparse(url).hostname or "").lower()
        if host == SEC_HOST_SUFFIX or host.endswith("." + SEC_HOST_SUFFIX):
            return "sec"
        return host

    def _interval(self, url: str) -> float:
        return self.sec_interval if self._bucket(url) == "sec" else self.default_interval

    def _wait(self, url: str) -> None:
        bucket = self._bucket(url)
        interval = self._interval(url)
        last = self._last_by_bucket.get(bucket, 0.0)
        delay = interval - (time.monotonic() - last)
        if delay > 0:
            time.sleep(delay)

    def get(self, url: str, *, retries: int = 3) -> requests.Response:
        last_error: Optional[Exception] = None
        for attempt in range(retries):
            self._wait(url)
            self._last_by_bucket[self._bucket(url)] = time.monotonic()
            try:
                response = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            except requests.RequestException as exc:
                last_error = exc
                if attempt + 1 < retries:
                    time.sleep(min(2 ** attempt, 8))
                continue
            self._last_by_bucket[self._bucket(url)] = time.monotonic()
            if response.status_code in {429, 500, 502, 503, 504}:
                last_error = HttpError(url, response.status_code, response.reason)
                delay = self._retry_after(response.headers.get("Retry-After"), min(2 ** attempt, 8))
                if delay > 60:
                    raise HttpError(url, response.status_code, f"Retry-After={delay:.0f}s; retry later")
                if attempt + 1 < retries:
                    time.sleep(delay)
                continue
            if response.status_code == 403 and self._bucket(url) == "sec":
                raise HttpError(
                    url,
                    403,
                    "SEC rejected the request; verify identifying User-Agent and fair-access limits before retrying",
                )
            if response.status_code >= 400:
                raise HttpError(url, response.status_code, response.reason)
            return response
        if last_error:
            raise HttpError(url, getattr(last_error, "status", 0), str(last_error)) from last_error
        raise HttpError(url, 0, "exhausted retries")

    @staticmethod
    def _retry_after(value: Optional[str], fallback: float) -> float:
        if value:
            try:
                return max(0, float(value))
            except ValueError:
                try:
                    when = parsedate_to_datetime(value)
                    if when.tzinfo is None:
                        when = when.replace(tzinfo=timezone.utc)
                    return max(0, (when - datetime.now(timezone.utc)).total_seconds())
                except (ValueError, TypeError, OverflowError):
                    pass
        return fallback

    def get_json(self, url: str) -> Any:
        response = self.get(url)
        try:
            return response.json()
        except ValueError as exc:
            raise HttpError(url, response.status_code, f"invalid JSON: {exc}") from exc

    def get_text(self, url: str) -> str:
        response = self.get(url)
        response.encoding = response.encoding or "utf-8"
        return response.text

    def get_bytes(self, url: str) -> bytes:
        return self.get(url).content
