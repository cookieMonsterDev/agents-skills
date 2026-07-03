"""Classes & objects in Python.

A class bundles state (owner, balance) with the behavior that guards
it; each instance gets independent state via __init__. Class attributes
are shared across instances (the account counter), and per-instance
state must be assigned in __init__ — a class-level mutable would be
shared by every account. transfer() stays a module-level free function
because it belongs to no single account.
"""

from __future__ import annotations


class BankAccount:
    """Blueprint: every account has an owner, a balance, and a number."""

    _accounts_opened = 0  # class attribute: shared by all instances

    def __init__(self, owner: str, opening_balance: float = 0.0) -> None:
        if opening_balance < 0:
            raise ValueError("opening balance cannot be negative")
        BankAccount._accounts_opened += 1
        self.number = f"ACC-{BankAccount._accounts_opened:04d}"
        self.owner = owner            # instance attributes: one copy
        self.balance = opening_balance  # per object, never shared

    # Instance methods: functions with an implicit reference (self).
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError(f"{self.number}: insufficient funds")
        self.balance -= amount

    def __repr__(self) -> str:
        return f"{self.number} ({self.owner}): ${self.balance:.2f}"

    # Class method: bound to the class, callable with zero instances.
    @classmethod
    def total_opened(cls) -> int:
        return cls._accounts_opened


def transfer(source: BankAccount, target: BankAccount, amount: float) -> None:
    """Free function: coordinates two objects, owns neither."""
    source.withdraw(amount)
    target.deposit(amount)


if __name__ == "__main__":
    # Two objects from one blueprint, each with independent state.
    alice = BankAccount("Alice", opening_balance=100.0)
    bob = BankAccount("Bob")

    alice.deposit(50.0)
    bob.deposit(20.0)
    alice.withdraw(30.0)

    print(alice)  # Alice's mutations never touched Bob's balance
    print(bob)

    transfer(alice, bob, 40.0)
    print(f"after transfer -> {alice} | {bob}")

    print(f"accounts opened: {BankAccount.total_opened()}")
