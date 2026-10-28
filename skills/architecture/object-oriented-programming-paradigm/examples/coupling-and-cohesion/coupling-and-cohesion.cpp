// Coupling and Cohesion in C++.
//
// A god OrderProcessor that computes tax, validates, and ships couples
// three volatile concerns. Focused classes with high cohesion let a tax
// change touch only OrderCalculator.

#include <iostream>
#include <stdexcept>
#include <string>

// --- Before (tightly coupled, sketched): ---
//
// class OrderProcessor {
// public:
//     double process(Order& o) {
//         double total = o.subtotal * 1.20;  // tax
//         if (total <= 0) throw ...;         // validation
//         std::cout << "shipped " << o.id;   // shipping
//         return total;
//     }
// };

struct Order {
    std::string id;
    double subtotal;
};

// Finance's class: only tax-rule changes touch this file.
class OrderCalculator {
public:
    explicit OrderCalculator(double taxRate) : taxRate_(taxRate) {}

    double total(const Order& order) const {
        return order.subtotal * (1.0 + taxRate_);
    }

private:
    double taxRate_;
};

// Compliance's class: only validation rules change touch this file.
class OrderValidator {
public:
    void validate(const Order& order, double total) const {
        if (order.subtotal <= 0) throw std::invalid_argument("subtotal must be positive");
        if (total <= 0) throw std::invalid_argument("total must be positive");
    }
};

// Fulfillment's class: only carrier/API changes touch this file.
class OrderShipper {
public:
    std::string ship(const Order& order) const {
        return "shipped " + order.id;
    }
};

// Thin orchestrator: wires cohesive pieces together.
class OrderService {
public:
    OrderService(OrderCalculator calc, OrderValidator validator, OrderShipper shipper)
        : calc_(std::move(calc)), validator_(std::move(validator)), shipper_(std::move(shipper)) {}

    double process(const Order& order) const {
        double total = calc_.total(order);
        validator_.validate(order, total);
        std::cout << shipper_.ship(order) << "\n";
        return total;
    }

private:
    OrderCalculator calc_;
    OrderValidator validator_;
    OrderShipper shipper_;
};

int main() {
    Order order{"ORD-204", 80.00};

    OrderService service(OrderCalculator(0.20), OrderValidator{}, OrderShipper{});
    double total = service.process(order);
    std::cout << "total with 20% tax: $" << total << "\n";

    OrderService newRateService(OrderCalculator(0.08), OrderValidator{}, OrderShipper{});
    double newTotal = newRateService.process(order);
    std::cout << "total with 8% tax:  $" << newTotal
              << "  (only OrderCalculator changed)\n";
    return 0;
}
