<?php
// Chain of Responsibility pattern in PHP.
//
// Support ticket escalation: an abstract handler holds the next link;
// each level resolves tickets up to its competence or forwards them.
// PSR-15 HTTP middleware is the same pattern in production form.

declare(strict_types=1);

final class Ticket
{
    public function __construct(
        public readonly string $subject,
        public readonly int $severity, // 1 (trivial) .. 4 (critical)
    ) {
    }
}

abstract class Handler
{
    private ?Handler $next = null;

    public function setNext(Handler $handler): Handler
    {
        $this->next = $handler;
        return $handler; // enables $a->setNext($b)->setNext($c)
    }

    public function handle(Ticket $ticket): void
    {
        if ($this->next !== null) {
            $this->next->handle($ticket);
        } else {
            printf(
                "UNRESOLVED: \"%s\" (severity %d) -> escalate to engineering\n",
                $ticket->subject,
                $ticket->severity,
            );
        }
    }
}

final class SupportLevel extends Handler
{
    public function __construct(
        private readonly string $name,
        private readonly int $maxSeverity,
    ) {
    }

    public function handle(Ticket $ticket): void
    {
        if ($ticket->severity <= $this->maxSeverity) {
            printf(
                "%s resolved \"%s\" (severity %d)\n",
                $this->name,
                $ticket->subject,
                $ticket->severity,
            );
        } else {
            parent::handle($ticket);
        }
    }
}

$chain = new SupportLevel('Help bot', 1);
$chain->setNext(new SupportLevel('Frontline agent', 2))
    ->setNext(new SupportLevel('Support manager', 3));

$tickets = [
    new Ticket('Reset my password', 1),
    new Ticket('Invoice shows wrong amount', 2),
    new Ticket('Account data corrupted', 3),
    new Ticket('Full region outage', 4),
];

foreach ($tickets as $ticket) {
    $chain->handle($ticket);
}
