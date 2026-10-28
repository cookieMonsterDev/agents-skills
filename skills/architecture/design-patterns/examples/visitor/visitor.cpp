// Visitor pattern in C++.
//
// The classic double dispatch: virtual accept() on the shape resolves
// the concrete shape type, the visit call resolves the operation.
// Modern C++ often replaces this with std::variant + std::visit, which
// gives the same "new operation without touching the types" property
// with less boilerplate; the classic form is shown here.

#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Circle;
class Rectangle;
class Triangle;

class ShapeVisitor {
public:
    virtual ~ShapeVisitor() = default;
    virtual void visit(const Circle& circle) = 0;
    virtual void visit(const Rectangle& rectangle) = 0;
    virtual void visit(const Triangle& triangle) = 0;
};

class Shape {
public:
    virtual ~Shape() = default;
    virtual void accept(ShapeVisitor& visitor) const = 0;
};

class Circle : public Shape {
public:
    explicit Circle(double radius) : radius(radius) {}
    void accept(ShapeVisitor& visitor) const override { visitor.visit(*this); }
    double radius;
};

class Rectangle : public Shape {
public:
    Rectangle(double width, double height) : width(width), height(height) {}
    void accept(ShapeVisitor& visitor) const override { visitor.visit(*this); }
    double width, height;
};

class Triangle : public Shape {
public:
    Triangle(double base, double height) : base(base), height(height) {}
    void accept(ShapeVisitor& visitor) const override { visitor.visit(*this); }
    double base, height;
};

class AreaVisitor : public ShapeVisitor {
public:
    void visit(const Circle& c) override { area = M_PI * c.radius * c.radius; }
    void visit(const Rectangle& r) override { area = r.width * r.height; }
    void visit(const Triangle& t) override { area = 0.5 * t.base * t.height; }
    double area = 0.0;
};

class SvgExportVisitor : public ShapeVisitor {
public:
    void visit(const Circle& c) override {
        markup = format("<circle r=\"%g\" />", c.radius, 0.0);
    }
    void visit(const Rectangle& r) override {
        markup = format("<rect width=\"%g\" height=\"%g\" />", r.width, r.height);
    }
    void visit(const Triangle& t) override {
        char buf[96];
        std::snprintf(buf, sizeof(buf), "<polygon points=\"0,%g %g,%g 0,0\" />",
                      t.height, t.base, t.height);
        markup = buf;
    }
    std::string markup;

private:
    static std::string format(const char* fmt, double a, double b) {
        char buf[96];
        std::snprintf(buf, sizeof(buf), fmt, a, b);
        return buf;
    }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(2));
    shapes.push_back(std::make_unique<Rectangle>(3, 4));
    shapes.push_back(std::make_unique<Triangle>(6, 2));

    AreaVisitor area;
    SvgExportVisitor svg;
    double total = 0.0;

    std::cout << std::fixed << std::setprecision(2);
    for (const auto& shape : shapes) {
        shape->accept(area);
        shape->accept(svg);
        std::cout << "area=" << std::setw(6) << area.area << "  " << svg.markup << "\n";
        total += area.area;
    }
    std::cout << "total area: " << total << "\n";
    return 0;
}
