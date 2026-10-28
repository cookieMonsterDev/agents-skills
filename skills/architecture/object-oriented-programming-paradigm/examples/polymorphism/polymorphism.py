"""Polymorphism in Python.

One loop calls area()/describe() on a mixed list and each object
answers with its own implementation (subtype polymorphism via an ABC).
Python's everyday form is duck typing: Square never inherits Shape,
yet it works at the same call site because it has the right methods.
"""

from __future__ import annotations

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """The abstraction: the only type the client mentions."""

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def describe(self) -> str: ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def describe(self) -> str:
        return f"circle r={self.radius}"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def describe(self) -> str:
        return f"rectangle {self.width}x{self.height}"


class Square:
    """No Shape base class: duck typing (ad-hoc polymorphism).

    Any object with area() and describe() fits the same loop.
    """

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2

    def describe(self) -> str:
        return f"square {self.side}x{self.side}"


def total_area(shapes) -> float:
    """Parametric in spirit: works for any iterable of shape-like objects."""
    return sum(s.area() for s in shapes)


if __name__ == "__main__":
    shapes = [Circle(1.0), Rectangle(3.0, 4.0), Square(2.0)]

    # One call site, three implementations: the runtime type decides.
    for shape in shapes:
        print(f"{shape.describe():>18}: area {shape.area():.2f}")

    print(f"{'total':>18}: area {total_area(shapes):.2f}")
