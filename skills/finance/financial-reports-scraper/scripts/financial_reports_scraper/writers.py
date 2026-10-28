from __future__ import annotations

from pathlib import Path

import pandas as pd

from .schema import COLUMNS, validate_rows


def rows_to_frame(rows: list[dict[str, str]]) -> pd.DataFrame:
    problems = validate_rows(rows)
    if problems:
        raise ValueError("invalid report rows: " + "; ".join(problems[:8]))
    frame = pd.DataFrame(rows, columns=COLUMNS).drop_duplicates()
    for column in ("cik", "isin", "ticker", "accession", "value"):
        if column in frame.columns:
            frame[column] = frame[column].astype("string")
    sort_cols = [
        "entity_type",
        "ticker",
        "isin",
        "record_kind",
        "statement",
        "concept",
        "period_end",
        "filed_at",
    ]
    return frame.sort_values(sort_cols, kind="mergesort").reset_index(drop=True)


def write_csv(frame: pd.DataFrame, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation preserves earlier runs and avoids a check/write race.
    with path.open("x", encoding="utf-8", newline="") as stream:
        frame.to_csv(stream, index=False, na_rep="")
    return path
