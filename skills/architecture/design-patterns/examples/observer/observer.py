"""Observer pattern in Python.

A stock ticker notifies subscribers of price changes. Plain callables
are the idiomatic observer in Python — any function, lambda, or bound
method can subscribe, no interface required.
"""

from __future__ import annotations

from typing import Callable

PriceObserver = Callable[[str, float], None]


class StockTicker:
    """Subject: keeps prices and notifies subscribers on change."""

    def __init__(self) -> None:
        self._prices: dict[str, float] = {}
        self._observers: list[PriceObserver] = []

    def subscribe(self, observer: PriceObserver) -> Callable[[], None]:
        self._observers.append(observer)

        def unsubscribe() -> None:
            self._observers.remove(observer)

        return unsubscribe

    def update_price(self, symbol: str, price: float) -> None:
        self._prices[symbol] = price
        for observer in list(self._observers):
            observer(symbol, price)


class PriceDisplay:
    """An observer implemented as a class with a bound method."""

    def __init__(self, name: str) -> None:
        self.name = name

    def on_price(self, symbol: str, price: float) -> None:
        print(f"{self.name}: {symbol} is now ${price:.2f}")


def make_alert(symbol: str, threshold: float) -> PriceObserver:
    """An observer implemented as a closure."""

    def on_price(updated_symbol: str, price: float) -> None:
        if updated_symbol == symbol and price > threshold:
            print(f"ALERT: {symbol} crossed ${threshold:.2f} (now ${price:.2f})")

    return on_price


if __name__ == "__main__":
    ticker = StockTicker()
    lobby_display = PriceDisplay("Lobby display")
    unsubscribe = ticker.subscribe(lobby_display.on_price)
    ticker.subscribe(make_alert("ACME", 100.0))

    ticker.update_price("ACME", 98.5)
    ticker.update_price("ACME", 101.25)

    unsubscribe()
    ticker.update_price("GLOBEX", 45.0)  # only the alert remains subscribed
