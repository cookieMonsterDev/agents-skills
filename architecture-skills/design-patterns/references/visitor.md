# Visitor

**Category:** Behavioral

## Intent

Represent an operation to be performed on the elements of an object structure as its own object, so you can add new operations without changing the element classes. Double dispatch — `shape.accept(visitor)` calling back `visitor.visit(concreteShape)` — routes each element to the right handler.

## Problem

- A stable class hierarchy (shapes, AST nodes, file-system entries) keeps growing *operations* (area, export, type-check, pretty-print), and adding each one to every class bloats the hierarchy with unrelated concerns.
- Operations don't belong in the element classes at all (an SVG exporter inside `Circle` drags rendering concerns into a geometry type).
- Single dispatch can't select behavior on *both* the element's concrete type and the operation; you end up with type checks and casts.

## Structure

- **Visitor** — declares one `visit` method per concrete element type (`visitCircle`, `visitRectangle`, ...).
- **Concrete visitors** — one per operation (`AreaVisitor`, `SvgExportVisitor`); each must handle every element type, so the compiler flags incomplete operations.
- **Element** — declares `accept(visitor)`.
- **Concrete elements** — implement `accept` as `visitor.visit(this)`; the overload resolved by `this`'s concrete type is the second dispatch.

## When to Use

- The element hierarchy is stable but operations are added often — the pattern inverts the usual axis of extension.
- Many unrelated operations would otherwise pollute the element classes.
- An operation needs to accumulate state while walking a heterogeneous structure (a compiler pass over an AST is the canonical case).
- You want the compiler to enforce that every operation handles every element type.

## When Not to Use

- Element types change often: every new element breaks every visitor. If the hierarchy is the growing axis, put operations on the elements instead.
- Languages with sum types and exhaustive matching (Rust `enum` + `match`, Swift `enum` + `switch`, C# / Java pattern matching over sealed hierarchies) get the same guarantees with far less plumbing for closed sets — see Language Notes.
- Only one or two operations exist and the hierarchy is small; methods on the elements are simpler.
- The visitor needs access to element internals that would have to be exposed publicly just for it.

## Trade-offs

- **Pros:** new operations without touching element classes; related behavior gathered in one class instead of smeared across the hierarchy; visitors can carry per-traversal state; missing element handlers are compile errors.
- **Cons:** adding an element type touches every visitor; the `accept`/`visit` indirection is boilerplate and hard to follow for newcomers; elements may need to expose state to visitors; double dispatch defeats some inlining/optimization.

## Language Notes

- **Java / C#:** the classic home (e.g. `javax.lang.model` element visitors, Roslyn's `CSharpSyntaxVisitor`). A generic result type (`ShapeVisitor<R>` / `IShapeVisitor<TResult>`) avoids mutable visitor state. Sealed hierarchies + pattern-matching `switch` are the modern lighter alternative for closed sets.
- **Rust:** usually replaced by an `enum` + `match`, which is exhaustive and needs no `accept` plumbing; the trait-based double-dispatch form (shown in the example) matters when the type set must stay open to downstream crates. `syn` and compiler passes still use visitor traits for large ASTs.
- **Swift:** same story — a closed set is an `enum` with exhaustive `switch`; the protocol form with an `associatedtype` result keeps the hierarchy open.
- **Go:** a type switch (`switch s := shape.(type)`) is the common alternative; the visitor interface pays off when every operation must provably handle every type.
- **Python / JavaScript / PHP:** dynamic typing means dispatch can be done with `functools.singledispatch`, type tags, or `isinstance` checks; the `accept` form still keeps operations grouped and complete. Visitors can be plain objects/dicts of functions.
- **C:** emulated with a tagged union plus a struct of function pointers; the `switch` on the tag inside `accept` is the double dispatch.
- **C++:** the classic virtual `accept`/`visit` pair, or `std::variant` + `std::visit` for closed sets with no boilerplate.

## Examples

- [examples/visitor/visitor.py](../examples/visitor/visitor.py)
- [examples/visitor/visitor.c](../examples/visitor/visitor.c)
- [examples/visitor/visitor.cpp](../examples/visitor/visitor.cpp)
- [examples/visitor/visitor.java](../examples/visitor/visitor.java)
- [examples/visitor/visitor.cs](../examples/visitor/visitor.cs)
- [examples/visitor/visitor.js](../examples/visitor/visitor.js)
- [examples/visitor/visitor.rs](../examples/visitor/visitor.rs)
- [examples/visitor/visitor.go](../examples/visitor/visitor.go)
- [examples/visitor/visitor.php](../examples/visitor/visitor.php)
- [examples/visitor/visitor.swift](../examples/visitor/visitor.swift)

## Related Patterns

- **Composite** structures are the most common thing visitors traverse; the visitor walks the tree the composite defines.
- **Iterator** externalizes *traversal order*; Visitor externalizes the *operation performed* at each element. They combine naturally.
- **Interpreter** often implements each grammar operation as a visitor over the AST.
- **Strategy** varies one algorithm behind one interface; Visitor varies an operation across a whole hierarchy of types.
