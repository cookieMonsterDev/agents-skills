// Abstract Factory pattern in Go.
//
// Small per-product interfaces plus a factory interface; concrete factories
// are zero-size structs. Implicit interface satisfaction means no family
// declares that it implements anything.

package main

import "fmt"

type Button interface {
	Render() string
}

type Checkbox interface {
	Render() string
}

type macButton struct{}
type macCheckbox struct{}
type windowsButton struct{}
type windowsCheckbox struct{}

func (macButton) Render() string       { return "( OK )  // rounded macOS button" }
func (macCheckbox) Render() string     { return "◉ Remember me  // macOS checkbox" }
func (windowsButton) Render() string   { return "[ OK ]  // rectangular Windows button" }
func (windowsCheckbox) Render() string { return "[x] Remember me  // Windows checkbox" }

// WidgetFactory has one creation method per product kind; products are
// guaranteed to match.
type WidgetFactory interface {
	CreateButton() Button
	CreateCheckbox() Checkbox
}

type MacFactory struct{}

func (MacFactory) CreateButton() Button     { return macButton{} }
func (MacFactory) CreateCheckbox() Checkbox { return macCheckbox{} }

type WindowsFactory struct{}

func (WindowsFactory) CreateButton() Button     { return windowsButton{} }
func (WindowsFactory) CreateCheckbox() Checkbox { return windowsCheckbox{} }

// renderDialog is the client: it depends only on the factory interface.
func renderDialog(factory WidgetFactory) {
	fmt.Println(factory.CreateButton().Render())
	fmt.Println(factory.CreateCheckbox().Render())
}

func main() {
	themes := []struct {
		name    string
		factory WidgetFactory
	}{
		{"macOS", MacFactory{}},
		{"Windows", WindowsFactory{}},
	}

	for _, theme := range themes {
		fmt.Printf("-- %s theme --\n", theme.name)
		renderDialog(theme.factory)
	}
}
