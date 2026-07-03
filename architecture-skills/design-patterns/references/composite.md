# Composite

**Category:** Structural

## Intent

Compose objects into tree structures representing part-whole hierarchies, and give leaves and containers one interface so clients treat individual objects and groups of objects uniformly.

## Problem

- The domain is a tree: file systems, org charts, UI widget hierarchies, menus, arithmetic expressions.
- Client code is littered with "is this a single item or a group?" checks before every operation.
- Aggregate operations (total size, rendering, search) must recurse, and every caller reimplements the recursion.

## Structure

- **Component** — the common interface for everything in the tree (`Node.size()`, `Node.print()`).
- **Leaf** — an end object with no children (`File`); implements the operations directly.
- **Composite** — a container (`Directory`) holding child components; implements the operations by combining results from its children, recursing transparently.
- **Client** — works through the component interface and never distinguishes leaf from composite.

## When to Use

- The data is naturally hierarchical and clients should be able to ignore the leaf/container distinction.
- Aggregate results (sums, rendering, matching) should be computed by the structure itself, not by every caller.
- Groups must nest inside groups to arbitrary depth.

## When Not to Use

- The structure is flat — a list plus a loop beats a tree.
- Leaves and containers share almost no meaningful operations; forcing one interface produces awkward no-ops (`addChild` on a `File`).
- You need to strictly control what kinds of children a container may hold; the uniform interface trades that type safety away.

## Trade-offs

- **Pros:** client code is uniform and the recursion lives in one place; new node types slot in without touching clients; arbitrarily deep nesting comes for free.
- **Cons:** the component interface tends to become overly general (child management declared on leaves); invariants like "a directory may not contain itself" need runtime checks; naive recursive operations get expensive on huge trees without caching.

## Language Notes

- **Python / JavaScript / PHP:** duck typing keeps the component "interface" implicit; an ABC (Python) or `interface` (PHP) just documents it. The DOM is the everyday composite in JavaScript.
- **Java / C#:** the classic home — Swing containers, WPF's visual tree, and XML DOMs are all composites.
- **Rust:** trait objects (`Vec<Box<dyn Node>>`) give the open GoF form; a recursive `enum` is often more idiomatic when the set of node kinds is closed.
- **Go:** a small interface plus a `[]Node` slice in the composite; no other machinery needed.
- **C:** function-pointer structs for polymorphism, with a child array inside the composite node.
- **Swift:** a protocol for the component; composites are classes (reference semantics suit shared tree nodes), or an `indirect enum` for closed node sets.

## Examples

- [examples/composite/composite.py](../examples/composite/composite.py)
- [examples/composite/composite.c](../examples/composite/composite.c)
- [examples/composite/composite.cpp](../examples/composite/composite.cpp)
- [examples/composite/composite.java](../examples/composite/composite.java)
- [examples/composite/composite.cs](../examples/composite/composite.cs)
- [examples/composite/composite.js](../examples/composite/composite.js)
- [examples/composite/composite.rs](../examples/composite/composite.rs)
- [examples/composite/composite.go](../examples/composite/composite.go)
- [examples/composite/composite.php](../examples/composite/composite.php)
- [examples/composite/composite.swift](../examples/composite/composite.swift)

## Related Patterns

- **Decorator** is essentially a composite with exactly one child, focused on adding behavior rather than aggregating children; the two are often used together.
- **Iterator** walks composite structures without exposing their shape.
- **Visitor** adds new operations over a composite without changing the node classes.
- **Builder** is a natural way to assemble complex composite trees.
