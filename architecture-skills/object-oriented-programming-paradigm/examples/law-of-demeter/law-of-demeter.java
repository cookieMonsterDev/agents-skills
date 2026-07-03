// Law of Demeter in Java.
//
// `order.getCustomer().getWallet().deduct(due)` is the classic train
// wreck in getter-heavy languages. `customer.pay(due)` keeps wallet
// logic inside Customer and gives checkout one hop, not three.

// --- Before (train wreck, sketched): ---
//
// class Checkout {
//     void collect(Order order, double due) {
//         order.getCustomer().getWallet().deduct(due);
//     }
// }

// --- After: tell, don't ask ---

class LawOfDemeter {

    static final class Wallet {
        private double balance;

        Wallet(double opening) {
            if (opening < 0) throw new IllegalArgumentException("opening balance cannot be negative");
            this.balance = opening;
        }

        void deduct(double amount) {
            if (amount <= 0) throw new IllegalArgumentException("payment must be positive");
            if (amount > balance) throw new IllegalArgumentException("insufficient funds");
            balance -= amount;
        }

        double balance() { return balance; }
    }

    static final class Customer {
        final String name;
        private final Wallet wallet; // no getWallet() — outsiders must not reach in

        Customer(String name, double opening) {
            this.name = name;
            this.wallet = new Wallet(opening);
        }

        void pay(double amount) {
            wallet.deduct(amount);
        }

        double balance() {
            return wallet.balance();
        }
    }

    static final class Order {
        final String id;
        final Customer customer;
        final double total;

        Order(String id, Customer customer, double total) {
            this.id = id;
            this.customer = customer;
            this.total = total;
        }
    }

    static final class Checkout {
        void collect(Order order, double due) {
            order.customer.pay(due); // one hop
        }
    }

    public static void main(String[] args) {
        Customer ada = new Customer("Ada", 50.00);
        Order order = new Order("ORD-101", ada, 12.50);
        Checkout checkout = new Checkout();

        System.out.printf("%s wallet before: $%.2f%n", ada.name, ada.balance());
        checkout.collect(order, order.total);
        System.out.printf("collected $%.2f for %s%n", order.total, order.id);
        System.out.printf("%s wallet after:  $%.2f  (invariant intact)%n",
                ada.name, ada.balance());
    }
}
