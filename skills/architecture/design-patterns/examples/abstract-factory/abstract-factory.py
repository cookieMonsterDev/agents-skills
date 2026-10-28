"""Abstract Factory pattern in Python.

Note: classes are first-class objects, so a lighter idiom is a dict of
constructors or a module per family. ABCs are worth it when the family
is larger and you want the contract to be explicit.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: ...


class MacButton(Button):
    def render(self) -> str:
        return "( OK )  # rounded macOS button"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "◉ Remember me  # macOS checkbox"


class WindowsButton(Button):
    def render(self) -> str:
        return "[ OK ]  # rectangular Windows button"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "[x] Remember me  # Windows checkbox"


class WidgetFactory(ABC):
    """One creation method per product kind; products are guaranteed to match."""

    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...


class MacFactory(WidgetFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class WindowsFactory(WidgetFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


def render_dialog(factory: WidgetFactory) -> None:
    """Client code: depends only on the abstract factory and products."""
    print(factory.create_button().render())
    print(factory.create_checkbox().render())


if __name__ == "__main__":
    for name, factory in [("macOS", MacFactory()), ("Windows", WindowsFactory())]:
        print(f"-- {name} theme --")
        render_dialog(factory)
