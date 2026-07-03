# Single Responsibility Principle

**Category:** SOLID Principles

## Intent

Give each class exactly one reason to change: one actor (a stakeholder or axis of change) whose requirements it serves. When different actors' concerns live in separate classes, a change requested by one actor cannot break behavior another actor depends on.

## Problem

- An `Invoice` class computes totals, formats itself for printing, and saves itself to the database. Finance changes the tax rule, and the layout team's carefully tuned print output breaks in the same commit — three departments queue changes on one file.
- Every feature touches the same "god class"; merge conflicts pile up there, its test file is enormous, and nobody dares refactor it because everything depends on it.
- You cannot reuse the calculation logic in a batch job without also dragging in the formatting code and a live database connection, so the batch job re-implements it — and the two copies drift.

## Structure

- **Domain object** — holds the data and the invariants intrinsic to it (an `Invoice` with its line items); it knows nothing about presentation or storage.
- **One collaborator per actor** — a `Calculator` for the finance rules, a `Formatter` for the presentation rules, a `Repository` for the persistence rules; each changes only when its actor's requirements change.
- **Composition root / caller** — wires the collaborators together and passes the domain object between them; the pieces stay independent because only the caller knows about all of them.

Note the definition: a "responsibility" is a *reason to change* — an actor whose requests would force an edit — not "the class does one thing." A class with ten methods all serving one actor honors SRP; a two-method class serving two actors violates it.

## When to Use

- Change requests from unrelated stakeholders (finance, UX, ops) keep landing in the same class — each stakeholder is an actor, and each actor deserves its own class.
- A class imports from several unrelated layers at once (database driver, HTML/templating, domain math) — the import list is a list of its reasons to change.
- You struggle to name a class without "And", "Manager", or "Processor", or its unit tests need a database just to check arithmetic.
- Git history shows the same file modified by most feature branches — a hotspot is usually a responsibility magnet.

## When Not to Use

- Don't over-split into anemic one-method classes: exploding an invoice into `InvoiceSubtotaler`, `InvoiceTaxAdder`, and `InvoiceRounder` serves no distinct actors — that's fragmentation, not SRP, and it just moves the complexity into the wiring.
- Don't separate speculatively. If formatting and calculation have always changed together for the same reason, splitting them "in case" adds indirection with no payoff; split when a second actor actually shows up (YAGNI).
- If the real problem is one class knowing too much about *other objects'* internals rather than serving too many actors, that is a coupling problem — see **Law of Demeter** and **Coupling and Cohesion** rather than slicing the class.

## Trade-offs

- **Pros:** changes are localized, so one actor's change can't break another's feature; each piece is testable in isolation (the calculator needs no database); smaller classes mean fewer merge conflicts; collaborators become reusable in new contexts (batch jobs, other UIs).
- **Cons:** more classes/files and more wiring code; behavior for one use case is spread across several units, so readers must follow the composition; drawing the actor boundaries wrongly means paired changes now span multiple files; taken too far it yields an anemic design where no class does anything meaningful.

## Language Notes

- **Python / JavaScript / PHP:** the module/file is a unit of responsibility too — a 2,000-line `utils.py` violates SRP just like a god class. Small responsibilities are often plain functions in separate modules rather than one-method classes.
- **Java / C#:** the classic home of the principle; the one-public-class-per-file convention makes responsibilities visible in the file tree. Beware "Manager"/"Service" classes that accrete every use case — split by actor, and let the DI container do the wiring at the composition root.
- **Go:** the unit is the package and the function, not the class. SRP shows up as small, focused packages (`invoice`, `render`, `storage`) and small interfaces declared by the consumer; a package that imports both `database/sql` and `html/template` is the god-class smell.
- **Rust:** modules and traits carry responsibilities; the borrow checker actively punishes god structs (two responsibilities needing `&mut self` on one struct collide), so splitting by concern is often forced before it's a design choice.
- **C:** no classes — the unit is the translation unit and the function. SRP means one `.c`/`.h` pair per concern (`invoice.c`, `format.c`, `store.c`) with the header as the seam; the single-file example simulates this with sections.
- **C++:** applies at class and header level; a header that pulls in `<iostream>`, a DB client, and domain math forces recompilation of every client when any one concern changes — physical coupling makes SRP violations expensive.
- **Swift:** extensions let you group one type's code by concern, but they don't fix mixed reasons to change — the extension still ships and recompiles with the type. Use separate types (often protocols + small structs) per actor.

## Examples

- [examples/single-responsibility/single-responsibility.py](../examples/single-responsibility/single-responsibility.py)
- [examples/single-responsibility/single-responsibility.cpp](../examples/single-responsibility/single-responsibility.cpp)
- [examples/single-responsibility/single-responsibility.java](../examples/single-responsibility/single-responsibility.java)
- [examples/single-responsibility/single-responsibility.cs](../examples/single-responsibility/single-responsibility.cs)
- [examples/single-responsibility/single-responsibility.js](../examples/single-responsibility/single-responsibility.js)
- [examples/single-responsibility/single-responsibility.php](../examples/single-responsibility/single-responsibility.php)
- [examples/single-responsibility/single-responsibility.swift](../examples/single-responsibility/single-responsibility.swift)

## Related Concepts

- **[Coupling and Cohesion](coupling-and-cohesion.md)** — SRP is a rule of thumb for maximizing cohesion: a class serving one actor is cohesive by construction, and splitting by actor lowers the coupling between unrelated concerns.
- **[Open-Closed](open-closed.md)** — single-responsibility classes are the raw material for open-closed designs: once formatting lives behind its own seam, adding an HTML formatter extends the system without touching calculation or storage.
- **[Encapsulation](encapsulation.md)** — encapsulation hides *how* a class does its job; SRP decides *how much* job it should have. A class can be perfectly encapsulated and still serve three actors.
- **[Interface Segregation](interface-segregation.md)** — the same "split by client/actor" idea applied to interfaces instead of implementations; a fat interface is the interface-shaped version of a god class.
