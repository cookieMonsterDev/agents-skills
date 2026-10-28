// Prototype pattern in Go.
//
// Struct assignment already copies value fields, but slices and maps are
// shared by such a copy. An explicit Clone method duplicates them, which
// is the whole point of the pattern in Go.

package main

import "fmt"

type Circle struct {
	X, Y   float64
	Radius float64
	Color  string
	Tags   []string
}

// Clone deep-copies the slice; `copy := *c` alone would alias Tags.
func (c *Circle) Clone() *Circle {
	clone := *c
	clone.Tags = append([]string(nil), c.Tags...)
	return &clone
}

func (c *Circle) Describe() string {
	return fmt.Sprintf("Circle r=%.0f %s at (%.0f, %.0f) tags=%v",
		c.Radius, c.Color, c.X, c.Y, c.Tags)
}

// ShapeRegistry is a catalog of pre-configured prototypes, cloned instead
// of constructed.
type ShapeRegistry struct {
	prototypes map[string]*Circle
}

func NewShapeRegistry() *ShapeRegistry {
	return &ShapeRegistry{prototypes: map[string]*Circle{}}
}

func (r *ShapeRegistry) Register(name string, prototype *Circle) {
	r.prototypes[name] = prototype
}

func (r *ShapeRegistry) Create(name string) *Circle {
	return r.prototypes[name].Clone()
}

func main() {
	registry := NewShapeRegistry()
	registry.Register("warning-marker", &Circle{
		Radius: 12,
		Color:  "red",
		Tags:   []string{"alert"},
	})

	first := registry.Create("warning-marker")
	second := registry.Create("warning-marker")
	second.X, second.Y = 40, 25
	second.Tags = append(second.Tags, "muted")

	fmt.Println(first.Describe())
	fmt.Println(second.Describe())
	// first still has one tag: appending to second's slice didn't touch it.
	fmt.Println("independent copies:", len(first.Tags) == 1)
}
