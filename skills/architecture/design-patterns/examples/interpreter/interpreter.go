// Interpreter pattern in Go.
//
// A tiny arithmetic grammar: literals, variables, +, -, *. A small Expr
// interface with one struct per grammar rule; a sentence is a struct
// tree evaluated against a map of variable bindings.

package main

import "fmt"

type Context map[string]int

type Expr interface {
	Interpret(ctx Context) int
}

type Literal struct {
	Value int
}

func (l Literal) Interpret(Context) int { return l.Value }

type Variable struct {
	Name string
}

func (v Variable) Interpret(ctx Context) int { return ctx[v.Name] }

type Add struct{ Left, Right Expr }

func (a Add) Interpret(ctx Context) int { return a.Left.Interpret(ctx) + a.Right.Interpret(ctx) }

type Sub struct{ Left, Right Expr }

func (s Sub) Interpret(ctx Context) int { return s.Left.Interpret(ctx) - s.Right.Interpret(ctx) }

type Mul struct{ Left, Right Expr }

func (m Mul) Interpret(ctx Context) int { return m.Left.Interpret(ctx) * m.Right.Interpret(ctx) }

func main() {
	// (x + y) * 2 - z
	expression := Sub{
		Left: Mul{
			Left:  Add{Left: Variable{"x"}, Right: Variable{"y"}},
			Right: Literal{2},
		},
		Right: Variable{"z"},
	}

	first := Context{"x": 6, "y": 2, "z": 3}
	second := Context{"x": 1, "y": 1, "z": 10}

	fmt.Printf("(x + y) * 2 - z with x=6 y=2 z=3   = %d\n", expression.Interpret(first))
	fmt.Printf("(x + y) * 2 - z with x=1 y=1 z=10  = %d\n", expression.Interpret(second))
}
