"""Liskov Substitution Principle in Python.

Square-extends-Rectangle is the classic violation: overriding the
setters to keep the sides equal breaks Rectangle's invariant that
width and height vary independently. Duck typing means Python raises
no error -- the caller just silently gets the wrong area. The fix
keeps Rectangle and Square as separate immutable types behind a
common Shape protocol.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


# --- Violation: Square pretends to be a mutable Rectangle ---


class Rectangle:
    """Contract: width and height vary independently."""

    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def set_width(self, width: float) -> None:
        self._width = width

    def set_height(self, height: float) -> None:
        self._height = height

    def area(self) -> float:
        return self._width * self._height


class Square(Rectangle):
    """Keeps its sides equal -- and thereby breaks the base contract."""

    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    def set_width(self, width: float) -> None:  # also changes height!
        self._width = self._height = width

    def set_height(self, height: float) -> None:  # also changes width!
        self._width = self._height = height


def stretch_to_4x5(rect: Rectangle) -> float:
    """Written against Rectangle's contract: expects area 4 * 5 = 20."""
    rect.set_width(4)
    rect.set_height(5)
    return rect.area()


# --- Fix: separate immutable types behind a common Shape protocol ---


class Shape(Protocol):
    def area(self) -> float: ...


@dataclass(frozen=True)
class Rect:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height


@dataclass(frozen=True)
class Sq:
    side: float

    def area(self) -> float:
        return self.side * self.side


def total_area(shapes: list[Shape]) -> float:
    """Relies only on Shape's contract -- safe for every conformer."""
    return sum(shape.area() for shape in shapes)


if __name__ == "__main__":
    print("-- Violation: Square substituted for Rectangle --")
    for rect in (Rectangle(2, 3), Square(2)):
        got = stretch_to_4x5(rect)
        verdict = "ok" if got == 20 else "CONTRACT BROKEN"
        print(f"{type(rect).__name__:>9}: expected 20, got {got:g}  ({verdict})")

    print("\n-- Fix: separate types behind Shape --")
    shapes: list[Shape] = [Rect(4, 5), Sq(5)]
    for shape in shapes:
        print(f"{type(shape).__name__:>9}: area {shape.area():g}")
    print(f"    total: {total_area(shapes):g}")
