// Chain of Responsibility pattern in Rust.
//
// Support ticket escalation. Instead of linked next-pointers (which
// fight the borrow checker), the idiomatic Rust form iterates a
// Vec<Box<dyn Handler>> until one handler claims the request.

struct Ticket {
    subject: &'static str,
    severity: u8, // 1 (trivial) .. 4 (critical)
}

trait Handler {
    /// Returns true if the ticket was resolved at this level.
    fn handle(&self, ticket: &Ticket) -> bool;
}

struct SupportLevel {
    name: &'static str,
    max_severity: u8,
}

impl Handler for SupportLevel {
    fn handle(&self, ticket: &Ticket) -> bool {
        if ticket.severity <= self.max_severity {
            println!(
                "{} resolved \"{}\" (severity {})",
                self.name, ticket.subject, ticket.severity
            );
            true
        } else {
            false
        }
    }
}

struct Chain {
    handlers: Vec<Box<dyn Handler>>,
}

impl Chain {
    fn dispatch(&self, ticket: &Ticket) {
        if !self.handlers.iter().any(|h| h.handle(ticket)) {
            println!(
                "UNRESOLVED: \"{}\" (severity {}) -> escalate to engineering",
                ticket.subject, ticket.severity
            );
        }
    }
}

fn main() {
    let chain = Chain {
        handlers: vec![
            Box::new(SupportLevel { name: "Help bot", max_severity: 1 }),
            Box::new(SupportLevel { name: "Frontline agent", max_severity: 2 }),
            Box::new(SupportLevel { name: "Support manager", max_severity: 3 }),
        ],
    };

    let tickets = [
        Ticket { subject: "Reset my password", severity: 1 },
        Ticket { subject: "Invoice shows wrong amount", severity: 2 },
        Ticket { subject: "Account data corrupted", severity: 3 },
        Ticket { subject: "Full region outage", severity: 4 },
    ];

    for ticket in &tickets {
        chain.dispatch(ticket);
    }
}
