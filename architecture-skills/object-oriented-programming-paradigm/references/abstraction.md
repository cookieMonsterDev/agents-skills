# Abstraction

**Category:** The Four Pillars

## Intent

Expose the essential model of a component — what it does for its callers — behind a small, stable contract, and hide every operational detail behind it, so callers can be written once and implementations can be swapped without touching them. Abstraction decides _what to expose_; its sibling encapsulation decides _how to hide the rest_.

## Problem

- Business code talks to a concrete backend directly (a dict, a file format, an SQL client), so "move notes from memory to disk" means editing every call site instead of one class.
- Callers are cluttered with operational noise — connection handling, serialization, path juggling — drowning out the one line that says what the code actually means (`store.save(key, text)`).
- Nothing can be tested without the real infrastructure, because there is no seam where a cheap in-memory implementation could stand in for the file- or network-backed one.
- Code mixes levels of abstraction: a function that reads as policy ("archive the order") suddenly drops into byte offsets and retry loops, forcing every reader to context-switch between the what and the how.

## Structure

- **Abstraction** — the contract (interface, abstract class, trait, protocol, or function-pointer table): a handful of operations named in the caller's vocabulary (`save`, `load`), with no trace of files, sockets, or dicts. This is the _essential model_ of the component.
- **Implementations** — one type per operational choice (in-memory map, append-only file, remote service). All the "how" lives here and nowhere else.
- **Client** — written once against the abstraction. The proof that the abstraction works: the client runs unchanged when the implementation behind it swaps.

Each layer should read at one level: clients speak the domain, the abstraction names domain operations, implementations speak mechanism. When a level skips down (a caller peeking at the file path), the layering has failed.

## When to Use

- Two or more plausible implementations of the same job exist now or are foreseeable (in-memory vs file-backed vs remote), or tests need a fake in place of real infrastructure.
- A change of mechanism (new file format, new vendor) would today ripple through many call sites — an abstraction turns that into a one-class change.
- Callers keep re-stating the same operational boilerplate around every use of a component; a contract with the boilerplate folded inside restores one-level-of-abstraction reading.
- You are designing a module boundary: the contract is the published surface, everything else stays private to the module.

## When Not to Use

- There is exactly one implementation and no test seam is needed — an interface with a single implementer is speculative ceremony; introduce the abstraction when the second implementation (or the fake) actually arrives.
- The "abstraction" would just mirror one concrete API method-for-method (a thin wrapper over one vendor SDK). That is coupling with extra steps; either wrap in _your domain's_ vocabulary or call the SDK directly.
- The hidden detail refuses to stay hidden — performance, failure modes, or transactional behavior of one backend leak into how callers must be written (the _leaky abstraction_ problem). If callers must know it is a network call to use it correctly, put that in the contract (timeouts, error types) rather than pretending it away.
- The real goal is protecting invariants inside one class rather than defining a swappable contract — that is **encapsulation**; see Related Concepts.

## Trade-offs

- **Pros:** callers survive implementation swaps untouched; tests run against cheap fakes; each piece of code reads at a single level of abstraction; the contract documents what actually matters about the component.
- **Cons:** one more layer of indirection to navigate ("where does `save` actually go?"); a wrong abstraction is worse than none — callers contort around a contract that fits no implementation well; every abstraction leaks a little (latency, ordering, failure modes), and hiding those completely can produce code that is correct against the interface but wrong against reality.

## Language Notes

- **Python / JavaScript / PHP:** duck typing means the client would accept any object with `save`/`load` — the abstraction can be purely conventional. Naming it still pays: Python uses `abc.ABC` or `typing.Protocol`, PHP an `interface`; JavaScript typically documents the shape (or moves to TypeScript for a checked `interface`).
- **Java / C#:** `interface` is the direct tool, and the ecosystem's default seam for dependency injection and mocking. C# convention prefixes with `I` (`INoteStore`); keep the interface small rather than mirroring an implementation.
- **C++:** an abstract base class with pure `virtual` methods (and a `virtual` destructor) for runtime swapping; templates/concepts give the same contract at compile time with no vtable cost.
- **Rust:** a `trait` is the abstraction; clients take `&dyn Trait` (runtime polymorphism) or `impl Trait`/generics (static, zero-cost). The borrow checker pushes contracts toward explicit ownership in signatures — a healthy anti-leak pressure.
- **Go:** interfaces are satisfied implicitly, and idiom says to declare the interface next to the _consumer_, sized to what that consumer needs (often one or two methods) — abstraction from the caller's point of view by construction.
- **Swift:** protocols, usually adopted by value types (`struct`); protocol extensions can supply shared behavior without a base class.
- **C:** no language support — the abstraction is a hand-rolled table of function pointers plus an opaque `void *` state pointer (the same shape as an interface vtable). Opaque struct pointers in headers (`typedef struct Store Store;`) hide layout the way private fields hide state elsewhere.

## Examples

- [examples/abstraction/abstraction.py](../examples/abstraction/abstraction.py)
- [examples/abstraction/abstraction.cpp](../examples/abstraction/abstraction.cpp)
- [examples/abstraction/abstraction.java](../examples/abstraction/abstraction.java)
- [examples/abstraction/abstraction.cs](../examples/abstraction/abstraction.cs)
- [examples/abstraction/abstraction.js](../examples/abstraction/abstraction.js)
- [examples/abstraction/abstraction.php](../examples/abstraction/abstraction.php)
- [examples/abstraction/abstraction.swift](../examples/abstraction/abstraction.swift)

## Related Concepts

- **Encapsulation** is the pillar most confused with this one. Abstraction is outward-facing: it chooses the essential model callers see (`save`/`load` and nothing else). Encapsulation is inward-facing: it hides state and enforces invariants behind that surface (private fields, no reaching into the dict or file). You can encapsulate without abstracting (a concrete class with private fields) and abstract without much to encapsulate (a stateless contract) — mature designs do both.
- **Interfaces and Abstract Classes** are the language mechanisms this pillar is usually built from; that concept covers when to pick a pure interface versus an abstract class with shared behavior.
- **Polymorphism** is what makes the swap work at runtime: the client's `store.save(...)` dispatches to whichever implementation is behind the contract. Abstraction defines the contract; polymorphism selects the implementation.
- **Dependency Inversion** applies abstraction to architecture: high-level policy depends on the abstraction it defines, and low-level mechanisms implement it — which is exactly why the client in the examples never imports the file-backed store.
