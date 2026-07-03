"""Bridge pattern in Python.

Splits shapes (the abstraction) from renderers (the implementation) so
the two hierarchies vary independently: adding a shape never touches
the renderers, and adding a renderer never touches the shapes. With
duck typing the Renderer ABC is optional documentation.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Renderer(ABC):
    """Implementation interface."""

    @abstractmethod
    def circle(self, radius: float) -> str: ...

    @abstractmethod
    def rectangle(self, width: float, height: float) -> str: ...


class VectorRenderer(Renderer):
    def circle(self, radius: float) -> str:
        return f"<circle r={radius:.1f}/>"

    def rectangle(self, width: float, height: float) -> str:
        return f"<rect w={width:.1f} h={height:.1f}/>"


class RasterRenderer(Renderer):
    def circle(self, radius: float) -> str:
        return f"pixels for a circle of radius {radius:.1f}"

    def rectangle(self, width: float, height: float) -> str:
        return f"pixels for a {width:.1f}x{height:.1f} rectangle"


class Shape(ABC):
    """Abstraction: holds a renderer and delegates the drawing to it."""

    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> str: ...


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float) -> None:
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> str:
        return self.renderer.circle(self.radius)


class Rectangle(Shape):
    def __init__(self, renderer: Renderer, width: float, height: float) -> None:
        super().__init__(renderer)
        self.width = width
        self.height = height

    def draw(self) -> str:
        return self.renderer.rectangle(self.width, self.height)


if __name__ == "__main__":
    for renderer in (VectorRenderer(), RasterRenderer()):
        for shape in (Circle(renderer, 5.0), Rectangle(renderer, 3.0, 4.0)):
            print(shape.draw())
