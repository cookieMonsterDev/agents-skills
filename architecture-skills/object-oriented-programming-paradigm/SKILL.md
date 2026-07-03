---
name: object-oriented-programming-paradigm
description: Explains and applies the object-oriented programming paradigm — classes, the four pillars (encapsulation, abstraction, inheritance, polymorphism), object relationships, SOLID, and design qualities — with idiomatic code examples in Python, C++, Java, C#, JavaScript, PHP, and Swift. Use when users ask about OOP concepts or SOLID principles, when they need help modeling a domain with classes and interfaces, when reviewing or refactoring class hierarchies, or when they want an OOP concept example in a specific language.
---

# Object-Oriented Programming Paradigm

Ground OOP answers in the reference files bundled with this skill instead of improvising definitions. Each concept has a reference file explaining it and a folder of runnable examples in popular languages.

## When to Use

- The user names a concept directly ("show me encapsulation in Swift", "what is the Liskov substitution principle?")
- The user describes a design problem that maps to a concept ("my subclass breaks when passed to code written for the base class")
- The user asks to compare concepts ("composition vs inheritance?", "coupling vs cohesion?")
- The user wants existing code reviewed or refactored against OOP principles (god classes, deep hierarchies, leaky abstractions, train-wreck call chains)

## Workflow

1. **Identify the concept(s)** from the user's question using the catalog below.
2. **Read the reference file** at `references/<concept>.md` for the explanation, applicability, trade-offs, and related concepts.
3. **Read the language example** at `examples/<concept>/<concept>.<ext>` when the user works in (or asks for) a specific language. Adapt it to their domain rather than pasting the generic example verbatim.
4. **Answer** with: what the concept means, when it applies (and when it doesn't), and code adapted to the user's context.

If the user's problem does not call for object orientation, say so — plain functions and data structures are often simpler than a class model.

## Concept Catalog

### Building Blocks

The vocabulary of object-oriented code: what classes, objects, and contracts are.

| Concept                       | Intent                                                                              | Reference                                                                                      |
| ----------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Classes & Objects             | Bundle state and behavior into a blueprint; instantiate independent objects from it | [references/classes-and-objects.md](references/classes-and-objects.md)                         |
| Interfaces & Abstract Classes | Separate a contract from its implementations; share partial implementation safely   | [references/interfaces-and-abstract-classes.md](references/interfaces-and-abstract-classes.md) |

### The Four Pillars

The defining properties of the paradigm.

| Concept       | Intent                                                                          | Reference                                                  |
| ------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Encapsulation | Hide internal state behind a controlled interface that preserves invariants     | [references/encapsulation.md](references/encapsulation.md) |
| Abstraction   | Expose a component's essential model while hiding operational detail            | [references/abstraction.md](references/abstraction.md)     |
| Inheritance   | Derive specialized classes from a base, reusing and extending its behavior      | [references/inheritance.md](references/inheritance.md)     |
| Polymorphism  | Let one call site work across many concrete types (subtype, parametric, ad hoc) | [references/polymorphism.md](references/polymorphism.md)   |

### Object Relationships

How objects reference, own, and assemble each other.

| Concept                      | Intent                                                                          | Reference                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Object Relationships         | Distinguish association, aggregation, and composition by ownership and lifetime | [references/object-relationships.md](references/object-relationships.md)                 |
| Composition over Inheritance | Build behavior by assembling parts instead of extending deep hierarchies        | [references/composition-over-inheritance.md](references/composition-over-inheritance.md) |

### SOLID Principles

Five principles for class design that keep change local.

| Principle             | Intent                                                                      | Reference                                                                  |
| --------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Single Responsibility | Give each class one reason to change                                        | [references/single-responsibility.md](references/single-responsibility.md) |
| Open/Closed           | Make code open for extension without modifying what already works           | [references/open-closed.md](references/open-closed.md)                     |
| Liskov Substitution   | Ensure subtypes are usable anywhere their base type is expected             | [references/liskov-substitution.md](references/liskov-substitution.md)     |
| Interface Segregation | Prefer many small client-specific interfaces over one fat interface         | [references/interface-segregation.md](references/interface-segregation.md) |
| Dependency Inversion  | Make high-level policy depend on abstractions, not concrete implementations | [references/dependency-inversion.md](references/dependency-inversion.md)   |

### Design Qualities

Cross-cutting qualities used to judge an object-oriented design.

| Concept             | Intent                                                                         | Reference                                                                  |
| ------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Coupling & Cohesion | Minimize dependence between modules and maximize relatedness within them       | [references/coupling-and-cohesion.md](references/coupling-and-cohesion.md) |
| Law of Demeter      | Talk only to immediate collaborators instead of reaching through object graphs | [references/law-of-demeter.md](references/law-of-demeter.md)               |

## Examples

Each concept has a folder `examples/<concept>/` with self-contained, runnable examples named `<concept>.<ext>`:

| Language   | File              | Notes |
| ---------- | ----------------- | ----- |
| Python     | `<concept>.py`    |       |
| C++        | `<concept>.cpp`   |       |
| Java       | `<concept>.java`  |       |
| C#         | `<concept>.cs`    |       |
| JavaScript | `<concept>.js`    |       |
| PHP        | `<concept>.php`   |       |
| Swift      | `<concept>.swift` |       |

Examples are limited to languages with first-class classes (or class-like syntax). Languages without classes — C, Go, Rust — are omitted; their reference files still note how each concept maps idiomatically when a user asks.

A language file may be absent when a concept does not translate meaningfully to that language; the concept's reference file notes such gaps (e.g. Swift structs and protocols as an alternative to deep class inheritance).

## Answering Guidelines

- Prefer the language's idiomatic form over a textbook Java-style class diagram (e.g. protocols and duck typing in Python, structs and protocols in Swift, closures where a one-method class would be ceremony).
- Mention trade-offs and simpler alternatives, not just the mechanics — not every problem needs a class.
- When comparing concepts, read both reference files and contrast intent, not structure.
- Do not present deep inheritance hierarchies as the default way to reuse code; prefer composition and interfaces unless true subtype specialization exists.
- When reviewing code, name the violated principle and show the minimal refactor, not a full rewrite.
