"""Interfaces & abstract classes in Python.

Python has no `interface` keyword: an abc.ABC with only abstract
methods plays the pure-contract role (typing.Protocol is the
structural alternative), while an ABC with implemented methods is an
abstract class. TabularExporter captures the shared line-assembly
logic once; JsonExporter satisfies the contract directly.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Metric:
    name: str
    value: float


class Exporter(ABC):
    """The interface: a pure contract, no implementation."""

    @property
    @abstractmethod
    def content_type(self) -> str: ...

    @abstractmethod
    def export(self, metrics: list[Metric]) -> str: ...

    def file_name(self) -> str:
        """A "default method": derived purely from the contract itself."""
        return "report." + self.content_type.rsplit("/", 1)[-1]


class TabularExporter(Exporter):
    """Abstract class: implements export() once, defers the varying parts."""

    @abstractmethod
    def header(self) -> str: ...

    @abstractmethod
    def row(self, metric: Metric) -> str: ...

    def export(self, metrics: list[Metric]) -> str:
        lines = [self.header(), *(self.row(m) for m in metrics)]
        lines.append(f"# {len(metrics)} records")
        return "\n".join(lines)


class CsvExporter(TabularExporter):
    content_type = "text/csv"

    def header(self) -> str:
        return "name,value"

    def row(self, metric: Metric) -> str:
        return f"{metric.name},{metric.value:.2f}"


class JsonExporter(Exporter):
    """Implements the contract directly — no base-class logic needed."""

    content_type = "application/json"

    def export(self, metrics: list[Metric]) -> str:
        entries = ", ".join(
            f'{{"name": "{m.name}", "value": {m.value:.2f}}}' for m in metrics
        )
        return f"[{entries}]"


def deliver(exporter: Exporter, metrics: list[Metric]) -> None:
    """The client programs to the contract, never to a concrete class."""
    print(f"--- {exporter.content_type} -> {exporter.file_name()} ---")
    print(exporter.export(metrics))
    print()


if __name__ == "__main__":
    metrics = [Metric("cpu", 0.93), Metric("memory", 0.67), Metric("disk", 0.41)]
    for exporter in (CsvExporter(), JsonExporter()):
        deliver(exporter, metrics)
