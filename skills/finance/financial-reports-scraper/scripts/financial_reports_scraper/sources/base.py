from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Protocol

from ..periods import Window


class HttpClient(Protocol):
    def get_json(self, url: str) -> Any: ...

    def get_text(self, url: str) -> str: ...

    def get_bytes(self, url: str) -> bytes: ...


class SourceAdapter(ABC):
    name: str

    @abstractmethod
    def collect(self, entity: dict[str, str], window: Window) -> list[dict[str, str]]:
        """Return tidy rows for one entity and window."""
