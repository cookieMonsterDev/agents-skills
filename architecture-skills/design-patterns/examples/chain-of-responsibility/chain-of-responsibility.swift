// Chain of Responsibility pattern in Swift.
//
// Support ticket escalation: a protocol-based chain where each level
// resolves tickets up to its competence or forwards them. UIKit's
// responder chain is the canonical platform incarnation.

struct Ticket {
    let subject: String
    let severity: Int // 1 (trivial) .. 4 (critical)
}

protocol Handler: AnyObject {
    var next: Handler? { get set }
    func handle(_ ticket: Ticket)
}

extension Handler {
    @discardableResult
    func setNext(_ handler: Handler) -> Handler {
        next = handler
        return handler // enables a.setNext(b).setNext(c)
    }

    func forward(_ ticket: Ticket) {
        if let next {
            next.handle(ticket)
        } else {
            print("UNRESOLVED: \"\(ticket.subject)\" (severity \(ticket.severity))"
                + " -> escalate to engineering")
        }
    }
}

final class SupportLevel: Handler {
    var next: Handler?
    private let name: String
    private let maxSeverity: Int

    init(name: String, maxSeverity: Int) {
        self.name = name
        self.maxSeverity = maxSeverity
    }

    func handle(_ ticket: Ticket) {
        if ticket.severity <= maxSeverity {
            print("\(name) resolved \"\(ticket.subject)\" (severity \(ticket.severity))")
        } else {
            forward(ticket)
        }
    }
}

let chain = SupportLevel(name: "Help bot", maxSeverity: 1)
chain.setNext(SupportLevel(name: "Frontline agent", maxSeverity: 2))
    .setNext(SupportLevel(name: "Support manager", maxSeverity: 3))

let tickets = [
    Ticket(subject: "Reset my password", severity: 1),
    Ticket(subject: "Invoice shows wrong amount", severity: 2),
    Ticket(subject: "Account data corrupted", severity: 3),
    Ticket(subject: "Full region outage", severity: 4),
]

for ticket in tickets {
    chain.handle(ticket)
}
