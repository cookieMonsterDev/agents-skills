"""Composition over inheritance in Python.

A robot hierarchy would need one subclass per movement x weapon combo
(WalkingLaserRobot, FlyingDrillRobot, ...). Composing a Robot from
swappable parts needs 3 + 2 components for all 6 combos — and parts can
be replaced at runtime. Protocol gives static checking without a base
class; duck typing alone would also do.
"""

from __future__ import annotations

from typing import Protocol


class MoveBehavior(Protocol):
    def move(self) -> str: ...


class AttackBehavior(Protocol):
    def attack(self) -> str: ...


# --- Concrete components: one capability each, independently testable ---


class Treads:
    def move(self) -> str:
        return "rolls forward on treads"


class Rotors:
    def move(self) -> str:
        return "lifts off on quad rotors"


class Turbines:
    def move(self) -> str:
        return "dives and swims with turbines"


class Laser:
    def attack(self) -> str:
        return "fires a precision laser"


class Drill:
    def attack(self) -> str:
        return "spins up a mining drill"


class Robot:
    """Host object: owns its parts and delegates behavior to them."""

    def __init__(self, name: str, mover: MoveBehavior, weapon: AttackBehavior) -> None:
        self.name = name
        self.mover = mover
        self.weapon = weapon

    def perform(self) -> str:
        return f"{self.name:>8}: {self.mover.move()} and {self.weapon.attack()}"


if __name__ == "__main__":
    # Any combination is just wiring — no FlyingDrillRobot subclass needed.
    squad = [
        Robot("Scout", Treads(), Laser()),
        Robot("Miner", Treads(), Drill()),
        Robot("Wasp", Rotors(), Drill()),  # flying driller: new subclass in a hierarchy
        Robot("Manta", Turbines(), Laser()),
    ]
    for robot in squad:
        print(robot.perform())

    # Inheritance fixes behavior at construction; composition swaps it live.
    print("-- field upgrade: Miner receives rotors --")
    squad[1].mover = Rotors()
    print(squad[1].perform())
