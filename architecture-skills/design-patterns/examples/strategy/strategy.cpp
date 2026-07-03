// Strategy pattern in C++.
//
// Modern C++ stores strategies as std::function (or a template
// parameter), so lambdas and function objects both fit; a virtual-method
// hierarchy is rarely needed. A function object (CarrierRate) shows the
// stateful case.

#include <functional>
#include <iomanip>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

struct Order {
    double weight_kg;
    double distance_km;
};

using ShippingStrategy = std::function<double(const Order&)>;

// Context: delegates the pricing decision to the current strategy.
class Checkout {
public:
    explicit Checkout(ShippingStrategy strategy) : strategy_(std::move(strategy)) {}

    void setStrategy(ShippingStrategy strategy) { strategy_ = std::move(strategy); }

    double shippingFor(const Order& order) const { return strategy_(order); }

private:
    ShippingStrategy strategy_;
};

// A stateful strategy: the negotiated rates are its state.
class CarrierRate {
public:
    CarrierRate(double base, double per_kg) : base_(base), per_kg_(per_kg) {}

    double operator()(const Order& order) const {
        return base_ + per_kg_ * order.weight_kg;
    }

private:
    double base_;
    double per_kg_;
};

int main() {
    const Order order{2.4, 120.0};

    const std::vector<std::pair<std::string, ShippingStrategy>> strategies = {
        {"flat", [](const Order&) { return 5.00; }},
        {"weight", [](const Order& o) { return 4.00 + 1.50 * o.weight_kg; }},
        {"distance", [](const Order& o) { return 2.00 + 0.05 * o.distance_km; }},
        {"carrier", CarrierRate{3.00, 2.00}},
    };

    Checkout checkout{strategies.front().second};
    std::cout << std::fixed << std::setprecision(2);
    for (const auto& [name, strategy] : strategies) {
        checkout.setStrategy(strategy);
        std::cout << std::setw(8) << name << ": $" << checkout.shippingFor(order) << "\n";
    }
    return 0;
}
