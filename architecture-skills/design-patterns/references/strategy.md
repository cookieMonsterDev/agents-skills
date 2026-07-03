# Strategy

**Category:** Behavioral

## Intent

Define a family of interchangeable algorithms, encapsulate each one, and let the client pick one at runtime. The algorithm varies independently from the code that uses it.

## Problem

- A class chooses between several ways of doing the same job with a growing `if`/`switch` on some "type" or "mode" flag, and every new variant means editing that conditional.
- The algorithm must be selectable at runtime (user setting, configuration, A/B test).
- Variants are hard to test in isolation because they are tangled into the host class.

## Structure

- **Strategy** — the common interface for all variants, usually a single method (`cost(order)`).
- **Concrete strategies** — one class (or function) per algorithm variant.
- **Context** — holds a reference to the current strategy and delegates to it; clients swap the strategy without the context noticing.

## When to Use

- Several variants of one algorithm exist and the choice happens at runtime.
- You want to add variants without modifying the code that selects between them (open/closed).
- A big conditional dispatches on "which algorithm" — each branch is a strategy waiting to be extracted.
- Variants need isolated unit tests or come from different modules/plugins.

## When Not to Use

- There are only two variants and they never change; a plain `if` is simpler and clearer.
- In languages with first-class functions, a full strategy interface is overkill for stateless one-method strategies — just pass a function (see Language Notes).
- The variants differ in _which steps run_, not the whole algorithm — that is Template Method's territory.

## Trade-offs

- **Pros:** swaps algorithms at runtime, isolates each variant for testing, removes conditional sprawl, new variants need no changes to existing code.
- **Cons:** more objects/indirection than a conditional; clients must know the differences between strategies to choose one; stateless strategies as classes are ceremony in functional-capable languages.

## Language Notes

- **Python / JavaScript / PHP:** a strategy is usually just a first-class function or closure; reserve classes for strategies with state or several methods. All three examples show both forms.
- **Java / C#:** the classic home of the pattern (`Comparator`, `Comparison<T>`, LINQ selectors). Single-method strategy interfaces are functional interfaces/delegates, so lambdas replace one-off classes.
- **Rust:** closures (`Box<dyn Fn(&Order) -> f64>`) cover most cases; a trait handles stateful or multi-method strategies, and a trait-based strategy plugs into a closure-taking context via a capturing closure.
- **Go:** a named function type (like `http.HandlerFunc`) is the idiomatic strategy; an interface is only needed for multi-method strategies.
- **Swift:** closures cover stateless strategies (`sorted(by:)` takes one); use a protocol when the strategy carries state.
- **C:** a strategy is literally a function pointer; a `void *` context argument carries strategy state.
- **C++:** store the strategy as `std::function` (or a template parameter) so lambdas and function objects both fit; virtual hierarchies are rarely needed.

## Examples

- [examples/strategy/strategy.py](../examples/strategy/strategy.py)
- [examples/strategy/strategy.c](../examples/strategy/strategy.c)
- [examples/strategy/strategy.cpp](../examples/strategy/strategy.cpp)
- [examples/strategy/strategy.java](../examples/strategy/strategy.java)
- [examples/strategy/strategy.cs](../examples/strategy/strategy.cs)
- [examples/strategy/strategy.js](../examples/strategy/strategy.js)
- [examples/strategy/strategy.rs](../examples/strategy/strategy.rs)
- [examples/strategy/strategy.go](../examples/strategy/strategy.go)
- [examples/strategy/strategy.php](../examples/strategy/strategy.php)
- [examples/strategy/strategy.swift](../examples/strategy/strategy.swift)

## Related Patterns

- **Template Method** varies steps of an algorithm via inheritance; Strategy swaps the whole algorithm via composition. Prefer Strategy when the variation is the entire algorithm.
- **State** has the same structure, but strategies are chosen by the client and rarely know about each other, while states switch themselves as the context's condition changes.
- **Command** also wraps behavior in an object, but to parameterize _when/whether_ something runs (queueing, undo), not _which variant_ runs.
