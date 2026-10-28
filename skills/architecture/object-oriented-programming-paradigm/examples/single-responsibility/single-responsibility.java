// Single Responsibility Principle in Java.
//
// The top-level class is non-public so the hyphenated filename still
// runs via the source launcher: `java single-responsibility.java`.
//
// A god Invoice would compute totals, format itself, and persist
// itself — three actors, three reasons to change, one file. The
// refactor gives each actor its own class; in a real project each
// would be its own file and a DI container would do the wiring.

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class SingleResponsibility {

    // --- Before (god class, sketched): three reasons to change ---
    //
    // class Invoice {
    //     double total()       { ... }  // changes when FINANCE changes tax
    //     String toText()      { ... }  // changes when LAYOUT changes
    //     void saveToDb()      { ... }  // changes when STORAGE changes
    // }

    // --- After: one collaborator per actor ---

    record LineItem(String description, double amount) {}

    /** Domain object: owns the data, knows nothing of tax, text, or storage. */
    static final class Invoice {
        final String id;
        final String customer;
        final List<LineItem> items = new ArrayList<>();

        Invoice(String id, String customer) {
            this.id = id;
            this.customer = customer;
        }

        void addItem(String description, double amount) {
            items.add(new LineItem(description, amount));
        }
    }

    /** Finance's class: only tax-rule changes touch this file. */
    static final class InvoiceCalculator {
        private final double taxRate;

        InvoiceCalculator(double taxRate) {
            this.taxRate = taxRate;
        }

        double total(Invoice invoice) {
            double subtotal = invoice.items.stream()
                    .mapToDouble(LineItem::amount).sum();
            return subtotal * (1 + taxRate);
        }
    }

    /** Presentation's class: only layout changes touch this file. */
    static final class TextInvoiceFormatter {
        String format(Invoice invoice, double total) {
            StringBuilder out = new StringBuilder(
                    "Invoice %s for %s".formatted(invoice.id, invoice.customer));
            for (LineItem item : invoice.items) {
                out.append("\n  %-12s $%8.2f"
                        .formatted(item.description(), item.amount()));
            }
            return out.append("\n  %-12s $%8.2f".formatted("TOTAL", total))
                    .toString();
        }
    }

    /** Ops' class: only storage changes (schema, driver) touch this file. */
    static final class InMemoryInvoiceRepository {
        private final Map<String, Invoice> rows = new HashMap<>();

        void save(Invoice invoice) {
            rows.put(invoice.id, invoice);
        }

        int count() {
            return rows.size();
        }
    }

    public static void main(String[] args) {
        Invoice invoice = new Invoice("INV-042", "ACME Corp");
        invoice.addItem("Consulting", 1200.00);
        invoice.addItem("Hosting", 90.00);

        InvoiceCalculator calculator = new InvoiceCalculator(0.20);
        TextInvoiceFormatter formatter = new TextInvoiceFormatter();
        InMemoryInvoiceRepository repository = new InMemoryInvoiceRepository();

        double total = calculator.total(invoice);
        System.out.println(formatter.format(invoice, total));

        repository.save(invoice);
        System.out.printf("saved %s (%d record(s) stored)%n",
                invoice.id, repository.count());
    }
}
