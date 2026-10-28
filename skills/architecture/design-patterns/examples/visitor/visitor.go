// Visitor pattern in Go.
//
// Classic double dispatch via Accept(). Go's common alternative is a
// type switch (switch s := shape.(type)), which is fine for a handful
// of operations; the visitor interface pays off when many operations
// exist and each must handle every shape (the compiler enforces the
// interface, unlike a type switch's optional default).

package main

import (
	"fmt"
	"math"
)

type ShapeVisitor interface {
	VisitCircle(c Circle)
	VisitRectangle(r Rectangle)
	VisitTriangle(t Triangle)
}

type Shape interface {
	Accept(v ShapeVisitor)
}

type Circle struct {
	Radius float64
}

func (c Circle) Accept(v ShapeVisitor) { v.VisitCircle(c) }

type Rectangle struct {
	Width, Height float64
}

func (r Rectangle) Accept(v ShapeVisitor) { v.VisitRectangle(r) }

type Triangle struct {
	Base, Height float64
}

func (t Triangle) Accept(v ShapeVisitor) { v.VisitTriangle(t) }

type AreaVisitor struct {
	Area float64
}

func (a *AreaVisitor) VisitCircle(c Circle)       { a.Area = math.Pi * c.Radius * c.Radius }
func (a *AreaVisitor) VisitRectangle(r Rectangle) { a.Area = r.Width * r.Height }
func (a *AreaVisitor) VisitTriangle(t Triangle)   { a.Area = 0.5 * t.Base * t.Height }

type SvgExportVisitor struct {
	Markup string
}

func (s *SvgExportVisitor) VisitCircle(c Circle) {
	s.Markup = fmt.Sprintf(`<circle r="%g" />`, c.Radius)
}

func (s *SvgExportVisitor) VisitRectangle(r Rectangle) {
	s.Markup = fmt.Sprintf(`<rect width="%g" height="%g" />`, r.Width, r.Height)
}

func (s *SvgExportVisitor) VisitTriangle(t Triangle) {
	s.Markup = fmt.Sprintf(`<polygon points="0,%g %g,%g 0,0" />`, t.Height, t.Base, t.Height)
}

func main() {
	shapes := []Shape{Circle{2}, Rectangle{3, 4}, Triangle{6, 2}}

	area := &AreaVisitor{}
	svg := &SvgExportVisitor{}
	total := 0.0

	for _, shape := range shapes {
		shape.Accept(area)
		shape.Accept(svg)
		fmt.Printf("area=%6.2f  %s\n", area.Area, svg.Markup)
		total += area.Area
	}
	fmt.Printf("total area: %.2f\n", total)
}
