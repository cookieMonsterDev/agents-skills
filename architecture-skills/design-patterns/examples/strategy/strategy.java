// Strategy pattern in Java.
//
// The classic home of the pattern (java.util.Comparator is a strategy).
// Since Java 8 a single-method strategy interface is a functional
// interface, so lambdas replace one-off concrete classes; a named class
// is still useful when the strategy carries state (CarrierRate).

import java.util.LinkedHashMap;
import java.util.Map;

public class strategy {

    record Order(double weightKg, double distanceKm) {}

    @FunctionalInterface
    interface ShippingStrategy {
        double cost(Order order);
    }

    /** A stateful strategy: the negotiated rates are its state. */
    static final class CarrierRate implements ShippingStrategy {
        private final double base;
        private final double perKg;

        CarrierRate(double base, double perKg) {
            this.base = base;
            this.perKg = perKg;
        }

        @Override
        public double cost(Order order) {
            return base + perKg * order.weightKg();
        }
    }

    /** Context: delegates the pricing decision to the current strategy. */
    static final class Checkout {
        private ShippingStrategy strategy;

        Checkout(ShippingStrategy strategy) {
            this.strategy = strategy;
        }

        void setStrategy(ShippingStrategy strategy) {
            this.strategy = strategy;
        }

        double shippingFor(Order order) {
            return strategy.cost(order);
        }
    }

    public static void main(String[] args) {
        Order order = new Order(2.4, 120);

        Map<String, ShippingStrategy> strategies = new LinkedHashMap<>();
        strategies.put("flat", o -> 5.00);
        strategies.put("weight", o -> 4.00 + 1.50 * o.weightKg());
        strategies.put("distance", o -> 2.00 + 0.05 * o.distanceKm());
        strategies.put("carrier", new CarrierRate(3.00, 2.00));

        Checkout checkout = new Checkout(strategies.get("flat"));
        strategies.forEach((name, s) -> {
            checkout.setStrategy(s);
            System.out.printf("%8s: $%.2f%n", name, checkout.shippingFor(order));
        });
    }
}
