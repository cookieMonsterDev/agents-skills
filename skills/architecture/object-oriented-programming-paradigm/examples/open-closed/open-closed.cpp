// Open/Closed Principle in C++.
//
// PricingEngine is closed: it iterates registered rules through the
// DiscountRule interface and never names a concrete rule. FlashSale
// is added later as a new class -- zero edits to the engine. (A
// template + concept would give the same openness at compile time.)

#include <iostream>
#include <iomanip>
#include <memory>
#include <string>
#include <vector>

struct Order {
    double subtotal;
    int item_count;
    bool is_member;
};

// Extension point.
class DiscountRule {
public:
    virtual ~DiscountRule() = default;
    virtual std::string name() const = 0;
    virtual double discount(const Order& order) const = 0;
};

// --- Extensions: the engine never mentions these types ---

class BulkDiscount : public DiscountRule {
public:
    std::string name() const override { return "bulk"; }
    double discount(const Order& o) const override {
        return o.item_count >= 10 ? 0.05 * o.subtotal : 0.0;
    }
};

class MemberDiscount : public DiscountRule {
public:
    std::string name() const override { return "member"; }
    double discount(const Order& o) const override {
        return o.is_member ? 0.10 * o.subtotal : 0.0;
    }
};

// Closed core: computes a total over whatever rules it was given.
class PricingEngine {
public:
    void register_rule(std::unique_ptr<DiscountRule> rule) {
        rules_.push_back(std::move(rule));
    }

    double total(const Order& order) const {
        double total = order.subtotal;
        for (const auto& rule : rules_) {
            double amount = rule->discount(order);
            if (amount > 0.0)
                std::cout << "  " << std::setw(6) << rule->name()
                          << ": -$" << amount << "\n";
            total -= amount;
        }
        return total;
    }

private:
    std::vector<std::unique_ptr<DiscountRule>> rules_;
};

// A NEW rule, written later -- nothing above is touched.
class FlashSale : public DiscountRule {
public:
    FlashSale(double amount, double threshold)
        : amount_(amount), threshold_(threshold) {}
    std::string name() const override { return "flash"; }
    double discount(const Order& o) const override {
        return o.subtotal > threshold_ ? amount_ : 0.0;
    }

private:
    double amount_;
    double threshold_;
};

int main() {
    std::cout << std::fixed << std::setprecision(2);
    Order order{120.00, 12, true};

    PricingEngine engine;
    engine.register_rule(std::make_unique<BulkDiscount>());
    engine.register_rule(std::make_unique<MemberDiscount>());

    std::cout << "subtotal: $" << order.subtotal << "\n";
    std::cout << "total:    $" << engine.total(order) << "\n";

    std::cout << "-- registering FlashSale: no engine edits --\n";
    engine.register_rule(std::make_unique<FlashSale>(15.00, 100.00));
    std::cout << "total:    $" << engine.total(order) << "\n";
    return 0;
}
