// Abstract Factory pattern in Java.
//
// Java identifiers cannot contain hyphens, so unlike the other examples the
// class cannot be named after this file; a package-private class keeps the
// single-file source launcher (`java abstract-factory.java`) working.

class AbstractFactoryDemo {

    interface Button {
        String render();
    }

    interface Checkbox {
        String render();
    }

    static final class MacButton implements Button {
        public String render() { return "( OK )  // rounded macOS button"; }
    }

    static final class MacCheckbox implements Checkbox {
        public String render() { return "◉ Remember me  // macOS checkbox"; }
    }

    static final class WindowsButton implements Button {
        public String render() { return "[ OK ]  // rectangular Windows button"; }
    }

    static final class WindowsCheckbox implements Checkbox {
        public String render() { return "[x] Remember me  // Windows checkbox"; }
    }

    /** One creation method per product kind; products are guaranteed to match. */
    interface WidgetFactory {
        Button createButton();
        Checkbox createCheckbox();
    }

    static final class MacFactory implements WidgetFactory {
        public Button createButton() { return new MacButton(); }
        public Checkbox createCheckbox() { return new MacCheckbox(); }
    }

    static final class WindowsFactory implements WidgetFactory {
        public Button createButton() { return new WindowsButton(); }
        public Checkbox createCheckbox() { return new WindowsCheckbox(); }
    }

    /** Client code: depends only on the abstract factory and products. */
    static void renderDialog(WidgetFactory factory) {
        System.out.println(factory.createButton().render());
        System.out.println(factory.createCheckbox().render());
    }

    public static void main(String[] args) {
        System.out.println("-- macOS theme --");
        renderDialog(new MacFactory());

        System.out.println("-- Windows theme --");
        renderDialog(new WindowsFactory());
    }
}
