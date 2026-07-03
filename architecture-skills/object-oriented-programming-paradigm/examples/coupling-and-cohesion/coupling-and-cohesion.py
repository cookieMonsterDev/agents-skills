"""Coupling and Cohesion in Python.

A god OrderProcessor that computes tax, validates, and ships in one
class is tightly coupled: a tax-rule change risks breaking validation
or shipping. Split into cohesive collaborators — only OrderCalculator
changes when finance updates tax.
"""

from __future__ import annotations

from dataclasses import dataclass


# --- Before (tightly coupled, sketched): one class, three reasons to change ---
#
# class OrderProcessor:
#     def process(self, order):
#         total = order.subtotal * (1 + 0.20)   # tax logic
#         if total <= 0: raise ...              # validation
#         print(f"shipped {order.id}")          # shipping
#         return total


# --- After: loose coupling via focused collaborators ---


@dataclass
class Order:
    order_id: str
    subtotal: float


class OrderCalculator:
    """Finance's class: only tax-rule changes touch this file."""

    def __init__(self, tax_rate: float) -> None:
        self._tax_rate = tax_rate

    def total(self, order: Order) -> float:
        return order.subtotal * (1 + self._tax_rate)


class OrderValidator:
    """Compliance's class: only validation rules change touch this file."""

    def validate(self, order: Order, total: float) -> None:
        if order.subtotal <= 0:
            raise ValueError("subtotal must be positive")
        if total <= 0:
            raise ValueError("total must be positive")


class OrderShipper:
    """Fulfillment's class: only carrier/API changes touch this file."""

    def ship(self, order: Order) -> str:
        return f"shipped {order.order_id}"


class OrderService:
    """Thin orchestrator: wires cohesive pieces, owns no domain rules."""

    def __init__(
        self,
        calculator: OrderCalculator,
        validator: OrderValidator,
        shipper: OrderShipper,
    ) -> None:
        self._calculator = calculator
        self._validator = validator
        self._shipper = shipper

    def process(self, order: Order) -> float:
        total = self._calculator.total(order)
        self._validator.validate(order, total)
        print(self._shipper.ship(order))
        return total


if __name__ == "__main__":
    order = Order("ORD-204", subtotal=80.00)

    service = OrderService(
        calculator=OrderCalculator(tax_rate=0.20),
        validator=OrderValidator(),
        shipper=OrderShipper(),
    )
    total = service.process(order)
    print(f"total with 20% tax: ${total:.2f}")

    # Tax rule changes: swap calculator only — validator and shipper untouched.
    new_rate_service = OrderService(
        calculator=OrderCalculator(tax_rate=0.08),
        validator=OrderValidator(),
        shipper=OrderShipper(),
    )
    new_total = new_rate_service.process(order)
    print(f"total with 8% tax:  ${new_total:.2f}  (only OrderCalculator changed)")
