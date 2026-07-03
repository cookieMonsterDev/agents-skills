"""Dependency Inversion Principle in Python.

OrderService owns the Notifier protocol and receives an implementation
through its constructor — never `new SmtpNotifier(...)`. main() is the
composition root that wires ConsoleNotifier or RecordingNotifier.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Order:
    id: str
    customer_email: str


class Notifier(Protocol):
    """Abstraction owned by policy: shaped to what place() needs."""

    def notify(self, email: str, message: str) -> None: ...


class OrderService:
    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier

    def place(self, order: Order) -> None:
        print(f"placed {order.id} for {order.customer_email}")
        self._notifier.notify(
            order.customer_email,
            f"order {order.id} confirmed",
        )


# --- Low-level details: depend on the policy's protocol, not vice versa ---


class ConsoleNotifier:
    def notify(self, email: str, message: str) -> None:
        print(f"notify {email}: {message}")


class RecordingNotifier:
    """Test double: captures notifications without I/O."""

    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    def notify(self, email: str, message: str) -> None:
        self.sent.append((email, message))


if __name__ == "__main__":
    order = Order(id="ORD-001", customer_email="alice@example.com")

    print("-- ConsoleNotifier at composition root --")
    OrderService(ConsoleNotifier()).place(order)

    print("\n-- RecordingNotifier: policy testable without I/O --")
    recorder = RecordingNotifier()
    OrderService(recorder).place(Order(id="ORD-002", customer_email="bob@example.com"))
    print(f"{len(recorder.sent)} notification(s) recorded")
