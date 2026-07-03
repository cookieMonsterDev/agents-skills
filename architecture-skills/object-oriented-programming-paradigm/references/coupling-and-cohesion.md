# Coupling and Cohesion

**Category:** Design Qualities

## Intent

Build modules that are strongly related inside and weakly dependent on each other outside. **Cohesion** measures whether the pieces inside a module belong together; **coupling** measures how much one module must know about another to do its job. Good design maximizes the first and minimizes the second.

## Problem

- `OrderProcessor` constructs `new MySqlOrderRepository(host, password)`, embeds raw SQL, and reads column names from `Order` fields directly. Switching to Postgres means editing the processor, the tests, and every other class that copied the same pattern — one storage decision fans out across the codebase.
- A `utils` package exports `formatDate`, `sendEmail`, `calculateTax`, and `parseCsv` — callers import the whole grab bag for one function, and a tax-rule change recompiles modules that only format dates.
- Two teams share a "common" DTO that exposes every field both domains need; when team A adds a field for their feature, team B's service breaks because it serializes the whole object and the new field violates an invariant team B never knew about.
- The opposite failure is just as costly: a module so fragmented that tracing one use case hops through twelve one-method classes — low coupling achieved by dissolving cohesion, so nobody can see the whole story in one place.

## Structure

Think of each module (class, package, file) as a box:

- **High cohesion (inside the box)** — everything in the module serves one clear purpose. An `OrderTotalCalculator` that knows tax rules and line-item math belongs together; tax logic scattered across formatters and repositories does not.
- **Loose coupling (between boxes)** — modules interact through narrow, stable seams: a method call, a small interface, a message — not through each other's fields, SQL strings, or config keys.
- **Tight coupling (the smell)** — module A reaches into module B's internals (fields, SQL schema, file layout, private helpers). A change in B forces a coordinated edit in A, and often in C, D, and E that made the same reach.

```
Tight coupling                         Loose coupling

  OrderProcessor                         OrderProcessor
        |                                      |
        | new MySqlRepo()                      | OrderRepository (interface)
        | "SELECT * FROM orders..."            v
        v                                PostgresRepo / InMemoryRepo
  MySqlOrderRepository
  (schema, connection, SQL)
```

Coupling has *kinds*: content coupling (reaching into internals) is worst; common coupling (shared global state) is fragile; data coupling (passing plain values through a narrow API) is healthy. Cohesion has *levels*: functional cohesion (one job) is the goal; coincidental cohesion (unrelated things dumped together) is the floor.

## When to Use

These qualities are not a technique you "apply" at one moment — they are the lens for every structural decision:

- A change in one module keeps forcing edits in others that have no logical reason to care — trace the dependency; the seam is too wide or too concrete.
- A module's name needs "And" or "Utils" to describe its contents, or its import list spans unrelated layers (database, HTTP, templating, domain math) — cohesion is low.
- Tests for one unit require constructing or mocking distant modules (a live database to test arithmetic, a mail server to test a price rule) — coupling has leaked inward.
- You are drawing a boundary (new package, new service, new interface) and need a rule of thumb: things that change together and serve one purpose belong inside; things that change on different schedules belong on opposite sides of a narrow contract.

## When Not to Use

- **Don't decouple for its own sake.** Depending directly on a stable, ubiquitous type (the standard library, a value object, a pure function) is data coupling, not a problem — inventing `IStringFormatter` around `str.join` adds indirection with no seam to protect. **Dependency Inversion** covers when abstraction is worth the cost.
- **Don't chase zero coupling inside a cohesive unit.** Methods on the same class *should* know each other's fields — that is functional cohesion, not tight coupling. The boundary is the class (or package) wall, not every method pair.
- **Plain data can be coupled by shape without harm.** Passing a `Point` struct or a config record through several layers is fine when it carries no behavior and no invariant — the coupling is to data, not to decisions. See **Encapsulation** and **Law of Demeter** for when the payload is an object with rules, not a record.
- **Micro-modules are not loose coupling.** Splitting one coherent algorithm into fifteen one-line classes lowers cohesion and can *increase* coupling through wiring — more boxes, same entanglement, harder to read.

## Trade-offs

