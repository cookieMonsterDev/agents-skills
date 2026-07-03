"""Memento pattern in Python.

A text editor saves snapshots of its state so a history object can undo
edits without ever looking inside the editor. A frozen dataclass makes
the memento immutable; Python has no enforced privacy, so opacity is by
convention (the caretaker just never touches snapshot fields).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Snapshot:
    """Memento: immutable, opaque to the caretaker."""

    text: str
    cursor: int


class TextEditor:
    """Originator: the only class that reads or writes snapshot state."""

    def __init__(self) -> None:
        self._text = ""
        self._cursor = 0

    def type(self, text: str) -> None:
        self._text = self._text[: self._cursor] + text + self._text[self._cursor :]
        self._cursor += len(text)

    def save(self) -> Snapshot:
        return Snapshot(self._text, self._cursor)

    def restore(self, snapshot: Snapshot) -> None:
        self._text = snapshot.text
        self._cursor = snapshot.cursor

    def __str__(self) -> str:
        return f"{self._text!r} (cursor at {self._cursor})"


class History:
    """Caretaker: stores mementos but never inspects them."""

    def __init__(self) -> None:
        self._snapshots: list[Snapshot] = []

    def push(self, snapshot: Snapshot) -> None:
        self._snapshots.append(snapshot)

    def pop(self) -> Snapshot | None:
        return self._snapshots.pop() if self._snapshots else None


if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.type("Hello")
    history.push(editor.save())
    editor.type(", world")
    history.push(editor.save())
    editor.type("!!!")
    print("current:", editor)

    for _ in range(2):
        snapshot = history.pop()
        if snapshot:
            editor.restore(snapshot)
            print("undo:   ", editor)
