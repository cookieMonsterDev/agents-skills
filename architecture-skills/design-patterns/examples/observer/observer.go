// Observer pattern in Go.
//
// A one-method interface keeps observers decoupled; structs and funcs
// (via an adapter, like http.HandlerFunc) can both subscribe. For
// concurrent programs, Go usually prefers channels: each observer
// reads from its own channel and the subject fans out.

package main

import "fmt"

type PriceObserver interface {
	OnPrice(symbol string, price float64)
}

// ObserverFunc adapts a plain function to the interface.
type ObserverFunc func(symbol string, price float64)

func (f ObserverFunc) OnPrice(symbol string, price float64) { f(symbol, price) }

type StockTicker struct { // subject
	observers []PriceObserver
}

func (t *StockTicker) Subscribe(o PriceObserver) {
	t.observers = append(t.observers, o)
}

func (t *StockTicker) Unsubscribe(o PriceObserver) {
	for i, existing := range t.observers {
		if existing == o {
			t.observers = append(t.observers[:i], t.observers[i+1:]...)
			return
		}
	}
}

func (t *StockTicker) UpdatePrice(symbol string, price float64) {
	for _, o := range t.observers {
		o.OnPrice(symbol, price)
	}
}

type PriceDisplay struct {
	Name string
}

func (d *PriceDisplay) OnPrice(symbol string, price float64) {
	fmt.Printf("%s: %s is now $%.2f\n", d.Name, symbol, price)
}

func main() {
	ticker := &StockTicker{}
	display := &PriceDisplay{Name: "Lobby display"}
	ticker.Subscribe(display)

	ticker.Subscribe(ObserverFunc(func(symbol string, price float64) {
		if symbol == "ACME" && price > 100 {
			fmt.Printf("ALERT: ACME crossed $100.00 (now $%.2f)\n", price)
		}
	}))

	ticker.UpdatePrice("ACME", 98.5)
	ticker.UpdatePrice("ACME", 101.25)

	ticker.Unsubscribe(display)
	ticker.UpdatePrice("GLOBEX", 45) // only the alert remains
}
