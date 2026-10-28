/* Chain of Responsibility pattern in C.
 *
 * Support ticket escalation. C has no classes, so polymorphism is
 * emulated with a Handler struct holding a function pointer and a
 * next pointer: each handler either resolves the ticket or forwards
 * it along the chain.
 */

#include <stdio.h>

typedef struct {
    const char *subject;
    int severity; /* 1 (trivial) .. 4 (critical) */
} Ticket;

typedef struct Handler Handler;
struct Handler {
    const char *name;
    int max_severity;
    /* Returns 1 if the ticket was resolved at this level. */
    int (*handle)(const Handler *self, const Ticket *ticket);
    const Handler *next;
};

static void dispatch(const Handler *first, const Ticket *ticket) {
    for (const Handler *h = first; h != NULL; h = h->next) {
        if (h->handle(h, ticket)) {
            return;
        }
    }
    printf("UNRESOLVED: \"%s\" (severity %d) -> escalate to engineering\n",
           ticket->subject, ticket->severity);
}

static int support_level_handle(const Handler *self, const Ticket *ticket) {
    if (ticket->severity <= self->max_severity) {
        printf("%s resolved \"%s\" (severity %d)\n",
               self->name, ticket->subject, ticket->severity);
        return 1;
    }
    return 0;
}

int main(void) {
    Handler manager = {"Support manager", 3, support_level_handle, NULL};
    Handler frontline = {"Frontline agent", 2, support_level_handle, &manager};
    Handler bot = {"Help bot", 1, support_level_handle, &frontline};

    const Ticket tickets[] = {
        {"Reset my password", 1},
        {"Invoice shows wrong amount", 2},
        {"Account data corrupted", 3},
        {"Full region outage", 4},
    };

    for (size_t i = 0; i < sizeof(tickets) / sizeof(tickets[0]); i++) {
        dispatch(&bot, &tickets[i]);
    }
    return 0;
}
