# Iterator

**Category:** Behavioral

## Intent

Provide a way to access the elements of a collection sequentially without exposing its underlying representation. The collection hands out an iterator object that tracks the traversal position.

## Problem

- Client code wants to walk a collection (tree, graph, ring buffer, paginated API) without knowing or depending on how it stores elements.
- Several traversals of the same collection must be in flight at once, each with its own position.
- Different traversal orders (in-order vs. breadth-first, filtered vs. full) should be offered without bloating the collection's interface.

## Structure

- **Iterator** — the traversal interface; canonically `hasNext()`/`next()`, though every modern language defines its own shape (`__next__`, `next() -> Option<T>`, `MoveNext()/Current`).
- **Concrete iterator** — tracks the current position; for tree traversal this typically means an explicit stack replacing the call stack of a recursive walk.
- **Iterable / aggregate** — the collection, with a method producing a fresh iterator.
- **Client** — usually the language's `for` loop, which drives the iterator implicitly.

## When to Use

- You are building a custom collection and want it to work with the language's `for` loop and standard library algorithms — implement the native iteration protocol.
- Traversal state must be pausable, or multiple independent traversals must coexist.
- You want to hide a complex structure (tree, composite, remote pages) behind simple sequential access, possibly lazily.

## When Not to Use

- The data is already in a built-in list/array/map — those ship with iterators; wrapping them adds nothing.
- You control both sides and a plain index loop over an array is clearer.
- Hand-rolling the GoF class hierarchy in a language with generators: `yield` produces the iterator for you and keeps traversal logic in one readable function.

## Trade-offs

- **Pros:** decouples clients from the collection's representation, supports multiple simultaneous and lazy traversals, plugs custom collections into the entire language ecosystem (loops, comprehensions, adapter chains).
- **Cons:** explicit iterator state (e.g. a stack for tree traversal) is more intricate than the recursive equivalent — generators remove this cost where available; iterators over mutating collections need an invalidation policy; sequential access can hide expensive per-element work.

## Language Notes

This pattern is built into essentially every modern language; the examples implement the *native protocol* for a custom collection rather than a GoF class hierarchy.

- **Python:** implement `__iter__`, most easily as a generator (`yield`); generators alone cover most iterator needs.
- **JavaScript:** implement `[Symbol.iterator]`, most easily with a generator `function*`; this enables `for...of` and spread.
- **C#:** implement `IEnumerable<T>` with a `yield return` iterator method; LINQ then works on the collection for free.
- **Java:** implement `Iterable<T>` returning an `Iterator<T>`; no generators, so tree traversal carries an explicit stack (`Deque`).
- **Rust:** implement the `Iterator` trait (`next() -> Option<T>`); the entire adapter ecosystem (`map`, `filter`, `sum`) then applies.
- **Go:** since 1.23, range-over-func iterators (`iter.Seq[T]`, a `func(yield func(T) bool)`) are the standard form and work directly with `range`.
- **Swift:** conform to `Sequence`/`IteratorProtocol`; `for-in`, `map`, and friends follow.
- **PHP:** implement `Iterator` or, more simply, `IteratorAggregate` returning a generator.
- **C:** no protocol exists; the convention is an iterator struct plus a `next` function returning whether an element was produced.
- **C++:** iterators are the STL's core abstraction; a minimal `begin()`/`end()` pair with `operator++`/`operator*`/`operator!=` enables range-based `for`.

## Examples

- [examples/iterator/iterator.py](../examples/iterator/iterator.py)
- [examples/iterator/iterator.c](../examples/iterator/iterator.c)
- [examples/iterator/iterator.cpp](../examples/iterator/iterator.cpp)
- [examples/iterator/iterator.java](../examples/iterator/iterator.java)
- [examples/iterator/iterator.cs](../examples/iterator/iterator.cs)
- [examples/iterator/iterator.js](../examples/iterator/iterator.js)
- [examples/iterator/iterator.rs](../examples/iterator/iterator.rs)
- [examples/iterator/iterator.go](../examples/iterator/iterator.go)
- [examples/iterator/iterator.php](../examples/iterator/iterator.php)
- [examples/iterator/iterator.swift](../examples/iterator/iterator.swift)

## Related Patterns

- **Composite** trees are the classic structure an Iterator flattens into a sequence.
- **Visitor** also walks a structure, but the structure drives the traversal and calls back; an Iterator lets the *client* drive.
- **Memento** can capture an iterator's position to resume a traversal later.
- **Factory Method** — the collection's `iterator()`/`__iter__` method is a factory method for iterator objects.
