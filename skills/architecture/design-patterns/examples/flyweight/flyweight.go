// Flyweight pattern in Go.
//
// The factory hands out *TreeType pointers from a map cache, so every
// oak/green tree shares one struct. Immutability of the shared state is
// by convention in Go: nothing mutates a TreeType after creation.

package main

import "fmt"

// TreeType is the flyweight: intrinsic state shared by many trees.
type TreeType struct {
	Name  string
	Color string
}

func (t *TreeType) Draw(x, y int) {
	fmt.Printf("%s %s at (%d, %d)\n", t.Color, t.Name, x, y)
}

type TreeTypeFactory struct {
	cache map[string]*TreeType
}

func NewTreeTypeFactory() *TreeTypeFactory {
	return &TreeTypeFactory{cache: map[string]*TreeType{}}
}

func (f *TreeTypeFactory) Get(name, color string) *TreeType {
	key := name + "/" + color
	if t, ok := f.cache[key]; ok {
		return t
	}
	t := &TreeType{Name: name, Color: color}
	f.cache[key] = t
	return t
}

func (f *TreeTypeFactory) Len() int { return len(f.cache) }

// Tree is the context: extrinsic state plus the shared flyweight.
type Tree struct {
	X, Y int
	Kind *TreeType
}

func main() {
	factory := NewTreeTypeFactory()
	forest := []Tree{
		{1, 1, factory.Get("oak", "green")},
		{2, 4, factory.Get("pine", "dark green")},
		{5, 2, factory.Get("oak", "green")},
		{6, 6, factory.Get("birch", "light green")},
		{8, 3, factory.Get("pine", "dark green")},
		{9, 9, factory.Get("oak", "green")},
	}

	for _, tree := range forest {
		tree.Kind.Draw(tree.X, tree.Y)
	}

	fmt.Printf("trees planted: %d, tree types in memory: %d\n", len(forest), factory.Len())
}
