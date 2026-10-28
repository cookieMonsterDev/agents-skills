# Mediator

**Category:** Behavioral

## Intent

Define an object that encapsulates how a set of objects interact. Colleagues communicate only through the mediator instead of referring to each other directly, turning a many-to-many web of dependencies into a star.

## Problem

- A group of objects (dialog widgets, chat users, aircraft) all need to react to each other, and every object ends up holding references to most of the others.
- Interaction rules ("when the checkbox is ticked, enable the submit button") are scattered across the participants instead of living in one place.
- You cannot reuse a component elsewhere because it is hard-wired to its current collaborators.

## Structure

- **Mediator** — interface declaring how colleagues notify it (`broadcast`, `notify(sender, event)`).
- **Concrete mediator** — knows all colleagues and owns the coordination logic; routes, filters, and sequences their interactions.
- **Colleagues** — hold a reference to the mediator only; they send events to it and receive calls from it, never from each other.

## When to Use

- Objects interact in complex but well-defined ways and the pairwise references are becoming unmanageable.
- You want to reuse colleagues independently of how they are wired together.
- Interaction logic should be testable and changeable in one place (e.g. form validation rules, chat routing, air-traffic sequencing).

## When Not to Use

- Only two or three objects interact; direct references or simple callbacks are clearer.
- The interactions are pure one-way notifications with no coordination logic — that is Observer's job.
- The mediator would just forward calls verbatim; you would be adding indirection without centralizing any rules.

## Trade-offs

- **Pros:** replaces many-to-many coupling with one-to-many, centralizes interaction rules, makes colleagues reusable and individually testable.
- **Cons:** the mediator can grow into a god object that knows everything; the flow of control is harder to trace because everything goes through one hub.

## Language Notes

- **Python / JavaScript / PHP:** duck typing keeps the mediator light — no interface needed; in JS an `EventEmitter`/`EventTarget`, and in PHP an event dispatcher, often plays the mediator role.
- **Java / C#:** classic interface-based form; in C#, events or the MediatR library's request/notification handlers are the common production shapes.
- **Rust:** cross-references between colleagues fight the borrow checker, so the idiomatic shape is a mediator that *owns* its colleagues and addresses them by id; shared colleagues require `Rc<RefCell<...>>`.
- **Go:** a small mediator interface plus struct colleagues; concurrent designs often replace the pattern with a goroutine owning a message channel.
- **C:** emulated with structs and function pointers — each colleague carries a callback the mediator invokes.
- **Swift:** protocol-based mediator with `weak` back-references to avoid retain cycles; `NotificationCenter` is the built-in broadcast mediator.

## Examples

- [examples/mediator/mediator.py](../examples/mediator/mediator.py)
- [examples/mediator/mediator.c](../examples/mediator/mediator.c)
- [examples/mediator/mediator.cpp](../examples/mediator/mediator.cpp)
- [examples/mediator/mediator.java](../examples/mediator/mediator.java)
- [examples/mediator/mediator.cs](../examples/mediator/mediator.cs)
- [examples/mediator/mediator.js](../examples/mediator/mediator.js)
- [examples/mediator/mediator.rs](../examples/mediator/mediator.rs)
- [examples/mediator/mediator.go](../examples/mediator/mediator.go)
- [examples/mediator/mediator.php](../examples/mediator/mediator.php)
- [examples/mediator/mediator.swift](../examples/mediator/mediator.swift)

## Related Patterns

- **Observer** distributes one-way notifications; Mediator centralizes two-way coordination logic. Mediators are often implemented *using* Observer internally.
- **Facade** simplifies access to a subsystem one-way; Mediator adds cooperative behavior between peers.
- **Command** objects can be the messages a mediator routes between colleagues.
