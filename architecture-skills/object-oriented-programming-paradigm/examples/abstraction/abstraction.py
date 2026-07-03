"""Abstraction in Python.

Callers see the essential model of a note store -- save and load --
while each implementation hides its operational detail (a dict vs a
file on disk). Python could rely on duck typing alone, but an ABC
names the contract explicitly; the same client runs against both
implementations untouched.
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod


class NoteStore(ABC):
    """The abstraction: the only surface callers may rely on."""

    @abstractmethod
    def save(self, key: str, text: str) -> None: ...

    @abstractmethod
    def load(self, key: str) -> str | None: ...


class MemoryStore(NoteStore):
    """Operational detail: a dict. Callers never see it."""

    def __init__(self) -> None:
        self._notes: dict[str, str] = {}

    def save(self, key: str, text: str) -> None:
        self._notes[key] = text

    def load(self, key: str) -> str | None:
        return self._notes.get(key)


class FileStore(NoteStore):
    """Operational detail: append-only lines in a file, last write wins."""

    def __init__(self, path: str) -> None:
        self._path = path

    def save(self, key: str, text: str) -> None:
        with open(self._path, "a", encoding="utf-8") as f:
            f.write(f"{key}\t{text}\n")

    def load(self, key: str) -> str | None:
        if not os.path.exists(self._path):
            return None
        found = None
        with open(self._path, encoding="utf-8") as f:
            for line in f:
                k, _, text = line.rstrip("\n").partition("\t")
                if k == key:
                    found = text  # keep scanning: last write wins
        return found


def run_session(store: NoteStore) -> None:
    """Client: written once against the abstraction, never edited when
    the implementation behind it swaps."""
    store.save("groceries", "eggs, flour")
    store.save("groceries", "eggs, flour, milk")  # overwrite
    store.save("idea", "hide the how, expose the what")
    print("  groceries:", store.load("groceries"))
    print("  idea:     ", store.load("idea"))
    print("  missing:  ", store.load("missing"))


if __name__ == "__main__":
    print("memory-backed store:")
    run_session(MemoryStore())

    path = "abstraction_demo.txt"
    try:
        print("file-backed store:")
        run_session(FileStore(path))
    finally:
        if os.path.exists(path):
            os.remove(path)
