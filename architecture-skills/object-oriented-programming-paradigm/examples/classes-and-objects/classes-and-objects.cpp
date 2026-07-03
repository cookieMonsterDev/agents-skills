// Classes & objects in C++.
//
// A class ties initialization to allocation: the constructor runs the
// moment the object exists, so invariants hold from birth. `inline
// static` (C++17) defines the shared class member in-class. A free
// function like transfer() is a legitimate part of the interface —
// C++ does not force behavior into classes.

#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>

class BankAccount {
public:
    // Constructor: the only way in; if it returns, the state is valid.
    BankAccount(std::string owner, double opening_balance = 0.0)
        : owner_(std::move(owner)), balance_(opening_balance) {
        if (opening_balance < 0) {
            throw std::invalid_argument("opening balance cannot be negative");
        }
        std::ostringstream num;
        num << "ACC-" << std::setfill('0') << std::setw(4) << ++accounts_opened_;
        number_ = num.str();
    }

    // Instance methods: operate on this object's own fields.
    void deposit(double amount) {
        if (amount <= 0) {
            throw std::invalid_argument("deposit must be positive");
        }
        balance_ += amount;
    }

    void withdraw(double amount) {
        if (amount > balance_) {
            throw std::runtime_error(number_ + ": insufficient funds");
        }
        balance_ -= amount;
    }

    std::string describe() const {
        std::ostringstream out;
        out << number_ << " (" << owner_ << "): $" << std::fixed
            << std::setprecision(2) << balance_;
        return out.str();
    }

    // Static member function: bound to the class, not to any instance.
    static int total_opened() { return accounts_opened_; }

private:
    inline static int accounts_opened_ = 0; // one per class, not per object
    std::string number_;
    std::string owner_;
    double balance_;
};

// Free function: coordinates two objects, owns neither.
void transfer(BankAccount& from, BankAccount& to, double amount) {
    from.withdraw(amount);
    to.deposit(amount);
}

int main() {
    // Two objects from one blueprint, each with independent state.
    BankAccount alice("Alice", 100.00);
    BankAccount bob("Bob");

    alice.deposit(50.00);
    bob.deposit(20.00);
    alice.withdraw(30.00);

    std::cout << alice.describe() << "\n"; // Bob's balance is untouched
    std::cout << bob.describe() << "\n";

    transfer(alice, bob, 40.00);
    std::cout << "after transfer:\n"
              << alice.describe() << "\n"
              << bob.describe() << "\n";

    std::cout << "accounts opened: " << BankAccount::total_opened() << "\n";
    return 0;
}
