from __future__ import annotations

import argparse
import os
import json
import sys
from pathlib import Path
from dateutil.relativedelta import relativedelta

from .http import PoliteClient
from .periods import resolve_window
from .pipeline import run_report
from .portfolio import resolve_entities


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch official issuer reports and write one tidy CSV under --out-dir"
        )
    )
    parser.add_argument("--portfolio", type=Path, help="CSV with name, type, isin, ticker")
    parser.add_argument(
        "--tickers",
        help="Comma-separated tickers (US equities via EDGAR)",
    )
    parser.add_argument(
        "--period",
        default="month",
        help="month (default), quarter, year, or custom with --start/--end",
    )
    parser.add_argument("--start", help="YYYY-MM-DD inclusive start (optional)")
    parser.add_argument("--end", help="YYYY-MM-DD inclusive end (optional)")
    parser.add_argument("--as-of", dest="as_of", help="As-of date, default today")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("reports"),
        help="Directory for the CSV (default: reports/ in the current directory)",
    )
    parser.add_argument(
        "--user-agent",
        default=os.environ.get("SEC_USER_AGENT", ""),
        help='Identifying User-Agent, e.g. "finances-research you@example.com"',
    )
    parser.add_argument(
        "--all-facts",
        action="store_true",
        help="Emit every us-gaap/ifrs-full/dei/srt tag, not only core face-statement tags",
    )
    parser.add_argument("--history-years", type=int, help="Multi-year window ending at the cutoff; cannot combine with --start")
    parser.add_argument("--download-filings", action="store_true", help="Save SEC primary filing HTML/PDF and readable HTML text with hashes")
    parser.add_argument("--max-filings", type=int, default=12, help="Maximum SEC snapshots per report (default: 12; manifest lists omitted files)")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    tickers = [args.tickers] if args.tickers else None
    try:
        entities = resolve_entities(portfolio=args.portfolio, tickers=tickers)
        window = resolve_window(
            period="month" if args.history_years is not None else args.period, as_of=args.as_of, start=args.start, end=args.end
        )
        if args.history_years is not None:
            if args.start or not 1 <= args.history_years <= 30:
                raise ValueError("--history-years requires 1–30 years and cannot combine with --start")
            window = resolve_window(period="custom", as_of=window.as_of, end=window.cutoff,
                                    start=window.cutoff - relativedelta(years=args.history_years))
        if args.max_filings < 1:
            raise ValueError("--max-filings must be positive")
        client = PoliteClient(args.user_agent)
        path = run_report(
            entities, window, client, out_dir=args.out_dir, core_only=not args.all_facts,
            download_filings=args.download_filings, max_filings=args.max_filings,
        )
    except (ValueError, OSError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(path)
    manifest_path = path.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    print(f"Coverage/provenance: {manifest_path}", file=sys.stderr)
    if manifest["error_count"]:
        print(f"Partial report: {manifest['error_count']} collection/download error(s); inspect the manifest", file=sys.stderr)
        return 1
    return 0
