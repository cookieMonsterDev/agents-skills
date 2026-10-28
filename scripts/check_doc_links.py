#!/usr/bin/env python3
"""Check every HTTP(S) link inside the skill Markdown files.

The docs skills exist to hand out authoritative links, so a rotted link is a
real defect. This script extracts links, requests each one, and reports the
ones that no longer resolve to a live page.

Links that answer 401/403/429 are reported separately as inconclusive: those
statuses mean the host refused a scripted request, not that the page is gone.

Usage:
    scripts/check_doc_links.py                        # check every skill
    scripts/check_doc_links.py skills/docs/redis-docs # check selected paths
    scripts/check_doc_links.py --json report.json     # machine-readable output
    scripts/check_doc_links.py --host-delay 2         # slow hosts that answer 429
    scripts/check_doc_links.py --strict               # count blocked links as failures

Exit status is 1 when at least one link is broken, so it can gate CI.
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ROOTS = ("skills",)

# Markdown inline links, angle-bracket autolinks and bare URLs all appear in the
# skills, so match the URL itself and strip trailing punctuation afterwards.
URL_RE = re.compile(r"https?://[^\s)\]>\"'`]+")
TRAILING_PUNCT = ".,;:!?"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

# 403/429 mean the host refused to talk to a script, not that the page is gone.
# Reporting those as broken buries the real 404s, so they get their own bucket.
BLOCKED_STATUSES = frozenset({401, 403, 429})


def iter_markdown_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        target = Path(raw)
        if not target.is_absolute():
            target = REPO_ROOT / target
        if target.is_file() and target.suffix == ".md":
            files.append(target)
        elif target.is_dir():
            files.extend(sorted(target.rglob("*.md")))
        else:
            print(f"warning: skipping {raw} (not a Markdown file or directory)", file=sys.stderr)
    return files


def extract_links(files: list[Path]) -> dict[str, list[str]]:
    """Map each URL to the `path:line` locations that reference it."""
    locations: dict[str, list[str]] = defaultdict(list)
    for path in files:
        rel = path.relative_to(REPO_ROOT)
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in URL_RE.finditer(line):
                url = match.group(0).rstrip(TRAILING_PUNCT)
                locations[url].append(f"{rel}:{lineno}")
    return dict(locations)


class HostThrottle:
    """Serialize requests per host with a minimum gap between them.

    Docs hosts such as docs.djangoproject.com answer 429 when a link sweep
    hits them with 24 parallel requests, which produces noise rather than
    findings.
    """

    def __init__(self, delay: float) -> None:
        self.delay = delay
        self._lock = threading.Lock()
        self._locks: dict[str, threading.Lock] = {}
        self._last: dict[str, float] = {}

    def _host_lock(self, host: str) -> threading.Lock:
        with self._lock:
            return self._locks.setdefault(host, threading.Lock())

    def wait(self, url: str) -> "HostSlot":
        host = urllib.parse.urlsplit(url).netloc
        return HostSlot(self, host)

    def acquire(self, host: str) -> None:
        if self.delay <= 0:
            return
        lock = self._host_lock(host)
        lock.acquire()
        gap = self.delay - (time.monotonic() - self._last.get(host, 0.0))
        if gap > 0:
            time.sleep(gap)

    def release(self, host: str) -> None:
        if self.delay <= 0:
            return
        self._last[host] = time.monotonic()
        self._host_lock(host).release()


class HostSlot:
    def __init__(self, throttle: HostThrottle, host: str) -> None:
        self.throttle = throttle
        self.host = host

    def __enter__(self) -> "HostSlot":
        self.throttle.acquire(self.host)
        return self

    def __exit__(self, *exc) -> None:
        self.throttle.release(self.host)


def interleave_by_host(urls: list[str]) -> list[str]:
    """Round-robin the URLs across hosts.

    Submitting a host-sorted list starves the pool: every worker grabs a URL
    from the same host and all but one block on that host's throttle lock.
    Interleaving keeps as many distinct hosts in flight as there are workers.
    """
    buckets: dict[str, list[str]] = defaultdict(list)
    for url in urls:
        buckets[urllib.parse.urlsplit(url).netloc].append(url)
    queues = list(buckets.values())
    ordered: list[str] = []
    for index in range(max((len(q) for q in queues), default=0)):
        for queue in queues:
            if index < len(queue):
                ordered.append(queue[index])
    return ordered


def build_opener(insecure: bool) -> urllib.request.OpenerDirector:
    context = ssl._create_unverified_context() if insecure else ssl.create_default_context()
    return urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))


def check_url(opener, url: str, timeout: float, retries: int, throttle: HostThrottle) -> tuple[int | None, str]:
    """Return (status, note). A None status means the request never completed."""
    last_error = ""
    for attempt in range(retries + 1):
        with throttle.wait(url):
            status, note, last_error = attempt_url(opener, url, timeout)
        if status is not None:
            return status, note
    return None, last_error or "request failed"


def attempt_url(opener, url: str, timeout: float) -> tuple[int | None, str, str]:
    """One pass over the request methods. Returns (status, note, error)."""
    last_error = ""
    # Several docs hosts reject HEAD, so fall back to GET before calling it broken.
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method)
        request.add_header("User-Agent", USER_AGENT)
        request.add_header("Accept", "text/html,application/xhtml+xml,*/*")
        try:
            with opener.open(request, timeout=timeout) as response:
                final = response.geturl()
                note = "" if final == url else f"redirected to {final}"
                return response.status, note, ""
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in (400, 403, 404, 405, 429, 501):
                continue  # host dislikes HEAD; retry the same URL with GET
            return exc.code, exc.reason or "", ""
        except urllib.error.URLError as exc:
            last_error = str(exc.reason)
            break
        except Exception as exc:  # timeouts, malformed responses, resets
            last_error = f"{type(exc).__name__}: {exc}"
            break
    return None, "", last_error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", default=list(DEFAULT_ROOTS),
                        help="Markdown files or directories to scan (default: skills)")
    parser.add_argument("--workers", type=int, default=16, help="concurrent requests (default: 16)")
    parser.add_argument("--timeout", type=float, default=25.0, help="per-request timeout in seconds (default: 25)")
    parser.add_argument("--retries", type=int, default=1, help="retries for network-level failures (default: 1)")
    parser.add_argument("--host-delay", type=float, default=0.5,
                        help="minimum seconds between requests to the same host (default: 0.5)")
    parser.add_argument("--strict", action="store_true",
                        help="treat bot-blocked responses (401/403/429) as failures too")
    parser.add_argument("--json", metavar="FILE", help="write the full result set to FILE as JSON")
    parser.add_argument("--insecure", action="store_true", help="skip TLS certificate verification")
    parser.add_argument("--show-redirects", action="store_true", help="also list links that resolved via a redirect")
    args = parser.parse_args()

    files = iter_markdown_files(args.paths or list(DEFAULT_ROOTS))
    if not files:
        print("no Markdown files found", file=sys.stderr)
        return 2

    locations = extract_links(files)
    urls = interleave_by_host(sorted(locations))
    print(f"checking {len(urls)} unique links from {len(files)} files", file=sys.stderr)

    opener = build_opener(args.insecure)
    throttle = HostThrottle(args.host_delay)
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        statuses = pool.map(lambda u: check_url(opener, u, args.timeout, args.retries, throttle), urls)
        for url, (status, note) in zip(urls, statuses):
            ok = status is not None and 200 <= status < 400
            blocked = status in BLOCKED_STATUSES
            results.append({
                "url": url,
                "status": status,
                "note": note,
                "ok": ok,
                "blocked": blocked,
                "locations": locations[url],
            })
            print("." if ok else ("?" if blocked else "F"), end="", flush=True, file=sys.stderr)
    print("", file=sys.stderr)

    blocked = [r for r in results if r["blocked"]]
    failures = [r for r in results if not r["ok"] and (args.strict or not r["blocked"])]
    redirects = [r for r in results if r["ok"] and r["note"]]

    if args.json:
        Path(args.json).write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {args.json}", file=sys.stderr)

    if args.show_redirects and redirects:
        print(f"\n{len(redirects)} redirected links:")
        for r in redirects:
            print(f"  {r['url']}\n    {r['note']}\n    {', '.join(r['locations'])}")

    if blocked and not args.strict:
        print(f"\n{len(blocked)} links inconclusive - the host blocked the checker (verify by hand):")
        for r in sorted(blocked, key=lambda r: r["url"]):
            print(f"  [{r['status']}] {r['url']}")

    if failures:
        print(f"\n{len(failures)} broken links:")
        for r in sorted(failures, key=lambda r: r["locations"][0]):
            status = r["status"] if r["status"] is not None else "ERR"
            detail = f" ({r['note']})" if r["note"] else ""
            print(f"  [{status}]{detail} {r['url']}")
            for loc in r["locations"]:
                print(f"    {loc}")
        return 1

    print(f"\n{len(results) - len(blocked)} links OK, {len(blocked)} inconclusive, 0 broken")
    return 0


if __name__ == "__main__":
    sys.exit(main())
