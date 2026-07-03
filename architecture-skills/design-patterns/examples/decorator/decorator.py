"""Decorator pattern in Python.

Wraps an object with another object of the same interface to add
behavior at runtime. Related to but different from Python's @decorator
syntax, which wraps functions or classes once at definition time; this
pattern stacks wrappers around individual instances dynamically.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def description(self) -> str: ...

    @abstractmethod
    def cost(self) -> float: ...


class Espresso(Beverage):
    def description(self) -> str:
        return "espresso"

    def cost(self) -> float:
        return 2.00


class AddOn(Beverage):
    """Base decorator: holds the wrapped beverage."""

    def __init__(self, inner: Beverage) -> None:
        self._inner = inner


class Milk(AddOn):
    def description(self) -> str:
        return f"{self._inner.description()} + milk"

    def cost(self) -> float:
        return self._inner.cost() + 0.30


class Mocha(AddOn):
    def description(self) -> str:
        return f"{self._inner.description()} + mocha"

    def cost(self) -> float:
        return self._inner.cost() + 0.50


class WhippedCream(AddOn):
    def description(self) -> str:
        return f"{self._inner.description()} + whipped cream"

    def cost(self) -> float:
        return self._inner.cost() + 0.40


if __name__ == "__main__":
    plain = Espresso()
    fancy = WhippedCream(Mocha(Milk(Espresso())))
    for drink in (plain, fancy):
        print(f"{drink.description()}: ${drink.cost():.2f}")
