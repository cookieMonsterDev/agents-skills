// Chain of Responsibility pattern in Java.
//
// Support ticket escalation: an abstract handler holds the next link;
// each level resolves tickets up to its competence or forwards them.
// Servlet filters are the same pattern built into the platform.
//
// The top-level class is package-private so the filename does not have
// to match a (hyphen-containing) public class name.

import java.util.List;

class ChainOfResponsibilityDemo {

    record Ticket(String subject, int severity) {} // severity 1..4

    abstract static class Handler {
        private Handler next;

        Handler setNext(Handler handler) {
            this.next = handler;
            return handler; // enables a.setNext(b).setNext(c)
        }

        void handle(Ticket ticket) {
            if (next != null) {
                next.handle(ticket);
            } else {
                System.out.printf("UNRESOLVED: \"%s\" (severity %d) -> escalate to engineering%n",
                        ticket.subject(), ticket.severity());
            }
        }
    }

    static final class SupportLevel extends Handler {
        private final String name;
        private final int maxSeverity;

        SupportLevel(String name, int maxSeverity) {
            this.name = name;
            this.maxSeverity = maxSeverity;
        }

        @Override
        void handle(Ticket ticket) {
            if (ticket.severity() <= maxSeverity) {
                System.out.printf("%s resolved \"%s\" (severity %d)%n",
                        name, ticket.subject(), ticket.severity());
            } else {
                super.handle(ticket);
            }
        }
    }

    public static void main(String[] args) {
        Handler chain = new SupportLevel("Help bot", 1);
        chain.setNext(new SupportLevel("Frontline agent", 2))
                .setNext(new SupportLevel("Support manager", 3));

        List<Ticket> tickets = List.of(
                new Ticket("Reset my password", 1),
                new Ticket("Invoice shows wrong amount", 2),
                new Ticket("Account data corrupted", 3),
                new Ticket("Full region outage", 4));

        for (Ticket ticket : tickets) {
            chain.handle(ticket);
        }
    }
}
