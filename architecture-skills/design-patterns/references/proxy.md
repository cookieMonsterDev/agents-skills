# Proxy

**Category:** Structural

## Intent

Provide a stand-in for another object that controls access to it. The proxy implements the same interface as the real object, so clients use it unchanged, while the proxy adds behavior *around* the access: deferring expensive creation, caching, access checks, logging, or remote communication.

## Problem

- An object is expensive to create (loads a large file, opens a connection) but often never actually used.
- You need to add caching, access control, or auditing around an object without modifying it or its callers.
- The real object lives elsewhere (another process, another machine) and callers should not care.

## Structure

- **Subject interface** — the operations both the real object and the proxy expose (`display()`).
- **Real subject** — the object that does the actual work; often expensive to create or sensitive to access.
- **Proxy** — holds a reference (possibly not-yet-initialized) to the real subject, implements the same interface, and decides when/whether to delegate.
- **Client** — works through the subject interface and cannot tell proxy from real subject.

Common variants: **virtual proxy** (lazy creation, shown in the examples), **protection proxy** (access control), **caching proxy**, **remote proxy** (stub for a remote object), **smart reference** (extra bookkeeping on access).

## When to Use

- Lazy initialization: the real object is heavy and frequently unused (virtual proxy).
- You must add a concern (cache, permissions, logging, rate limiting) around an object you can't or shouldn't modify.
- The real object is remote and you want local call syntax (remote proxy — the basis of most RPC stubs).

## When Not to Use

- The object is cheap to create — lazy indirection just obscures the code.
- You control the real class and the added behavior belongs inside it (or in a **Decorator** the caller opts into).
- The proxy would change the interface; that's an **Adapter**, not a proxy.

## Trade-offs

- **Pros:** clients are untouched; expensive work is deferred or avoided; cross-cutting concerns live in one place; the real subject stays single-purpose.
- **Cons:** another layer of indirection and delegation boilerplate; lazy proxies can move latency to an awkward moment (first access); a hidden cache or permission check can surprise callers debugging "identical" calls that behave differently.

## Language Notes

- **JavaScript:** the built-in `Proxy` object intercepts property access on *any* target without writing delegation by hand — the language-native form of this pattern (shown alongside the classic form in the example).
- **Python:** duck typing means no interface is required; `__getattr__` forwards everything not overridden to the real subject, so a proxy only writes the methods it intercepts.
- **PHP:** the `__call`/`__get` magic methods play the same role as Python's `__getattr__`; Doctrine lazy-loads entities through generated virtual proxies.
- **Java / C#:** interface + delegating class is the classic form; both platforms also offer dynamic proxies (`java.lang.reflect.Proxy`, `DispatchProxy`) used heavily by ORMs and mocking frameworks.
- **Rust:** smart pointers are proxy-like by design — `Deref` lets a wrapper transparently expose its target, and `Box`/`Rc`/`RefCell` interpose on access. The example uses a trait object plus `OnceCell` for lazy initialization.
- **Go:** an interface satisfied by both the real struct and the proxy; the proxy holds a nil pointer until first use.
- **C++:** `unique_ptr` created on first call implements the virtual proxy; smart pointers themselves (`shared_ptr`, `weak_ptr`) are the standard library's proxy-like constructs.
- **C:** polymorphism is emulated with a struct of function pointers, so the proxy and the real subject are interchangeable behind the same "vtable".
- **Swift:** a protocol as the subject interface; the proxy is a class holding an optional real subject created on first use (a stored `lazy var` works when the trigger is property access).

## Examples

- [examples/proxy/proxy.py](../examples/proxy/proxy.py)
- [examples/proxy/proxy.c](../examples/proxy/proxy.c)
- [examples/proxy/proxy.cpp](../examples/proxy/proxy.cpp)
- [examples/proxy/proxy.java](../examples/proxy/proxy.java)
- [examples/proxy/proxy.cs](../examples/proxy/proxy.cs)
- [examples/proxy/proxy.js](../examples/proxy/proxy.js)
- [examples/proxy/proxy.rs](../examples/proxy/proxy.rs)
- [examples/proxy/proxy.go](../examples/proxy/proxy.go)
- [examples/proxy/proxy.php](../examples/proxy/proxy.php)
- [examples/proxy/proxy.swift](../examples/proxy/proxy.swift)

## Related Patterns

- **Decorator** has the same shape (same interface, wraps the subject) but different intent: decorators *add behavior the client wants*; proxies *control access*, often without the client knowing.
- **Adapter** changes the interface; a proxy keeps it identical.
- **Facade** simplifies a whole subsystem; a proxy stands in for one object.
- A caching proxy often hands out **Flyweight**-style shared results.
