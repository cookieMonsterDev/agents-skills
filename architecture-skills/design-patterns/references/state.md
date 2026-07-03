# State

**Category:** Behavioral

## Intent

Allow an object to alter its behavior when its internal state changes, so it appears to change class. Behavior for each state lives in its own unit (class, enum variant, or handler table) instead of in conditionals scattered through the object.

## Problem

- An object's methods are full of `if state == X` / `switch (state)` blocks, and every new state or event means editing all of them.
- State transitions are implicit and easy to get wrong — nothing documents which events are valid in which state.
- The object behaves so differently per mode (a connection that is open/closed, an order that is pending/shipped) that one flat implementation is hard to follow.

## Structure

- **Context** — the object clients use (vending machine, TCP connection); holds the current state and delegates events to it.
- **State** — the contract every state fulfills: one handler per event (`insertCoin`, `selectItem`).
- **Concrete states** — one per mode (Idle, HasCoin, SoldOut); each handles events its own way and performs transitions by installing the next state on the context.

## When to Use

- Behavior genuinely differs by mode and the modes are named domain concepts (order lifecycle, connection status, game phases, protocol steps).
- The same conditional over a status field is repeated across several methods.
- Transitions need to be explicit, valid, and testable per state.

## When Not to Use

- Two or three states with trivial differences — a plain enum field and a couple of `switch` statements are easier to read than a class hierarchy.
- The "states" don't change at runtime; that's just polymorphism, use **Strategy** or plain subtypes.
- The machine is complex enough (nested states, guards, timers) that a statechart library beats a hand-rolled pattern.

## Trade-offs

- **Pros:** eliminates repeated conditionals; each state is small and independently testable; adding a state doesn't touch the others; invalid (state, event) pairs become visible.
- **Cons:** more moving parts than a `switch` for small machines; behavior for one event is spread across files; transition logic can end up duplicated between states.

## Language Notes

- **Python / JavaScript / PHP:** duck typing keeps states light — small classes in Python (ABC optional), a plain object lookup table in JS (XState is the ecosystem's heavyweight version), classes or PHP 8.1 enums with methods in PHP.
- **Java / C#:** Java enums with per-constant method bodies are the idiomatic home for a fixed state set; C# uses class-per-state with shared singletons, or a `switch` expression over an enum for simple machines.
- **Rust:** an enum + `match` is the idiomatic state machine — the compiler enforces that every (state, event) pair is handled, and variants can carry per-state data. The trait-object form (`Box<dyn State>`) is only worth it for open-ended state sets.
- **Go:** small structs implementing a state interface, swapped on transition; a `switch` over an int/string state is common for simple machines.
- **C:** emulated with structs of function pointers — each state is a handler table and transitions swap the pointer; a `switch` over an enum is the lighter C idiom.
- **Swift:** an enum with `mutating` methods and exhaustive `switch` is idiomatic; associated values carry per-state data.

## Examples

- [examples/state/state.py](../examples/state/state.py)
- [examples/state/state.c](../examples/state/state.c)
- [examples/state/state.cpp](../examples/state/state.cpp)
- [examples/state/state.java](../examples/state/state.java)
- [examples/state/state.cs](../examples/state/state.cs)
- [examples/state/state.js](../examples/state/state.js)
- [examples/state/state.rs](../examples/state/state.rs)
- [examples/state/state.go](../examples/state/state.go)
- [examples/state/state.php](../examples/state/state.php)
- [examples/state/state.swift](../examples/state/state.swift)

## Related Patterns

- **Strategy** has the same delegate-to-an-object shape, but strategies are chosen by the client and don't know about each other; states transition among themselves.
- **Singleton** — stateless state objects are often shared as singletons to avoid per-transition allocation.
- **Memento** can capture the context's state (including which state object is active) for undo.
