# Memento

**Category:** Behavioral

## Intent

Capture and externalize an object's internal state — without violating its encapsulation — so the object can be restored to that state later. The classic mechanism behind undo.

## Problem

- You need undo/rollback (editor history, transaction abort, game save points), which requires storing earlier states somewhere.
- Exposing the object's fields so another component can copy them would break encapsulation and freeze the internal representation forever.
- Letting the object manage its own history bloats it with concerns (storage limits, undo stacks) that aren't its job.

## Structure

- **Originator** — the object whose state is saved; it creates mementos (`save()`) and is the only party that can read one back (`restore(m)`).
- **Memento** — an immutable value object holding the captured state; opaque to everyone but the originator.
- **Caretaker** — stores mementos (typically a stack for undo) and decides *when* to save and restore, but never looks inside one.

## When to Use

- Undo/redo, checkpoints, or rollback over an object whose internals should stay private.
- You want history management (how many snapshots, when to prune) separated from the domain object itself.
- Transactional operations that must restore a consistent prior state on failure.

## When Not to Use

- State is large and changes often — full snapshots get expensive; consider **Command** with inverse operations, or incremental diffs, instead.
- The state is trivially public (a plain data record); just copy it, no pattern needed.
- You need to persist across processes — that's serialization; memento is about in-memory restore without exposing structure.

## Trade-offs

- **Pros:** encapsulation survives; undo logic lives outside the domain object; snapshots are simple and reliable to restore (no inverse-operation bugs).
- **Cons:** memory cost of copies, especially with frequent saves; caretakers can't prune "important" states intelligently because the mementos are opaque; true opacity is hard to enforce in dynamic languages.

## Language Notes

- **Python / JavaScript / PHP:** no enforceable privacy, so memento opacity is by convention; a frozen dataclass, `Object.freeze`, or `readonly` properties at least make snapshots immutable. JS `structuredClone()` and PHP `clone` cover crude whole-state snapshots.
- **Java / C#:** nested types give real opacity — a private nested record (Java) or a nested record with `internal` accessors (C#) is readable only by the originator.
- **Rust:** ownership makes the pattern natural: `save()` clones state into a value the caretaker owns; private fields plus module boundaries enforce opacity. Deriving `Clone` on the originator often suffices.
- **Go:** unexported snapshot fields make mementos opaque outside the package; returning the struct by value hands the caretaker an independent copy for free.
- **C:** emulated with a snapshot struct copied by value; opacity is purely a convention (only `editor_*` functions touch its fields).
- **Swift:** struct snapshots get value semantics for free; making them `Codable` connects the pattern to state-restoration and persistence APIs.

## Examples

- [examples/memento/memento.py](../examples/memento/memento.py)
- [examples/memento/memento.c](../examples/memento/memento.c)
- [examples/memento/memento.cpp](../examples/memento/memento.cpp)
- [examples/memento/memento.java](../examples/memento/memento.java)
- [examples/memento/memento.cs](../examples/memento/memento.cs)
- [examples/memento/memento.js](../examples/memento/memento.js)
- [examples/memento/memento.rs](../examples/memento/memento.rs)
- [examples/memento/memento.go](../examples/memento/memento.go)
- [examples/memento/memento.php](../examples/memento/memento.php)
- [examples/memento/memento.swift](../examples/memento/memento.swift)

## Related Patterns

- **Command** implements undo the other way — by storing inverse operations instead of snapshots; the two are often combined (commands save a memento before executing).
- **Iterator** state can be captured in a memento to resume a traversal later.
- **Prototype** also copies objects, but to create new independents, not to restore an original.
