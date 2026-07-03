// State pattern in Go.
//
// Each state is a small struct implementing a state interface; the
// machine embeds the current state and delegates to it. For simple
// machines a switch over an int/string state is common Go; the
// interface form pays off when per-state behavior grows.

package main

import "fmt"

type state interface {
	InsertCoin(m *VendingMachine)
	SelectItem(m *VendingMachine)
}

type VendingMachine struct { // context
	state state
	stock int
}

func NewVendingMachine(stock int) *VendingMachine {
	m := &VendingMachine{stock: stock}
	if stock > 0 {
		m.state = idle{}
	} else {
		m.state = soldOut{}
	}
	return m
}

func (m *VendingMachine) InsertCoin() { m.state.InsertCoin(m) }
func (m *VendingMachine) SelectItem() { m.state.SelectItem(m) }

type idle struct{}

func (idle) InsertCoin(m *VendingMachine) {
	fmt.Println("coin accepted")
	m.state = hasCoin{}
}

func (idle) SelectItem(*VendingMachine) {
	fmt.Println("insert a coin first")
}

type hasCoin struct{}

func (hasCoin) InsertCoin(*VendingMachine) {
	fmt.Println("coin already inserted, returning it")
}

func (hasCoin) SelectItem(m *VendingMachine) {
	m.stock--
	fmt.Printf("item dispensed (%d left)\n", m.stock)
	if m.stock == 0 {
		m.state = soldOut{}
	} else {
		m.state = idle{}
	}
}

type soldOut struct{}

func (soldOut) InsertCoin(*VendingMachine) {
	fmt.Println("sold out, returning coin")
}

func (soldOut) SelectItem(*VendingMachine) {
	fmt.Println("sold out")
}

func main() {
	machine := NewVendingMachine(2)
	machine.SelectItem() // insert a coin first
	machine.InsertCoin()
	machine.InsertCoin() // coin already inserted
	machine.SelectItem() // item dispensed (1 left)
	machine.InsertCoin()
	machine.SelectItem() // item dispensed (0 left)
	machine.InsertCoin() // sold out, returning coin
}
