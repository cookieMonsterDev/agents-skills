// Iterator pattern in Go.
//
// A binary search tree traversed in sorted order. Since Go 1.23 the
// pattern is built in as range-over-func iterators: a method returning
// iter.Seq[T] (a func(yield func(T) bool)) works directly with range,
// so no hand-rolled Next() interface is needed. The yield callback's
// bool return handles early loop exit (break).

package main

import (
	"fmt"
	"iter"
)

type node struct {
	value       int
	left, right *node
}

// SortedTree is the custom collection: an unbalanced binary search tree.
type SortedTree struct {
	root *node
}

func (t *SortedTree) Add(value int) {
	slot := &t.root
	for *slot != nil {
		if value < (*slot).value {
			slot = &(*slot).left
		} else {
			slot = &(*slot).right
		}
	}
	*slot = &node{value: value}
}

// InOrder returns a reusable iterator over the values in sorted order.
func (t *SortedTree) InOrder() iter.Seq[int] {
	return func(yield func(int) bool) {
		walk(t.root, yield)
	}
}

func walk(n *node, yield func(int) bool) bool {
	if n == nil {
		return true
	}
	return walk(n.left, yield) && yield(n.value) && walk(n.right, yield)
}

func main() {
	tree := &SortedTree{}
	for _, value := range []int{5, 3, 8, 1, 4, 9, 7} {
		tree.Add(value)
	}

	fmt.Print("in order:")
	for value := range tree.InOrder() {
		fmt.Printf(" %d", value)
	}
	fmt.Println()

	sum := 0
	for value := range tree.InOrder() {
		sum += value
	}
	fmt.Println("sum:", sum)
}
