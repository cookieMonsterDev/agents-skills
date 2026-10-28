# Builder

**Category:** Creational

## Intent

Separate the construction of a complex object from its representation, so the same construction process can create different representations. In practice: build an object step by step instead of through a constructor with many parameters.

## Problem

- A class needs many constructor parameters, several of them optional, and call sites become unreadable (`new House(4, 2, true, false, null, true)`).
- Construction requires multiple steps or validation that should happen before the object exists.
- You want the finished object to be immutable, but assembling it takes several stages.

## Structure

- **Builder** — declares the steps (`setWalls`, `setRoof`, ...), each usually returning the builder for chaining.
- **Concrete builder** — implements the steps and tracks the partially built product.
- **Product** — the complex object being built; ideally immutable once `build()` returns it.
- **Director** (optional) — encapsulates a fixed sequence of steps to produce a known configuration. Most modern code omits the director and chains the builder directly.

## When to Use

- Constructors would need many optional parameters (the "telescoping constructor" problem).
- The object must be validated or assembled in stages before it is usable.
- The same steps should produce different representations (e.g. a `Report` built as HTML or PDF).
- You want an immutable product without exposing a mutable intermediate.

## When Not to Use

- The object has few fields; a plain constructor, named/keyword arguments, or a struct literal is simpler.
- The language already solves the problem: Python keyword arguments with defaults, JavaScript object parameters with destructuring, Swift memberwise initializers with default values, and C# object initializers often make a builder unnecessary.

## Trade-offs

- **Pros:** readable call sites, stepwise validation, immutable products, reusable construction logic.
- **Cons:** roughly doubles the code for the class; a half-built builder can be misused if `build()` doesn't validate required fields.

## Language Notes

- **Python / JavaScript / PHP:** keyword or object arguments cover most simple cases; use a builder only for multi-stage construction or validation.
- **Java / C#:** the most common home of the pattern (e.g. `StringBuilder`, Lombok `@Builder`, `HttpRequest.newBuilder()`).
- **Rust:** the idiomatic non-derive way to construct complex structs (`std::process::Command` is a builder); crates like `typed-builder` enforce required fields at compile time.
- **Go:** functional options (`func WithTimeout(d time.Duration) Option`) are often preferred over a builder struct; both are shown in the example.
- **C:** emulated with a plain struct holding the pending configuration and a `build` function that validates and produces the product.
- **Swift:** result builders (`@resultBuilder`, as in SwiftUI) are the language-native evolution of this idea for declarative trees.

## Examples

- [examples/builder/builder.py](../examples/builder/builder.py)
- [examples/builder/builder.c](../examples/builder/builder.c)
- [examples/builder/builder.cpp](../examples/builder/builder.cpp)
- [examples/builder/builder.java](../examples/builder/builder.java)
- [examples/builder/builder.cs](../examples/builder/builder.cs)
- [examples/builder/builder.js](../examples/builder/builder.js)
- [examples/builder/builder.rs](../examples/builder/builder.rs)
- [examples/builder/builder.go](../examples/builder/builder.go)
- [examples/builder/builder.php](../examples/builder/builder.php)
- [examples/builder/builder.swift](../examples/builder/builder.swift)

## Related Patterns

- **Abstract Factory** creates families of objects in one shot; Builder assembles one object step by step.
- **Composite** products are often constructed by a Builder.
- A Builder's `build()` can return a **Prototype**-cloned template.
