"""State pattern in Python.

A vending machine changes behavior as its state changes: the same
insert_coin/select_item calls do different things in Idle, HasCoin, and
SoldOut. Each state is a small class; duck typing means no ABC is
strictly required (one is used here for documentation value).
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def insert_coin(self, machine: VendingMachine) -> None: ...

    @abstractmethod
    def select_item(self, machine: VendingMachine) -> None: ...


class Idle(State):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("coin accepted")
        machine.state = HasCoin()

    def select_item(self, machine: VendingMachine) -> None:
        print("insert a coin first")


class HasCoin(State):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("coin already inserted, returning it")

    def select_item(self, machine: VendingMachine) -> None:
        machine.stock -= 1
        print(f"item dispensed ({machine.stock} left)")
        machine.state = SoldOut() if machine.stock == 0 else Idle()


class SoldOut(State):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("sold out, returning coin")

    def select_item(self, machine: VendingMachine) -> None:
        print("sold out")


class VendingMachine:
    """Context: delegates every request to its current state."""

    def __init__(self, stock: int) -> None:
        self.stock = stock
        self.state: State = Idle() if stock > 0 else SoldOut()

    def insert_coin(self) -> None:
        self.state.insert_coin(self)

    def select_item(self) -> None:
        self.state.select_item(self)


if __name__ == "__main__":
    machine = VendingMachine(stock=2)
    machine.select_item()   # insert a coin first
    machine.insert_coin()
    machine.insert_coin()   # coin already inserted
    machine.select_item()   # item dispensed (1 left)
    machine.insert_coin()
    machine.select_item()   # item dispensed (0 left)
    machine.insert_coin()   # sold out, returning coin
