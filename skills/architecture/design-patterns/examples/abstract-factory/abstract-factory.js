// Abstract Factory pattern in JavaScript.
//
// Note: with first-class functions, a factory can be a plain object literal
// of constructors — shown here instead of class hierarchies. Duck typing
// replaces the abstract interfaces; each factory returns a matched family.

class MacButton {
  render() {
    return "( OK )  // rounded macOS button";
  }
}

class MacCheckbox {
  render() {
    return "◉ Remember me  // macOS checkbox";
  }
}

class WindowsButton {
  render() {
    return "[ OK ]  // rectangular Windows button";
  }
}

class WindowsCheckbox {
  render() {
    return "[x] Remember me  // Windows checkbox";
  }
}

// Each factory is an object literal with one creation method per product
// kind. Anything with the same shape works — no interface needed.
const macFactory = {
  name: "macOS",
  createButton: () => new MacButton(),
  createCheckbox: () => new MacCheckbox(),
};

const windowsFactory = {
  name: "Windows",
  createButton: () => new WindowsButton(),
  createCheckbox: () => new WindowsCheckbox(),
};

// Client code: depends only on the factory shape, never on a family.
function renderDialog(factory) {
  console.log(factory.createButton().render());
  console.log(factory.createCheckbox().render());
}

for (const factory of [macFactory, windowsFactory]) {
  console.log(`-- ${factory.name} theme --`);
  renderDialog(factory);
}
