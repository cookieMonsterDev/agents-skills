"""Single Responsibility Principle in Python.

An Invoice that computes totals, formats itself, AND persists itself
serves three actors (finance, presentation, ops) and has three reasons
to change. The refactor gives each actor its own collaborator; the
Invoice keeps only the data it truly owns.
"""

from __future__ import annotations

from dataclasses import dataclass


# --- Before (god class, sketched): three reasons to change ---
#
# class Invoice:
#     def add_item(self, desc, amount): ...   # domain data
#     def total(self): ...                    # changes when FINANCE changes tax
#     def to_text(self): ...                  # changes when LAYOUT changes
#     def save(self): ...                     # changes when STORAGE changes


# --- After: one collaborator per actor ---


@dataclass(frozen=True)
class LineItem:
    description: str
    amount: float


class Invoice:
    """Domain object: owns the data, knows nothing of tax, text, or storage."""

    def __init__(self, invoice_id: str, customer: str) -> None:
        self.invoice_id = invoice_id
        self.customer = customer
        self.items: list[LineItem] = []

    def add_item(self, description: str, amount: float) -> None:
        self.items.append(LineItem(description, amount))


class InvoiceCalculator:
    """Finance's class: only tax-rule changes touch this file."""

    def __init__(self, tax_rate: float) -> None:
        self._tax_rate = tax_rate

    def total(self, invoice: Invoice) -> float:
        subtotal = sum(item.amount for item in invoice.items)
        return subtotal * (1 + self._tax_rate)


class TextInvoiceFormatter:
    """Presentation's class: only layout changes touch this file."""

    def format(self, invoice: Invoice, total: float) -> str:
        lines = [f"Invoice {invoice.invoice_id} for {invoice.customer}"]
        lines += [f"  {i.description:<12} ${i.amount:>7.2f}" for i in invoice.items]
        lines.append(f"  {'TOTAL':<12} ${total:>7.2f}")
        return "\n".join(lines)


class InMemoryInvoiceRepository:
    """Ops' class: only storage changes (schema, driver) touch this file."""

    def __init__(self) -> None:
        self._rows: dict[str, Invoice] = {}

    def save(self, invoice: Invoice) -> None:
        self._rows[invoice.invoice_id] = invoice

    def count(self) -> int:
        return len(self._rows)


if __name__ == "__main__":
    invoice = Invoice("INV-042", "ACME Corp")
    invoice.add_item("Consulting", 1200.00)
    invoice.add_item("Hosting", 90.00)

    calculator = InvoiceCalculator(tax_rate=0.20)
    formatter = TextInvoiceFormatter()
    repository = InMemoryInvoiceRepository()

    total = calculator.total(invoice)
    print(formatter.format(invoice, total))

    repository.save(invoice)
    print(f"saved {invoice.invoice_id} ({repository.count()} record(s) stored)")
