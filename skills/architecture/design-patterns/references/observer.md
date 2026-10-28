# Observer

**Category:** Behavioral

## Intent

Define a one-to-many dependency between objects so that when one object (the subject) changes state, all its dependents (observers) are notified automatically — without the subject knowing who they are.

## Problem

- One object's state changes must be reflected in an open-ended set of others (a stock price feeding displays, alerts, and loggers), but hard-coding those calls couples the subject to every consumer.
- The set of interested parties changes at runtime; the subject shouldn't need modification each time a consumer is added.
- Polling for changes wastes work and delays reactions; you want push-based notification.

## Structure

- **Subject** — maintains a list of observers and offers `subscribe`/`unsubscribe`; on each state change it calls every registered observer.
- **Observer** — the notification contract: a one-method interface, a plain callback/closure, or a language event, receiving the event data as arguments.
- **Concrete observers** — displays, alerts, loggers — react to notifications; the subject never knows their concrete types.

## When to Use

- Changes in one object must propagate to an unknown or changing set of others (UI updates, domain events, live feeds, cache invalidation).
- You want the publishing side compilable and testable with zero knowledge of its consumers.
- Subscribers come and go at runtime.

## When Not to Use

- There is exactly one, fixed consumer — a direct call or injected callback is simpler and traceable.
- Notification order or a reply matters; observers are unordered fire-and-forget by contract. If observers must coordinate, that's a **Mediator**.
- Cascading updates (observers mutating state that triggers more notifications) would be hard to reason about — a sign to restructure the flow instead.

## Trade-offs

- **Pros:** subject and observers evolve independently; new consumers require no subject changes; runtime subscription.
- **Cons:** control flow becomes implicit and harder to debug ("who reacted, and why?"); forgotten unsubscribes cause memory leaks (the classic "lapsed listener" bug); notification storms and update ordering can surprise you.

## Language Notes

- **Python / JavaScript / PHP:** plain callables/closures are the idiomatic observer; `subscribe()` conventionally returns an unsubscribe function. JS should prefer the platform's `EventTarget` (browser) or `EventEmitter` (Node) over hand-rolled subjects. PHP's built-in `SplSubject`/`SplObserver` carry no payload, so closures are used in practice.
- **Java / C#:** Java uses listener interfaces (often `@FunctionalInterface` so lambdas work) — `java.util.Observer` is deprecated. C# has the pattern built in as events (multicast delegates), with `IObservable<T>`/`IObserver<T>` for Rx pipelines.
- **Rust:** the GoF form fights the borrow checker; store boxed closures owned by the subject, or use `Rc<RefCell<dyn Observer>>` for shared observers at the cost of runtime borrow checks. Most Rust code reaches for channels (`std::sync::mpsc`) instead.
- **Go:** a one-method interface plus a func adapter (like `http.HandlerFunc`); concurrent programs usually fan out over channels rather than calling observers synchronously.
- **C:** emulated with function pointers — each subscription is a callback plus a `void*` context pointer (the C idiom for closures).
- **Swift:** closures with token-based unsubscription work, but real apps prefer Combine publishers, the Observation framework (`@Observable`), `NotificationCenter`, or KVO; mind strong captures in stored closures (`[weak self]`).

## Examples

- [examples/observer/observer.py](../examples/observer/observer.py)
- [examples/observer/observer.c](../examples/observer/observer.c)
- [examples/observer/observer.cpp](../examples/observer/observer.cpp)
- [examples/observer/observer.java](../examples/observer/observer.java)
- [examples/observer/observer.cs](../examples/observer/observer.cs)
- [examples/observer/observer.js](../examples/observer/observer.js)
- [examples/observer/observer.rs](../examples/observer/observer.rs)
- [examples/observer/observer.go](../examples/observer/observer.go)
- [examples/observer/observer.php](../examples/observer/observer.php)
- [examples/observer/observer.swift](../examples/observer/observer.swift)

## Related Patterns

- **Mediator** centralizes many-to-many coordination; Observer broadcasts one-to-many notifications. Mediators are often built on Observer internally.
- **Publish–subscribe** is Observer with a broker in between, decoupling publishers from subscribers entirely (often across processes).
- **Memento** pairs well when observers need to react to *what* changed by comparing snapshots.
