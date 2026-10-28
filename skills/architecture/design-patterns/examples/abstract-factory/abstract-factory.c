/* Abstract Factory pattern in C.
 *
 * C has no interfaces, so the factory is emulated as a struct of function
 * pointers (a hand-rolled vtable). Each concrete factory fills the struct
 * with constructors from one family, guaranteeing matched products.
 */

#include <stdio.h>

typedef struct {
    const char *(*render)(void);
} Button;

typedef struct {
    const char *(*render)(void);
} Checkbox;

/* --- macOS family --- */

static const char *mac_button_render(void) { return "( OK )  /* rounded macOS button */"; }
static const char *mac_checkbox_render(void) { return "* Remember me  /* macOS checkbox */"; }

static Button mac_create_button(void) {
    Button b = { mac_button_render };
    return b;
}

static Checkbox mac_create_checkbox(void) {
    Checkbox c = { mac_checkbox_render };
    return c;
}

/* --- Windows family --- */

static const char *win_button_render(void) { return "[ OK ]  /* rectangular Windows button */"; }
static const char *win_checkbox_render(void) { return "[x] Remember me  /* Windows checkbox */"; }

static Button win_create_button(void) {
    Button b = { win_button_render };
    return b;
}

static Checkbox win_create_checkbox(void) {
    Checkbox c = { win_checkbox_render };
    return c;
}

/* The abstract factory: one function pointer per product kind. */
typedef struct {
    const char *name;
    Button (*create_button)(void);
    Checkbox (*create_checkbox)(void);
} WidgetFactory;

static const WidgetFactory MAC_FACTORY = { "macOS", mac_create_button, mac_create_checkbox };
static const WidgetFactory WIN_FACTORY = { "Windows", win_create_button, win_create_checkbox };

/* Client code: depends only on the factory struct, never on a family. */
static void render_dialog(const WidgetFactory *factory) {
    Button button = factory->create_button();
    Checkbox checkbox = factory->create_checkbox();
    printf("-- %s theme --\n", factory->name);
    printf("%s\n", button.render());
    printf("%s\n", checkbox.render());
}

int main(void) {
    render_dialog(&MAC_FACTORY);
    render_dialog(&WIN_FACTORY);
    return 0;
}
