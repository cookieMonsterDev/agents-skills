// Encapsulation in Java.
//
// A private field plus methods is the norm; note there is no setter for
// balance — a public unchecked setBalance would make the field public
// again with extra syntax. The constructor establishes the invariant
// (balance >= 0) and deposit/withdraw maintain it.

public class encapsulation {

    static final class BankAccount {
        private double balance; // only this class's methods may touch it

        BankAccount(double openingBalance) {
            if (openingBalance < 0) {
                throw new IllegalArgumentException("opening balance cannot be negative");
            }
            this.balance = openingBalance;
        }

        double balance() {
            return balance; // read access only: no setter exists
        }

        void deposit(double amount) {
            if (amount <= 0) {
                throw new IllegalArgumentException("deposit must be positive");
            }
            balance += amount;
        }

        void withdraw(double amount) {
            if (amount <= 0) {
                throw new IllegalArgumentException("withdrawal must be positive");
            }
            if (amount > balance) {
                throw new IllegalArgumentException("insufficient funds");
            }
            balance -= amount;
        }
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount(100.00);

        account.deposit(50.00);
        System.out.printf("after deposit:  $%.2f%n", account.balance());

        try {
            account.withdraw(250.00);
        } catch (IllegalArgumentException err) {
            System.out.println("withdraw $250 rejected: " + err.getMessage());
        }

        account.withdraw(30.00);
        System.out.printf("after withdraw: $%.2f  (invariant intact)%n", account.balance());

        // account.balance = -500;  // compile error outside BankAccount's class file
    }
}
