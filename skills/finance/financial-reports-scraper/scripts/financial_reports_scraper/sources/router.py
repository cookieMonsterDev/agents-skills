"""Route an entity to one adapter. Unknown homes become error rows, not Yahoo."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from .ishares import load_catalog

_DEFAULT_CATALOG = (
    Path(__file__).resolve().parents[2] / "data" / "ishares_catalog.json"
)


def choose_adapter(
    entity: dict[str, str], catalog: Optional[dict] = None
) -> Optional[str]:
    catalog = catalog if catalog is not None else load_catalog(_DEFAULT_CATALOG)
    entity_type = (entity.get("entity_type") or "").lower()
    name = (entity.get("entity_name") or "").lower()
    isin = (entity.get("isin") or "").upper()

    if isin in catalog or "ishares" in name:
        return "ishares"
    if entity_type in {"etf", "etc"}:
        return None
    if entity.get("ticker") or entity.get("cik"):
        return "edgar"
    return None
