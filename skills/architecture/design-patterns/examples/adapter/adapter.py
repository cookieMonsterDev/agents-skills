"""Adapter pattern in Python.

Converts the interface of a legacy class into the one clients expect.
With duck typing a formal adapter is only needed when the legacy class
is missing the expected method names and cannot be changed; often a
thin wrapper class or even a function is enough.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class TemperatureSource(ABC):
    """Target interface the monitoring code expects."""

    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def celsius(self) -> float: ...


class ModernSensor(TemperatureSource):
    def __init__(self, name: str, celsius: float) -> None:
        self._name = name
        self._celsius = celsius

    def name(self) -> str:
        return self._name

    def celsius(self) -> float:
        return self._celsius


class LegacyFahrenheitSensor:
    """Adaptee: third-party class we cannot modify."""

    def __init__(self, sensor_id: str, fahrenheit: float) -> None:
        self.sensor_id = sensor_id
        self._fahrenheit = fahrenheit

    def read_fahrenheit(self) -> float:
        return self._fahrenheit


class FahrenheitAdapter(TemperatureSource):
    """Wraps the legacy sensor and converts units on the fly."""

    def __init__(self, legacy: LegacyFahrenheitSensor) -> None:
        self._legacy = legacy

    def name(self) -> str:
        return self._legacy.sensor_id

    def celsius(self) -> float:
        return (self._legacy.read_fahrenheit() - 32.0) * 5.0 / 9.0


def report(sources: list[TemperatureSource]) -> None:
    for source in sources:
        print(f"{source.name()}: {source.celsius():.1f}°C")


if __name__ == "__main__":
    report([
        ModernSensor("server-room", 21.5),
        FahrenheitAdapter(LegacyFahrenheitSensor("warehouse-legacy", 77.0)),
    ])
