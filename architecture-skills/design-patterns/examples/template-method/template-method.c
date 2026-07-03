/* Template Method pattern in C.
 *
 * C has no inheritance, so the "abstract class" is a struct of function
 * pointers (a hand-rolled vtable) and the template method is a plain
 * function that fixes the skeleton — iteration and totalling — and
 * calls through the pointers for the varying formatting steps.
 */

#include <stdio.h>

typedef struct {
    const char *product;
    int units;
    double price;
} LineItem;

typedef struct {
    const char *name;
    void (*header)(void);
    void (*row)(const LineItem *item, double subtotal);
    void (*footer)(double total);
} ReportSteps;

/* The template method: the skeleton never varies. */
void generate_report(const ReportSteps *steps, const LineItem *items, size_t count) {
    printf("--- %s ---\n", steps->name);
    steps->header();
    double total = 0.0;
    for (size_t i = 0; i < count; i++) {
        double subtotal = items[i].units * items[i].price;
        steps->row(&items[i], subtotal);
        total += subtotal;
    }
    steps->footer(total);
    printf("\n");
}

/* --- CSV variant --- */

void csv_header(void) {
    printf("product,units,price,subtotal\n");
}

void csv_row(const LineItem *item, double subtotal) {
    printf("%s,%d,%.2f,%.2f\n", item->product, item->units, item->price, subtotal);
}

void csv_footer(double total) {
    printf("total,,,%.2f\n", total);
}

/* --- Markdown variant --- */

void md_header(void) {
    printf("| Product | Units | Subtotal |\n| --- | --- | --- |\n");
}

void md_row(const LineItem *item, double subtotal) {
    printf("| %s | %d | $%.2f |\n", item->product, item->units, subtotal);
}

void md_footer(double total) {
    printf("\n**Total: $%.2f**\n", total);
}

int main(void) {
    LineItem items[] = {
        { "Keyboard", 2, 80.00 },
        { "Mouse", 1, 25.50 },
        { "Monitor", 3, 210.00 },
    };
    size_t count = sizeof(items) / sizeof(items[0]);

    ReportSteps csv = { "CsvReport", csv_header, csv_row, csv_footer };
    ReportSteps markdown = { "MarkdownReport", md_header, md_row, md_footer };

    generate_report(&csv, items, count);
    generate_report(&markdown, items, count);
    return 0;
}
