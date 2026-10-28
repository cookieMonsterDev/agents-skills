// Abstract Factory pattern in Rust.
//
// Traits model the products and the factory; boxed trait objects allow the
// family to be chosen at runtime. When the set of families is closed and
// known up front, an enum with match arms is often more idiomatic.

trait Button {
    fn render(&self) -> String;
}

trait Checkbox {
    fn render(&self) -> String;
}

struct MacButton;
struct MacCheckbox;
struct WindowsButton;
struct WindowsCheckbox;

impl Button for MacButton {
    fn render(&self) -> String {
        "( OK )  // rounded macOS button".to_string()
    }
}

impl Checkbox for MacCheckbox {
    fn render(&self) -> String {
        "◉ Remember me  // macOS checkbox".to_string()
    }
}

impl Button for WindowsButton {
    fn render(&self) -> String {
        "[ OK ]  // rectangular Windows button".to_string()
    }
}

impl Checkbox for WindowsCheckbox {
    fn render(&self) -> String {
        "[x] Remember me  // Windows checkbox".to_string()
    }
}

/// One creation method per product kind; products are guaranteed to match.
trait WidgetFactory {
    fn create_button(&self) -> Box<dyn Button>;
    fn create_checkbox(&self) -> Box<dyn Checkbox>;
}

struct MacFactory;
struct WindowsFactory;

impl WidgetFactory for MacFactory {
    fn create_button(&self) -> Box<dyn Button> {
        Box::new(MacButton)
    }
    fn create_checkbox(&self) -> Box<dyn Checkbox> {
        Box::new(MacCheckbox)
    }
}

impl WidgetFactory for WindowsFactory {
    fn create_button(&self) -> Box<dyn Button> {
        Box::new(WindowsButton)
    }
    fn create_checkbox(&self) -> Box<dyn Checkbox> {
        Box::new(WindowsCheckbox)
    }
}

/// Client code: depends only on the factory trait, never on a family.
fn render_dialog(factory: &dyn WidgetFactory) {
    println!("{}", factory.create_button().render());
    println!("{}", factory.create_checkbox().render());
}

fn main() {
    let themes: [(&str, Box<dyn WidgetFactory>); 2] = [
        ("macOS", Box::new(MacFactory)),
        ("Windows", Box::new(WindowsFactory)),
    ];

    for (name, factory) in &themes {
        println!("-- {name} theme --");
        render_dialog(factory.as_ref());
    }
}
