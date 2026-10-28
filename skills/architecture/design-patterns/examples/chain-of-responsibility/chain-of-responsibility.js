// Chain of Responsibility pattern in JavaScript.
//
// Support ticket escalation, written middleware-style: each handler is a
// function (ticket, next) => ... that either resolves the ticket or calls
// next(). This is the native JS shape of the pattern (compare Express or
// Koa middleware); a class hierarchy is rarely needed.

const supportLevel = (name, maxSeverity) => (ticket, next) => {
  if (ticket.severity <= maxSeverity) {
    console.log(`${name} resolved "${ticket.subject}" (severity ${ticket.severity})`);
  } else {
    next(ticket);
  }
};

const unresolved = (ticket) => {
  console.log(
    `UNRESOLVED: "${ticket.subject}" (severity ${ticket.severity}) -> escalate to engineering`,
  );
};

// Compose handlers right-to-left so the first argument is tried first.
function buildChain(handlers, fallback) {
  return handlers.reduceRight(
    (next, handler) => (ticket) => handler(ticket, next),
    fallback,
  );
}

const handle = buildChain(
  [
    supportLevel("Help bot", 1),
    supportLevel("Frontline agent", 2),
    supportLevel("Support manager", 3),
  ],
  unresolved,
);

const tickets = [
  { subject: "Reset my password", severity: 1 },
  { subject: "Invoice shows wrong amount", severity: 2 },
  { subject: "Account data corrupted", severity: 3 },
  { subject: "Full region outage", severity: 4 },
];

for (const ticket of tickets) {
  handle(ticket);
}
