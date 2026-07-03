"""Facade pattern in Python.

One simple entry point (HomeTheater) orchestrates several subsystem
classes. Note: in Python a module exposing a few top-level functions is
often facade enough; use a class when the facade holds the subsystems
as state, as here.
"""


class Amplifier:
    def on(self) -> None:
        print("Amplifier: on")

    def set_volume(self, level: int) -> None:
        print(f"Amplifier: volume {level}")

    def off(self) -> None:
        print("Amplifier: off")


class Projector:
    def on(self) -> None:
        print("Projector: on")

    def wide_screen_mode(self) -> None:
        print("Projector: 16:9 widescreen mode")

    def off(self) -> None:
        print("Projector: off")


class StreamingPlayer:
    def on(self) -> None:
        print("StreamingPlayer: on")

    def play(self, movie: str) -> None:
        print(f'StreamingPlayer: playing "{movie}"')

    def stop(self) -> None:
        print("StreamingPlayer: stopped")

    def off(self) -> None:
        print("StreamingPlayer: off")


class HomeTheater:
    """One method per use case; subsystems stay reachable for power users."""

    def __init__(self, amp: Amplifier, projector: Projector, player: StreamingPlayer) -> None:
        self._amp = amp
        self._projector = projector
        self._player = player

    def watch_movie(self, movie: str) -> None:
        print("= Movie night =")
        self._amp.on()
        self._amp.set_volume(5)
        self._projector.on()
        self._projector.wide_screen_mode()
        self._player.on()
        self._player.play(movie)

    def end_movie(self) -> None:
        print("= Shutting down =")
        self._player.stop()
        self._player.off()
        self._projector.off()
        self._amp.off()


if __name__ == "__main__":
    theater = HomeTheater(Amplifier(), Projector(), StreamingPlayer())
    theater.watch_movie("Inception")
    theater.end_movie()
