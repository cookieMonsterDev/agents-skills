"""Load one entity or a portfolio table. Blank NOTES rows are skipped."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Iterable, Optional

from .schema import pad_cik

ENTITY_FIELDS = (
    "entity_name",
    "entity_type",
    "ticker",
    "isin",
    "cik",
    "lei",
    "market",
)

TYPE_ALIASES = {
    "stock": "stock",
    "equity": "stock",
    "share": "stock",
    "etf": "etf",
    "etc": "etc",
    "fund": "etf",
}


def normalize_type(value: str) -> str:
    key = (value or "").strip().lower()
    return TYPE_ALIASES.get(key, key)


def _blank(value: Any) -> bool:
    return value is None or str(value).strip() == ""


def make_entity(
    *,
    entity_name: str = "",
    entity_type: str = "",
    ticker: str = "",
    isin: str = "",
    cik: str = "",
    lei: str = "",
    market: str = "",
) -> dict[str, str]:
    return {
        "entity_name": entity_name.strip(),
        "entity_type": normalize_type(entity_type),
        "ticker": ticker.strip().upper(),
        "isin": isin.strip().upper(),
        "cik": pad_cik(cik),
        "lei": lei.strip(),
        "market": market.strip(),
    }


def is_blank_entity(entity: dict[str, str]) -> bool:
    return not any(entity.get(key) for key in ("ticker", "isin", "cik", "entity_name"))


def entities_from_tickers(tickers: Iterable[str], entity_type: str = "stock") -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for raw in tickers:
        for piece in str(raw).split(","):
            ticker = piece.strip()
            if not ticker:
                continue
            out.append(make_entity(ticker=ticker, entity_type=entity_type, entity_name=ticker))
    return out


def _pick(row: dict[str, str], *names: str) -> str:
    lower = {key.strip().lower().replace(" ", "_"): value for key, value in row.items()}
    for name in names:
        if name in lower and not _blank(lower[name]):
            return str(lower[name]).strip()
    return ""


def load_portfolio(path: Path) -> list[dict[str, str]]:
    entities: list[dict[str, str]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path} has no header row")
        for row in reader:
            entity = make_entity(
                entity_name=_pick(row, "entity_name", "company_name", "name"),
                entity_type=_pick(row, "entity_type", "type"),
                ticker=_pick(row, "ticker"),
                isin=_pick(row, "isin"),
                cik=_pick(row, "cik"),
                lei=_pick(row, "lei"),
                market=_pick(row, "market", "exchange"),
            )
            if is_blank_entity(entity):
                continue
            entities.append(entity)
    return entities


def resolve_entities(
    *,
    portfolio: Optional[Path] = None,
    tickers: Optional[Iterable[str]] = None,
) -> list[dict[str, str]]:
    entities: list[dict[str, str]] = []
    if portfolio is not None:
        entities.extend(load_portfolio(portfolio))
    if tickers:
        entities.extend(entities_from_tickers(tickers))
    # De-dupe on the strongest identifier present.
    seen: set[tuple[str, str, str]] = set()
    unique: list[dict[str, str]] = []
    for entity in entities:
        key = (entity["isin"], entity["cik"], entity["ticker"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(entity)
    if not unique:
        raise ValueError("no entities resolved; pass --portfolio or --tickers")
    return unique
