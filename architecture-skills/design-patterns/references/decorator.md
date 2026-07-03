# Decorator

**Category:** Structural

## Intent

Attach additional responsibilities to an individual object dynamically by wrapping it in another object with the same interface — a flexible alternative to subclassing for extending behavior.

## Problem

- Optional features combine freely: a coffee can have milk, mocha, and whipped cream in any combination, and subclassing every combination explodes (`EspressoWithMilkAndMocha`, ...).
- Behavior must be added or removed at runtime, per object — not per class at compile time.
- Inheritance would extend *every* instance of a class when only some instances need the extra behavior.

## Structure

- **Component** — the common interface (`Beverage.description()`, `Beverage.cost()`).
- **Concrete component** — the plain object being decorated (`Espresso`).
- **Decorator** — implements the component interface and holds a wrapped component; forwards calls, adding its own behavior before or after (`AddOn`).
- **Concrete decorators** — `Milk`, `Mocha`, `WhippedCream`; each adds one responsibility, and they stack in any order.

## When to Use

- Independent optional features that combine, where subclassing would multiply classes.
- Adding behavior to individual objects at runtime without affecting the rest.
- Extending a class that is closed to inheritance (`final`/sealed) but open through its interface.
- Layered I/O and middleware: buffering, compression, logging, or auth wrapped around a core handler.

## When Not to Use

- One fixed extension — a field or a single subclass is simpler than a wrapper stack.
- Client code relies on the concrete identity of the object (`instanceof`, reference equality); a decorator is a different object and breaks those checks.
- Behavior that must inspect, reorder, or remove layers of the stack dynamically; peeling decorators off is awkward.

## Trade-offs

- **Pros:** feature combinations compose at runtime instead of multiplying subclasses; each decorator has one small responsibility; the core component stays simple.
- **Cons:** many small look-alike objects make debugging harder; deep stacks obscure where behavior comes from; identity-sensitive code breaks; wrapping order can matter in non-obvious ways.

## Language Notes

- **Python:** `@decorator` syntax is related but different — it wraps functions or classes once at definition time, while this pattern wraps object instances at runtime.
- **JavaScript / PHP:** higher-order functions and middleware chains (Express, PSR-15) are the everyday decorator; the TC39 `@decorator` proposal, like Python's, is definition-time.
- **Java:** `java.io` streams are the canonical example (`new BufferedInputStream(new FileInputStream(...))`).
- **C#:** `System.IO` stream wrappers (`BufferedStream`, `GZipStream`) play the same role.
- **Rust:** wrapper types over a generic inner value (`BufReader<R: Read>`, iterator adapters) are the idiom; generics compose statically, `Box<dyn Trait>` when stacks are assembled at runtime.
- **Go:** a struct embedding the wrapped interface promotes the methods you don't override; `http.Handler` middleware is decorators all the way down.
- **Swift:** protocol extensions add behavior to *all* conformers at compile time; wrap instances instead when only some objects need the extra behavior.
- **C:** emulated with function-pointer structs; each decorator holds a pointer to the beverage it wraps.

## Examples

- [examples/decorator/decorator.py](../examples/decorator/decorator.py)
- [examples/decorator/decorator.c](../examples/decorator/decorator.c)
- [examples/decorator/decorator.cpp](../examples/decorator/decorator.cpp)
- [examples/decorator/decorator.java](../examples/decorator/decorator.java)
- [examples/decorator/decorator.cs](../examples/decorator/decorator.cs)
- [examples/decorator/decorator.js](../examples/decorator/decorator.js)
- [examples/decorator/decorator.rs](../examples/decorator/decorator.rs)
- [examples/decorator/decorator.go](../examples/decorator/decorator.go)
- [examples/decorator/decorator.php](../examples/decorator/decorator.php)
- [examples/decorator/decorator.swift](../examples/decorator/decorator.swift)

## Related Patterns

- **Adapter** changes an object's interface; Decorator keeps it and adds behavior.
- **Composite** aggregates many children; a decorator is like a composite with exactly one child, adding responsibilities instead of aggregating results.
- **Proxy** has the same wrapper shape but controls access (lazy loading, permissions) rather than adding features.
- **Strategy** changes the guts of an object by swapping what is inside; Decorator changes the skin by wrapping the outside.
