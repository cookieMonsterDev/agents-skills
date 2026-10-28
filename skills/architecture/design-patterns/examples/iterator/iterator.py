"""Iterator pattern in Python.

A binary search tree that yields its values in sorted order. Python has
iterators built in: instead of a hand-rolled GoF iterator class, the
idiomatic form implements __iter__ as a generator — the generator's
paused frame *is* the iterator state. This plugs the collection into
for loops, comprehensions, sum(), list(), etc.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class _Node:
    value: int
    left: _Node | None = None
    right: _Node | None = None


class SortedTree:
    """Custom collection: an unbalanced binary search tree."""

    def __init__(self) -> None:
        self._root: _Node | None = None

    def add(self, value: int) -> None:
        if self._root is None:
            self._root = _Node(value)
            return
        node = self._root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = _Node(value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = _Node(value)
                    return
                node = node.right

    def __iter__(self) -> Iterator[int]:
        """In-order traversal; each call returns a fresh, independent iterator."""
        yield from self._walk(self._root)

    def _walk(self, node: _Node | None) -> Iterator[int]:
        if node is not None:
            yield from self._walk(node.left)
            yield node.value
            yield from self._walk(node.right)


if __name__ == "__main__":
    tree = SortedTree()
    for value in (5, 3, 8, 1, 4, 9, 7):
        tree.add(value)

    print("in order:", list(tree))
    print("sum:     ", sum(tree))
    print("evens:   ", [v for v in tree if v % 2 == 0])
