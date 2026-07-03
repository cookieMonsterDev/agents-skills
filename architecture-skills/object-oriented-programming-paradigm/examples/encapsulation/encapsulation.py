"""Encapsulation in Python.

Privacy is convention: a single underscore means "internal", a double
underscore adds name mangling as a stronger deterrent. @property exposes
the balance read-only, so the only writes go through deposit/withdraw,
which enforce the invariant: balance never goes negative.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BrokenAccount:
    """The broken version: a raw public field. Nothing stops a caller
    from violating the "never negative" rule."""

    balance: float = 0.0


class BankAccount:
    """Invariant: balance >= 0, always, between any two method calls."""

    def __init__(self, opening_balance: float = 0.0) -> None:
        if opening_balance < 0:
            raise ValueError("opening balance cannot be negative")
        self.__balance = opening_balance  # mangled to _BankAccount__balance

    @property
    def balance(self) -> float:
        """Read access only: there is no balance setter."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance -= amount


if __name__ == "__main__":
    broken = BrokenAccount(balance=100.0)
    broken.balance -= 250.0  # nobody checks; the invariant silently breaks
    print(f"broken account balance: ${broken.balance:.2f}  <- invalid state")

    account = BankAccount(100.0)
    account.deposit(50.0)
    print(f"after deposit:  ${account.balance:.2f}")

    try:
        account.withdraw(250.0)
    except ValueError as err:
        print(f"withdraw $250 rejected: {err}")

    account.withdraw(30.0)
    print(f"after withdraw: ${account.balance:.2f}  (invariant intact)")
