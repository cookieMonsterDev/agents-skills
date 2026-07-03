"""Singleton pattern in Python.

Note: the idiomatic Python singleton is a module-level instance — modules
are imported once and cached, so `config = AppConfig()` in a module already
guarantees uniqueness. The __new__-based class below shows the explicit
pattern. Prefer passing the instance in (dependency injection); singletons
leak state between tests.
"""

from __future__ import annotations

import threading


class AppConfig:
    """Application configuration loaded once per process."""

    _instance: AppConfig | None = None
    _lock = threading.Lock()

    def __new__(cls) -> AppConfig:
        if cls._instance is None:
            with cls._lock:  # double-checked so later calls skip the lock
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance._load()
                    cls._instance = instance
        return cls._instance

    def _load(self) -> None:
        # Stands in for reading a config file or environment once.
        print("Loading configuration (expensive, happens once)")
        self._settings = {
            "app_name": "InventoryService",
            "db_url": "postgres://localhost/inventory",
            "log_level": "INFO",
        }

    def get(self, key: str) -> str:
        return self._settings[key]


if __name__ == "__main__":
    config_a = AppConfig()
    config_b = AppConfig()

    print("same instance:", config_a is config_b)
    print("app_name:", config_a.get("app_name"))
    print("db_url:", config_b.get("db_url"))
