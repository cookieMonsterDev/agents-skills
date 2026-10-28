# Prototype

**Category:** Creational

## Intent

Create new objects by copying an existing, fully configured instance (the prototype) instead of instantiating a class and re-applying the configuration. The object itself knows how to clone itself, including its private state.

## Problem

- Setting up an object is expensive or verbose (loaded from a file, computed, or configured through many steps), and you need many near-identical copies.
- Code that copies objects field by field from the outside breaks encapsulation and silently goes stale when fields are added.
- You want to create objects whose concrete class you don't know — you only hold a reference through an interface, so you can't call a constructor.

## Structure

- **Prototype** — the interface declaring `clone()`.
- **Concrete prototypes** — implement `clone()`, deciding how deep the copy is (shared vs. duplicated sub-objects).
- **Prototype registry** (optional) — a catalog of named, pre-configured prototypes that clients clone instead of constructing (`registry.create("warning-circle")`).
- **Client** — clones a prototype and tweaks the copy.

## When to Use

- Instances differ only in configuration, and stamping out copies of a template is cheaper or clearer than reconstructing.
- You need a copy of an object reachable only through an interface, where its concrete class is unknown or inaccessible.
- A registry of pre-configured exemplars can replace a hierarchy of creator subclasses (compare Factory Method).

## When Not to Use

- Objects are cheap to construct and have little configuration; a constructor call is clearer than a clone-and-mutate dance.
- The object owns resources that can't be meaningfully copied (open sockets, file handles, locks).
- Deep-vs-shallow copy semantics of circular or shared structures would be subtle — get copying wrong and you get aliasing bugs.

## Trade-offs

- **Pros:** copies made without coupling to concrete classes, expensive setup paid once, registry replaces subclass explosions, copy logic lives with the object's own fields.
- **Cons:** deep-copying object graphs with cycles or shared state is genuinely hard; every new reference field is a chance to introduce an aliasing bug in `clone()`.

## Language Notes

- **Python:** the `copy` module (`copy.copy` / `copy.deepcopy`, customizable via `__copy__` / `__deepcopy__`) is the pattern built into the standard library.
- **JavaScript:** `structuredClone()` deep-copies plain data; for class instances a `clone()` method (often via spread) is still needed. The language's prototypal inheritance (`Object.create`) is a different mechanism despite the shared name.
- **Java:** `Cloneable` is widely considered broken (no `clone` in the interface, checked exceptions, shallow default); prefer copy constructors or static `copyOf` factories.
- **C# / PHP:** C# records get nondestructive copies via `with` expressions and classes have `MemberwiseClone`; PHP has a `clone` keyword with a `__clone` hook for fixing up deep-copied fields — in both, the pattern is a language feature.
- **Rust:** `#[derive(Clone)]` is the pattern as a compiler-checked language feature; for trait objects a `clone_box`-style method is the standard workaround since `Clone` isn't object-safe.
- **Go / Swift:** value types (structs) copy on assignment, so the pattern applies mainly to pointer/reference types, which need explicit `Clone()`/`clone()` methods that copy referenced data.
- **C:** plain structs copy by assignment; anything holding pointers needs an explicit clone function that duplicates the pointed-to data.

## Examples

- [examples/prototype/prototype.py](../examples/prototype/prototype.py)
- [examples/prototype/prototype.c](../examples/prototype/prototype.c)
- [examples/prototype/prototype.cpp](../examples/prototype/prototype.cpp)
- [examples/prototype/prototype.java](../examples/prototype/prototype.java)
- [examples/prototype/prototype.cs](../examples/prototype/prototype.cs)
- [examples/prototype/prototype.js](../examples/prototype/prototype.js)
- [examples/prototype/prototype.rs](../examples/prototype/prototype.rs)
- [examples/prototype/prototype.go](../examples/prototype/prototype.go)
- [examples/prototype/prototype.php](../examples/prototype/prototype.php)
- [examples/prototype/prototype.swift](../examples/prototype/prototype.swift)

## Related Patterns

- **Factory Method**: a prototype registry can replace a hierarchy of creator subclasses — register configured instances instead of writing a class per variant.
- **Abstract Factory** can be implemented by cloning a registered exemplar for each product instead of instantiating classes.
- **Memento** snapshots and restores state; Prototype produces an independent live object.
- Heavily composed structures (**Composite**, **Decorator**) benefit from cloning instead of reassembling.
