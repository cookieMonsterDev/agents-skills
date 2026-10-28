"""Composite pattern in Python.

Files and directories share one interface, so callers can total sizes
or print trees without caring whether a node is a leaf or a container.
Duck typing would work without the ABC; it is kept as documentation.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def size(self) -> int:
        """Total size in bytes."""

    @abstractmethod
    def print_tree(self, indent: int = 0) -> None: ...


class File(Node):
    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self._size = size

    def size(self) -> int:
        return self._size

    def print_tree(self, indent: int = 0) -> None:
        print(f"{' ' * indent}{self.name} ({self._size} B)")


class Directory(Node):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: list[Node] = []

    def add(self, child: Node) -> Directory:
        self._children.append(child)
        return self

    def size(self) -> int:
        return sum(child.size() for child in self._children)

    def print_tree(self, indent: int = 0) -> None:
        print(f"{' ' * indent}{self.name}/ ({self.size()} B)")
        for child in self._children:
            child.print_tree(indent + 2)


if __name__ == "__main__":
    project = (
        Directory("project")
        .add(Directory("src").add(File("main.py", 1200)).add(File("util.py", 450)))
        .add(Directory("docs").add(File("readme.md", 800)))
        .add(File(".gitignore", 20))
    )
    project.print_tree()
