// Decorator pattern in Go.
//
// Each add-on embeds the wrapped Beverage interface: methods that are
// not overridden would be promoted automatically, so a decorator only
// writes the behavior it changes. http.Handler middleware uses the
// same wrapping technique.

package main

import "fmt"

type Beverage interface {
	Description() string
	Cost() float64
}

type Espresso struct{}

func (Espresso) Description() string { return "espresso" }
func (Espresso) Cost() float64       { return 2.00 }

type Milk struct{ Beverage }

func (m Milk) Description() string { return m.Beverage.Description() + " + milk" }
func (m Milk) Cost() float64       { return m.Beverage.Cost() + 0.30 }

type Mocha struct{ Beverage }

func (m Mocha) Description() string { return m.Beverage.Description() + " + mocha" }
func (m Mocha) Cost() float64       { return m.Beverage.Cost() + 0.50 }

type WhippedCream struct{ Beverage }

func (w WhippedCream) Description() string { return w.Beverage.Description() + " + whipped cream" }
func (w WhippedCream) Cost() float64       { return w.Beverage.Cost() + 0.40 }

func main() {
	plain := Espresso{}
	fancy := WhippedCream{Mocha{Milk{Espresso{}}}}
	for _, drink := range []Beverage{plain, fancy} {
		fmt.Printf("%s: $%.2f\n", drink.Description(), drink.Cost())
	}
}
