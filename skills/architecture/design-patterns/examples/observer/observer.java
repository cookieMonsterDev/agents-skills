// Observer pattern in Java.
//
// A functional interface lets observers be lambdas, method references,
// or classes alike. (java.util.Observer is deprecated; real code uses
// listener interfaces like this, or java.util.concurrent.Flow for
// reactive streams.)

import java.util.ArrayList;
import java.util.List;

public class observer {

    @FunctionalInterface
    interface PriceObserver {
        void onPrice(String symbol, double price);
    }

    static final class StockTicker {
        private final List<PriceObserver> observers = new ArrayList<>();

        void subscribe(PriceObserver o) {
            observers.add(o);
        }

        void unsubscribe(PriceObserver o) {
            observers.remove(o);
        }

        void updatePrice(String symbol, double price) {
            for (PriceObserver o : List.copyOf(observers)) {
                o.onPrice(symbol, price);
            }
        }
    }

    static final class PriceDisplay implements PriceObserver {
        private final String name;

        PriceDisplay(String name) {
            this.name = name;
        }

        @Override
        public void onPrice(String symbol, double price) {
            System.out.printf("%s: %s is now $%.2f%n", name, symbol, price);
        }
    }

    public static void main(String[] args) {
        StockTicker ticker = new StockTicker();
        PriceDisplay display = new PriceDisplay("Lobby display");
        ticker.subscribe(display);

        PriceObserver alert = (symbol, price) -> {
            if (symbol.equals("ACME") && price > 100.0) {
                System.out.printf("ALERT: ACME crossed $100.00 (now $%.2f)%n", price);
            }
        };
        ticker.subscribe(alert);

        ticker.updatePrice("ACME", 98.5);
        ticker.updatePrice("ACME", 101.25);

        ticker.unsubscribe(display);
        ticker.updatePrice("GLOBEX", 45.0); // only the alert remains
    }
}
