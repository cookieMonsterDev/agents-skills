"""Named extract windows. Grain labels the extract; it does not invent monthly P&L."""

from __future__ import annotations

from dataclasses import dataclass
import re
from datetime import date, datetime
from typing import Optional, Union

from dateutil.relativedelta import relativedelta

Dateish = Union[str, date, datetime, None]

GRAIN_ALIASES = {
    "month": "month",
    "1m": "month",
    "1mo": "month",
    "m": "month",
    "quarter": "quarter",
    "1q": "quarter",
    "q": "quarter",
    "year": "year",
    "1y": "year",
    "y": "year",
    "annual": "year",
    "custom": "custom",
}

_DELTAS = {
    "month": relativedelta(months=1),
    "quarter": relativedelta(months=3),
    "year": relativedelta(years=1),
}


@dataclass(frozen=True)
class Window:
    start: date
    end: date
    grain: str
    as_of: date

    def contains(self, day: Optional[date]) -> bool:
        if day is None:
            return False
        return self.start <= day <= self.end

    @property
    def cutoff(self) -> date:
        """Latest information date, distinct from the observation window."""
        return min(self.end, self.as_of)

    @property
    def start_iso(self) -> str:
        return self.start.isoformat()

    @property
    def end_iso(self) -> str:
        return self.end.isoformat()

    @property
    def as_of_iso(self) -> str:
        return self.as_of.isoformat()


def parse_date(value: Dateish) -> Optional[date]:
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value).strip()
    if not text:
        return None
    if "T" in text:
        text = text.split("T", 1)[0]
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def normalize_grain(period: str) -> str:
    key = (period or "month").strip().lower()
    if key not in GRAIN_ALIASES:
        allowed = ", ".join(sorted(set(GRAIN_ALIASES.values())))
        raise ValueError(f"unknown period {period!r}; use {allowed}")
    return GRAIN_ALIASES[key]


def resolve_window(
    period: str = "month",
    as_of: Dateish = None,
    start: Dateish = None,
    end: Dateish = None,
) -> Window:
    for label, value in (("as-of", as_of), ("start", start), ("end", end)):
        if value is not None and (parse_date(value) is None or (isinstance(value, str) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value))):
            raise ValueError(f"invalid {label} date: {value!r}; use YYYY-MM-DD")
    as_of_date = parse_date(as_of) or date.today()
    start_date = parse_date(start)
    end_date = parse_date(end)

    if start_date and end_date:
        if start_date > end_date:
            raise ValueError("start_date must be on or before end_date")
        grain = "custom" if normalize_grain(period) == "custom" else normalize_grain(period)
        if start is not None and end is not None and period in GRAIN_ALIASES:
            grain = normalize_grain(period)
        return Window(start=start_date, end=end_date, grain=grain, as_of=as_of_date)

    grain = normalize_grain(period)
    if grain == "custom":
        raise ValueError("custom period requires both --start and --end")
    end_date = end_date or as_of_date
    start_date = start_date or (end_date - _DELTAS[grain])
    if start_date > end_date:
        raise ValueError("start_date must be on or before end_date")
    return Window(start=start_date, end=end_date, grain=grain, as_of=as_of_date)


def report_filename(window: Window, as_of: Optional[date] = None) -> str:
    current = (as_of or window.as_of).isoformat()
    return f"{current}-report-{window.start_iso}-{window.end_iso}.csv"
