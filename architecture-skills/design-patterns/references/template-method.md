# Template Method

**Category:** Behavioral

## Intent

Define the skeleton of an algorithm in one place and let subtypes redefine specific steps without changing the skeleton's structure. The invariant parts are written once; only the varying steps are open for override.

## Problem

- Several classes implement almost the same algorithm — same overall flow, different details — and the duplicated skeleton drifts out of sync when one copy is fixed.
- You want to guarantee that the ordering, iteration, or bookkeeping of an algorithm cannot be altered by variants, only the individual steps.
- A framework needs to call user code at defined points ("don't call us, we'll call you" — the Hollywood principle).

## Structure

- **Abstract class** — implements the template method (`generate()`), which fixes the step order and is typically `final`/non-virtual; declares the varying steps (`header()`, `row()`, `footer()`) as abstract.
- **Concrete classes** — implement the varying steps only; they never touch the skeleton.
- **Hooks** (optional) — steps with a default (often empty) body that subclasses *may* override, unlike abstract steps they *must*.

## When to Use

- Multiple variants share an invariant flow with a few differing steps (report generation, data pipelines, test lifecycles).
- You must enforce the skeleton: variants may fill in blanks but not reorder or skip stages.
- You are building a framework whose extension points are well-defined moments in a fixed process.

## When Not to Use

- The *whole* algorithm varies, not just steps — that is Strategy.
- The language favors composition: passing the steps as functions or a small steps-object is more flexible and testable than inheritance (see Language Notes). Prefer that unless you specifically need the enforced-skeleton guarantee of a sealed template.
- There is only one variant; a plain function with no extension points is simpler.

## Trade-offs

- **Pros:** removes duplicated skeletons, enforces the invariant flow, gives frameworks well-defined extension points, changes to the skeleton happen in exactly one place.
- **Cons:** built on inheritance, so variants are coupled to the base class and fixed at compile time; skeletons with many steps become rigid and hard to follow; the base class calling "down" into subclasses can surprise readers (and bites in constructors).

## Language Notes

- **Java / C# / PHP / C++:** the classic home of the pattern; mark the template method `final` / non-virtual (in C++, the NVI idiom: public non-virtual method calling private virtuals) so the skeleton truly cannot vary.
- **Python:** an `ABC` with `@abstractmethod` steps works, but composition or a higher-order function taking the steps as arguments is often preferred.
- **JavaScript:** no abstract classes; base methods that `throw` simulate them. A function taking a steps object is the more common idiom — the example shows both.
- **Rust:** no inheritance; a trait default method *is* the template, built on required methods (`Iterator`'s default methods over `next()` are exactly this).
- **Go:** no inheritance; the idiomatic form is a plain function taking an interface that supplies only the varying steps.
- **Swift:** protocol extensions provide the template as a default method over protocol requirements — no base class, works with structs. Passing closures is often preferred over any inheritance form.

## Examples

- [examples/template-method/template-method.py](../examples/template-method/template-method.py)
- [examples/template-method/template-method.c](../examples/template-method/template-method.c)
- [examples/template-method/template-method.cpp](../examples/template-method/template-method.cpp)
- [examples/template-method/template-method.java](../examples/template-method/template-method.java)
- [examples/template-method/template-method.cs](../examples/template-method/template-method.cs)
- [examples/template-method/template-method.js](../examples/template-method/template-method.js)
- [examples/template-method/template-method.rs](../examples/template-method/template-method.rs)
- [examples/template-method/template-method.go](../examples/template-method/template-method.go)
- [examples/template-method/template-method.php](../examples/template-method/template-method.php)
- [examples/template-method/template-method.swift](../examples/template-method/template-method.swift)

## Related Patterns

- **Strategy** swaps the entire algorithm via composition at runtime; Template Method varies steps via inheritance at compile time. Strategy is usually the more flexible default.
- **Factory Method** is a Template Method specialized to one step: object creation.
- **Hooks** in a template are the same idea as **Observer** notification points, but bound by inheritance rather than subscription.
