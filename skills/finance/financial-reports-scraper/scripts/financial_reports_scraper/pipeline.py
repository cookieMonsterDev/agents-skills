"""One entry point: entities + window -> one tidy CSV."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from .periods import Window, report_filename
from .schema import fill_row, merge_entity
from .sources.edgar import EdgarAdapter
from .sources.ishares import IsharesAdapter, load_catalog
from .sources.router import choose_adapter
from .writers import rows_to_frame, write_csv
from .http import HttpError
from .evidence import snapshot_filings, write_manifest

CATALOG_PATH = Path(__file__).resolve().parents[1] / "data" / "ishares_catalog.json"


def run_report(
    entities: list[dict[str, str]],
    window: Window,
    client,
    out_dir: Optional[Path] = None,
    *,
    core_only: bool = True,
    adapters: Optional[dict] = None,
    download_filings: bool = False,
    max_filings: int = 12,
) -> Path:
    if max_filings < 1:
        raise ValueError("max_filings must be positive")
    dest = (out_dir or Path("reports")) / report_filename(window)
    companions = [dest, dest.with_suffix(".manifest.json"), dest.parent / (dest.stem + "-documents")]
    if any(p.exists() for p in companions):
        raise FileExistsError(f"Report bundle exists; choose a new --out-dir: {dest}")
    catalog = load_catalog(CATALOG_PATH)
    built = adapters or {
        "edgar": EdgarAdapter(client, core_only=core_only),
        "ishares": IsharesAdapter(client, catalog=catalog),
    }
    rows: list[dict[str, str]] = []
    for entity in entities:
        name = choose_adapter(entity, catalog)
        if name is None:
            row = fill_row(
                {
                    "as_of_date": window.as_of_iso,
                    "window_start": window.start_iso,
                    "window_end": window.end_iso,
                    "grain": window.grain,
                    "record_kind": "error",
                    "inclusion_reason": "adapter_error",
                    "concept": "no_adapter",
                    "notes": (
                        "no official adapter for this entity; see "
                        "references/topic-map.md (do not fall back to Yahoo)"
                    ),
                }
            )
            merge_entity(row, entity)
            rows.append(row)
            continue
        adapter = built[name]
        try:
            collected = adapter.collect(entity, window)
            if not collected:
                raise ValueError("adapter returned no observations")
            rows.extend(collected)
        except (HttpError, OSError, ValueError, TypeError) as exc:
            row = fill_row({"as_of_date": window.as_of_iso, "window_start": window.start_iso,
                           "window_end": window.end_iso, "grain": window.grain, "record_kind": "error",
                           "inclusion_reason": "adapter_error", "source": name, "concept": "collection_error", "notes": str(exc)})
            merge_entity(row, entity)
            rows.append(row)

    if not rows:
        raise RuntimeError("adapters returned no rows")

    frame = rows_to_frame(rows)
    write_csv(frame, dest)
    documents = snapshot_filings(frame.to_dict("records"), client, companions[2], max_filings) if download_filings else []
    write_manifest(dest, frame, window, documents, download_filings)
    return dest
