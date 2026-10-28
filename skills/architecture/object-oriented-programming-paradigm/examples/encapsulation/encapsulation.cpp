// Encapsulation in C++.
//
// private/public sections enforce the boundary at compile time: the
// constructor establishes the invariant (balance >= 0) and the methods
// maintain it. Writing account.balance_ from outside is a compile
// error, so the invalid state is unrepresentable to callers.

#include <iostream>
#include <stdexcept>

class BankAccount {
public:
    explicit BankAccount(double opening_balance) {
        if (opening_balance < 0) {
            throw std::invalid_argument("opening balance cannot be negative");
        }
        balance_ = opening_balance;
    }

    double balance() const { return balance_; }

    void deposit(double amount) {
        if (amount <= 0) {
            throw std::invalid_argument("deposit must be positive");
        }
        balance_ += amount;
    }

    void withdraw(double amount) {
        if (amount <= 0) {
            throw std::invalid_argument("withdrawal must be positive");
        }
        if (amount > balance_) {
            throw std::invalid_argument("insufficient funds");
        }
        balance_ -= amount;
    }

private:
    double balance_; // invisible to callers; only methods above touch it
};

int main() {
    BankAccount account(100.00);

    account.deposit(50.00);
    std::cout << "after deposit:  $" << account.balance() << "\n";

    try {
        account.withdraw(250.00);
    } catch (const std::invalid_argument &err) {
        std::cout << "withdraw $250 rejected: " << err.what() << "\n";
    }

    account.withdraw(30.00);
    std::cout << "after withdraw: $" << account.balance()
              << "  (invariant intact)\n";

    // account.balance_ = -500.0;  // compile error: 'balance_' is private
    return 0;
}