- **Pros (loose coupling, high cohesion):** changes stay local — swap storage, swap vendor, refactor internals without a repo-wide hunt; modules are testable in isolation behind their seams; boundaries match team and deployment boundaries; readers find related code in one place.
- **Cons:** seams cost ceremony — interfaces, injection, adapter layers, and indirection at the composition root; a wrongly drawn boundary splits code that always changes together, so every feature now touches three files; over-abstraction at every call site produces the "enterprise lasagna" where tracing behavior means opening twelve interfaces; judgment matters more than any metric.

## Language Notes

- **Java / C#:** coupling is visible in `import`/`using` lists and constructor signatures — a class importing twelve packages from different layers is a coupling map. Packages/namespaces are the natural cohesion unit; `internal`/`package-private` narrows seams. DI containers manage loose coupling at scale but are not required for it.
- **Python / JavaScript / PHP:** the module/file is the box — a 3,000-line `helpers.py` or `utils.js` is low cohesion regardless of class design. Loose coupling often means separate modules and explicit constructor parameters, not necessarily interfaces (duck typing is already loose if callers name no concrete type).
- **Go:** packages are the primary cohesion boundary; the compiler forbids import cycles, which forces loose coupling physically. Small consumer-declared interfaces keep cross-package coupling minimal — but exporting every struct field across packages is tight content coupling by another name.
- **Rust:** modules and crates are cohesion units; `pub` vs private is the seam. Generics and traits decouple without runtime cost; `pub` fields on behavior-bearing types are the Rust equivalent of public mutable state — keep internals private, expose narrow methods.
- **C:** translation units (`.c`/`.h` pairs) are the modules. Content coupling is `#include`-ing another module's internal header or reaching through its structs; loose coupling is an opaque pointer and a small function API in the header. Low cohesion is the god `.c` file that mixes I/O, parsing, and business rules.
- **C++:** headers are coupling multipliers — including a wide header pulls every client into every change. Pimpl/idoms and small abstract interfaces in headers reduce compile-time coupling; a `.cpp` that includes `<iostream>`, a DB client, and domain headers is the cohesion smell in one file.
- **Swift:** modules and `internal`/`private` access control define seams; protocols decouple like interfaces. Extensions can raise cohesion (grouping one type's concerns) or lower it (sprinkling unrelated helpers on a type) depending on what they contain.

## Examples

- [examples/coupling-and-cohesion/coupling-and-cohesion.py](../examples/coupling-and-cohesion/coupling-and-cohesion.py)
- [examples/coupling-and-cohesion/coupling-and-cohesion.cpp](../examples/coupling-and-cohesion/coupling-and-cohesion.cpp)
- [examples/coupling-and-cohesion/coupling-and-cohesion.java](../examples/coupling-and-cohesion/coupling-and-cohesion.java)
- [examples/coupling-and-cohesion/coupling-and-cohesion.cs](../examples/coupling-and-cohesion/coupling-and-cohesion.cs)
- [examples/coupling-and-cohesion/coupling-and-cohesion.js](../examples/coupling-and-cohesion/coupling-and-cohesion.js)
- [examples/coupling-and-cohesion/coupling-and-cohesion.php](../examples/coupling-and-cohesion/coupling-and-cohesion.php)
- [examples/coupling-and-cohesion/coupling-and-cohesion.swift](../examples/coupling-and-cohesion/coupling-and-cohesion.swift)

## Related Concepts

- **[Encapsulation](encapsulation.md)** — hiding a module's internals behind a narrow public surface is the main mechanism for loosening coupling; without encapsulation, every caller is content-coupled to every field.
- **[Law of Demeter](law-of-demeter.md)** — a concrete coupling rule: don't reach past your immediate collaborators into their internals. Violations are a particular kind of tight content coupling across an object graph.
- **[Dependency Inversion](dependency-inversion.md)** — the primary technique for converting a tight compile-time dependency on a volatile detail into a loose dependency on a stable abstraction owned by the consumer.
- **[Single Responsibility](single-responsibility.md)** — splitting a class by actor raises cohesion (related reasons to change stay together) and lowers coupling (unrelated actors stop sharing a file).
- **[Interface Segregation](interface-segregation.md)** — a fat interface is a wide coupling surface; segregating it lets each client couple only to the methods it actually uses.
- **[Composition over Inheritance](composition-over-inheritance.md)** — inheritance couples subclasses to the parent's full surface and layout; composing small collaborators behind narrow interfaces typically yields looser coupling and higher cohesion per unit.
