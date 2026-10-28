"""Mediator pattern in Python.

A chat room routes messages between users so users never hold direct
references to each other. Duck typing keeps it light: anything with a
`receive()` method can join the room.
"""

from __future__ import annotations


class ChatRoom:
    """Mediator: knows every participant and owns the routing rules."""

    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def register(self, user: User) -> None:
        self._users[user.name] = user
        user.room = self

    def broadcast(self, sender: User, text: str) -> None:
        for user in self._users.values():
            if user is not sender:
                user.receive(sender.name, text)

    def direct(self, sender: User, recipient: str, text: str) -> None:
        user = self._users.get(recipient)
        if user is None:
            sender.receive("room", f"no such user: {recipient}")
        else:
            user.receive(sender.name, f"(dm) {text}")


class User:
    """Colleague: talks only to the mediator."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.room: ChatRoom | None = None

    def say(self, text: str) -> None:
        assert self.room is not None, "user must join a room first"
        self.room.broadcast(self, text)

    def dm(self, recipient: str, text: str) -> None:
        assert self.room is not None, "user must join a room first"
        self.room.direct(self, recipient, text)

    def receive(self, sender: str, text: str) -> None:
        print(f"[{self.name}] {sender}: {text}")


if __name__ == "__main__":
    room = ChatRoom()
    ada, grace, alan = User("Ada"), User("Grace"), User("Alan")
    for user in (ada, grace, alan):
        room.register(user)

    ada.say("Hello, everyone!")
    grace.dm("Ada", "Hi Ada, got a minute?")
    alan.dm("Linus", "ping")
