// Dependency Inversion Principle in Java.
//
// OrderService owns the Notifier interface and receives an implementation
// through its constructor — never `new SmtpNotifier(...)`. main() is the
// composition root that wires ConsoleNotifier or RecordingNotifier.
//
// Java identifiers cannot contain hyphens; a package-private class keeps
// the single-file source launcher (`java dependency-inversion.java`) working.

import java.util.ArrayList;
import java.util.List;

class DependencyInversion {

    record Order(String id, String customerEmail) {}

    /** Abstraction owned by policy: shaped to what place() needs. */
    interface Notifier {
        void notify(String email, String message);
    }

    static final class OrderService {
        private final Notifier notifier;

        OrderService(Notifier notifier) {
            this.notifier = notifier;
        }

        void place(Order order) {
            System.out.printf("placed %s for %s%n", order.id(), order.customerEmail());
            notifier.notify(order.customerEmail(), "order " + order.id() + " confirmed");
        }
    }

    // --- Low-level details: depend on the policy's interface ---

    static final class ConsoleNotifier implements Notifier {
        public void notify(String email, String message) {
            System.out.printf("notify %s: %s%n", email, message);
        }
    }

    static final class RecordingNotifier implements Notifier {
        final List<String[]> sent = new ArrayList<>();

        public void notify(String email, String message) {
            sent.add(new String[] { email, message });
        }
    }

    public static void main(String[] args) {
        System.out.println("-- ConsoleNotifier at composition root --");
        new OrderService(new ConsoleNotifier())
                .place(new Order("ORD-001", "alice@example.com"));

        System.out.println("\n-- RecordingNotifier: policy testable without I/O --");
        RecordingNotifier recorder = new RecordingNotifier();
        new OrderService(recorder)
                .place(new Order("ORD-002", "bob@example.com"));
        System.out.printf("%d notification(s) recorded%n", recorder.sent.size());
    }
}
