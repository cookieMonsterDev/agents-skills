// Open/Closed Principle in Java.
//
// PricingEngine is closed: it iterates registered DiscountRule
// implementations and never names a concrete rule. FlashSale is
// added later as a new class -- zero edits to the engine. (In real
// systems the registrations come from DI or ServiceLoader.)
//
// Java identifiers cannot contain hyphens, so the class cannot be named
// after this file; a package-private class keeps the single-file source
// launcher (`java open-closed.java`) working.

import java.util.ArrayList;
import java.util.List;

class OpenClosedDemo {

    record Order(double subtotal, int itemCount, boolean isMember) {}

    /** Extension point: one implementation per business rule. */
    interface DiscountRule {
        String name();
        double discount(Order order);
    }

    // --- Extensions: the engine never mentions these types ---

    static final class BulkDiscount implements DiscountRule {
        public String name() { return "bulk"; }
        public double discount(Order o) {
            return o.itemCount() >= 10 ? 0.05 * o.subtotal() : 0.0;
        }
    }

    static final class MemberDiscount implements DiscountRule {
        public String name() { return "member"; }
        public double discount(Order o) {
            return o.isMember() ? 0.10 * o.subtotal() : 0.0;
        }
    }

    /** Closed core: computes a total over whatever rules it was given. */
    static final class PricingEngine {
        private final List<DiscountRule> rules = new ArrayList<>();

        void register(DiscountRule rule) {
            rules.add(rule);
        }

        double total(Order order) {
            double total = order.subtotal();
            for (DiscountRule rule : rules) {
                double amount = rule.discount(order);
                if (amount > 0.0)
                    System.out.printf("  %6s: -$%.2f%n", rule.name(), amount);
                total -= amount;
            }
            return total;
        }
    }

    /** A NEW rule, written later -- nothing above is touched. */
    static final class FlashSale implements DiscountRule {
        private final double amount;
        private final double threshold;

        FlashSale(double amount, double threshold) {
            this.amount = amount;
            this.threshold = threshold;
        }

        public String name() { return "flash"; }
        public double discount(Order o) {
            return o.subtotal() > threshold ? amount : 0.0;
        }
    }

    public static void main(String[] args) {
        Order order = new Order(120.00, 12, true);

        PricingEngine engine = new PricingEngine();
        engine.register(new BulkDiscount());
        engine.register(new MemberDiscount());

        System.out.printf("subtotal: $%.2f%n", order.subtotal());
        System.out.printf("total:    $%.2f%n", engine.total(order));

        System.out.println("-- registering FlashSale: no engine edits --");
        engine.register(new FlashSale(15.00, 100.00));
        System.out.printf("total:    $%.2f%n", engine.total(order));
    }
}
