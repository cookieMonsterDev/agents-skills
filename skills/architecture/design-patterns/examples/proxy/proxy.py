"""Proxy pattern in Python (virtual proxy: lazy-loading image).

Duck typing means no formal interface is needed: the proxy just quacks
like the real image. __getattr__ forwards anything the proxy doesn't
override to the real subject, so only intercepted methods are written
by hand.
"""

from __future__ import annotations


class RealImage:
    """Real subject: expensive to create."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        print(f"Loading {filename} from disk (expensive)")

    def display(self) -> None:
        print(f"Displaying {self.filename}")

    def width(self) -> int:
        return 1920


class ImageProxy:
    """Virtual proxy: defers creating RealImage until first use."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._real: RealImage | None = None

    def display(self) -> None:
        if self._real is None:
            self._real = RealImage(self.filename)
        self._real.display()

    def __getattr__(self, name: str):
        # Forward anything else to the real subject, loading it on demand.
        if self._real is None:
            self._real = RealImage(self.filename)
        return getattr(self._real, name)


if __name__ == "__main__":
    gallery = [ImageProxy("holiday.png"), ImageProxy("unused.png")]
    print("Proxies created; nothing loaded yet")

    gallery[0].display()
    gallery[0].display()  # loaded once, displayed twice
    print(f"width via __getattr__: {gallery[0].width()}")

    print("unused.png was never loaded")
