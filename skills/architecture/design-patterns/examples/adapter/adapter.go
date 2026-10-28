// Adapter pattern in Go.
//
// Go interfaces are satisfied implicitly, so an adapter is just a small
// struct (or function type) that wraps the legacy value and adds the
// missing methods — the same trick http.HandlerFunc uses to adapt a
// plain function to the http.Handler interface.

package main

import "fmt"

type TemperatureSource interface {
	Name() string
	Celsius() float64
}

type ModernSensor struct {
	label   string
	celsius float64
}

func (s ModernSensor) Name() string     { return s.label }
func (s ModernSensor) Celsius() float64 { return s.celsius }

// LegacyFahrenheitSensor is the adaptee we cannot change.
type LegacyFahrenheitSensor struct {
	SensorID   string
	fahrenheit float64
}

func (s LegacyFahrenheitSensor) ReadFahrenheit() float64 { return s.fahrenheit }

// FahrenheitAdapter makes the legacy sensor satisfy TemperatureSource.
type FahrenheitAdapter struct {
	Legacy LegacyFahrenheitSensor
}

func (a FahrenheitAdapter) Name() string { return a.Legacy.SensorID }
func (a FahrenheitAdapter) Celsius() float64 {
	return (a.Legacy.ReadFahrenheit() - 32.0) * 5.0 / 9.0
}

func report(sources []TemperatureSource) {
	for _, source := range sources {
		fmt.Printf("%s: %.1f°C\n", source.Name(), source.Celsius())
	}
}

func main() {
	report([]TemperatureSource{
		ModernSensor{label: "server-room", celsius: 21.5},
		FahrenheitAdapter{Legacy: LegacyFahrenheitSensor{SensorID: "warehouse-legacy", fahrenheit: 77.0}},
	})
}
