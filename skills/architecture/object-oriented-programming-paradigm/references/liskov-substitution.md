# Liskov Substitution Principle

**Category:** SOLID Principles

## Intent

Any code written against a base type must keep working — unchanged and unsurprised — when handed any subtype. Subtyping is a promise about *behavior*, not just matching method signatures: a subtype may only ever be a drop-in replacement.

## Problem

- A function takes a `Rectangle`, sets its width and height, and computes the area — then someone passes a `Square` subclass whose setters keep the sides equal, and the function silently returns the wrong number. No compiler error, no exception; just a caller whose reasonable assumption was broken.
- An override throws `NotSupportedException`/`UnsupportedOperationException` for an operation the base type advertises (a "read-only collection" subtype whose `add` throws). Every caller of the base type now needs to know which concrete subtype it might be holding — which defeats the point of having the base type.
- Code starts sprouting `instanceof`/`is`/type-switch checks before calling inherited methods "just in case." That's the codebase routing around a hierarchy whose subtypes can't actually stand in for their base.

## Structure

LSP has no class diagram; its "roles" are the terms of the behavioral contract every subtype signs:

- **Preconditions may not be strengthened** — the subtype must accept every input the base type accepts. An override that rejects inputs the base allowed (narrower range, extra validation, new required state) breaks callers that were playing by the base's rules.
- **Postconditions may not be weakened** — the subtype must deliver everything the base promised. Returning less, doing less, leaving work undone, or throwing where the base guaranteed success all count as weakening.
- **Invariants must be preserved** — properties the base type maintains ("width and height vary independently", "count grows after add") must still hold after any subtype method runs, including inherited ones.
- **No surprise state changes (history rule)** — the subtype may not mutate in ways the base type ruled out; a mutable subtype of an immutable type breaks every caller that cached or shared the value.

## When to Use

- Always — LSP is not an opt-in design move but the criterion for whether a subtype relationship is legitimate at all. Apply it as a test whenever you write `extends`, `implements`, or a trait/protocol conformance.
- When deciding between inheritance and composition: ask "can this new type honor *every* promise the base makes, everywhere the base is used?" If not, it's not a subtype — wrap or compose instead.
- When reviewing an override: if it strengthens a precondition, weakens a postcondition, throws something new, or stubs a method out, the hierarchy is wrong even though the code compiles.
- When writing an interface/trait: state the contract (allowed inputs, guaranteed outputs, error behavior) in its docs, because that contract — not the signatures — is what implementations must satisfy.

## When Not to Use

- Don't force an is-a hierarchy just because two types share vocabulary. A square *is* a rectangle in geometry, but a *mutable* `Square` is not a *mutable* `Rectangle` — real-world taxonomy is not a substitutability proof.
- Don't "fix" a violation by adding type checks in callers (`if (shape instanceof Square) ...`); that trades one violation for a shotgun-surgery problem. Fix the hierarchy instead: split the types, or make them immutable.
- Don't satisfy LSP by watering the base contract down to nothing ("any method may throw anything") — a contract too weak to rely on makes the base type useless. If implementations can't share a meaningful contract, they need narrower interfaces — see [Interface Segregation](interface-segregation.md).

## Trade-offs

- **Pros:** callers can be reasoned about from the base type alone; polymorphism stays safe without defensive type checks; hierarchies stay honest (fewer stub overrides and `NotSupported` landmines); test suites written against the base contract verify every conforming implementation for free.
- **Cons:** honoring it often means *less* inheritance — separate types, wrapper composition, or immutability where a subclass felt natural; behavioral contracts mostly live in documentation and tests, since no mainstream compiler checks pre/postconditions; splitting a false hierarchy multiplies types and can duplicate a little code.

## Language Notes

- **Java / C#:** the classic home of the violation: standard libraries ship it (`java.util.Arrays.asList` returns a `List` whose `add` throws; `Array.IList.Add` throws `NotSupportedException`). Compilers enforce signature variance (covariant returns; Java also caps checked exceptions in overrides) but nothing behavioral. `sealed` hierarchies limit who can sign the contract.
- **C++:** same rules for `virtual` overrides, plus a C++-specific trap: passing derived objects *by value* slices them, so substitution requires pointer/reference. `final` and `override` keep hierarchies deliberate.
- **Python / JavaScript / PHP:** duck typing means there is often no declared base type — the "contract" is whatever callers assume — so violations surface only as wrong answers or runtime errors in production. Python's `abc`/`typing.Protocol`, TypeScript, and PHP's interfaces (with enforced contravariant parameters / covariant returns since PHP 7.4) restore compile-or-import-time signature checks, but behavior still rides on docs and tests.
- **Rust / Go:** no subclassing exists, but LSP applies with full force to trait and interface *implementations*: every `impl`/method-set signs the contract in the trait's or interface's documentation (`io.Reader`'s doc comment is a behavioral contract; violating it breaks every consumer). Go's implicit interface satisfaction makes accidental "compiles but lies" implementations especially easy.
- **Swift:** applies to both class overrides and protocol conformances; the "protocols + value types" idiom sidesteps the mutable-subtype traps (a `struct` copy can't surprise its sharer), and `final` closes classes not designed for substitution.
- **C:** no language subtyping — substitution happens through hand-rolled vtables (structs of function pointers), so the contract is purely conventional and *nothing* is checked. Discipline about what each function pointer must accept and guarantee is all there is.

## Examples

- [examples/liskov-substitution/liskov-substitution.py](../examples/liskov-substitution/liskov-substitution.py)
- [examples/liskov-substitution/liskov-substitution.cpp](../examples/liskov-substitution/liskov-substitution.cpp)
- [examples/liskov-substitution/liskov-substitution.java](../examples/liskov-substitution/liskov-substitution.java)
- [examples/liskov-substitution/liskov-substitution.cs](../examples/liskov-substitution/liskov-substitution.cs)
- [examples/liskov-substitution/liskov-substitution.js](../examples/liskov-substitution/liskov-substitution.js)
- [examples/liskov-substitution/liskov-substitution.php](../examples/liskov-substitution/liskov-substitution.php)
- [examples/liskov-substitution/liskov-substitution.swift](../examples/liskov-substitution/liskov-substitution.swift)

## Related Concepts

- **[Inheritance](inheritance.md)** — LSP is the litmus test for it: `extends` creates a subtype claim, and a subclass that can't honor the base's contract everywhere shouldn't be a subclass.
- **[Interface Segregation](interface-segregation.md)** — many LSP violations are really fat interfaces in disguise: a `NotSupported`-throwing override means the type was forced to promise more than it can deliver; splitting the interface lets each type sign only contracts it can keep.
- **[Composition over Inheritance](composition-over-inheritance.md)** — the standard escape hatch when substitution fails: a type that can't be a subtype can still *hold* the other type, or both can sit as siblings behind a narrower shared interface.
- **[Polymorphism](polymorphism.md)** — what LSP protects: dynamic dispatch is only useful if every implementation behind the base type behaves; substitutability is the precondition that makes polymorphic call sites trustworthy.
