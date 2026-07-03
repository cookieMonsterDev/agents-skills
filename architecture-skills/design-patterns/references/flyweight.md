# Flyweight

**Category:** Structural

## Intent

Support huge numbers of fine-grained objects by sharing the state they have in common. Split each object into *intrinsic* state (immutable, shared across instances) and *extrinsic* state (unique per instance, supplied by the caller), and keep only one copy of each distinct intrinsic combination.

## Problem

- A program creates millions of similar objects (map tiles, text glyphs, forest trees, particles) and runs out of memory.
- Most of each object's fields are identical across instances (sprite, font metrics, texture), yet every instance carries its own copy.
- Only a few fields actually differ per instance (position, current value), and those could be passed in from outside.

## Structure

- **Flyweight** — holds the intrinsic state; immutable so sharing is safe. Its operations take extrinsic state as parameters (`draw(x, y)`).
- **Flyweight factory** — caches flyweights and returns an existing instance for a repeated intrinsic combination instead of creating a new one.
- **Context** — stores the extrinsic state plus a reference to its shared flyweight (e.g. a `Tree` holding `x, y` and a pointer to its `TreeType`).
- **Client** — obtains flyweights only through the factory and never mutates them.

## When to Use

- Object count is large enough that memory (or allocation churn) is a real, measured problem.
- Object state can be cleanly split into a shared immutable part and a small per-instance part.
- Identity doesn't matter to callers — two contexts pointing at the same flyweight must be indistinguishable from two separate objects.

## When Not to Use

- You have thousands of objects, not millions — the factory, cache, and indirection cost more than they save.
- The "shared" state actually needs per-instance mutation; a mutated flyweight corrupts every context that shares it.
- Extrinsic state is so large that passing it around erases the savings.

## Trade-offs

- **Pros:** dramatic memory savings when duplication is high; fewer allocations; immutable shared state is trivially thread-safe to read.
- **Cons:** code complexity (state split, factory, cache); CPU/memory trade — extrinsic state may be recomputed or passed on every call; the cache can leak if flyweights are never evicted.

## Language Notes

- **Python:** interned small ints and strings are built-in flyweights; `functools.lru_cache` on a factory function is the shortest implementation, and `__slots__` shrinks the per-context cost.
- **Java:** `Integer.valueOf` caches −128..127 and `String` interning are standard-library flyweights; a `HashMap`-backed factory is the classic form.
- **C#:** string interning (`string.Intern`) is the built-in example; share references to immutable objects via a `Dictionary` cache.
- **JavaScript / PHP:** engine-interned strings already share storage; a `Map`/array cache of frozen or immutable objects covers the explicit form.
- **Rust:** `Rc<TreeType>` (or `Arc` across threads) makes the sharing explicit and cheap — cloning the pointer, not the data; the borrow checker guarantees the shared state can't be mutated behind your back.
- **Go:** share `*TreeType` pointers handed out by a map-backed factory; immutability is by convention.
- **C:** flyweights are `const` structs in a small pool; contexts hold plain pointers into it. No polymorphism is needed.
- **C++:** `std::shared_ptr<const TreeType>` communicates both sharing and immutability in the type.
- **Swift:** use a `class` (reference semantics) for the flyweight so instances are shared; a `struct` would be copied on assignment, defeating the pattern.

## Examples

- [examples/flyweight/flyweight.py](../examples/flyweight/flyweight.py)
- [examples/flyweight/flyweight.c](../examples/flyweight/flyweight.c)
- [examples/flyweight/flyweight.cpp](../examples/flyweight/flyweight.cpp)
- [examples/flyweight/flyweight.java](../examples/flyweight/flyweight.java)
- [examples/flyweight/flyweight.cs](../examples/flyweight/flyweight.cs)
- [examples/flyweight/flyweight.js](../examples/flyweight/flyweight.js)
- [examples/flyweight/flyweight.rs](../examples/flyweight/flyweight.rs)
- [examples/flyweight/flyweight.go](../examples/flyweight/flyweight.go)
- [examples/flyweight/flyweight.php](../examples/flyweight/flyweight.php)
- [examples/flyweight/flyweight.swift](../examples/flyweight/flyweight.swift)

## Related Patterns

- **Factory Method / Singleton** — the flyweight factory is usually a singleton-ish cache built on a creation method.
- **Composite** leaf nodes are often implemented as shared flyweights.
- **Prototype** clones objects to *avoid* sharing; Flyweight shares to avoid cloning.
- **Proxy** also interposes on access to an object, but for control rather than for memory sharing.
