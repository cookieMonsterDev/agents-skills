---
name: design-patterns
description: Gang of Four (GoF) design patterns, with a reference and runnable examples per pattern. Use when a question names a pattern (singleton, factory, builder, observer, strategy, adapter...), describes a design problem a pattern might solve, compares patterns, or asks to refactor code toward one.
---

# Design Patterns

Ground every pattern answer in this skill's reference files, not in improvised definitions. A pattern is the answer to specific **forces** in a design problem: recommend one only when the user's problem shows the forces it resolves.

## Workflow

1. **Identify the pattern(s)** in the catalog below, by name or by the forces in the user's problem. Done when every pattern the question names or implies is listed, or when no pattern's forces are present; then answer with the plain function, data structure, or language feature that solves the problem.
2. **Read each identified reference** at `references/<pattern>.md` in full. When comparing patterns, read every one compared and contrast their intent, not their structure.
3. **Read the language example** at `examples/<pattern>/<pattern>.<ext>` for the user's language. For a language without an example, use the reference's Language Notes for the idiomatic form.
4. **Answer** with what the pattern does, the forces that call for it, the simpler alternative and when it wins, and code adapted to the user's domain (their own code, when refactoring). Write the language's idiomatic form rather than a literal GoF class diagram: closures for Strategy in JavaScript, enums for State in Rust, `sync.Once` for Singleton in Go. Done when every identified pattern has all four parts.

## Pattern Catalog

### Creational

Patterns that abstract the instantiation process.

| Pattern          | Intent                                                                              | Reference                                                        |
| ---------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Abstract Factory | Create families of related objects without specifying concrete classes              | [references/abstract-factory.md](references/abstract-factory.md) |
| Builder          | Construct complex objects step by step, separating construction from representation | [references/builder.md](references/builder.md)                   |
| Factory Method   | Let subclasses decide which class to instantiate                                    | [references/factory-method.md](references/factory-method.md)     |
| Prototype        | Create objects by cloning an existing instance                                      | [references/prototype.md](references/prototype.md)               |
| Singleton        | Ensure a class has one instance with a global access point                          | [references/singleton.md](references/singleton.md)               |

### Structural

Patterns that compose classes and objects into larger structures.

| Pattern   | Intent                                                                 | Reference                                          |
| --------- | ---------------------------------------------------------------------- | -------------------------------------------------- |
| Adapter   | Convert one interface into another that clients expect                 | [references/adapter.md](references/adapter.md)     |
| Bridge    | Decouple an abstraction from its implementation so both can vary       | [references/bridge.md](references/bridge.md)       |
| Composite | Treat individual objects and compositions uniformly in tree structures | [references/composite.md](references/composite.md) |
| Decorator | Attach responsibilities to objects dynamically without subclassing     | [references/decorator.md](references/decorator.md) |
| Facade    | Provide a simple unified interface to a complex subsystem              | [references/facade.md](references/facade.md)       |
| Flyweight | Share fine-grained objects to support large numbers efficiently        | [references/flyweight.md](references/flyweight.md) |
| Proxy     | Provide a surrogate that controls access to another object             | [references/proxy.md](references/proxy.md)         |

### Behavioral

Patterns that assign responsibilities and manage communication between objects.

| Pattern                 | Intent                                                                        | Reference                                                                      |
| ----------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Chain of Responsibility | Pass a request along a chain of handlers until one handles it                 | [references/chain-of-responsibility.md](references/chain-of-responsibility.md) |
| Command                 | Encapsulate a request as an object, enabling queues and undo                  | [references/command.md](references/command.md)                                 |
| Interpreter             | Define a grammar and an interpreter for a small language                      | [references/interpreter.md](references/interpreter.md)                         |
| Iterator                | Access elements of a collection sequentially without exposing its internals   | [references/iterator.md](references/iterator.md)                               |
| Mediator                | Centralize complex communication between objects in one mediator              | [references/mediator.md](references/mediator.md)                               |
| Memento                 | Capture and restore an object's internal state without breaking encapsulation | [references/memento.md](references/memento.md)                                 |
| Observer                | Notify dependents automatically when an object's state changes                | [references/observer.md](references/observer.md)                               |
| State                   | Let an object change its behavior when its internal state changes             | [references/state.md](references/state.md)                                     |
| Strategy                | Define interchangeable algorithms behind a common interface                   | [references/strategy.md](references/strategy.md)                               |
| Template Method         | Define an algorithm's skeleton, deferring some steps to subclasses            | [references/template-method.md](references/template-method.md)                 |
| Visitor                 | Add operations to an object structure without modifying its classes           | [references/visitor.md](references/visitor.md)                                 |

## Examples

Examples are self-contained and runnable, in Python, C, C++, Java, C#, JavaScript, Rust, Go, PHP, and Swift. Each is written in its language's idiom: C emulates objects with structs and function pointers; Rust and Go use traits, interfaces, and composition in place of inheritance.
