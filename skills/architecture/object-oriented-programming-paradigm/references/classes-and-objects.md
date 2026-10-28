# Classes & Objects

**Category:** Building Blocks

## Intent

Define a class as a blueprint that bundles related state and the behavior that operates on it, so that any number of independent objects can be instantiated from it without their data leaking into each other or into global scope.

## Problem

- Related data travels as loose variables (`ownerName`, `balance`, `accountNumber`) threaded through function after function; adding a fourth field means touching every signature.
- The functions that manipulate that data live far from it, so nothing stops one call site from updating `balance` while forgetting the matching ledger entry — the invariants have no home.
- Supporting "a second account" (or a thousand) means duplicating the variable set or bolting on arrays indexed in parallel, because state and behavior were written for exactly one instance.

## Structure

- **Class** — the blueprint: declares the fields every instance will carry, the methods that operate on them, and the constructor that establishes a valid starting state.
- **Object (instance)** — one concrete allocation of that blueprint with its own copies of the instance fields; two objects of the same class share behavior but never state.
- **Constructor / initializer** — the single entry point that turns raw arguments into a valid object; if it runs, the invariants hold from the first moment.
- **Instance members** — fields and methods bound to one object (`account.balance`, `account.deposit(...)`); a method is a function with an implicit reference to its instance (`this`/`self`).
- **Class (static) members** — fields and methods bound to the class itself, shared by all instances (an account counter, a `totalOpened()` query); they exist even when no instance does.
- **Free functions** — behavior that belongs to no single instance (a `transfer(from, to, amount)` coordinating two objects); forcing it into one class distorts ownership.

## When to Use

- The same cluster of variables keeps appearing together in signatures — that cluster is a class asking to exist.
- You need many independent instances of one shape (accounts, sessions, connections), each with its own lifecycle and state.
- Data has invariants ("balance never negative") that must be enforced at every mutation; methods next to the fields are the natural checkpoint.
- Construction requires setup logic (validation, ID assignment, resource acquisition) that must not be skippable.

## When Not to Use

- The "class" would hold no state — it is a namespace of functions; use a module/package of free functions instead.
- Only one instance will ever exist and it has no lifecycle — plain module-level functions and data are simpler than a class plus the temptation of Singleton.
- You are modeling pure data with no behavior — a record/struct/dataclass/tuple is lighter than a hand-rolled class.
- Behavior spans several peer objects equally (formatting, transfer, comparison across types) — a free function or separate service fits better than shoehorning it into one of the classes.

## Trade-offs

- **Pros:** state and the code that guards it live together; N instances come for free from one definition; constructors make invalid states unrepresentable from birth; the class name gives the domain concept a vocabulary word.
- **Cons:** classes invite hoarding — unrelated behavior accretes onto convenient types until they bloat; class-level (static) mutable state is a global in disguise and hurts tests and concurrency; object graphs hide aliasing (two references, one mutation) that loose values never had; in class-mandatory languages, stateless logic gets wrapped in ceremony.

## Language Notes

- **Python:** everything is an object, including classes. Beware the class-attribute trap: `balance = []` in the class body is shared by all instances — per-instance state must be assigned in `__init__`. `@classmethod` receives the class, `@staticmethod` neither; free functions live at module level and are first-class citizens. Use `@dataclass` when the class is mostly fields.
- **JavaScript:** `class` is sugar over prototypes — methods live on the prototype, fields on the instance. `#name` fields are truly private; `static` members hang off the constructor function. Object literals and closures also produce objects, so reserve `class` for when many instances share one shape.
- **PHP:** classes since PHP 5 look classic; PHP 8 constructor property promotion declares and assigns fields in the constructor signature, and `readonly` locks them after construction. `static` properties/methods and `self::`/`static::` cover class members; free functions are ordinary namespaced functions.
- **Java / C#:** class-mandatory — there are no free functions, so cross-object behavior becomes a `static` method on some class (utility classes, C# extension methods). Records (`record` in both) replace hand-written data-only classes. C# distinguishes `class` (reference) from `struct` (value); Java objects are always references.
- **C++:** `class` and `struct` differ only in default access. Constructors tie initialization to allocation (RAII); prefer member-initializer lists. A `static` data member is one variable per class — `inline static` (C++17) lets it be defined in-class. Free functions taking the class are a first-class part of its interface (ADL, `operator<<`).
- **Rust:** no `class` keyword — a `struct` holds state and `impl` blocks attach behavior. There are no constructors; the convention is an associated function `fn new(...) -> Self` that returns a validated value. Methods take `&self`/`&mut self`; associated functions (no `self`) are the "static" form. Class-level mutable state needs explicit synchronization (`static AtomicU32`), which is the language telling you to avoid it.
- **Go:** a `struct` plus methods declared with receivers (`func (a *Account) Deposit(...)`) is the class. Constructors are plain `NewAccount(...)` factory functions; package-level variables stand in for static members, scoped to the package rather than the type. Free functions are the default, methods the special case.
- **Swift:** both `struct` (value semantics, copied on assignment) and `class` (reference semantics, shared identity) bundle state and behavior with `init` initializers. Default to `struct`; choose `class` when instances have identity that must be shared — like a bank account two references should see mutate. `static` members work on both; `class` members are additionally overridable.
- **C:** no classes — emulate with a `struct` for state and prefixed free functions (`account_deposit(Account *a, ...)`) that take the struct pointer as an explicit `this`. A "constructor" is an init/open function that returns a validated struct; a file-scope `static` variable plays the class-member role. The discipline is manual, which makes the mechanics visible.

## Examples

- [examples/classes-and-objects/classes-and-objects.py](../examples/classes-and-objects/classes-and-objects.py)
- [examples/classes-and-objects/classes-and-objects.cpp](../examples/classes-and-objects/classes-and-objects.cpp)
- [examples/classes-and-objects/classes-and-objects.java](../examples/classes-and-objects/classes-and-objects.java)
- [examples/classes-and-objects/classes-and-objects.cs](../examples/classes-and-objects/classes-and-objects.cs)
- [examples/classes-and-objects/classes-and-objects.js](../examples/classes-and-objects/classes-and-objects.js)
- [examples/classes-and-objects/classes-and-objects.php](../examples/classes-and-objects/classes-and-objects.php)
- [examples/classes-and-objects/classes-and-objects.swift](../examples/classes-and-objects/classes-and-objects.swift)

## Related Concepts

- **Encapsulation** takes the bundling a class provides one step further: it hides the fields behind the methods so invariants cannot be bypassed. A class is the container; encapsulation is the access policy.
- **Abstraction** decides *what* a class exposes conceptually (an "account" you deposit into) versus the representation underneath; classes are the mechanism abstractions are usually built from.
- **Interfaces & Abstract Classes** describe a contract without (fully) providing the blueprint — use them when several concrete classes must be interchangeable behind one shape.
- **Object Relationships** covers how instances reference each other (association, aggregation, composition) once you have more than one class; the `transfer` free function in the examples is the first hint that objects collaborate.
