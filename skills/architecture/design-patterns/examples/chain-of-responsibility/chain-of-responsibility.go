// Chain of Responsibility pattern in Go.
//
// Support ticket escalation. Go favors small interfaces or plain
// functions over linked handler objects: here the chain is a slice of
// handler funcs tried in order. net/http middleware wrapping
// (func(next http.Handler) http.Handler) is the same idea.

package main

import "fmt"

type Ticket struct {
	Subject  string
	Severity int // 1 (trivial) .. 4 (critical)
}

// HandlerFunc reports whether it resolved the ticket.
type HandlerFunc func(Ticket) bool

func supportLevel(name string, maxSeverity int) HandlerFunc {
	return func(t Ticket) bool {
		if t.Severity <= maxSeverity {
			fmt.Printf("%s resolved %q (severity %d)\n", name, t.Subject, t.Severity)
			return true
		}
		return false
	}
}

type Chain []HandlerFunc

func (c Chain) Dispatch(t Ticket) {
	for _, handle := range c {
		if handle(t) {
			return
		}
	}
	fmt.Printf("UNRESOLVED: %q (severity %d) -> escalate to engineering\n",
		t.Subject, t.Severity)
}

func main() {
	chain := Chain{
		supportLevel("Help bot", 1),
		supportLevel("Frontline agent", 2),
		supportLevel("Support manager", 3),
	}

	tickets := []Ticket{
		{"Reset my password", 1},
		{"Invoice shows wrong amount", 2},
		{"Account data corrupted", 3},
		{"Full region outage", 4},
	}

	for _, ticket := range tickets {
		chain.Dispatch(ticket)
	}
}
