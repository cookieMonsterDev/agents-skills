# Bridge

**Category:** Structural

## Intent

Decouple an abstraction from its implementation so the two can vary independently — split one class hierarchy that grows in two dimensions into two hierarchies connected by composition.

## Problem

- A hierarchy varies along two axes at once (shapes × renderers, remotes × devices, windows × platforms), and subclassing every combination explodes: 2×2 already needs `VectorCircle`, `RasterCircle`, `VectorRectangle`, `RasterRectangle`.
- Adding one new shape or one new renderer means creating or touching classes across the entire other axis.
- The implementation should be selectable — or swappable — at runtime.

## Structure

- **Abstraction** — the high-level class clients use (`Shape`); holds a reference to an implementation and delegates the primitive operations to it.
- **Refined abstractions** — variants of it (`Circle`, `Rectangle`).
- **Implementation** — the interface for the low-level work (`Renderer`).
- **Concrete implementations** — `VectorRenderer`, `RasterRenderer`.
- Each hierarchy is then extended independently of the other.

## When to Use

- A class hierarchy is (or is about to become) a cartesian product of two independent concerns.
- The implementation must be chosen at runtime or replaced without touching the domain classes.
- You want platform-specific or backend-specific code behind a small interface, with the domain logic on the other side of the divide.

## When Not to Use

- Only one axis actually varies — plain polymorphism or a strategy field is enough.
- The "two hierarchies" are not really independent: if every new shape needs a new renderer method, the split creates coupled churn instead of preventing it.
- As up-front structure for a class that will never have a second implementation.

## Trade-offs

- **Pros:** hierarchies grow additively (N + M classes instead of N × M); implementations swap at runtime; platform details stay out of the domain classes.
- **Cons:** an extra indirection and one more interface to maintain; the implementation interface must be designed carefully up front, because a wrong split is expensive to undo.

## Language Notes

- **Python / JavaScript / PHP:** the implementor interface can stay implicit (duck typing) — the pattern reduces to "the shape holds a renderer object"; an ABC or PHP `interface` just documents the contract.
- **Java / C#:** the textbook home; JDBC's API/driver split and ADO.NET's `DbConnection`/provider split are large-scale bridges.
- **Rust:** hold a `&dyn Renderer` or `Box<dyn Renderer>` for runtime pairing, or make the shape generic (`Circle<R: Renderer>`) for a zero-cost static bridge.
- **Go:** an interface-typed field in a struct is the whole pattern; no hierarchy machinery needed.
- **C:** the renderer is a struct of function pointers; each shape holds a pointer to it.
- **Swift:** a protocol-typed property on a value-type shape; protocol-oriented design makes this split routine.

## Examples

- [examples/bridge/bridge.py](../examples/bridge/bridge.py)
- [examples/bridge/bridge.c](../examples/bridge/bridge.c)
- [examples/bridge/bridge.cpp](../examples/bridge/bridge.cpp)
- [examples/bridge/bridge.java](../examples/bridge/bridge.java)
- [examples/bridge/bridge.cs](../examples/bridge/bridge.cs)
- [examples/bridge/bridge.js](../examples/bridge/bridge.js)
- [examples/bridge/bridge.rs](../examples/bridge/bridge.rs)
- [examples/bridge/bridge.go](../examples/bridge/bridge.go)
- [examples/bridge/bridge.php](../examples/bridge/bridge.php)
- [examples/bridge/bridge.swift](../examples/bridge/bridge.swift)

## Related Patterns

- **Adapter** makes existing incompatible pieces work together after the fact; Bridge is designed in up front so the parts can vary independently.
- **Strategy** also swaps behavior via composition, but replaces a single algorithm; Bridge connects two whole hierarchies.
- **Abstract Factory** can create and pair a matching abstraction and implementation.
- **State** shares the delegation mechanics but models an object changing mode over time.
