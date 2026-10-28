// Strategy pattern in Go.
//
// Go usually skips the one-method interface: a named function type is
// the strategy, plain functions and closures implement it (compare
// http.HandlerFunc). An interface is only needed when strategies have
// several methods.

package main

import "fmt"

type Order struct {
	WeightKg   float64
	DistanceKm float64
}

// ShippingStrategy is the strategy: any func with this signature fits.
type ShippingStrategy func(Order) float64

func flatRate(Order) float64 {
	return 5.00
}

func weightBased(o Order) float64 {
	return 4.00 + 1.50*o.WeightKg
}

func distanceBased(o Order) float64 {
	return 2.00 + 0.05*o.DistanceKm
}

// A stateful strategy: a closure captures the negotiated rates.
func carrierRate(base, perKg float64) ShippingStrategy {
	return func(o Order) float64 {
		return base + perKg*o.WeightKg
	}
}

// Checkout is the context: it delegates pricing to the current strategy.
type Checkout struct {
	strategy ShippingStrategy
}

func (c *Checkout) SetStrategy(s ShippingStrategy) {
	c.strategy = s
}

func (c *Checkout) ShippingFor(o Order) float64 {
	return c.strategy(o)
}

func main() {
	order := Order{WeightKg: 2.4, DistanceKm: 120}

	strategies := []struct {
		name     string
		strategy ShippingStrategy
	}{
		{"flat", flatRate},
		{"weight", weightBased},
		{"distance", distanceBased},
		{"carrier", carrierRate(3.00, 2.00)},
	}

	checkout := &Checkout{strategy: flatRate}
	for _, s := range strategies {
		checkout.SetStrategy(s.strategy)
		fmt.Printf("%8s: $%.2f\n", s.name, checkout.ShippingFor(order))
	}
}
