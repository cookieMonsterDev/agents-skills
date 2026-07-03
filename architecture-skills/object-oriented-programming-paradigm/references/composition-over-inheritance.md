# Composition over Inheritance

**Category:** Object Relationships

## Intent

Build an object's behavior by assembling smaller collaborating parts (has-a) instead of extending a class hierarchy (is-a), so that behaviors can be mixed, swapped, and tested independently without minting a new subclass for every combination.

## Problem

- Two independent axes of variation meet in one hierarchy: `WalkingLaserRobot`, `FlyingLaserRobot`, `WalkingDrillRobot`, `FlyingDrillRobot`... every new movement mode or weapon multiplies the subclass count (n movements × m weapons = n×m classes), and most of them are copy-paste shells.
- A subclass inherits everything from its parent whether it wants it or not — the classic rubber `Duck` that inherits `fly()` and has to override it to throw — because the base class baked in behavior that not all children share.
- Behavior needs to change at runtime (a robot gets a rotor upgrade mid-mission), but an object's class — and therefore its inherited behavior — is fixed at construction.
- A deep hierarchy couples every subclass to base-class internals; a "small" change to the base ripples through descendants you've never read (the fragile base class problem).

## Structure

- **Component interfaces** — one small contract per axis of variation (`MoveBehavior`, `AttackBehavior`); each describes a capability, not a kind of thing.
- **Concrete components** — self-contained implementations of one capability (`Wheels`, `Rotors`, `Laser`); independently testable, no knowledge of their host.
- **Composite (host) object** — holds references to its components and **delegates** to them; its public methods forward to the parts. New combinations are wiring, not new classes, and setters allow swapping parts at runtime.

## When to Use

- You catch yourself naming subclasses by concatenating features (`FlyingSwimmingDuck`) — that's two or more variation axes fighting over one hierarchy; give each axis its own component.
- Subclasses override inherited methods to disable them ("this bird can't fly") — the base contract is wrong for some children, so the behavior belongs in a part, not the parent.
- Behavior must change per-instance or at runtime, not per-class at compile time.
- You want to unit-test a behavior without instantiating the whole host object.

## When Not to Use

- A true, stable is-a relationship with a small and unchanging base contract — `ArgumentError` extending `Error`, a `Rectangle` node in a fixed scene-graph API. Inheritance is the simpler, honest model here; don't add delegation layers to avoid a perfectly good `extends`.
- Frameworks that are designed around subclassing (template-method-style base classes, abstract test cases): fighting the framework costs more than the hierarchy does.
- One axis of variation with two or three variants that never change — a plain conditional or a single small hierarchy beats a component system nobody will ever reconfigure.
- If what varies is a whole interchangeable algorithm, or you're stacking optional behaviors around a core, you're in Strategy / Decorator territory (design-patterns skill) — same principle, more specific shapes.

## Trade-offs

- **Pros:** combinations grow additively (n + m components) instead of multiplicatively (n × m subclasses); parts are swappable at runtime and testable in isolation; no fragile-base-class coupling — hosts depend on small interfaces, not superclass internals; each part gets a single responsibility.
- **Cons:** delegation boilerplate — the host hand-writes forwarding methods that inheritance would have given for free; behavior is spread across more objects, so "where does this actually happen?" takes one more hop; wiring components (who builds and injects them?) becomes a design question of its own; overdone, it produces bags of parts with no coherent identity.

## Language Notes

- **Rust:** enforced by design — there is no implementation inheritance at all. Structs hold other structs and `Box<dyn Trait>` fields; traits (with default methods) are the only behavior-sharing mechanism. The question "composition or inheritance?" simply doesn't come up.
- **Go:** also no inheritance by design. Struct embedding *is* composition with automatic forwarding: an embedded type's methods are promoted to the outer struct, giving reuse without an is-a relationship (no polymorphic assignment to the embedded type's "supertype" beyond interfaces it satisfies). Interface fields cover the swappable-part case.
- **Java:** the language that made the advice famous (Effective Java, Item 18). Delegation boilerplate is the main cost — one forwarding method per exposed operation; `default` methods on interfaces recover some mixin-style reuse without a base class. Prefer small interfaces + `final` component classes.
- **C#:** same shape as Java; default interface methods (C# 8+) and extension members reduce forwarding ceremony, and properties make injected components pleasant to expose. `sealed` components keep the parts honest.
- **Python:** duck typing means components need no formal interface; `Protocol` adds static checking if wanted. `__getattr__` can auto-forward to a part, eliminating delegation boilerplate — but use it sparingly, explicit forwarding reads better. Multiple inheritance/mixins are the traditional alternative; composition avoids their MRO surprises.
- **JavaScript / TypeScript:** object literals and closures make components nearly free; `Object.assign`-style mixins exist but plain "object holding behavior objects" is clearer. Class syntax supports only single inheritance, which pushes multi-axis variation toward composition anyway.
- **PHP:** traits provide compiler-assisted mixins (horizontal reuse), but they still copy code into the class; constructor-promoted readonly properties make injected components concise, and that's the idiomatic modern form.
- **Swift:** protocol-oriented programming is this principle with language support — protocols + protocol extensions provide shared behavior, and structs (which cannot inherit) compose parts. Class inheritance exists but is reserved for reference-semantics frameworks (UIKit-style).
- **C++:** rich in both directions — public inheritance for is-a, but member objects plus `std::unique_ptr<Interface>` for parts is the default advice; private inheritance and CRTP are niche middle grounds. Prefer members unless you need to override a virtual.
- **C:** no inheritance to overuse; structs containing structs and function pointers are composition by necessity. A component is a struct of function pointers plus a state pointer — assembling them into a host struct is exactly this concept, hand-rolled.

## Examples

- [examples/composition-over-inheritance/composition-over-inheritance.py](../examples/composition-over-inheritance/composition-over-inheritance.py)
- [examples/composition-over-inheritance/composition-over-inheritance.cpp](../examples/composition-over-inheritance/composition-over-inheritance.cpp)
- [examples/composition-over-inheritance/composition-over-inheritance.java](../examples/composition-over-inheritance/composition-over-inheritance.java)
- [examples/composition-over-inheritance/composition-over-inheritance.cs](../examples/composition-over-inheritance/composition-over-inheritance.cs)
- [examples/composition-over-inheritance/composition-over-inheritance.js](../examples/composition-over-inheritance/composition-over-inheritance.js)
- [examples/composition-over-inheritance/composition-over-inheritance.php](../examples/composition-over-inheritance/composition-over-inheritance.php)
- [examples/composition-over-inheritance/composition-over-inheritance.swift](../examples/composition-over-inheritance/composition-over-inheritance.swift)

## Related Concepts

- **[Inheritance](inheritance.md)** is the alternative this principle argues against overusing — reach for it only when the relationship is genuinely is-a with a stable base contract, not to share code between things that merely overlap.
- **[Interfaces and Abstract Classes](interfaces-and-abstract-classes.md)** supply the component contracts: composition swaps parts safely only because the host depends on a small interface rather than a concrete class.
- **[Single Responsibility](single-responsibility.md)** is what each extracted component ends up with — one axis of variation per part is SRP applied to behavior.
- **[Coupling and Cohesion](coupling-and-cohesion.md)** names the payoff: delegation to interfaces gives looser coupling than inheriting a base class's internals, at the cost of behavior spread across more (individually cohesive) objects.
