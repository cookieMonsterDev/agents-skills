// Dependency Inversion Principle in Swift.
//
// OrderService owns the Notifier protocol and receives an implementation
// through its initializer — never SmtpNotifier(). main is the composition
// root that wires ConsoleNotifier or RecordingNotifier.

import Foundation

struct Order {
    let id: String
    let customerEmail: String
}

/// Abstraction owned by policy: shaped to what place() needs.
protocol Notifier {
    func notify(email: String, message: String)
}

final class OrderService {
    private let notifier: Notifier

    init(notifier: Notifier) {
        self.notifier = notifier
    }

    func place(_ order: Order) {
        print("placed \(order.id) for \(order.customerEmail)")
        notifier.notify(
            email: order.customerEmail,
            message: "order \(order.id) confirmed",
        )
    }
}

// --- Low-level details: depend on the policy's protocol ---

final class ConsoleNotifier: Notifier {
    func notify(email: String, message: String) {
        print("notify \(email): \(message)")
    }
}

final class RecordingNotifier: Notifier {
    private(set) var sent: [(String, String)] = []

    func notify(email: String, message: String) {
        sent.append((email, message))
    }
}

print("-- ConsoleNotifier at composition root --")
OrderService(notifier: ConsoleNotifier()).place(
    Order(id: "ORD-001", customerEmail: "alice@example.com"),
)

print("\n-- RecordingNotifier: policy testable without I/O --")
let recorder = RecordingNotifier()
OrderService(notifier: recorder).place(
    Order(id: "ORD-002", customerEmail: "bob@example.com"),
)
print("\(recorder.sent.count) notification(s) recorded")
