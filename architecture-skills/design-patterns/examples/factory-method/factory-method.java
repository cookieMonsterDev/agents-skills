// Factory Method pattern in Java.
//
// The classic form: an abstract creator with a shared workflow and a
// protected factory method. Java identifiers cannot contain hyphens, so the
// class cannot be named after this file; a package-private class keeps the
// single-file source launcher (`java factory-method.java`) working.

class FactoryMethodDemo {

    interface Transport {
        String deliver(String cargo);
    }

    static final class Truck implements Transport {
        public String deliver(String cargo) {
            return "Truck delivers " + cargo + " by road in a box";
        }
    }

    static final class Ship implements Transport {
        public String deliver(String cargo) {
            return "Ship delivers " + cargo + " by sea in a container";
        }
    }

    /** Creator: shared workflow around one overridable creation step. */
    static abstract class Logistics {
        protected abstract Transport createTransport();

        String planDelivery(String cargo) {
            Transport transport = createTransport();
            return "[" + getClass().getSimpleName() + "] " + transport.deliver(cargo);
        }
    }

    static final class RoadLogistics extends Logistics {
        protected Transport createTransport() {
            return new Truck();
        }
    }

    static final class SeaLogistics extends Logistics {
        protected Transport createTransport() {
            return new Ship();
        }
    }

    public static void main(String[] args) {
        Logistics[] all = { new RoadLogistics(), new SeaLogistics() };
        for (Logistics logistics : all) {
            System.out.println(logistics.planDelivery("machine parts"));
        }
    }
}
