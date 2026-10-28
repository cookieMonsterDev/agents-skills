// Decorator pattern in Java.
//
// Add-ons wrap another Beverage behind the same interface — exactly how
// java.io composes streams: new BufferedInputStream(new FileInputStream(...)).
//
// The public class is lowercase so the filename matches the pattern name.

public class decorator {

    interface Beverage {
        String description();
        double cost();
    }

    static class Espresso implements Beverage {
        public String description() { return "espresso"; }
        public double cost() { return 2.00; }
    }

    /** Base decorator: holds the wrapped beverage. */
    abstract static class AddOn implements Beverage {
        protected final Beverage inner;

        AddOn(Beverage inner) {
            this.inner = inner;
        }
    }

    static class Milk extends AddOn {
        Milk(Beverage inner) { super(inner); }
        public String description() { return inner.description() + " + milk"; }
        public double cost() { return inner.cost() + 0.30; }
    }

    static class Mocha extends AddOn {
        Mocha(Beverage inner) { super(inner); }
        public String description() { return inner.description() + " + mocha"; }
        public double cost() { return inner.cost() + 0.50; }
    }

    static class WhippedCream extends AddOn {
        WhippedCream(Beverage inner) { super(inner); }
        public String description() { return inner.description() + " + whipped cream"; }
        public double cost() { return inner.cost() + 0.40; }
    }

    public static void main(String[] args) {
        Beverage plain = new Espresso();
        Beverage fancy = new WhippedCream(new Mocha(new Milk(new Espresso())));
        for (Beverage drink : new Beverage[] {plain, fancy}) {
            System.out.printf("%s: $%.2f%n", drink.description(), drink.cost());
        }
    }
}
