# Open/Closed Principle

**Category:** SOLID Principles

## Intent

Design modules so that new behavior is added by writing new code (a new implementation of an extension point), not by editing code that already works — open for extension, closed for modification.

## Problem

- A calculation engine dispatches on a type tag (`switch (rule.kind)`), and every new business rule means reopening the engine, adding a branch, and re-testing everything that already worked.
- The same variant list is switched on in several places (pricing, reporting, validation), so one new variant forces coordinated edits across files — and a missed spot becomes a silent bug.
- A stable, widely depended-on module keeps churning because unrelated feature requests all land as edits inside it; every edit risks regressions in callers that never asked for the change.

## Structure

- **Extension point** — a small abstraction (interface, function type, trait) that names the thing that varies, e.g. `DiscountRule.apply(order)`.
- **Closed core** — the engine/policy code that works purely against the extension point; it iterates or delegates, and never mentions concrete variants.
- **Extensions** — one implementation per variant; new behavior arrives as a new implementation, registered or injected from the outside (composition root, plugin registry, DI container).

## When to Use

- The same axis of change keeps hitting one module: your third "add a branch to this switch" commit is the signal to extract an extension point.
- Variants are contributed by different teams, modules, or plugins — they must be able to add behavior without touching (or even seeing) the core's source.
- A conditional on a type tag is duplicated across several functions; polymorphism collapses all of them into one dispatch.
- The core is stable and heavily depended on, and you want feature churn quarantined into new files rather than edits to it.

## When Not to Use

- **Speculative abstraction (YAGNI):** don't pre-build extension points for changes that haven't happened. The modern reading of OCP is to protect code that has *demonstrated* churn along an axis — abstract after the second or third variant, not before the first.
- **Closed sets of variants:** when the variants are genuinely fixed (card suits, HTTP methods, AST node kinds), an enum plus an exhaustive `switch`/`match` is better — the compiler then *forces* you to handle a new variant everywhere, which is a feature. Rust makes this trade explicit: `enum` + exhaustive `match` means adding a variant is a guided, compiler-checked edit; `trait` objects mean adding a variant needs no edits but the compiler can no longer enumerate them.
- **One place switches, many operations vary:** if you add new *operations* over a fixed set of types far more often than new types, the switch (or Visitor) side of the expression problem is the cheaper axis; forcing OCP here scatters each operation across every class.

## Trade-offs

- **Pros:** new variants ship as new files, so working code stays untouched and regression risk drops; extension by third parties/plugins becomes possible; the type-tag conditional disappears from every site at once; each variant is testable in isolation.
- **Cons:** an extra layer of indirection — readers can no longer see all behavior in one place and must find the implementations; the abstraction is a bet on the axis of change, and a wrong bet (variants that differ in ways the interface didn't anticipate) is expensive to unwind; registries and DI wiring add setup ceremony.

## Language Notes

- **Python / JavaScript / PHP:** duck typing means the extension point can be implicit — anything with an `apply(order)` method (or just a function) fits; a module-level registry list is the usual plugin mechanism. Python's `abc`/`Protocol` and PHP interfaces make the contract explicit when you want tooling to check it.
- **Java / C#:** the classic home of OCP — interfaces plus DI containers; new implementations are discovered via injection, `ServiceLoader` (Java), or assembly scanning (C#). `sealed` classes/interfaces (both languages) deliberately *close* a hierarchy to get exhaustive-switch checking — the enum side of the trade.
- **C++:** either runtime polymorphism (abstract base class, `std::function`) or compile-time extension (templates: new types satisfying a concept extend the algorithm with zero edits and zero virtual-call cost).
- **Rust:** the trade is explicit in the type system — `trait` objects (`Box<dyn Rule>`) are open to new variants but closed to enumeration; `enum` + `match` is the reverse. Choose the trait when downstream crates must add variants.
- **Go:** implicit interface satisfaction is OCP-friendly by design — a new type in any package extends the core just by having the right method set; registration via `init()` + a registry (as `database/sql` drivers do) is the idiomatic plugin form.
- **Swift:** protocols (plus protocol extensions for shared defaults) are the extension point; `enum` + exhaustive `switch` is preferred for closed sets, exactly mirroring the Rust trade.
- **C:** no interfaces, but function pointers registered in a table give the same shape — the core loops over the table, and a new rule is a new function plus one `register` call at startup (see the example).

## Examples

- [examples/open-closed/open-closed.py](../examples/open-closed/open-closed.py)
- [examples/open-closed/open-closed.cpp](../examples/open-closed/open-closed.cpp)
- [examples/open-closed/open-closed.java](../examples/open-closed/open-closed.java)
- [examples/open-closed/open-closed.cs](../examples/open-closed/open-closed.cs)
- [examples/open-closed/open-closed.js](../examples/open-closed/open-closed.js)
- [examples/open-closed/open-closed.php](../examples/open-closed/open-closed.php)
- [examples/open-closed/open-closed.swift](../examples/open-closed/open-closed.swift)

## Related Concepts

- **Polymorphism** is the mechanism OCP rides on: the closed core calls through one abstract operation, and dynamic dispatch selects the variant — that's what lets new variants plug in without edits.
- **Dependency Inversion** supplies the wiring: the core depends on the abstraction and receives concrete implementations from outside (composition root/registry), which is what keeps the core's source untouched when extensions arrive.
- **Interfaces and Abstract Classes** are the material extension points are made of; keeping them small (see **Interface Segregation**) keeps extensions cheap to write.
- **Liskov Substitution** is OCP's precondition: extension only works if every new implementation honors the contract the closed core relies on — a substitutable-in-name-only variant reopens the core via special cases.
