// Abstract Factory pattern in Swift.
//
// Protocols model both the products and the factory. The client is written
// as a generic function over the factory protocol, which avoids existential
// (`any`) overhead while staying fully abstract.

import Foundation

protocol Button {
    func render() -> String
}

protocol Checkbox {
    func render() -> String
}

struct MacButton: Button {
    func render() -> String { "( OK )  // rounded macOS button" }
}

struct MacCheckbox: Checkbox {
    func render() -> String { "◉ Remember me  // macOS checkbox" }
}

struct WindowsButton: Button {
    func render() -> String { "[ OK ]  // rectangular Windows button" }
}

struct WindowsCheckbox: Checkbox {
    func render() -> String { "[x] Remember me  // Windows checkbox" }
}

/// One creation method per product kind; products are guaranteed to match.
protocol WidgetFactory {
    func createButton() -> Button
    func createCheckbox() -> Checkbox
}

struct MacFactory: WidgetFactory {
    func createButton() -> Button { MacButton() }
    func createCheckbox() -> Checkbox { MacCheckbox() }
}

struct WindowsFactory: WidgetFactory {
    func createButton() -> Button { WindowsButton() }
    func createCheckbox() -> Checkbox { WindowsCheckbox() }
}

/// Client code: depends only on the factory protocol, never on a family.
func renderDialog<F: WidgetFactory>(using factory: F) {
    print(factory.createButton().render())
    print(factory.createCheckbox().render())
}

print("-- macOS theme --")
renderDialog(using: MacFactory())

print("-- Windows theme --")
renderDialog(using: WindowsFactory())
