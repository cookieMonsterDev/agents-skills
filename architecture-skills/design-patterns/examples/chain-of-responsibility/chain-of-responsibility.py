"""Chain of Responsibility pattern in Python.

Support ticket escalation: each support level resolves tickets up to its
competence and passes the rest along the chain.

Note: for simple cases a list of callables tried in order is often more
Pythonic; the linked-handler form shown here pays off when chains are
assembled or reordered at runtime.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Ticket:
    subject: str
    severity: int  # 1 (trivial) .. 4 (critical)


class Handler:
    """Base handler: holds the next link and forwards unhandled tickets."""

    def __init__(self) -> None:
        self._next: Handler | None = None

    def set_next(self, handler: Handler) -> Handler:
        self._next = handler
        return handler  # enables a.set_next(b).set_next(c)

    def handle(self, ticket: Ticket) -> None:
        if self._next is not None:
            self._next.handle(ticket)
        else:
            print(f"UNRESOLVED: {ticket.subject!r} (severity {ticket.severity})"
                  " -> escalate to engineering")


class SupportLevel(Handler):
    def __init__(self, name: str, max_severity: int) -> None:
        super().__init__()
        self._name = name
        self._max_severity = max_severity

    def handle(self, ticket: Ticket) -> None:
        if ticket.severity <= self._max_severity:
            print(f"{self._name} resolved {ticket.subject!r} (severity {ticket.severity})")
        else:
            super().handle(ticket)


if __name__ == "__main__":
    chain = SupportLevel("Help bot", 1)
    chain.set_next(SupportLevel("Frontline agent", 2)).set_next(
        SupportLevel("Support manager", 3)
    )

    tickets = [
        Ticket("Reset my password", 1),
        Ticket("Invoice shows wrong amount", 2),
        Ticket("Account data corrupted", 3),
        Ticket("Full region outage", 4),
    ]
    for ticket in tickets:
        chain.handle(ticket)
