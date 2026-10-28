// Command pattern in Go.
//
// Text editor with undo: a small Command interface with Execute/Undo
// and a history slice as the invoker. For fire-and-forget commands
// without undo, a plain func() value is the idiomatic Go form.

package main

import "fmt"

// Editor is the receiver.
type Editor struct {
	Text string
}

type Command interface {
	Execute()
	Undo()
}

type InsertText struct {
	editor *Editor
	text   string
}

func (c *InsertText) Execute() { c.editor.Text += c.text }
func (c *InsertText) Undo()    { c.editor.Text = c.editor.Text[:len(c.editor.Text)-len(c.text)] }

type DeleteLast struct {
	editor  *Editor
	count   int
	deleted string // captured on Execute so Undo can restore it
}

func (c *DeleteLast) Execute() {
	split := len(c.editor.Text) - c.count
	c.deleted = c.editor.Text[split:]
	c.editor.Text = c.editor.Text[:split]
}

func (c *DeleteLast) Undo() { c.editor.Text += c.deleted }

// History is the invoker: it runs commands and tracks them for undo.
type History struct {
	undoStack []Command
}

func (h *History) Execute(c Command) {
	c.Execute()
	h.undoStack = append(h.undoStack, c)
}

func (h *History) Undo() {
	if n := len(h.undoStack); n > 0 {
		h.undoStack[n-1].Undo()
		h.undoStack = h.undoStack[:n-1]
	}
}

func main() {
	editor := &Editor{}
	history := &History{}

	history.Execute(&InsertText{editor, "Hello"})
	history.Execute(&InsertText{editor, ", world!"})
	history.Execute(&DeleteLast{editor: editor, count: 1})
	fmt.Printf("after edits: %q\n", editor.Text)

	history.Undo()
	history.Undo()
	fmt.Printf("after 2 undos: %q\n", editor.Text)
}
