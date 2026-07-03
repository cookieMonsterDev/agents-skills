# Encapsulation

**Category:** The Four Pillars

## Intent

Hide an object's internal state behind a controlled interface of methods so that every mutation goes through code that can enforce the object's invariants — no caller can put the object into an invalid state without the object's cooperation.

## Problem

- A `balance` field is public, so any code anywhere can write `account.balance = -500`. The "never negative" rule lives only in developers' heads, and every bug report starts with "how did the balance go negative?"
- A validation rule is duplicated at every call site that touches the data (`if amount > 0 and amount <= balance` copy-pasted around the codebase); one missed copy breaks the invariant.
- Changing the internal representation (storing cents instead of a float, adding a transaction log) breaks every caller, because callers reach directly into the fields instead of going through an interface.

## Structure

- **Private state** — the raw fields (balance, temperature setpoint); invisible or at least off-limits to outside code.
- **Public interface** — the methods (`deposit`, `withdraw`) that are the *only* way to change the state; each method validates before mutating, so the invariant holds after every call.
- **Invariant** — the rule the class promises is always true between method calls (balance ≥ 0, setpoint within range); the reason encapsulation exists at all.
- **Read-only accessors** — getters/properties that expose *values* for inspection without exposing the *storage* for mutation.

The broken version has the same data but no boundary: public fields (or a blanket setter per field, which is the same thing with extra steps), invariants enforced nowhere, every caller trusted to know and repeat the rules.

## When to Use

- The data has rules — any field where "this must never be X" is true needs its writes funneled through a method that checks.
- Two or more fields must change together (balance and transaction log, start and end of a range); only a method can make the update atomic and consistent.
- You expect the representation to change — callers coupled to a method signature survive a storage change; callers coupled to fields do not.
- You find yourself validating the same field at multiple call sites: that validation belongs inside the type, once.

## When Not to Use

- Plain data carriers with no invariants (a point, a DTO, a config record) — getters/setters around rule-free fields are ceremony; use a public struct/record/dataclass and be done.
- Don't write a getter *and* a setter for every private field by reflex — a field with an unchecked public setter is effectively public, and the encapsulation is theater. Expose the operations the object supports, not the fields it happens to store.
- Inside a small private scope (a function-local helper struct) where all mutation sites are visible at once, the boundary buys little.

## Trade-offs

- **Pros:** invariants are enforced in one place and cannot be bypassed; representation can change without breaking callers; invalid states are caught at the mutation site, not diagnosed later from corrupted data; the public interface documents what the object can *do* rather than what it *stores*.
- **Cons:** more code than raw fields (methods, accessors, error paths); over-applied to rule-free data it adds noise; a leaky interface (returning internal mutable collections, blanket setters) gives the ceremony without the protection.

## Language Notes

- **Python:** privacy is convention — `_balance` means "don't touch", and `__balance` triggers name mangling (`_ClassName__balance`), which deters but does not prevent access. `@property` exposes read access (and validated write access via a setter) behind attribute syntax, so a raw attribute can be upgraded to a checked property without changing callers.
- **C:** no access modifiers. True encapsulation is the *opaque pointer* idiom: the header declares `typedef struct Account Account;` plus functions, the struct body lives only in the `.c` file, so callers physically cannot touch fields. In a single file it's convention plus discipline: mutate only through the functions.
- **C++:** `private`/`protected`/`public` sections enforce the boundary at compile time; constructors establish the invariant, methods maintain it. `friend` punches deliberate holes. The pimpl idiom is C++'s opaque pointer for hiding even the field *declarations*.
- **Java:** `private` fields plus methods is the norm; beware the reflexive getter/setter pair, which reintroduces public fields with extra syntax. Records (`record`) are for the no-invariant data-carrier case.
- **C#:** properties are the idiom — `public decimal Balance { get; private set; }` gives public read, class-only write, and a place to add validation later without breaking callers. `init` setters and records cover immutable data carriers.
- **PHP:** `private`/`protected`/`public` on properties and methods; PHP 8.1 `readonly` properties and 8.4 property hooks (`get`/`set` blocks) give C#-style validated properties without hand-written getters.
- **Swift:** `private`/`fileprivate`/`internal`/`public` plus `private(set) var balance` for public-read/private-write in one line; `willSet`/`didSet` observers and computed properties handle validation on assignment.
- **JavaScript / TypeScript:** `#balance` private class fields are enforced by the engine (access from outside is a syntax error); before class fields, closures did the same job — variables captured by the returned methods are unreachable from outside. TypeScript's `private` keyword is compile-time only.
- **Rust:** privacy is per *module*, not per type: fields are private outside the defining module by default, `pub fn` methods are the doorway. Code in the same module can still touch fields, so put the type in its own module. Errors return `Result` instead of throwing.
- **Go:** export is by capitalization and scoped to the *package*: field `balance` is invisible outside the package, method `Withdraw` is visible. A constructor function (`NewAccount`) establishes the invariant since there are no real constructors. Same-package code can bypass the methods, so give the type its own package when it matters.

## Examples

- [examples/encapsulation/encapsulation.py](../examples/encapsulation/encapsulation.py)
- [examples/encapsulation/encapsulation.cpp](../examples/encapsulation/encapsulation.cpp)
- [examples/encapsulation/encapsulation.java](../examples/encapsulation/encapsulation.java)
- [examples/encapsulation/encapsulation.cs](../examples/encapsulation/encapsulation.cs)
- [examples/encapsulation/encapsulation.js](../examples/encapsulation/encapsulation.js)
- [examples/encapsulation/encapsulation.php](../examples/encapsulation/encapsulation.php)
- [examples/encapsulation/encapsulation.swift](../examples/encapsulation/encapsulation.swift)

## Related Concepts

- **Abstraction** hides *complexity* behind a simpler model of what the object does; encapsulation hides *state* behind a boundary that protects it. An abstraction is what the interface says; encapsulation is what the interface refuses to let you touch.
- **Classes and Objects** provide the unit that encapsulation protects: a class bundles the state and the only methods allowed to change it.
- **Law of Demeter** is encapsulation applied across object graphs — reaching through `a.getB().getC().setX()` leaks B's and C's internals just as a public field leaks A's.
- **Coupling and Cohesion** name the payoff: callers coupled to a small method interface instead of a field layout can survive representation changes; state plus the rules governing it in one class is high cohesion.
