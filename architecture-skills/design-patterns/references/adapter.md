# Adapter

**Category:** Structural

## Intent

Convert the interface of an existing class into the interface clients expect, so code with incompatible interfaces can work together without modifying either side.

## Problem

- You want to reuse a legacy or third-party class, but its method names, argument shapes, or units don't match the interface your code is written against.
- You can't change the mismatched class (no source access, shared by other teams, or frozen for compatibility).
- Conversion logic (units, formats, naming) keeps leaking into call sites instead of living in one place.

## Structure

- **Target** — the interface the client code already works against (`TemperatureSource.celsius()`).
- **Adaptee** — the existing class with the incompatible interface (`LegacyFahrenheitSensor.readFahrenheit()`).
- **Adapter** — implements the target, holds the adaptee, and translates both calls and data (Fahrenheit → Celsius).
- The GoF "class adapter" variant inherits from both sides instead of composing; the object adapter via composition is almost always preferred.

## When to Use

- Integrating third-party or legacy code whose interface you cannot change.
- Unifying several existing classes with different interfaces behind one target interface.
- Confining unit or format conversions to a single boundary object.

## When Not to Use

- You own both sides — change the interface at the source instead of adding a translation layer.
- The objects already respond to the right methods (common in duck-typed languages); a formal adapter adds nothing.
- The mismatch is behavioral (different semantics, lifecycle, or error model), not just an interface: an adapter will paper over the gap rather than fix it.

## Trade-offs

- **Pros:** reuse without modification; conversion logic lives in exactly one place; client code stays clean, and adapters are easy to fake in tests.
- **Cons:** one more layer of indirection and one more class per adaptee; a pile of adapters can hide the fact that the underlying model genuinely doesn't fit.

## Language Notes

- **Python / JavaScript / PHP:** duck typing means an adapter is only needed when the legacy object lacks the expected method names; often a thin wrapper class or even a function suffices.
- **Java / C#:** the classic home — `InputStreamReader` (bytes → chars) and `StreamReader` are standard-library adapters; always object adapters via composition.
- **Rust:** the newtype idiom (`struct FahrenheitAdapter(LegacySensor)`) is the natural adapter and also the standard workaround for the orphan rule; `From`/`Into` cover pure value conversions.
- **Go:** implicit interface satisfaction keeps adapters tiny; `http.HandlerFunc` is a famous adapter that turns a plain function into an `http.Handler`.
- **C:** emulated with a struct of function pointers (a hand-rolled vtable) filled with translating functions.
- **Swift:** retroactive protocol conformance via an `extension` *is* the adapter — no wrapper type needed unless the conformance requires extra state.

## Examples

- [examples/adapter/adapter.py](../examples/adapter/adapter.py)
- [examples/adapter/adapter.c](../examples/adapter/adapter.c)
- [examples/adapter/adapter.cpp](../examples/adapter/adapter.cpp)
- [examples/adapter/adapter.java](../examples/adapter/adapter.java)
- [examples/adapter/adapter.cs](../examples/adapter/adapter.cs)
- [examples/adapter/adapter.js](../examples/adapter/adapter.js)
- [examples/adapter/adapter.rs](../examples/adapter/adapter.rs)
- [examples/adapter/adapter.go](../examples/adapter/adapter.go)
- [examples/adapter/adapter.php](../examples/adapter/adapter.php)
- [examples/adapter/adapter.swift](../examples/adapter/adapter.swift)

## Related Patterns

- **Bridge** separates abstraction from implementation up front by design; Adapter retrofits compatibility between existing pieces after the fact.
- **Decorator** keeps the interface the same and adds behavior; Adapter changes the interface without adding behavior.
- **Facade** invents a new, simpler interface over a whole subsystem; Adapter reshapes one object to match an interface that already exists.
- **Proxy** keeps the same interface and controls access to the object rather than translating it.
