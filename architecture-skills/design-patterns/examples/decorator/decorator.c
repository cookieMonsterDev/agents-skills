/* Decorator pattern in C.
 *
 * Polymorphism is emulated with structs and function pointers: every
 * beverage exposes description/cost through the same struct layout,
 * and a decorator holds a pointer to the beverage it wraps.
 */

#include <stdio.h>

typedef struct Beverage {
    void (*description)(const struct Beverage *self, char *out, size_t cap);
    double (*cost)(const struct Beverage *self);
    const struct Beverage *inner; /* NULL for base beverages */
    const char *label;
    double price; /* base price, or surcharge for add-ons */
} Beverage;

static void base_description(const Beverage *self, char *out, size_t cap) {
    snprintf(out, cap, "%s", self->label);
}

static double base_cost(const Beverage *self) {
    return self->price;
}

static void addon_description(const Beverage *self, char *out, size_t cap) {
    char inner[128];
    self->inner->description(self->inner, inner, sizeof(inner));
    snprintf(out, cap, "%s + %s", inner, self->label);
}

static double addon_cost(const Beverage *self) {
    return self->inner->cost(self->inner) + self->price;
}

static Beverage espresso(void) {
    Beverage b = {base_description, base_cost, NULL, "espresso", 2.00};
    return b;
}

static Beverage add_on(const Beverage *inner, const char *label, double surcharge) {
    Beverage b = {addon_description, addon_cost, inner, label, surcharge};
    return b;
}

static void print_drink(const Beverage *drink) {
    char text[128];
    drink->description(drink, text, sizeof(text));
    printf("%s: $%.2f\n", text, drink->cost(drink));
}

int main(void) {
    Beverage plain = espresso();

    Beverage base = espresso();
    Beverage with_milk = add_on(&base, "milk", 0.30);
    Beverage with_mocha = add_on(&with_milk, "mocha", 0.50);
    Beverage fancy = add_on(&with_mocha, "whipped cream", 0.40);

    print_drink(&plain);
    print_drink(&fancy);
    return 0;
}
