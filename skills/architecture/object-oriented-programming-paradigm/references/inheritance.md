# Inheritance

**Category:** The Four Pillars

## Intent

Derive a specialized class from a general base so the subclass inherits the base's interface and behavior, overriding only what genuinely differs — letting clients work with the whole family through the base type.

## Problem

- Several types share most of their fields and behavior (an hourly worker and a salaried worker both have a name, an ID, a payslip), and the copies have started to drift apart bug by bug.
- Code that should treat a family uniformly is full of `if (kind == MANAGER)` type switches, and every new kind means hunting down all of them.
- A variant needs to _adjust_ one step of shared behavior (add a bonus on top of the standard pay rule) without duplicating everything around that step.

## Structure

- **Base class (superclass)** — owns the common state and behavior; marks the methods subclasses may override (implicitly in Python/JS, `virtual` in C++/C#, non-`final` in Java).
- **Subclass** — declares the is-a relationship, inherits everything it doesn't mention, and **overrides** selected methods. An override can _extend_ the base behavior by calling the base implementation (`super()`, `base.`, `parent::`, `ClassName::method`) or _replace_ it outright.
- **Client** — holds references typed as the base class; dynamic dispatch routes each call to the most-derived override at runtime.

## When to Use

- The relationship is genuinely **is-a**: every subclass instance can stand in anywhere the base is expected, honoring the base's contract (see Liskov Substitution).
- The family shares real behavior with a few well-defined variation points — the subclass overrides two methods, not twelve.
- A framework hands you a base class with hook methods and subclassing is the designated extension point.

## When Not to Use

- **Code reuse without is-a.** Inheriting `Stack` from `ArrayList` gets you `insert(0, …)` for free — and a broken stack. If the honest phrasing is "has-a" or "uses-a", hold a field instead (see Composition over Inheritance).
- The subclass has to stub out, forbid, or weaken inherited behavior (`Penguin.fly()` throws). That is a Liskov violation announcing the hierarchy is wrong.
- Variation runs along **multiple independent axes** (pay scheme × contract type × region): subclassing one axis multiplies classes; compose the axes as collaborators instead.
- **Deep hierarchies rot.** Each level bakes assumptions into the ones below; behavior for one call ends up smeared across five files (the yo-yo problem); a change to the base risks every descendant (the fragile-base-class problem). Prefer hierarchies one or two levels deep, and keep them shallow on purpose.
- **Single vs multiple inheritance:** most languages here allow one base class, so inheriting spends a slot you can't get back; languages that allow several (Python, C++) add diamond ambiguity — who wins when two bases define the same method? Use multiple inheritance sparingly (mixins with no state, or C++ interface-style pure-virtual bases).

## Trade-offs

- **Pros:** removes duplication across a family; clients program against the base type and new subclasses slot in without client changes; overrides can extend behavior surgically via the base-call; the language enforces the shared interface.
- **Cons:** the strongest coupling OO offers — the subclass sees and depends on the base's internals; base changes ripple to every descendant; overridden behavior is harder to trace than a plain call; hierarchies are rigid at runtime (an object can't change its class), unlike composed collaborators which can be swapped.

## Language Notes

- **Python:** multiple inheritance is allowed; `super()` follows the class's **MRO** (method resolution order, C3 linearization), which is what makes cooperative mixins work — always call `super().__init__()` in `__init__`. No `final` enforcement (only `typing.final` hints).
- **C++:** overridable methods must be declared `virtual`; mark overrides `override` and lock classes/methods with `final`. A base class deleted through a base pointer needs a **virtual destructor** or the derived part leaks. Multiple inheritance exists; `virtual` bases resolve the diamond.
- **Java:** single class inheritance; call up with `super.method()`. `final` forbids overriding/extension; `sealed` (Java 17+) whitelists the permitted subclasses. Every non-`final` method is virtual by default.
- **C#:** single class inheritance; methods are non-virtual **by default** — opt in with `virtual` and override with `override` (hiding with `new` is almost always a mistake). `sealed` closes a class or an override; call up with `base.Method()`.
- **JavaScript / TypeScript:** `class`/`extends`/`super` is syntax over the **prototype chain** — inheritance is delegation between live objects, and methods are "virtual" by nature. TypeScript adds `abstract` and visibility, but no `final` on classes intended for extension.
- **PHP:** single class inheritance; call up with `parent::method()`. `final` seals classes and methods; `abstract` forces overrides. Traits provide horizontal reuse where multiple inheritance would otherwise be reached for.
- **Swift:** only `class` supports inheritance (structs/enums don't); overrides require the `override` keyword and `final` shuts it off. The community default is protocols + structs first, class inheritance only when reference semantics and an open hierarchy are genuinely needed.
- **Rust:** **no implementation inheritance at all** — there is no way for one struct to extend another. The nearest idiom is a **trait with default method bodies**: implementers "inherit" the defaults and override per method; there is no `super` call, so shared logic lives in the default body or a free helper. Cross-type reuse of fields is done with composition.
- **Go:** **no inheritance.** Struct **embedding** promotes the inner type's fields and methods, but it is composition with automatic forwarding, **not subtyping**: a promoted method still sees only the inner struct (no dynamic dispatch back to the outer type), and the outer type isn't assignable where the inner is expected. Polymorphism comes from interfaces instead.
- **C:** no language support; the classic emulation is **struct-prefix layout** — the "derived" struct's first member is the base struct, so a `Derived*` can be viewed as a `Base*` — plus **function pointers** in the base that the derived initializer overwrites (a hand-rolled vtable). Overrides call the base's function directly to extend it.

## Examples

- [examples/inheritance/inheritance.py](../examples/inheritance/inheritance.py)
- [examples/inheritance/inheritance.cpp](../examples/inheritance/inheritance.cpp)
- [examples/inheritance/inheritance.java](../examples/inheritance/inheritance.java)
- [examples/inheritance/inheritance.cs](../examples/inheritance/inheritance.cs)
- [examples/inheritance/inheritance.js](../examples/inheritance/inheritance.js)
- [examples/inheritance/inheritance.php](../examples/inheritance/inheritance.php)
- [examples/inheritance/inheritance.swift](../examples/inheritance/inheritance.swift)

## Related Concepts

- **[Composition over Inheritance](composition-over-inheritance.md)** — the corrective to inheritance's most common misuse: when the relationship is has-a or the variation is multi-axis, hold a collaborator instead of extending a base.
- **[Liskov Substitution](liskov-substitution.md)** — the litmus test for whether a hierarchy is legitimate: a subclass that can't honor the base's contract everywhere the base is used shouldn't be a subclass.
- **[Polymorphism](polymorphism.md)** — the payoff of inheritance: dynamic dispatch through the base type is why overriding works; interfaces deliver the same payoff without sharing implementation.
- **[Interfaces and Abstract Classes](interfaces-and-abstract-classes.md)** — the spectrum between "contract only" and "contract plus inherited behavior"; an abstract base is inheritance with the instantiation hole made explicit.
