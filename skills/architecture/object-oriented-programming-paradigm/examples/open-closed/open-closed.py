"""Open/Closed Principle in Python.

The pricing engine is closed: it computes a total over whatever
discount rules it was given and never names a concrete rule. New
behavior (FlashSale) arrives as a new class registered from outside
-- zero edits to PricingEngine. Duck typing makes the extension
point implicit; Protocol just documents it for tooling.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Order:
    subtotal: float
    item_count: int
    is_member: bool


class DiscountRule(Protocol):
    """Extension point: anything with name/discount fits."""

    name: str

    def discount(self, order: Order) -> float: ...


# --- Extensions: one class per rule, engine never sees these names ---


class BulkDiscount:
    name = "bulk"

    def discount(self, order: Order) -> float:
        return 0.05 * order.subtotal if order.item_count >= 10 else 0.0


class MemberDiscount:
    name = "member"

    def discount(self, order: Order) -> float:
        return 0.10 * order.subtotal if order.is_member else 0.0


class PricingEngine:
    """Closed core: iterates rules, never switches on a rule type."""

    def __init__(self) -> None:
        self._rules: list[DiscountRule] = []

    def register(self, rule: DiscountRule) -> None:
        self._rules.append(rule)

    def total(self, order: Order) -> float:
        for rule in self._rules:
            amount = rule.discount(order)
            if amount:
                print(f"  {rule.name:>6}: -${amount:.2f}")
        return order.subtotal - sum(r.discount(order) for r in self._rules)


# A NEW rule, written later -- the engine above is untouched.
class FlashSale:
    name = "flash"

    def __init__(self, amount: float, threshold: float) -> None:
        self._amount = amount
        self._threshold = threshold

    def discount(self, order: Order) -> float:
        return self._amount if order.subtotal > self._threshold else 0.0


if __name__ == "__main__":
    order = Order(subtotal=120.00, item_count=12, is_member=True)
    engine = PricingEngine()
    engine.register(BulkDiscount())
    engine.register(MemberDiscount())

    print(f"subtotal: ${order.subtotal:.2f}")
    print(f"total:    ${engine.total(order):.2f}")

    print("-- registering FlashSale: no engine edits --")
    engine.register(FlashSale(amount=15.00, threshold=100.00))
    print(f"total:    ${engine.total(order):.2f}")
