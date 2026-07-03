"""Flyweight pattern in Python.

Intrinsic state (tree species) is shared; extrinsic state (position)
lives in each context. Note: Python interns small ints and many strings
as built-in flyweights, and functools.lru_cache on a factory function
is the shortest explicit implementation — shown here.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class TreeType:
    """Flyweight: immutable intrinsic state shared by many trees."""

    name: str
    color: str

    def draw(self, x: int, y: int) -> None:
        print(f"{self.color} {self.name} at ({x}, {y})")


@lru_cache(maxsize=None)
def get_tree_type(name: str, color: str) -> TreeType:
    """Flyweight factory: same arguments always return the same instance."""
    return TreeType(name, color)


@dataclass
class Tree:
    """Context: extrinsic state plus a reference to the shared flyweight."""

    x: int
    y: int
    kind: TreeType


class Forest:
    def __init__(self) -> None:
        self._trees: list[Tree] = []

    def plant(self, x: int, y: int, name: str, color: str) -> None:
        self._trees.append(Tree(x, y, get_tree_type(name, color)))

    def draw(self) -> None:
        for tree in self._trees:
            tree.kind.draw(tree.x, tree.y)


if __name__ == "__main__":
    forest = Forest()
    forest.plant(1, 1, "oak", "green")
    forest.plant(2, 4, "pine", "dark green")
    forest.plant(5, 2, "oak", "green")
    forest.plant(6, 6, "birch", "light green")
    forest.plant(8, 3, "pine", "dark green")
    forest.plant(9, 9, "oak", "green")
    forest.draw()

    info = get_tree_type.cache_info()
    print(f"trees planted: 6, tree types in memory: {info.currsize}")
