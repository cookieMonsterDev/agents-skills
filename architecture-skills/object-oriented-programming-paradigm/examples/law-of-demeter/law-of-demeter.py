"""Law of Demeter in Python.

Checkout that calls order.get_customer().get_wallet().deduct(due) is a
train wreck — it knows that orders have customers who keep wallets.
Tell, don't ask: customer.pay(due) routes payment through the owner
who enforces the wallet-never-goes-negative rule.
"""

from __future__ import annotations


# --- Before (train wreck, sketched): checkout fishes through the graph ---
#
# class Checkout:
#     def collect(self, order: Order, due: float) -> None:
#         order.get_customer().get_wallet().deduct(due)  # three hops


# --- After: talk only to immediate collaborators ---


class Wallet:
    """Internal to Customer — outsiders should not reach in."""

    def __init__(self, balance: float) -> None:
        if balance < 0:
            raise ValueError("opening balance cannot be negative")
        self._balance = balance

    def deduct(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("payment must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    def balance(self) -> float:
        return self._balance


class Customer:
    """Owns the wallet and the rule about paying."""

    def __init__(self, name: str, opening_balance: float) -> None:
        self.name = name
        self._wallet = Wallet(opening_balance)

    def pay(self, amount: float) -> None:
        """Tell, don't ask: checkout asks the customer to pay, not the wallet."""
        self._wallet.deduct(amount)

    def balance(self) -> float:
        return self._wallet.balance()


class Order:
    def __init__(self, order_id: str, customer: Customer, total: float) -> None:
        self.order_id = order_id
        self.customer = customer
        self.total = total


class Checkout:
    """Paperboy: collects payment with one hop — order.customer.pay(due)."""

    def collect(self, order: Order, due: float) -> None:
        order.customer.pay(due)


if __name__ == "__main__":
    customer = Customer("Ada", opening_balance=50.00)
    order = Order("ORD-101", customer, total=12.50)
    checkout = Checkout()

    print(f"{customer.name} wallet before: ${customer.balance():.2f}")
    checkout.collect(order, order.total)
    print(f"collected ${order.total:.2f} for {order.order_id}")
    print(f"{customer.name} wallet after:  ${customer.balance():.2f}  (invariant intact)")
