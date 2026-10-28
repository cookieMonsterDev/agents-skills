<?php
// Dependency Inversion Principle in PHP.
//
// OrderService owns the Notifier interface and receives an implementation
// through its constructor — never `new SmtpNotifier(...)`. main() is the
// composition root that wires ConsoleNotifier or RecordingNotifier.

declare(strict_types=1);

final readonly class Order
{
    public function __construct(
        public string $id,
        public string $customerEmail,
    ) {}
}

/** Abstraction owned by policy: shaped to what place() needs. */
interface Notifier
{
    public function notify(string $email, string $message): void;
}

final class OrderService
{
    public function __construct(private Notifier $notifier) {}

    public function place(Order $order): void
    {
        echo "placed {$order->id} for {$order->customerEmail}\n";
        $this->notifier->notify(
            $order->customerEmail,
            "order {$order->id} confirmed",
        );
    }
}

// --- Low-level details: depend on the policy's interface ---

final class ConsoleNotifier implements Notifier
{
    public function notify(string $email, string $message): void
    {
        echo "notify {$email}: {$message}\n";
    }
}

final class RecordingNotifier implements Notifier
{
    /** @var list<array{string, string}> */
    public array $sent = [];

    public function notify(string $email, string $message): void
    {
        $this->sent[] = [$email, $message];
    }
}

function main(): void
{
    echo "-- ConsoleNotifier at composition root --\n";
    (new OrderService(new ConsoleNotifier()))->place(
        new Order('ORD-001', 'alice@example.com'),
    );

    echo "\n-- RecordingNotifier: policy testable without I/O --\n";
    $recorder = new RecordingNotifier();
    (new OrderService($recorder))->place(
        new Order('ORD-002', 'bob@example.com'),
    );
    echo count($recorder->sent) . " notification(s) recorded\n";
}

main();
