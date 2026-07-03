// Abstract Factory pattern in C++.
//
// Abstract products and factory are pure-virtual classes; factories hand
// back unique_ptr so ownership is explicit. The client renders a dialog
// through the abstract interfaces only.

#include <iostream>
#include <memory>
#include <string>

class Button {
public:
    virtual ~Button() = default;
    virtual std::string render() const = 0;
};

class Checkbox {
public:
    virtual ~Checkbox() = default;
    virtual std::string render() const = 0;
};

class MacButton : public Button {
public:
    std::string render() const override { return "( OK )  // rounded macOS button"; }
};

class MacCheckbox : public Checkbox {
public:
    std::string render() const override { return "◉ Remember me  // macOS checkbox"; }
};

class WindowsButton : public Button {
public:
    std::string render() const override { return "[ OK ]  // rectangular Windows button"; }
};

class WindowsCheckbox : public Checkbox {
public:
    std::string render() const override { return "[x] Remember me  // Windows checkbox"; }
};

class WidgetFactory {
public:
    virtual ~WidgetFactory() = default;
    virtual std::unique_ptr<Button> createButton() const = 0;
    virtual std::unique_ptr<Checkbox> createCheckbox() const = 0;
};

class MacFactory : public WidgetFactory {
public:
    std::unique_ptr<Button> createButton() const override { return std::make_unique<MacButton>(); }
    std::unique_ptr<Checkbox> createCheckbox() const override { return std::make_unique<MacCheckbox>(); }
};

class WindowsFactory : public WidgetFactory {
public:
    std::unique_ptr<Button> createButton() const override { return std::make_unique<WindowsButton>(); }
    std::unique_ptr<Checkbox> createCheckbox() const override { return std::make_unique<WindowsCheckbox>(); }
};

// Client code: depends only on the abstract factory and products.
void renderDialog(const WidgetFactory& factory) {
    std::cout << factory.createButton()->render() << '\n';
    std::cout << factory.createCheckbox()->render() << '\n';
}

int main() {
    std::cout << "-- macOS theme --\n";
    renderDialog(MacFactory{});

    std::cout << "-- Windows theme --\n";
    renderDialog(WindowsFactory{});
    return 0;
}
