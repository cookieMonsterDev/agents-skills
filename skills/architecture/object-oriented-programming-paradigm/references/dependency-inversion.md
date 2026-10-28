# Dependency Inversion Principle

**Category:** SOLID Principles

## Intent

Make high-level policy code depend on an abstraction it owns, and make low-level details implement that abstraction — so the source-code dependency arrows point from details toward policy, the opposite of the call direction. Concrete implementations are chosen and injected in one place at the edge of the program.

## Problem

- `OrderService` calls `new SmtpNotifier(host, port)` inside its own methods, so verifying "placing an order notifies the customer" requires a live SMTP server — the business rule cannot be unit tested without infrastructure.
- Swapping a vendor (SMTP → SendGrid → SMS) or adding a second channel means editing business logic, and every infrastructure change (a new config field on the mailer) ripples upward into policy code that shouldn't care.
- The domain module imports the infrastructure module, so the most important code in the system is hostage to the most volatile: it recompiles, redeploys, and breaks on the details' schedule, and import cycles start to appear.

## Structure

- **High-level policy** — the business rule (`OrderService.place`); it references only the abstraction and receives an implementation through its constructor, never constructing one itself.
- **Abstraction** — the `Notifier` interface. Crucially it is *owned by the high-level side*: it is written in the policy's vocabulary ("notify this customer"), sized to what the policy needs, and lives with the policy — not a mirror of what SMTP happens to offer.
- **Low-level detail** — `ConsoleNotifier`, `SmtpNotifier`, `RecordingNotifier`: implementations of the abstraction. Their source depends on the policy's interface; the policy's source never mentions them.
- **Composition root** — `main()` (or the app bootstrap): the one place allowed to know concrete types. It instantiates a detail and passes it into the policy's constructor (constructor injection), keeping the choice of implementation out of business code.

## DIP vs Dependency Injection vs DI Containers

Three things that travel together but are not the same:

- **DIP** is a *design principle* about the direction of dependencies: policy defines and owns the abstraction; details conform to it.
- **Dependency injection** is a *technique*: passing collaborators in (preferably through the constructor) instead of constructing them internally. You can inject without inverting — a service that takes a concrete `SmtpNotifier` in its constructor is injected but still coupled to the detail.
- **DI containers** (Spring, ASP.NET Core, etc.) are *tooling* that automates the composition root's wiring. They are optional: a hand-written `main()` that news up implementations and passes them in satisfies DIP completely, and every example below does exactly that.

## When to Use

- A business rule cannot be unit tested without a network, database, filesystem, clock, or random source — each of those concrete references is a seam waiting to be inverted.
- Import/`using` arrows run from your domain package into infrastructure packages; inverting flips them so infrastructure plugs into the domain.
- A dependency is *volatile* — vendor choice, I/O channel, anything configured per environment (prod vs. staging vs. local) — and you need to swap it without touching the policy.
- Two deployables or teams need to evolve independently: the interface becomes the stable contract between them, owned by the consumer.

## When Not to Use

- **Don't invert everything.** DIP targets *volatile* dependencies. Depending concretely on stable things — string formatting, math, collections, the standard library, a pure utility function — is fine; nobody needs an `IStringJoiner`.
- **The one-implementation-forever interface is a smell.** A `FooService`/`FooServiceImpl` pair where no second implementation (not even a test fake) will ever exist adds indirection with no payoff; call the class directly and extract an interface when a real second implementation or a testing need appears.
- **Small scripts and short-lived code:** direct construction is simpler and the wiring ceremony costs more than it saves. **Coupling and Cohesion** covers the broader judgment of which couplings are worth paying to remove.

## Trade-offs

- **Pros:** policy becomes unit-testable by swapping in a fake — no infrastructure, no mocks-over-network; implementations swap per environment at one wiring site; infrastructure churn stops rippling into domain code; modules can be compiled, versioned, and deployed independently.
- **Cons:** indirection — "go to definition" lands on an interface, and finding the runtime implementation means finding the composition root; abstractions extracted too early tend to mirror their single implementation and leak its details into the contract; a constructor accumulating many injected parameters is a **Single Responsibility** warning, not a wiring problem.

## Language Notes

- **Python / JavaScript / PHP:** duck typing inverts without a declared interface — inject any object with the right method and the policy never names a concrete type. Python's `typing.Protocol` (used in the example) and PHP's `interface` make the contract checkable by tools without coupling implementations to a base class; in JavaScript the contract stays implicit.
- **Java / C# / Swift:** the classic home — an interface/protocol plus constructor injection. DI containers (Spring, ASP.NET Core) automate the wiring at scale, but the principle needs none of them; the examples wire by hand in `main`.
- **Go:** consumer-side interfaces are the language default: the consuming package declares the small interface it needs, and any type with the right method set satisfies it implicitly — "abstraction owned by the high-level side" falls out of idiomatic Go for free.
- **Rust:** traits are the abstraction; choose `OrderService<N: Notifier>` (generics — static dispatch, zero cost, implementation fixed at compile time, one monomorphized copy per type) or `Box<dyn Notifier>` (runtime choice, one copy of the code). The example uses the generic form.
- **C++:** an abstract base class with a virtual method, injected by reference or smart pointer (the example), or a template parameter for compile-time injection mirroring Rust's generic form.
- **C:** no interfaces, so the abstraction is a struct of function pointers — a hand-rolled vtable — with a self pointer for implementation state; the policy holds only a pointer to that struct.

## Examples

- [examples/dependency-inversion/dependency-inversion.py](../examples/dependency-inversion/dependency-inversion.py)
- [examples/dependency-inversion/dependency-inversion.cpp](../examples/dependency-inversion/dependency-inversion.cpp)
- [examples/dependency-inversion/dependency-inversion.java](../examples/dependency-inversion/dependency-inversion.java)
- [examples/dependency-inversion/dependency-inversion.cs](../examples/dependency-inversion/dependency-inversion.cs)
- [examples/dependency-inversion/dependency-inversion.js](../examples/dependency-inversion/dependency-inversion.js)
- [examples/dependency-inversion/dependency-inversion.php](../examples/dependency-inversion/dependency-inversion.php)
- [examples/dependency-inversion/dependency-inversion.swift](../examples/dependency-inversion/dependency-inversion.swift)

## Related Concepts

- **Abstraction** is the raw material; DIP adds the ownership rule — the abstraction belongs to the code that *uses* it and is shaped by that code's needs, not by whatever the implementation happens to expose.
- **Open/Closed** is what inversion buys at the wiring level: because the policy sees only the abstraction, new implementations plug in at the composition root without editing policy source — DIP supplies the seam OCP extends through.
- **Coupling and Cohesion** frames the payoff: DIP is the main lever for converting a hard compile-time coupling to a volatile module into a loose coupling to a stable contract — and for judging which dependencies are stable enough to leave concrete.
- **Interfaces and Abstract Classes** cover the mechanics of the contract itself; keeping the inverted interface small and consumer-shaped is **Interface Segregation** applied at the inversion boundary.
