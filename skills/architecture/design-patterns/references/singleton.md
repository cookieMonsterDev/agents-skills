# Singleton

**Category:** Creational

## Intent

Ensure a class has exactly one instance and provide a single global access point to it. The class itself guards the "only one" invariant instead of trusting callers to construct it once.

## Problem

- A resource genuinely must exist once per process — a configuration snapshot, a logger, a connection pool, a hardware handle.
- Creating it twice would be wrong (double initialization, conflicting state) or wasteful (expensive load repeated).
- Passing the instance through every constructor feels heavyweight, so code reaches for a global — and a bare global has no lazy initialization and no protection against a second instance.

## Structure

- **Singleton class** — hides its constructor (private/module-level), stores the sole instance in a static/class-level field, and exposes a static accessor (`instance()` / `shared`) that creates the instance on first use.
- **Thread safety** — the accessor must make first-time construction race-free (locks, `Lazy<T>`, `sync.Once`, `OnceLock`, static-local initialization, module import).

## When to Use

- The "exactly one" constraint is real and violating it is a bug, not merely a waste — device handles, process-wide registries, config loaded once at startup.
- You need lazy construction plus global access and cannot inject the instance from the composition root.
- Sparingly: most codebases need fewer singletons than they have.

## When Not to Use

- The instance is single merely by convenience. This is the most overused GoF pattern: a singleton is global mutable state with a design-pattern name, and the default answer should be creating one instance at startup and passing it down (dependency injection).
- Code needs testing in isolation — singletons hard-wire their consumers to one shared instance that leaks state between tests and can't be swapped for a fake without hacks.
- The "one instance" scope might change (per-thread, per-tenant, per-test); the hard-coded static makes that scope change a refactor of every call site.

## Trade-offs

- **Pros:** guaranteed single instance, lazy construction, one well-known access point, no need to thread the object through many layers.
- **Cons:** hidden dependencies (call sites don't declare they use it), shared state couples tests to each other, concurrency hazards around both construction and the instance's own mutable state, and teardown/ordering at process exit is awkward. Widely considered an anti-pattern when used for anything a constructor argument could carry.

## Language Notes

- **Python:** a module-level instance is the idiomatic singleton — modules are imported once and cached, so `config = Config()` in a module needs no class machinery; `__new__`-based singletons are rarely worth it.
- **Java:** the initialization-on-demand holder idiom or a single-element `enum` (Effective Java) give thread-safe lazy singletons without locks; double-checked locking is famously easy to get wrong.
- **C#:** `Lazy<T>` with a static field is the standard thread-safe form; in practice most C# code registers a singleton *lifetime* in the DI container instead, which keeps the type testable.
- **JavaScript:** module scope is a natural singleton — export an instance and the module cache guarantees uniqueness; explicit singleton classes mostly reimplement what `import` already does.
- **Rust:** `OnceLock`/`LazyLock` in `std` (formerly the `lazy_static`/`once_cell` crates) initialize a static safely; the borrow checker pushes mutable singletons toward `Mutex`, making the shared-state cost explicit.
- **Go:** `sync.Once` inside an accessor function is the standard form; package-level `init` covers eager cases.
- **C:** a `static` variable inside an accessor function; guard first initialization with `pthread_once` or C11 `call_once` when threads are involved.
- **C++:** the Meyers singleton (function-local `static`) is thread-safe since C++11 and avoids the static-initialization-order fiasco.
- **Swift / PHP:** Swift's `static let shared` is lazily initialized and thread-safe by language guarantee (`URLSession.shared`); PHP uses a static instance with a private constructor, though frameworks favor DI containers.
- **Everywhere:** prefer constructor injection where feasible; reserve the singleton for the composition root and truly process-unique resources.

## Examples

- [examples/singleton/singleton.py](../examples/singleton/singleton.py)
- [examples/singleton/singleton.c](../examples/singleton/singleton.c)
- [examples/singleton/singleton.cpp](../examples/singleton/singleton.cpp)
- [examples/singleton/singleton.java](../examples/singleton/singleton.java)
- [examples/singleton/singleton.cs](../examples/singleton/singleton.cs)
- [examples/singleton/singleton.js](../examples/singleton/singleton.js)
- [examples/singleton/singleton.rs](../examples/singleton/singleton.rs)
- [examples/singleton/singleton.go](../examples/singleton/singleton.go)
- [examples/singleton/singleton.php](../examples/singleton/singleton.php)
- [examples/singleton/singleton.swift](../examples/singleton/singleton.swift)

## Related Patterns

- **Abstract Factory**, **Builder**, and **Prototype** registries are often implemented as singletons in practice.
- **Facade** objects are frequently single-instance for the same "one access point" reason.
- **Flyweight** shares many small immutable objects; Singleton shares exactly one — immutability is what makes either safe to share.
