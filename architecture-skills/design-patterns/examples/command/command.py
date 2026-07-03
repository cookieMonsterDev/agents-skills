"""Command pattern in Python.

Text editor with undo: each command mutates the editor and knows how to
reverse itself; a history stack replays undo in LIFO order.

Note: for one-shot commands without undo, a plain function or closure is
the Pythonic form (shown at the bottom); classes earn their keep once
commands carry undo state.
"""

from __future__ import annotations


class Editor:
    """Receiver: the object commands operate on."""

    def __init__(self) -> None:
        self.text = ""


class InsertText:
    def __init__(self, editor: Editor, text: str) -> None:
        self._editor = editor
        self._text = text

    def execute(self) -> None:
        self._editor.text += self._text

    def undo(self) -> None:
        self._editor.text = self._editor.text[: -len(self._text)]


class DeleteLast:
    def __init__(self, editor: Editor, count: int) -> None:
        self._editor = editor
        self._count = count
        self._deleted = ""  # captured on execute so undo can restore it

    def execute(self) -> None:
        self._deleted = self._editor.text[-self._count:]
        self._editor.text = self._editor.text[: -self._count]

    def undo(self) -> None:
        self._editor.text += self._deleted


class History:
    """Invoker: runs commands and tracks them for undo."""

    def __init__(self) -> None:
        self._undo_stack: list[InsertText | DeleteLast] = []

    def execute(self, command: InsertText | DeleteLast) -> None:
        command.execute()
        self._undo_stack.append(command)

    def undo(self) -> None:
        if self._undo_stack:
            self._undo_stack.pop().undo()


if __name__ == "__main__":
    editor = Editor()
    history = History()

    history.execute(InsertText(editor, "Hello"))
    history.execute(InsertText(editor, ", world!"))
    history.execute(DeleteLast(editor, 1))
    print(f"after edits: {editor.text!r}")

    history.undo()
    history.undo()
    print(f"after 2 undos: {editor.text!r}")

    # Closure form: fine when no undo state is needed.
    shout = lambda: print(editor.text.upper())  # noqa: E731
    shout()
