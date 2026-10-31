---
name: object-oriented-programming-paradigm
description: Object-oriented programming concepts (classes, the four pillars, object relationships, SOLID, coupling and cohesion, Law of Demeter), with a reference and runnable examples per concept. Use when a question names an OOP concept or SOLID principle, models a domain with classes and interfaces, compares concepts, or asks to review or refactor class designs.
---

# Object-Oriented Programming Paradigm

Ground every OOP answer in this skill's reference files, not in improvised definitions. Reuse behavior through composition and interfaces; reserve inheritance for true subtype specialization.

## Workflow

For class-design reviews or refactoring, first read [review and refactoring](references/review-and-refactoring.md) for caller-based evidence, invariant checks, and migration boundaries.

1. **Identify the concept(s)** in the catalog below, by name or by symptom: a subclass that breaks where its base is expected, a god class, a deep hierarchy, a leaky abstraction, a train-wreck call chain. Done when every concept the question names or implies is listed, or when the problem is better served by plain functions and data; then answer with those.
2. **Read each identified reference** at `references/<concept>.md` in full. When comparing concepts, read every one compared and contrast their intent, not their structure.
3. **Read the language example** at `examples/<concept>/<concept>.<ext>` for the user's language. For C, Go, Rust, or another language without an example, use the reference's Language Notes for the idiomatic mapping.
4. **Answer** with what the concept means, when it applies, the simpler alternative and when it wins, and code adapted to the user's domain. Write the language's idiomatic form rather than a textbook Java-style class diagram: protocols and duck typing in Python, structs and protocols in Swift, closures where a one-method class would be ceremony. When reviewing code, name the violated principle and show the minimal refactor of the user's code. Done when every identified concept has all four parts.

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

Examples are self-contained and runnable, in the languages with first-class classes: Python, C++, Java, C#, JavaScript, PHP, and Swift.
