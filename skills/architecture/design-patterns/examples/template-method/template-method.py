"""Template Method pattern in Python.

The base class fixes the report skeleton (generate); subclasses supply
the formatting steps. Note: Python often prefers composition or a
higher-order function taking the steps as arguments over inheritance;
the ABC form shown here is the classic pattern.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class LineItem:
    product: str
    units: int
    price: float

    @property
    def subtotal(self) -> float:
        return self.units * self.price


class SalesReport(ABC):
    def generate(self, items: list[LineItem]) -> str:
        """The template method: the skeleton is fixed here.

        Iteration and totalling never vary; only formatting does.
        """
        lines = [self.header()]
        lines.extend(self.row(item) for item in items)
        lines.append(self.footer(sum(item.subtotal for item in items)))
        return "\n".join(lines)

    @abstractmethod
    def header(self) -> str: ...

    @abstractmethod
    def row(self, item: LineItem) -> str: ...

    @abstractmethod
    def footer(self, total: float) -> str: ...


class CsvReport(SalesReport):
    def header(self) -> str:
        return "product,units,price,subtotal"

    def row(self, item: LineItem) -> str:
        return f"{item.product},{item.units},{item.price:.2f},{item.subtotal:.2f}"

    def footer(self, total: float) -> str:
        return f"total,,,{total:.2f}"


class MarkdownReport(SalesReport):
    def header(self) -> str:
        return "| Product | Units | Subtotal |\n| --- | --- | --- |"

    def row(self, item: LineItem) -> str:
        return f"| {item.product} | {item.units} | ${item.subtotal:.2f} |"

    def footer(self, total: float) -> str:
        return f"\n**Total: ${total:.2f}**"


if __name__ == "__main__":
    items = [
        LineItem("Keyboard", 2, 80.00),
        LineItem("Mouse", 1, 25.50),
        LineItem("Monitor", 3, 210.00),
    ]
    for report in (CsvReport(), MarkdownReport()):
        print(f"--- {type(report).__name__} ---")
        print(report.generate(items))
        print()
