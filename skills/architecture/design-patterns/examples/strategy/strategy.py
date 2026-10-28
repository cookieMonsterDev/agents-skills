"""Strategy pattern in Python.

In Python a stateless strategy is idiomatically just a first-class
function; a class is only worth it when the strategy carries
configuration or several methods. Both forms are shown.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Order:
    weight_kg: float
    distance_km: float


# --- Form 1: plain functions (idiomatic for stateless strategies) ---

ShippingStrategy = Callable[[Order], float]


def flat_rate(order: Order) -> float:
    return 5.00


def weight_based(order: Order) -> float:
    return 4.00 + 1.50 * order.weight_kg


def distance_based(order: Order) -> float:
    return 2.00 + 0.05 * order.distance_km


# --- Form 2: class form, for strategies that carry state ---


class CarrierRate:
    """A negotiated carrier tariff; the rates are the strategy's state."""

    def __init__(self, base: float, per_kg: float) -> None:
        self._base = base
        self._per_kg = per_kg

    def __call__(self, order: Order) -> float:
        return self._base + self._per_kg * order.weight_kg


class Checkout:
    """Context: delegates the pricing decision to the current strategy."""

    def __init__(self, strategy: ShippingStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy) -> None:
        self._strategy = strategy

    def shipping_for(self, order: Order) -> float:
        return self._strategy(order)


if __name__ == "__main__":
    order = Order(weight_kg=2.4, distance_km=120)
    checkout = Checkout(flat_rate)

    strategies: list[tuple[str, ShippingStrategy]] = [
        ("flat", flat_rate),
        ("weight", weight_based),
        ("distance", distance_based),
        ("carrier", CarrierRate(base=3.00, per_kg=2.00)),
    ]
    for name, strategy in strategies:
        checkout.set_strategy(strategy)
        print(f"{name:>8}: ${checkout.shipping_for(order):.2f}")
