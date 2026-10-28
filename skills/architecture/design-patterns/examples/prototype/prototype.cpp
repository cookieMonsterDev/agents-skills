// Prototype pattern in C++.
//
// The classic use: a virtual clone() returning unique_ptr lets you copy an
// object through its base-class interface, where the copy constructor is
// unusable because the dynamic type is unknown.

#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>
#include <vector>

class Shape {  // prototype interface
public:
    virtual ~Shape() = default;
    virtual std::unique_ptr<Shape> clone() const = 0;
    virtual std::string describe() const = 0;
    virtual void moveTo(double x, double y) = 0;
};

class Circle : public Shape {
public:
    Circle(double x, double y, double radius, std::string color, std::vector<std::string> tags)
        : x_(x), y_(y), radius_(radius), color_(std::move(color)), tags_(std::move(tags)) {}

    // The copy constructor already deep-copies the vector; clone() just
    // exposes it polymorphically.
    std::unique_ptr<Shape> clone() const override { return std::make_unique<Circle>(*this); }

    void moveTo(double x, double y) override {
        x_ = x;
        y_ = y;
    }

    std::string describe() const override {
        std::string tags;
        for (const auto& t : tags_) tags += t + ' ';
        return "Circle r=" + std::to_string(static_cast<int>(radius_)) + ' ' + color_ +
               " at (" + std::to_string(static_cast<int>(x_)) + ", " +
               std::to_string(static_cast<int>(y_)) + ") tags=[ " + tags + ']';
    }

private:
    double x_, y_;
    double radius_;
    std::string color_;
    std::vector<std::string> tags_;
};

// Catalog of pre-configured prototypes, cloned instead of constructed.
class ShapeRegistry {
public:
    void registerPrototype(const std::string& name, std::unique_ptr<Shape> prototype) {
        prototypes_[name] = std::move(prototype);
    }

    std::unique_ptr<Shape> create(const std::string& name) const {
        return prototypes_.at(name)->clone();
    }

private:
    std::unordered_map<std::string, std::unique_ptr<Shape>> prototypes_;
};

int main() {
    ShapeRegistry registry;
    registry.registerPrototype(
        "warning-marker", std::make_unique<Circle>(0, 0, 12, "red", std::vector<std::string>{"alert"}));

    auto first = registry.create("warning-marker");
    auto second = registry.create("warning-marker");
    second->moveTo(40, 25);

    std::cout << first->describe() << '\n';
    std::cout << second->describe() << '\n';
    return 0;
}
