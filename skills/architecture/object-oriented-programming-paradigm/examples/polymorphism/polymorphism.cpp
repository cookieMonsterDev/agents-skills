// Polymorphism in C++.
//
// Subtype polymorphism needs `virtual` and works through pointers or
// references (vector<Shape> by value would slice), hence the vector of
// unique_ptr<Shape>. The template `print_report` shows the parametric
// kind: static dispatch resolved per type at compile time.

#include <cmath>
#include <cstdio>
#include <memory>
#include <string>
#include <vector>

// The abstraction: virtual methods + virtual destructor.
class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
    virtual std::string describe() const = 0;
};

class Circle : public Shape {
public:
    explicit Circle(double radius) : radius_(radius) {}
    double area() const override { return M_PI * radius_ * radius_; }
    std::string describe() const override {
        return "circle r=" + std::to_string(radius_).substr(0, 3);
    }

private:
    double radius_;
};

class Rectangle : public Shape {
public:
    Rectangle(double width, double height) : width_(width), height_(height) {}
    double area() const override { return width_ * height_; }
    std::string describe() const override { return "rectangle"; }

private:
    double width_;
    double height_;
};

class Triangle : public Shape {
public:
    Triangle(double base, double height) : base_(base), height_(height) {}
    double area() const override { return 0.5 * base_ * height_; }
    std::string describe() const override { return "triangle"; }

private:
    double base_;
    double height_;
};

// Parametric polymorphism: one template, a specialized copy per T,
// dispatched statically — no vtable involved when T is concrete.
template <typename T>
void print_report(const T& shape) {
    std::printf("%12s: area %.2f\n", shape.describe().c_str(), shape.area());
}

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(1.0));
    shapes.push_back(std::make_unique<Rectangle>(3.0, 4.0));
    shapes.push_back(std::make_unique<Triangle>(6.0, 2.0));

    // One call site; the runtime type picks the override (dynamic dispatch).
    double total = 0.0;
    for (const auto& shape : shapes) {
        std::printf("%12s: area %.2f\n", shape->describe().c_str(), shape->area());
        total += shape->area();
    }
    std::printf("%12s: area %.2f\n", "total", total);

    // Static dispatch: the compiler binds Circle::area at compile time.
    print_report(Circle(2.0));
    return 0;
}
