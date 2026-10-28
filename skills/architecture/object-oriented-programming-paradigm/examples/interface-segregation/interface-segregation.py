"""Interface Segregation Principle in Python.

A fat OfficeMachine protocol forces SimplePrinter to implement scan()
and fax() with NotSupported stubs. The fix splits Printer and Scanner
so each client depends only on the methods it actually calls.
"""

from __future__ import annotations

from typing import Protocol


class NotSupportedError(Exception):
    pass


# --- Violation: one fat interface every device must implement ---


class OfficeMachine(Protocol):
    def print_document(self, path: str) -> None: ...
    def scan_document(self, path: str) -> None: ...
    def fax_document(self, path: str) -> None: ...


class SimplePrinter:
    """Only prints — but the fat interface forces stub methods."""

    def print_document(self, path: str) -> None:
        print(f"print {path}")

    def scan_document(self, path: str) -> None:
        raise NotSupportedError("scan")

    def fax_document(self, path: str) -> None:
        raise NotSupportedError("fax")


def run_office_job(machine: OfficeMachine, path: str) -> None:
    machine.print_document(path)
    for action, fn in (
        ("scan", machine.scan_document),
        ("fax", machine.fax_document),
    ):
        try:
            fn(path)
        except NotSupportedError:
            print(f"{action} attempt: NotSupported")


# --- Fix: small client-specific interfaces ---


class Printer(Protocol):
    def print_document(self, path: str) -> None: ...


class Scanner(Protocol):
    def scan_document(self, path: str) -> None: ...


class BasicPrinter:
    def print_document(self, path: str) -> None:
        print(f"print {path}")


class FlatbedScanner:
    def scan_document(self, path: str) -> None:
        print(f"scan {path}")


class MultiFunctionDevice:
    """Implements both interfaces — no stubs required."""

    def print_document(self, path: str) -> None:
        print(f"print {path}")

    def scan_document(self, path: str) -> None:
        print(f"scan {path}")


def print_job(printer: Printer, path: str) -> None:
    printer.print_document(path)


def scan_job(scanner: Scanner, path: str) -> None:
    scanner.scan_document(path)


if __name__ == "__main__":
    print("-- Violation: SimplePrinter forced to stub scan/fax --")
    run_office_job(SimplePrinter(), "document.pdf")

    print("\n-- Fix: clients depend only on what they need --")
    print_job(BasicPrinter(), "document.pdf")
    scan_job(FlatbedScanner(), "page.tif")
    mfd: Printer = MultiFunctionDevice()
    print_job(mfd, "report.pdf")
