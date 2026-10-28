// Dependency Inversion Principle in JavaScript.
//
// OrderService owns the notifier duck contract and receives an
// implementation through its constructor — never `new SmtpNotifier()`.
// main() is the composition root that wires ConsoleNotifier or
// RecordingNotifier.

class OrderService {
  constructor(notifier) {
    this._notifier = notifier;
  }

  place(order) {
    console.log(`placed ${order.id} for ${order.customerEmail}`);
    this._notifier.notify(
      order.customerEmail,
      `order ${order.id} confirmed`,
    );
  }
}

// --- Low-level details: conform to the policy's contract ---

class ConsoleNotifier {
  notify(email, message) {
    console.log(`notify ${email}: ${message}`);
  }
}

class RecordingNotifier {
  constructor() {
    this.sent = [];
  }

  notify(email, message) {
    this.sent.push([email, message]);
  }
}

function main() {
  console.log('-- ConsoleNotifier at composition root --');
  new OrderService(new ConsoleNotifier()).place({
    id: 'ORD-001',
    customerEmail: 'alice@example.com',
  });

  console.log('\n-- RecordingNotifier: policy testable without I/O --');
  const recorder = new RecordingNotifier();
  new OrderService(recorder).place({
    id: 'ORD-002',
    customerEmail: 'bob@example.com',
  });
  console.log(`${recorder.sent.length} notification(s) recorded`);
}

main();
