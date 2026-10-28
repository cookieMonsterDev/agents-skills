# Abstract Factory

**Category:** Creational

## Intent

Provide an interface for creating families of related objects without specifying their concrete classes. The client asks one factory for a matched set (a button *and* a checkbox that share a theme) instead of newing up each piece and hoping they fit together.

## Problem

- Code creates related objects (widgets, drivers, parsers) that must stay consistent with each other — a Mac button next to a Windows checkbox is a bug.
- `if (platform == "mac") new MacButton() else new WinButton()` conditionals spread through the codebase and must all change when a new family is added.
- You want to swap the whole family (theme, database vendor, cloud provider) with one configuration decision at startup.

## Structure

- **Abstract products** — one interface per kind of object in the family (`Button`, `Checkbox`).
- **Concrete products** — the family-specific implementations (`MacButton`, `WindowsButton`, ...).
- **Abstract factory** — declares one creation method per product kind (`createButton()`, `createCheckbox()`).
- **Concrete factories** — one per family; each returns products that are guaranteed to match.
- **Client** — works only through the abstract factory and product interfaces; picks a concrete factory once.

## When to Use

- Objects come in families whose members must be used together (cross-platform UI kits, SQL dialect + connection + cursor, sandbox vs. production API clients).
- You want to enforce the "no mixing" constraint in the type system rather than by convention.
- The concrete family is chosen once (config, environment, feature flag) and the rest of the code should not care.

## When Not to Use

- There is only one product kind — that's a plain Factory Method, not an abstract factory.
- Only one family exists and no second one is planned; the extra interfaces are speculative generality.
- Families gain new product kinds often: every new kind forces a change to the factory interface and every concrete factory.

## Trade-offs

- **Pros:** guarantees product compatibility, isolates concrete classes to one place, makes whole-family swaps trivial, easy to fake in tests.
- **Cons:** lots of interfaces and classes for small families; adding a new *product kind* (as opposed to a new family) ripples through every factory.

## Language Notes

- **Python / JavaScript / PHP:** classes and functions are first-class values, so a "factory" can be as light as a module, a dict of constructors, or an object literal; a full class hierarchy is only worth it for larger families.
- **Java / C#:** the classic home of the pattern; interfaces plus dependency injection containers make choosing the concrete factory a pure configuration concern.
- **Rust:** a trait with methods returning `Box<dyn Product>` works; when the set of families is closed, an enum with match arms is often more idiomatic than trait objects.
- **Go:** small interfaces per product plus a factory interface; concrete factories are usually zero-size structs.
- **C:** emulated with a struct of function pointers acting as the factory vtable; products carry their own function pointers too.
- **Swift:** protocols model both products and the factory naturally; a generic function over the factory protocol avoids existential overhead.

## Examples

- [examples/abstract-factory/abstract-factory.py](../examples/abstract-factory/abstract-factory.py)
- [examples/abstract-factory/abstract-factory.c](../examples/abstract-factory/abstract-factory.c)
- [examples/abstract-factory/abstract-factory.cpp](../examples/abstract-factory/abstract-factory.cpp)
- [examples/abstract-factory/abstract-factory.java](../examples/abstract-factory/abstract-factory.java)
- [examples/abstract-factory/abstract-factory.cs](../examples/abstract-factory/abstract-factory.cs)
- [examples/abstract-factory/abstract-factory.js](../examples/abstract-factory/abstract-factory.js)
- [examples/abstract-factory/abstract-factory.rs](../examples/abstract-factory/abstract-factory.rs)
- [examples/abstract-factory/abstract-factory.go](../examples/abstract-factory/abstract-factory.go)
- [examples/abstract-factory/abstract-factory.php](../examples/abstract-factory/abstract-factory.php)
- [examples/abstract-factory/abstract-factory.swift](../examples/abstract-factory/abstract-factory.swift)

## Related Patterns

- **Factory Method** creates one product; Abstract Factory groups several factory methods to create a matched family.
- **Builder** assembles one complex object step by step; Abstract Factory returns whole families in single calls.
- Concrete factories can be implemented with **Prototype** (clone a registered exemplar per product) and are often **Singletons** in practice.
