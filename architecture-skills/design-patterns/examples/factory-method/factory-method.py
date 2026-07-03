"""Factory Method pattern in Python.

Note: classes are first-class, so passing the transport class directly
(`plan_delivery(Truck)`) often replaces this pattern. A creator hierarchy
pays off when the creator carries real shared logic, as here.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Transport(ABC):
    """Product interface."""

    @abstractmethod
    def deliver(self, cargo: str) -> str: ...


class Truck(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Truck delivers {cargo} by road in a box"


class Ship(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Ship delivers {cargo} by sea in a container"


class Logistics(ABC):
    """Creator: shared workflow around one overridable creation step."""

    @abstractmethod
    def create_transport(self) -> Transport: ...

    def plan_delivery(self, cargo: str) -> str:
        transport = self.create_transport()
        return f"[{type(self).__name__}] {transport.deliver(cargo)}"


class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


if __name__ == "__main__":
    for logistics in (RoadLogistics(), SeaLogistics()):
        print(logistics.plan_delivery("machine parts"))
