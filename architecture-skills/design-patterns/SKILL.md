---
name: design-patterns
description: Explains and applies the 23 Gang of Four (GoF) design patterns with idiomatic code examples in Python, C, C++, Java, C#, JavaScript, Rust, Go, PHP, and Swift. Use when users ask about design patterns (singleton, factory, builder, observer, strategy, decorator, adapter, etc.), when they need help choosing a pattern for a design problem, when refactoring code toward a pattern, or when they want a pattern example in a specific language.
---

# Design Patterns

Ground design-pattern answers in the reference files bundled with this skill instead of improvising definitions. Each pattern has a reference file explaining it and a folder of runnable examples in popular languages.

## When to Use

- The user names a pattern directly ("show me the builder pattern in Rust")
- The user describes a design problem that maps to a pattern ("I need to create objects without specifying their concrete class")
- The user asks to compare patterns ("strategy vs state?")
- The user wants existing code refactored toward a pattern

## Workflow

1. **Identify the pattern(s)** from the user's question using the catalog below.
2. **Read the reference file** at `references/<pattern>.md` for the explanation, applicability, trade-offs, and related patterns.
3. **Read the language example** at `examples/<pattern>/<pattern>.<ext>` when the user works in (or asks for) a specific language. Adapt it to their domain rather than pasting the generic example verbatim.
4. **Answer** with: what the pattern does, when to use it (and when not to), and code adapted to the user's context.

If the user's problem does not match any pattern cleanly, say so — do not force a pattern where a plain function or data structure is simpler.

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

Each pattern has a folder `examples/<pattern>/` with self-contained, runnable examples named `<pattern>.<ext>`:

| Language   | File              | Notes                                                                       |
| ---------- | ----------------- | --------------------------------------------------------------------------- |
| Python     | `<pattern>.py`    |                                                                             |
| C          | `<pattern>.c`     | Emulated with structs and function pointers where the pattern relies on OOP |
| C++        | `<pattern>.cpp`   |                                                                             |
| Java       | `<pattern>.java`  |                                                                             |
| C#         | `<pattern>.cs`    |                                                                             |
| JavaScript | `<pattern>.js`    |                                                                             |
| Rust       | `<pattern>.rs`    | Uses traits and enums; no inheritance-based variants                        |
| Go         | `<pattern>.go`    | Uses interfaces and composition; no inheritance-based variants              |
| PHP        | `<pattern>.php`   |                                                                             |
| Swift      | `<pattern>.swift` |                                                                             |

A language file may be absent when the pattern does not translate meaningfully to that language; the pattern's reference file notes such gaps and idiomatic alternatives (e.g. iterators, decorators, and singletons that are built into a language).

## Answering Guidelines

- Prefer the language's idiomatic form over a literal GoF class diagram (e.g. closures for Strategy in JavaScript, enums for State in Rust, `sync.Once` for Singleton in Go).
- Mention trade-offs and simpler alternatives, not just the mechanics.
- When comparing patterns, read both reference files and contrast intent, not structure.
- Do not recommend Singleton, or any pattern, as a default; patterns are solutions to specific forces, not style goals.
