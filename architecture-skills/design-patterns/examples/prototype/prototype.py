"""Prototype pattern in Python.

Note: the pattern is built into the standard library as the `copy` module.
`copy.deepcopy` handles nested state; customize with __copy__/__deepcopy__
when some fields must be shared or reset instead of duplicated.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, field


@dataclass
class Circle:
    x: float
    y: float
    radius: float
    color: str
    tags: list[str] = field(default_factory=list)

    def clone(self) -> Circle:
        # deepcopy so the copy gets its own tags list, not an alias
        return copy.deepcopy(self)

    def describe(self) -> str:
        return f"Circle r={self.radius} {self.color} at ({self.x}, {self.y}) tags={self.tags}"


class ShapeRegistry:
    """Catalog of pre-configured prototypes, cloned instead of constructed."""

    def __init__(self) -> None:
        self._prototypes: dict[str, Circle] = {}

    def register(self, name: str, prototype: Circle) -> None:
        self._prototypes[name] = prototype

    def create(self, name: str) -> Circle:
        return self._prototypes[name].clone()


if __name__ == "__main__":
    registry = ShapeRegistry()
    registry.register(
        "warning-marker", Circle(x=0, y=0, radius=12, color="red", tags=["alert"])
    )

    first = registry.create("warning-marker")
    second = registry.create("warning-marker")
    second.x, second.y = 40, 25
    second.tags.append("muted")

    print(first.describe())
    print(second.describe())
    print("independent copies:", first.tags is not second.tags)
