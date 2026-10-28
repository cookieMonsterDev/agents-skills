// Coupling and Cohesion in Java.
//
// A god OrderProcessor that computes tax, validates, and ships is
// tightly coupled — a tax change can break validation or shipping.
// Focused collaborators with high cohesion isolate each concern.

// --- Before (tightly coupled, sketched): ---
//
// class OrderProcessor {
//     double process(Order o) {
//         double total = o.subtotal * 1.20;  // tax
//         if (total <= 0) throw ...;         // validation
//         System.out.println("shipped");     // shipping
//         return total;
//     }
// }

class CouplingAndCohesion {

    record Order(String id, double subtotal) {}

    /** Finance's class: only tax-rule changes touch this file. */
    static final class OrderCalculator {
        private final double taxRate;

        OrderCalculator(double taxRate) {
            this.taxRate = taxRate;
        }

        double total(Order order) {
            return order.subtotal() * (1 + taxRate);
        }
    }

    /** Compliance's class: only validation rules change touch this file. */
    static final class OrderValidator {
        void validate(Order order, double total) {
            if (order.subtotal() <= 0) throw new IllegalArgumentException("subtotal must be positive");
            if (total <= 0) throw new IllegalArgumentException("total must be positive");
        }
    }

    /** Fulfillment's class: only carrier/API changes touch this file. */
    static final class OrderShipper {
        String ship(Order order) {
            return "shipped " + order.id();
        }
    }

    /** Thin orchestrator: wires cohesive pieces, owns no domain rules. */
    static final class OrderService {
        private final OrderCalculator calculator;
        private final OrderValidator validator;
        private final OrderShipper shipper;

        OrderService(OrderCalculator calculator, OrderValidator validator, OrderShipper shipper) {
            this.calculator = calculator;
            this.validator = validator;
            this.shipper = shipper;
        }

        double process(Order order) {
            double total = calculator.total(order);
            validator.validate(order, total);
            System.out.println(shipper.ship(order));
            return total;
        }
    }

    public static void main(String[] args) {
        Order order = new Order("ORD-204", 80.00);

        OrderService service = new OrderService(
                new OrderCalculator(0.20), new OrderValidator(), new OrderShipper());
        double total = service.process(order);
        System.out.printf("total with 20%% tax: $%.2f%n", total);

        OrderService newRateService = new OrderService(
                new OrderCalculator(0.08), new OrderValidator(), new OrderShipper());
        double newTotal = newRateService.process(order);
        System.out.printf("total with 8%% tax:  $%.2f  (only OrderCalculator changed)%n", newTotal);
    }
}
