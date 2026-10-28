# Interfaces & Abstract Classes

**Category:** Building Blocks

## Intent

Separate what a type promises from how it works: an interface declares a pure contract that callers depend on, while an abstract class supplies a partial implementation that a family of implementers shares. Clients program to the contract, so implementations can be added or swapped without touching client code.

## Problem

- Client code names concrete classes directly (`CsvExporter`, `StripeProcessor`), so adding a new format or provider means editing every call site instead of just registering one new class.
- Several implementations of the same job copy-paste an identical skeleton (validate input, assemble output, append a footer) and the copies silently drift apart as bugs are fixed in one but not the others.
- Code is hard to test because the real implementation (network call, file write) is welded in — there is no seam where a fake satisfying the same contract could be substituted.

## Structure

- **Interface (the contract)** — method signatures only: the complete list of what callers may rely on, with no implementation. Many languages let it carry *default methods* — behavior derived purely from the contract's own methods (e.g. a `fileName()` computed from `contentType()`).
- **Abstract class (the partial implementation)** — implements the contract's invariant parts once and declares the varying parts as abstract hooks for subclasses. It cannot be instantiated; it exists only to be completed.
- **Concrete implementations** — either extend the abstract class (filling in the hooks) or implement the interface directly when the shared logic doesn't apply.
- **Client** — accepts the interface type and never mentions a concrete class; this is "programming to the contract."

## When to Use

- Use an **interface** when the only thing implementations share is the contract — unrelated types (a CSV writer, a JSON serializer, an in-memory fake) must all be usable through one client-facing type.
- Use an **abstract class** when several implementations share real logic or state, not just signatures — the shared `export()` skeleton belongs in one place, with only `header()`/`row()` varying.
- You need a substitution seam for testing: the client takes the interface, the test passes a stub.
- The best split is often both: an interface as the public contract, plus an *optional* abstract base for implementers who want the shared logic (Java's `List` + `AbstractList` is the canonical pair).

## When Not to Use

- There is exactly one implementation and no test needs a fake — a plain class is simpler; extract the interface when the second implementation actually arrives.
- The "interface" mirrors one concrete class method-for-method and exists only out of habit (`IUserService`/`UserService` pairs); it adds a file and an indirection but no seam anyone uses.
- You reach for an abstract class only to share utility code between unrelated types — that shared code has no is-a relationship to its users; prefer a helper the classes compose (see **composition-over-inheritance**).

## Trade-offs

- **Pros:** clients decouple from concrete types, so implementations can be added without modifying callers; shared logic lives once in the abstract base instead of being copy-pasted; contracts create natural test seams; the interface documents exactly what callers may assume.
- **Cons:** an extra layer of indirection — readers must find the concrete type behind the interface; abstract classes claim the single-inheritance slot in most languages and couple subclasses to base-class internals; a published contract is hard to change, since every implementer breaks; premature interfaces ossify a design that was still finding its shape.

## Language Notes

- **Python:** no `interface` keyword — an `abc.ABC` with only `@abstractmethod`s plays the interface role, and the same ABC with implemented methods is an abstract class. `typing.Protocol` is the structural alternative: implementers conform by shape, with no import or inheritance.
- **C:** neither construct exists; an interface is emulated as a struct of function pointers (a vtable), and the "abstract class" is a shared helper function that concrete implementations delegate to, passing their varying steps as function pointers.
- **C++:** an interface is a class with only pure virtual functions (`= 0`) and a virtual destructor; an abstract class mixes implemented and pure virtual members. A non-virtual member implemented in terms of the pure virtuals plays the default-method role.
- **Java:** the classic home of the pair — `interface` (with `default` methods since Java 8) and `abstract class`, often shipped together as contract + optional skeleton (`List` + `AbstractList`). Interfaces allow multiple inheritance of type; the abstract class costs the one `extends` slot.
- **C#:** `interface` (with default interface methods since C# 8 — reachable only through the interface type) and `abstract class` with `abstract`/`virtual`/`override` members. Interface names conventionally start with `I`.
- **PHP:** has both keywords, but `interface` methods cannot carry bodies — the default-method role is played by a `trait` that implementers `use`, or by the abstract class.
- **JavaScript:** no interfaces — the contract is a duck-typed shape ("anything with `export(metrics)`"), enforced by convention, tests, or TypeScript/JSDoc. An abstract class is a convention too: a base class whose unimplemented methods throw.
- **Rust:** traits are both roles at once — required methods are the contract, default method bodies are the partial implementation. A blanket `impl<T: Step> Contract for T` implements a whole trait once for every type providing the varying steps, which is the closest analog to an abstract base.
- **Go:** interfaces are implicit — a type satisfies one by having the methods, no `implements` clause — and are idiomatically small (1–3 methods). There are no abstract classes; shared logic lives in a helper function or a configurable struct that implementers embed (embedding has no virtual dispatch back to the outer type).
- **Swift:** protocols are the interface; protocol extensions supply default methods. There are no abstract classes — the partial-implementation role is a refining protocol whose extension implements the contract in terms of the requirements, and it works for structs as well as classes.

## Examples

- [examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.py](../examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.py)
- [examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.cpp](../examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.cpp)
- [examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.java](../examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.java)
- [examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.cs](../examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.cs)
- [examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.js](../examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.js)
- [examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.php](../examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.php)
- [examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.swift](../examples/interfaces-and-abstract-classes/interfaces-and-abstract-classes.swift)

## Related Concepts

- **Abstraction** is the principle both constructs serve: expose what a type does, hide how. Interfaces and abstract classes are the concrete language machinery for it.
- **Polymorphism** is what programming to the contract buys — one client call site dispatches to whichever implementation stands behind the interface.
- **Dependency Inversion** tells you *where* to put the interface: high-level clients own the contract and low-level implementations conform to it, not the other way around.
- **Composition over Inheritance** is the check on abstract classes — if the base class exists only to share utility code rather than to define a family, compose a helper instead of inheriting.
