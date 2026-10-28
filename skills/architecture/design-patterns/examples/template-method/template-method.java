// Template Method pattern in Java.
//
// The classic form: an abstract class with a final template method and
// abstract steps (compare java.io.InputStream or JUnit lifecycle hooks).
// The top-level class is non-public because "template-method" is not a
// valid Java class name.

import java.util.List;

class TemplateMethodDemo {

    record LineItem(String product, int units, double price) {
        double subtotal() {
            return units * price;
        }
    }

    abstract static class SalesReport {
        /** The template method: final, so the skeleton cannot vary. */
        final String generate(List<LineItem> items) {
            StringBuilder out = new StringBuilder(header()).append("\n");
            double total = 0;
            for (LineItem item : items) {
                out.append(row(item)).append("\n");
                total += item.subtotal();
            }
            return out.append(footer(total)).toString();
        }

        abstract String header();

        abstract String row(LineItem item);

        abstract String footer(double total);
    }

    static final class CsvReport extends SalesReport {
        @Override
        String header() {
            return "product,units,price,subtotal";
        }

        @Override
        String row(LineItem item) {
            return "%s,%d,%.2f,%.2f".formatted(item.product(), item.units(), item.price(), item.subtotal());
        }

        @Override
        String footer(double total) {
            return "total,,,%.2f".formatted(total);
        }
    }

    static final class MarkdownReport extends SalesReport {
        @Override
        String header() {
            return "| Product | Units | Subtotal |\n| --- | --- | --- |";
        }

        @Override
        String row(LineItem item) {
            return "| %s | %d | $%.2f |".formatted(item.product(), item.units(), item.subtotal());
        }

        @Override
        String footer(double total) {
            return "\n**Total: $%.2f**".formatted(total);
        }
    }

    public static void main(String[] args) {
        List<LineItem> items = List.of(
                new LineItem("Keyboard", 2, 80.00),
                new LineItem("Mouse", 1, 25.50),
                new LineItem("Monitor", 3, 210.00));

        for (SalesReport report : List.of(new CsvReport(), new MarkdownReport())) {
            System.out.println("--- " + report.getClass().getSimpleName() + " ---");
            System.out.println(report.generate(items));
            System.out.println();
        }
    }
}
