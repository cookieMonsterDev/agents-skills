# Object Relationships

**Category:** Object Relationships

## Intent

Name the three ways one object can refer to another — association (uses-a), aggregation (has-a), composition (owns-a) — so that ownership, lifetime, and dependency direction are deliberate design decisions instead of accidents of whichever reference was easiest to write.

## Problem

- A "container" object frees or closes things it merely borrowed — another owner is still using them — because nothing in the design said who owns what.
- Deleting or dissolving a whole leaves its internal parts alive and orphaned (cancelled orders still processing, sessions outliving their connection), because a part that should die with the whole was treated as an independent object.
- Two objects each think the other is "theirs": both cache, both mutate, both clean up, and the dependency arrows in the design point both ways for what should be a one-way uses-a relationship.

## Structure

- **Association (uses-a)** — the weakest link: an object *uses* another to do a job, typically receiving it as a method parameter or holding a non-owning reference. No lifetime coupling in either direction; a `Professor` uses the `Library`, and either can disappear without consulting the other. The dependency arrow points from user to used, and only that way.
- **Aggregation (has-a)** — a whole holds parts that were **created elsewhere**, can be **shared** with other wholes, and **outlive** the whole. A `Department` has `Professor`s on its roster, but professors exist independently and one professor can belong to two departments. Dissolving the department only shortens the roster.
- **Composition (owns-a)** — the strongest link: the whole **creates** its parts, is their **sole owner**, and the parts **die with it**. A `Department` composes its internal `Course` roster — a course of a dissolved department has no meaning, so it is never handed out for others to keep. Ownership is exclusive: a composed part has exactly one whole.

The dividing questions are always the same: *Who creates the part? Can it be shared? Does it survive the whole?* Association answers "someone else / n/a / yes", aggregation "someone else / yes / yes", composition "the whole / no / no".

## When to Use

- You are writing a destructor, `close()`, `dispose()`, or dissolve step and must decide what to tear down: composed parts yes, aggregated parts never — if that decision feels ambiguous, the relationship was never classified.
- The same object appears inside two containers (a professor in two departments, a product in two catalogs): that is aggregation by definition, and the design must not let either container destroy it.
- An object needs another only inside one operation — pass it as a parameter (association) instead of storing it as a field; the weakest relationship that works is the right one.
- Reviewing a diagram or module graph: labeling each edge as uses/has/owns exposes cycles and unclear ownership before they become double-free or leak bugs.

## When Not to Use

- Don't force every reference into a taxonomy debate — for short-lived local collaborators, "it's a parameter" is the whole answer; the distinction earns its keep only where lifetime and cleanup are at stake.
- Don't upgrade association to a stored field "for convenience": caching a reference you only need per-call creates hidden lifetime coupling and stale-object bugs. Keep it a parameter.
- Don't reach for composition when the part is conceptually shareable — hard-owning a `Logger` or `Config` inside every object duplicates state that should be aggregated or injected (see **Dependency Inversion**).
- If the question is "should I inherit or hold a field?", that is a different decision — see **Composition over Inheritance**.

## Trade-offs

- **Pros:** cleanup responsibility is unambiguous (no double-free, no leaks by hesitation); lifetime bugs become design-review findings instead of runtime surprises; the weakest-relationship rule keeps coupling low; diagrams with owns/has/uses edges communicate far more than plain arrows.
- **Cons:** the boundaries are genuinely fuzzy in garbage-collected languages, where all three compile to "a reference" and the discipline lives only in convention; over-classifying trivial links is ceremony; composition's exclusive ownership can force awkward APIs (returning copies or read-only views instead of the parts themselves).

## Language Notes

- **Rust:** the one language where this concept *is* the type system. An owned field (`Course` in a `Vec<Course>`) is composition — the part is dropped with the whole, enforced at compile time. A borrow (`&Library`, with lifetimes) is association — use without ownership, and the compiler rejects any attempt to outlive the lender. `Rc<T>`/`Arc<T>` is aggregation — shared ownership with the part living until its last holder drops. Choosing a relationship and writing the field type are the same act.
- **C:** no ownership in the type system, so the relationship is a documented discipline: a by-value struct member is composition (dies inside the whole's `destroy` function); a borrowed pointer member is aggregation (the whole must *never* free it); a pointer parameter is association. Comment which pointers are owning — the compiler won't say.
- **C++:** ownership is spelled in the member type: a by-value member or `std::unique_ptr` is composition (destructor cascades), `std::shared_ptr` is aggregation (part lives while any owner does), and a raw pointer or reference is association (non-owning by convention). Destructors make the lifetime difference directly observable.
- **Java / C#:** the GC erases the memory-level distinction — every field is just a reference. The relationships survive as conventions: composition means the whole constructs the part, never leaks it, and cancels it in `close()`/`Dispose()`; aggregation means the part arrives via constructor/setter and is left alone at teardown. C#'s `IDisposable` ownership rule ("dispose only what you created") is exactly the composition/aggregation line.
- **Python:** same convention-driven story as Java/C#; CPython's reference counting makes composed lifetime *observable* (a part referenced only by its whole is collected the moment the whole is), but rely on explicit lifecycle methods, not `__del__`, in real code.
- **JavaScript / TypeScript:** references all look alike; signal composition by creating parts inside the class and keeping the field private (`#courses`), aggregation by accepting the object from outside. TypeScript's `readonly` and visibility modifiers document intent but do not enforce lifetime.
- **PHP:** identical convention story; constructor promotion with `private` composed parts vs. injected aggregated collaborators makes the split readable at the constructor signature.
- **Go:** an embedded or by-value struct field is genuine composition of data (copied and destroyed with the whole); pointer fields and interface values are aggregation/association by convention. No destructors — encode the "part dies with whole" contract in an explicit `Close`/`Dissolve` method, as the standard library does.
- **Swift:** ARC makes the distinction semi-visible: a `let` reference held only by its whole behaves as composition (`deinit` fires when the whole goes), strong references shared across objects are aggregation, and `weak`/`unowned` references are the honest form of association because they add no lifetime coupling.

## Examples

- [examples/object-relationships/object-relationships.py](../examples/object-relationships/object-relationships.py)
- [examples/object-relationships/object-relationships.cpp](../examples/object-relationships/object-relationships.cpp)
- [examples/object-relationships/object-relationships.java](../examples/object-relationships/object-relationships.java)
- [examples/object-relationships/object-relationships.cs](../examples/object-relationships/object-relationships.cs)
- [examples/object-relationships/object-relationships.js](../examples/object-relationships/object-relationships.js)
- [examples/object-relationships/object-relationships.php](../examples/object-relationships/object-relationships.php)
- [examples/object-relationships/object-relationships.swift](../examples/object-relationships/object-relationships.swift)

## Related Concepts

- **Composition over Inheritance** answers a different question — *how to reuse behavior* (hold a part vs. subclass) — while this concept classifies the reference you end up holding; the two meet when the held part is composed vs. aggregated.
- **Coupling and Cohesion** gives the force behind the "weakest relationship that works" rule: association couples less than aggregation, aggregation less than composition, so each upgrade must buy something.
- **Dependency Inversion** governs *what type* the reference points at (an abstraction, not a concrete class); object relationships govern *who owns and outlives* whatever it points at — aggregated/associated collaborators are the natural injection points.
- **Encapsulation** is what keeps composition honest: a whole that leaks references to its composed parts has silently downgraded them to aggregation, because outsiders can now keep the parts alive.
