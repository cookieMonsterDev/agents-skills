// Classes & objects in Java.
//
// Java is class-mandatory: there are no free functions, so the
// cross-object transfer() becomes a static method. Java identifiers
// cannot contain hyphens, so the class cannot be named after this
// file; a package-private class keeps the single-file source launcher
// (`java classes-and-objects.java`) working.

class ClassesAndObjectsDemo {

    static class BankAccount {
        // Static member: one counter shared by all instances.
        private static int accountsOpened = 0;

        // Instance fields: one copy per object, never shared.
        private final String number;
        private final String owner;
        private double balance;

        // Constructor: the only way in; if it returns, state is valid.
        BankAccount(String owner, double openingBalance) {
            if (openingBalance < 0) {
                throw new IllegalArgumentException("opening balance cannot be negative");
            }
            this.number = String.format("ACC-%04d", ++accountsOpened);
            this.owner = owner;
            this.balance = openingBalance;
        }

        // Instance methods: implicit `this` binds them to one object.
        void deposit(double amount) {
            if (amount <= 0) {
                throw new IllegalArgumentException("deposit must be positive");
            }
            balance += amount;
        }

        void withdraw(double amount) {
            if (amount > balance) {
                throw new IllegalStateException(number + ": insufficient funds");
            }
            balance -= amount;
        }

        // Static method: bound to the class, callable with no instance.
        static int totalOpened() {
            return accountsOpened;
        }

        @Override
        public String toString() {
            return String.format("%s (%s): $%.2f", number, owner, balance);
        }
    }

    // No free functions in Java: a static method is the closest fit
    // for behavior that coordinates two objects and owns neither.
    static void transfer(BankAccount from, BankAccount to, double amount) {
        from.withdraw(amount);
        to.deposit(amount);
    }

    public static void main(String[] args) {
        // Two objects from one blueprint, each with independent state.
        BankAccount alice = new BankAccount("Alice", 100.00);
        BankAccount bob = new BankAccount("Bob", 0.00);

        alice.deposit(50.00);
        bob.deposit(20.00);
        alice.withdraw(30.00);

        System.out.println(alice); // Bob's balance is untouched
        System.out.println(bob);

        transfer(alice, bob, 40.00);
        System.out.println("after transfer:");
        System.out.println(alice);
        System.out.println(bob);

        System.out.println("accounts opened: " + BankAccount.totalOpened());
    }
}
