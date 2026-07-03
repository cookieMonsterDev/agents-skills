// Factory Method pattern in Go.
//
// Go has no inheritance, so the shared workflow is a plain function that
// accepts a creator interface (composition over subclassing). Concrete
// creators are small structs that supply only the factory method.

package main

import "fmt"

type Transport interface {
	Deliver(cargo string) string
}

type truck struct{}

func (truck) Deliver(cargo string) string {
	return "Truck delivers " + cargo + " by road in a box"
}

type ship struct{}

func (ship) Deliver(cargo string) string {
	return "Ship delivers " + cargo + " by sea in a container"
}

// Logistics is the creator: it supplies only the factory method.
type Logistics interface {
	Name() string
	CreateTransport() Transport
}

type RoadLogistics struct{}

func (RoadLogistics) Name() string               { return "RoadLogistics" }
func (RoadLogistics) CreateTransport() Transport { return truck{} }

type SeaLogistics struct{}

func (SeaLogistics) Name() string               { return "SeaLogistics" }
func (SeaLogistics) CreateTransport() Transport { return ship{} }

// PlanDelivery is the shared workflow, written once against the interface.
func PlanDelivery(logistics Logistics, cargo string) string {
	transport := logistics.CreateTransport()
	return "[" + logistics.Name() + "] " + transport.Deliver(cargo)
}

func main() {
	for _, logistics := range []Logistics{RoadLogistics{}, SeaLogistics{}} {
		fmt.Println(PlanDelivery(logistics, "machine parts"))
	}
}
