// Composite pattern in Go.
//
// Files and directories satisfy one small Node interface; a directory
// holds a []Node slice, so callers recurse without type switches.

package main

import (
	"fmt"
	"strings"
)

type Node interface {
	Size() int64
	Print(indent int)
}

type File struct {
	Name  string
	Bytes int64
}

func (f File) Size() int64 { return f.Bytes }

func (f File) Print(indent int) {
	fmt.Printf("%s%s (%d B)\n", strings.Repeat(" ", indent), f.Name, f.Bytes)
}

type Directory struct {
	Name     string
	Children []Node
}

func (d *Directory) Add(child Node) *Directory {
	d.Children = append(d.Children, child)
	return d
}

func (d *Directory) Size() int64 {
	var total int64
	for _, child := range d.Children {
		total += child.Size()
	}
	return total
}

func (d *Directory) Print(indent int) {
	fmt.Printf("%s%s/ (%d B)\n", strings.Repeat(" ", indent), d.Name, d.Size())
	for _, child := range d.Children {
		child.Print(indent + 2)
	}
}

func main() {
	src := (&Directory{Name: "src"}).
		Add(File{Name: "main.py", Bytes: 1200}).
		Add(File{Name: "util.py", Bytes: 450})
	docs := (&Directory{Name: "docs"}).Add(File{Name: "readme.md", Bytes: 800})

	project := (&Directory{Name: "project"}).
		Add(src).
		Add(docs).
		Add(File{Name: ".gitignore", Bytes: 20})

	project.Print(0)
}
