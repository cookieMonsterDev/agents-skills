# Command

**Category:** Behavioral

## Intent

Encapsulate a request as an object, so requests can be parameterized, queued, logged, and undone. The invoker triggers a command without knowing what it does or to whom.

## Problem

- UI elements (buttons, menu items, shortcuts) all need to trigger the same operation without duplicating its logic or coupling widgets to business objects.
- Operations must be undoable, which requires remembering what each operation did and how to reverse it.
- Requests need to be queued, scheduled, retried, or written to a log (job queues, transactional operations, macro recording).

## Structure

- **Command** — declares the execution interface, typically `execute()` and, for undoable systems, `undo()`.
- **Concrete command** — binds a receiver to an action and stores the arguments (and any state needed to undo).
- **Receiver** — the object that actually does the work (a document, a device, a service).
- **Invoker** — triggers commands and often keeps a history stack for undo/redo.
- **Client** — creates commands and hands them to the invoker.

## When to Use

- You need undo/redo: each command stores enough state to reverse itself, and a history stack replays or rolls back.
- Operations must be queued, delayed, logged, or transmitted (task queues, remote procedure batching, macros).
- Many invokers trigger the same operation, or the operation to run is chosen at runtime.

## When Not to Use

- A direct method call does the job and no queuing, undo, or decoupling is needed; command objects are pure ceremony then.
- In languages with first-class functions, a plain function or closure often _is_ the command; only reach for classes when commands carry undo state or multiple methods.

## Trade-offs

- **Pros:** decouples invoker from receiver, enables undo/redo and queuing, commands compose into macros, operations become inspectable values.
- **Cons:** one class (or closure pair) per operation adds indirection and code; undoable commands must carefully capture state, which gets tricky with large or shared state (Memento can help).

## Language Notes

- **Python / JavaScript:** a closure is the natural one-shot command; use classes (or a `(do, undo)` closure pair) when undo state must travel with the command. Both forms are shown in the examples.
- **Java:** the classic home of the pattern (`Runnable`, Swing `Action`); since lambdas, single-method commands are usually written as `Runnable`/`Consumer` instances.
- **C#:** `ICommand` in WPF/MVVM is this pattern institutionalized; delegates (`Action`) cover the non-undoable cases.
- **Rust:** a trait with `execute`/`undo` and `Box<dyn Command>` in a history vector; for one-shot commands, `Box<dyn FnOnce()>` suffices.
- **Go:** interfaces with `Execute`/`Undo` methods, or plain `func()` values for fire-and-forget commands.
- **C:** emulated with a struct of function pointers (`execute`, `undo`) plus a context pointer.
- **Swift:** protocol-based commands for undo; closures for simple actions. Foundation's `UndoManager` is the platform's built-in invoker.
- **PHP:** same class shape as Python; framework job/queue systems (Laravel jobs) are commands in production form.

## Examples

- [examples/command/command.py](../examples/command/command.py)
- [examples/command/command.c](../examples/command/command.c)
- [examples/command/command.cpp](../examples/command/command.cpp)
- [examples/command/command.java](../examples/command/command.java)
- [examples/command/command.cs](../examples/command/command.cs)
- [examples/command/command.js](../examples/command/command.js)
- [examples/command/command.rs](../examples/command/command.rs)
- [examples/command/command.go](../examples/command/command.go)
- [examples/command/command.php](../examples/command/command.php)
- [examples/command/command.swift](../examples/command/command.swift)

## Related Patterns

- **Memento** can store the receiver's snapshot for undo instead of the command computing an inverse operation.
- **Chain of Responsibility** handlers often receive command objects; a chain can decide which handler executes a command.
- **Strategy** also wraps behavior in an object, but a strategy is _how_ something is done while a command is _a request to do_ something (often carrying undo state).
- Composite commands (a command holding a list of commands) implement macros.
