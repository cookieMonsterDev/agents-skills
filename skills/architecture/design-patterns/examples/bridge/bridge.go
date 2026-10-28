// Bridge pattern in Go.
//
// The shape structs hold a Renderer interface value, so shapes and
// renderers form two independent axes. No inheritance is needed: the
// "abstraction hierarchy" is just the types sharing the Shape interface.

package main

import "fmt"

type Renderer interface {
	Circle(radius float64) string
	Rectangle(width, height float64) string
}

type VectorRenderer struct{}

func (VectorRenderer) Circle(radius float64) string {
	return fmt.Sprintf("<circle r=%.1f/>", radius)
}
func (VectorRenderer) Rectangle(width, height float64) string {
	return fmt.Sprintf("<rect w=%.1f h=%.1f/>", width, height)
}

type RasterRenderer struct{}

func (RasterRenderer) Circle(radius float64) string {
	return fmt.Sprintf("pixels for a circle of radius %.1f", radius)
}
func (RasterRenderer) Rectangle(width, height float64) string {
	return fmt.Sprintf("pixels for a %.1fx%.1f rectangle", width, height)
}

type Shape interface {
	Draw() string
}

type Circle struct {
	Renderer Renderer
	Radius   float64
}

func (c Circle) Draw() string { return c.Renderer.Circle(c.Radius) }

type Rectangle struct {
	Renderer      Renderer
	Width, Height float64
}

func (r Rectangle) Draw() string { return r.Renderer.Rectangle(r.Width, r.Height) }

func main() {
	for _, renderer := range []Renderer{VectorRenderer{}, RasterRenderer{}} {
		shapes := []Shape{
			Circle{Renderer: renderer, Radius: 5},
			Rectangle{Renderer: renderer, Width: 3, Height: 4},
		}
		for _, shape := range shapes {
			fmt.Println(shape.Draw())
		}
	}
}
