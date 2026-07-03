"""Visitor pattern in Python.

Classic double dispatch: each shape's accept() calls the visitor method
for its concrete type, so new operations (area, SVG export) are added
without touching the shape classes. Note: Python's dynamic typing also
allows singledispatch or isinstance-based dispatch, which many codebases
prefer over the accept() boilerplate.
"""

from __future__ import annotations

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass


class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: Circle): ...

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle): ...

    @abstractmethod
    def visit_triangle(self, triangle: Triangle): ...


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor): ...


@dataclass(frozen=True)
class Circle(Shape):
    radius: float

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_circle(self)


@dataclass(frozen=True)
class Rectangle(Shape):
    width: float
    height: float

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_rectangle(self)


@dataclass(frozen=True)
class Triangle(Shape):
    base: float
    height: float

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_triangle(self)


class AreaVisitor(ShapeVisitor):
    def visit_circle(self, circle: Circle) -> float:
        return math.pi * circle.radius**2

    def visit_rectangle(self, rectangle: Rectangle) -> float:
        return rectangle.width * rectangle.height

    def visit_triangle(self, triangle: Triangle) -> float:
        return 0.5 * triangle.base * triangle.height


class SvgExportVisitor(ShapeVisitor):
    def visit_circle(self, circle: Circle) -> str:
        return f'<circle r="{circle.radius}" />'

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return f'<rect width="{rectangle.width}" height="{rectangle.height}" />'

    def visit_triangle(self, triangle: Triangle) -> str:
        return f'<polygon points="0,{triangle.height} {triangle.base},{triangle.height} 0,0" />'


if __name__ == "__main__":
    shapes: list[Shape] = [Circle(2), Rectangle(3, 4), Triangle(6, 2)]
    area, svg = AreaVisitor(), SvgExportVisitor()

    for shape in shapes:
        print(f"{type(shape).__name__:>9}: area={shape.accept(area):6.2f}  {shape.accept(svg)}")
    print(f"total area: {sum(s.accept(area) for s in shapes):.2f}")
