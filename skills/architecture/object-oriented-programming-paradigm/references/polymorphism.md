# Polymorphism

**Category:** The Four Pillars

## Intent

Let one call site — `shape.area()`, one loop, one function — work with many concrete types, so behavior varies by the object's actual type without the caller branching on what that type is.

## Problem

- Code that handles several kinds of a thing grows a `switch`/`if` on a type tag (`if kind == "circle": ... elif kind == "rect": ...`) at *every* place that touches them, and each new kind means hunting down and editing all of those branches.
- A collection holds mixed elements (circles, rectangles, triangles) but processing it forces casts or type checks because there is no common way to ask each element to do its own work.
- A function is duplicated per type (`renderCircle`, `renderRect`, ...) even though every copy has the same shape, differing only in which operations it calls.

## Structure

Polymorphism comes in three kinds; the first is the pillar and the main focus here:

- **Subtype polymorphism (dynamic dispatch)** — a shared abstraction (interface, abstract class, trait, protocol) declares operations; concrete types supply their own implementations. The call site holds a reference of the abstract type, and the *runtime* type decides which implementation runs — typically via a vtable lookup. This is what makes `for shape in shapes: shape.area()` work over a heterogeneous collection.
- **Parametric polymorphism (generics)** — one definition works uniformly for *any* type: `List<T>`, `fn largest<T: Shape>(...)`. The type is a parameter; dispatch is resolved at compile time (static dispatch), often by generating a specialized copy per type (monomorphization).
- **Ad-hoc polymorphism** — one *name* means different things per type: method/operator overloading resolved statically by argument types, or duck typing in dynamic languages, where any object with the right methods qualifies regardless of declared type.

Roles in the subtype form:

- **Abstraction** — the interface or base type naming the operations (`Shape` with `area()` and `describe()`); it is the only type the client mentions.
- **Concrete types** — `Circle`, `Rectangle`, `Triangle`; each owns its data and its version of the operations.
- **Client (call site)** — code written once against the abstraction; it never inspects concrete types, so new types plug in without touching it.

## When to Use

- The same conditional on "what kind is this" appears in more than one place — each branch is a method override waiting to happen.
- You iterate over a mixed collection and want each element to behave according to its own type, without casts or `instanceof`/`isinstance` checks.
- New variants must be addable without editing existing call sites (the open/closed pressure): plugins, drivers, handlers, renderers.
- The set of *types* grows more often than the set of *operations* — polymorphism localizes each new type in one class. (If operations grow faster than types, a `switch` or visitor may fit better.)
- Choose the kind by binding time: subtype when the concrete type is only known at runtime; parametric when one algorithm should work identically for any type; ad-hoc overloading when a name should adapt to argument types at compile time.

## When Not to Use

- There are two fixed cases that will never grow — a plain `if` is shorter, flatter, and easier to read than a two-class hierarchy.
- The variation is in *data*, not behavior (only a label or a constant differs) — a field or a lookup table beats subclassing.
- The type is statically known and performance is tight in a hot loop — prefer generics/monomorphization (static dispatch) over virtual calls; dynamic dispatch defeats inlining.
- Subclasses would override methods in ways that break the base type's promises — that is a Liskov Substitution violation; polymorphism only pays off when every concrete type is honestly substitutable.

## Trade-offs

- **Pros:** call sites are written once and closed to modification while the type set stays open; type-dispatch conditionals disappear; each concrete type is testable in isolation; heterogeneous collections become natural.
- **Cons:** control flow is indirect — you can no longer see which code runs by reading the call site; behavior is scattered across many classes instead of one function; dynamic dispatch has a (usually small) runtime cost and blocks inlining; overloading resolved statically can surprise when the *static* type differs from the runtime type.

## Language Notes

- **Python:** duck typing is the default — any object with `area()` works, no shared base needed (ad-hoc polymorphism as the everyday form). Use `abc.ABC`/`@abstractmethod` or `typing.Protocol` when you want the contract explicit and checkable. No method overloading; use default arguments or `functools.singledispatch`.
- **C:** no built-in dispatch — build it: a struct of function pointers (a hand-rolled vtable) plus a `void *`/embedded-struct object pointer. This is exactly what C++ compilers generate, and it is how qsort-style callbacks and kernel driver ops tables work.
- **C++:** subtype polymorphism requires `virtual` (and a `virtual` destructor) and works through pointers/references — objects in a `std::vector<Shape>` would slice. Templates give parametric polymorphism with zero-cost static dispatch; overloading is pervasive ad-hoc polymorphism.
- **Java:** all instance methods are virtual by default; `interface` (or abstract class) is the abstraction. Generics (`<T extends Shape>`) are parametric but erased at runtime; overloading is resolved statically by the declared argument types — a classic interview trap.
- **C#:** methods are non-virtual unless marked `virtual`/`abstract`; interfaces dispatch dynamically. Generics are reified (real types at runtime, monomorphized for value types); overloading works as in Java.
- **JavaScript:** duck typing over prototypes — any object with the method responds; `class` is sugar over prototype-chain lookup, which *is* the dynamic dispatch mechanism. No overloading; inspect arguments instead.
- **Rust:** both forms are explicit at the call site: `&dyn Shape` / `Box<dyn Shape>` is a trait object with vtable dispatch (needed for heterogeneous collections); `fn f<T: Shape>(x: &T)` monomorphizes into per-type copies — static dispatch, zero overhead, but code-size cost. No inheritance, no overloading; traits carry all polymorphism.
- **Go:** interfaces are satisfied implicitly (structural, "static duck typing"); an interface value is a (type, pointer) pair and method calls dispatch dynamically through it. Generics (Go 1.18+) add the parametric kind. No overloading.
- **PHP:** `interface`/`abstract class` with dynamic dispatch, much like Java. No generics in the language (docblock templates only) and no true overloading — `__call` or variadics emulate it.
- **Swift:** protocols are the abstraction; `any Shape` (existential) dispatches dynamically, while generic constraints (`<T: Shape>`) are specialized statically where possible. Both overloading and default protocol implementations are ad-hoc forms; beware that methods added only in extensions (not protocol requirements) dispatch statically.

## Examples

- [examples/polymorphism/polymorphism.py](../examples/polymorphism/polymorphism.py)
- [examples/polymorphism/polymorphism.cpp](../examples/polymorphism/polymorphism.cpp)
- [examples/polymorphism/polymorphism.java](../examples/polymorphism/polymorphism.java)
- [examples/polymorphism/polymorphism.cs](../examples/polymorphism/polymorphism.cs)
- [examples/polymorphism/polymorphism.js](../examples/polymorphism/polymorphism.js)
- [examples/polymorphism/polymorphism.php](../examples/polymorphism/polymorphism.php)
- [examples/polymorphism/polymorphism.swift](../examples/polymorphism/polymorphism.swift)

## Related Concepts

- **Interfaces and Abstract Classes** supply the contract that subtype polymorphism dispatches through — the abstraction is *what* the client sees; polymorphism is *why* declaring it pays off.
- **Inheritance** is one mechanism for creating substitutable subtypes, but not the only one: interfaces, traits, and duck typing give polymorphism without an implementation hierarchy.
- **Liskov Substitution** is the correctness condition: dispatching through a base type is only safe if every concrete type honors the base type's contract.
- **Open-Closed** is the payoff: polymorphic call sites are the standard way to add new behavior (a new class) without modifying existing code.
