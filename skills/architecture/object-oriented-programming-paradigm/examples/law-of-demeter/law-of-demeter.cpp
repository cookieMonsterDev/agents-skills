// Law of Demeter in C++.
//
// order.getCustomer().getWallet().deduct(due) couples checkout to
// Customer's and Wallet's internals. customer.pay(due) moves the
// operation onto the owner; Wallet stays a private implementation detail.

#include <iostream>
#include <stdexcept>
#include <string>

// --- Before (train wreck, sketched): ---
//
// class Checkout {
// public:
//     void collect(Order& order, double due) {
//         order.getCustomer().getWallet().deduct(due);  // three hops
//     }
// };

// --- After: tell, don't ask ---

class Wallet {
public:
    explicit Wallet(double opening) : balance_(opening) {
        if (opening < 0) throw std::invalid_argument("opening balance cannot be negative");
    }

    void deduct(double amount) {
        if (amount <= 0) throw std::invalid_argument("payment must be positive");
        if (amount > balance_) throw std::invalid_argument("insufficient funds");
        balance_ -= amount;
    }

    double balance() const { return balance_; }

private:
    double balance_;
};

class Customer {
public:
    Customer(std::string name, double opening)
        : name_(std::move(name)), wallet_(opening) {}

    void pay(double amount) { wallet_.deduct(amount); }

    double balance() const { return wallet_.balance(); }
    const std::string& name() const { return name_; }

private:
    std::string name_;
    Wallet wallet_; // no public accessor — outsiders cannot reach in
};

class Order {
public:
    Order(std::string id, Customer& customer, double total)
        : id_(std::move(id)), customer_(customer), total_(total) {}

    const std::string& id() const { return id_; }
    Customer& customer() const { return customer_; }
    double total() const { return total_; }

private:
    std::string id_;
    Customer& customer_;
    double total_;
};

class Checkout {
public:
    void collect(Order& order, double due) {
        order.customer().pay(due); // one hop
    }
};

int main() {
    Customer ada("Ada", 50.00);
    Order order("ORD-101", ada, 12.50);
    Checkout checkout;

    std::cout << ada.name() << " wallet before: $" << ada.balance() << "\n";
    checkout.collect(order, order.total());
    std::cout << "collected $" << order.total() << " for " << order.id() << "\n";
    std::cout << ada.name() << " wallet after:  $" << ada.balance()
              << "  (invariant intact)\n";
    return 0;
}
