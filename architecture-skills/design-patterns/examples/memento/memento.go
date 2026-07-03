// Memento pattern in Go.
//
// The snapshot's fields are unexported, so outside this package the
// history could store snapshots without reading them — Go's package
// boundary is the opacity mechanism. Value semantics (returning the
// struct by value) give the caretaker an independent copy for free.

package main

import "fmt"

type snapshot struct { // memento
	text   string
	cursor int
}

type TextEditor struct { // originator
	text   string
	cursor int
}

func (e *TextEditor) Type(insert string) {
	e.text = e.text[:e.cursor] + insert + e.text[e.cursor:]
	e.cursor += len(insert)
}

func (e *TextEditor) Save() snapshot {
	return snapshot{text: e.text, cursor: e.cursor}
}

func (e *TextEditor) Restore(s snapshot) {
	e.text = s.text
	e.cursor = s.cursor
}

func (e *TextEditor) String() string {
	return fmt.Sprintf("'%s' (cursor at %d)", e.text, e.cursor)
}

type History struct { // caretaker
	snapshots []snapshot
}

func (h *History) Push(s snapshot) {
	h.snapshots = append(h.snapshots, s)
}

func (h *History) Pop() (snapshot, bool) {
	if len(h.snapshots) == 0 {
		return snapshot{}, false
	}
	s := h.snapshots[len(h.snapshots)-1]
	h.snapshots = h.snapshots[:len(h.snapshots)-1]
	return s, true
}

func main() {
	editor := &TextEditor{}
	history := &History{}

	editor.Type("Hello")
	history.Push(editor.Save())
	editor.Type(", world")
	history.Push(editor.Save())
	editor.Type("!!!")
	fmt.Println("current:", editor)

	for i := 0; i < 2; i++ {
		if s, ok := history.Pop(); ok {
			editor.Restore(s)
			fmt.Println("undo:   ", editor)
		}
	}
}
