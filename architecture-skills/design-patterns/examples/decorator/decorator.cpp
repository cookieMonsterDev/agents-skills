// Decorator pattern in C++.
//
// Add-ons wrap another Beverage behind the same interface. Ownership
// of the wrapped object moves into the decorator via unique_ptr, so a
// finished drink is one owning chain of wrappers.

#include <cstdio>
#include <memory>
#include <string>
#include <utility>

class Beverage {
public:
    virtual ~Beverage() = default;
    virtual std::string description() const = 0;
    virtual double cost() const = 0;
};

class Espresso : public Beverage {
public:
    std::string description() const override { return "espresso"; }
    double cost() const override { return 2.00; }
};

class AddOn : public Beverage {
public:
    AddOn(std::unique_ptr<Beverage> inner, std::string label, double surcharge)
        : inner_(std::move(inner)), label_(std::move(label)), surcharge_(surcharge) {}

    std::string description() const override {
        return inner_->description() + " + " + label_;
    }
    double cost() const override { return inner_->cost() + surcharge_; }

private:
    std::unique_ptr<Beverage> inner_;
    std::string label_;
    double surcharge_;
};

std::unique_ptr<Beverage> milk(std::unique_ptr<Beverage> inner) {
    return std::make_unique<AddOn>(std::move(inner), "milk", 0.30);
}

std::unique_ptr<Beverage> mocha(std::unique_ptr<Beverage> inner) {
    return std::make_unique<AddOn>(std::move(inner), "mocha", 0.50);
}

std::unique_ptr<Beverage> whippedCream(std::unique_ptr<Beverage> inner) {
    return std::make_unique<AddOn>(std::move(inner), "whipped cream", 0.40);
}

int main() {
    std::unique_ptr<Beverage> plain = std::make_unique<Espresso>();
    std::unique_ptr<Beverage> fancy =
        whippedCream(mocha(milk(std::make_unique<Espresso>())));

    for (const auto* drink : {plain.get(), fancy.get()}) {
        std::printf("%s: $%.2f\n", drink->description().c_str(), drink->cost());
    }
    return 0;
}
