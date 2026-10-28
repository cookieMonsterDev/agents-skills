# Facade

**Category:** Structural

## Intent

Provide a single, simplified interface to a complex subsystem. The facade doesn't hide the subsystem — it offers a convenient entry point for the common use cases while the full API stays available for callers that need it.

## Problem

- Using a subsystem correctly requires calling many classes in the right order (`amp.on(); amp.setVolume(5); projector.on(); ...`), and that knowledge leaks into every caller.
- Client code becomes tightly coupled to subsystem internals, so refactoring the subsystem breaks callers everywhere.
- You want a clean boundary between layers (e.g. UI code should trigger "watch movie", not orchestrate hardware).

## Structure

- **Facade** — knows which subsystem classes handle a request and in what order; exposes one method per use case (`watchMovie`, `endMovie`).
- **Subsystem classes** — do the actual work; they have no knowledge of the facade and remain directly usable.
- **Client** — calls the facade for common flows, and may still reach into the subsystem for advanced needs.

## When to Use

- A common workflow spans several subsystem objects and every caller repeats the same orchestration.
- You want to layer a system: higher layers talk to lower layers only through a small surface.
- You are wrapping a legacy or third-party API and want to isolate the rest of the codebase from its shape.

## When Not to Use

- The subsystem is already simple; a facade over one or two calls is pure indirection.
- Callers all need fine-grained control anyway — a facade that forwards every method one-to-one adds nothing.
- You are tempted to grow the facade into a god object that knows about everything; split it into several focused facades instead.

## Trade-offs

- **Pros:** decouples clients from subsystem internals, makes common flows one-liners, gives refactoring a stable seam, simplifies testing (mock one facade instead of five classes).
- **Cons:** risk of becoming a god object; can hide capabilities callers legitimately need, pushing them to bypass it; one more layer to keep in sync with the subsystem.

## Language Notes

- **Python:** a module or package `__init__.py` exposing a few top-level functions is a natural facade; a class is only needed when the facade holds state.
- **JavaScript / PHP:** a module exporting a handful of functions over internal classes is the common form. Note that Laravel "facades" are actually static proxies, not GoF facades.
- **Java / C#:** the textbook form — a plain class composing subsystem objects; often the entry point of a library (`javax.faces.context.FacesContext`-style).
- **Rust:** a struct owning the subsystems, or simply a module that `pub use`s a curated slice of a larger crate.
- **Go:** an idiomatic Go package *is* a facade: unexported types do the work, and a small exported API fronts them.
- **C:** no polymorphism needed — the facade is a couple of functions that call the subsystem structs in the right order.
- **Swift:** a plain struct or class wrapping the subsystems; no protocol required since clients depend on the facade concretely.

## Examples

- [examples/facade/facade.py](../examples/facade/facade.py)
- [examples/facade/facade.c](../examples/facade/facade.c)
- [examples/facade/facade.cpp](../examples/facade/facade.cpp)
- [examples/facade/facade.java](../examples/facade/facade.java)
- [examples/facade/facade.cs](../examples/facade/facade.cs)
- [examples/facade/facade.js](../examples/facade/facade.js)
- [examples/facade/facade.rs](../examples/facade/facade.rs)
- [examples/facade/facade.go](../examples/facade/facade.go)
- [examples/facade/facade.php](../examples/facade/facade.php)
- [examples/facade/facade.swift](../examples/facade/facade.swift)

## Related Patterns

- **Adapter** changes an interface to match what a client expects; Facade defines a *new*, simpler interface over many objects.
- **Mediator** also centralizes communication, but subsystem objects know the mediator; facade's subsystems are unaware of it.
- **Abstract Factory** can be used behind a facade to hide how subsystem objects are created.
- A facade over a remote or expensive subsystem often pairs with a **Proxy**.
