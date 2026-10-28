from __future__ import annotations

from datetime import date

import pytest

from financial_reports_scraper.periods import report_filename, resolve_window


def test_month_window_default_grain():
    window = resolve_window(period="month", as_of="2026-09-10")
    assert window.grain == "month"
    assert window.start == date(2026, 8, 10)
    assert window.end == date(2026, 9, 10)
    assert report_filename(window) == "2026-09-10-report-2026-08-10-2026-09-10.csv"


def test_quarter_and_year():
    quarter = resolve_window(period="quarter", as_of="2026-09-10")
    year = resolve_window(period="1y", as_of="2026-09-10")
    assert quarter.start == date(2026, 6, 10)
    assert year.start == date(2025, 9, 10)


def test_explicit_start_end_keeps_requested_grain():
    window = resolve_window(
        period="month", as_of="2026-09-10", start="2026-01-01", end="2026-03-31"
    )
    assert window.start == date(2026, 1, 1)
    assert window.end == date(2026, 3, 31)
    assert window.grain == "month"


def test_unknown_period_raises():
    with pytest.raises(ValueError, match="unknown period"):
        resolve_window(period="week")
