// Liskov Substitution Principle in C++.
//
// Square-extends-Rectangle is the classic violation: overriding setters
// to keep sides equal breaks Rectangle's invariant. The fix keeps
// Rectangle and Square as separate immutable types behind a Shape interface.

#include <iostream>
#include <memory>
#include <vector>

// --- Violation ---

class Rectangle {
public:
    Rectangle(double w, double h) : width_(w), height_(h) {}
    virtual void setWidth(double w) { width_ = w; }
    virtual void setHeight(double h) { height_ = h; }
    virtual double area() const { return width_ * height_; }

protected:
    double width_, height_;
};

class Square : public Rectangle {
public:
    explicit Square(double side) : Rectangle(side, side) {}
    void setWidth(double w) override { width_ = height_ = w; }
    void setHeight(double h) override { width_ = height_ = h; }
};

double stretchTo4x5(Rectangle& r) {
    r.setWidth(4);
    r.setHeight(5);
    return r.area();
}

// --- Fix: narrow Shape interface ---

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};

class Rect : public Shape {
public:
    Rect(double w, double h) : width_(w), height_(h) {}
    double area() const override { return width_ * height_; }

private:
    const double width_, height_;
};

class Sq : public Shape {
public:
    explicit Sq(double side) : side_(side) {}
    double area() const override { return side_ * side_; }

private:
    const double side_;
};

double totalArea(const std::vector<std::unique_ptr<Shape>>& shapes) {
    double sum = 0;
    for (const auto& s : shapes) sum += s->area();
    return sum;
}

int main() {
    std::cout << "-- Violation: Square substituted for Rectangle --\n";
    Rectangle rect(2, 3);
    double got = stretchTo4x5(rect);
    std::cout << "rectangle: expected 20, got " << got
              << "  (" << (got == 20 ? "ok" : "CONTRACT BROKEN") << ")\n";

    Square square(2);
    got = stretchTo4x5(square);
    std::cout << "   square: expected 20, got " << got
              << "  (" << (got == 20 ? "ok" : "CONTRACT BROKEN") << ")\n";

    std::cout << "\n-- Fix: separate types behind Shape --\n";
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Rect>(4, 5));
    shapes.push_back(std::make_unique<Sq>(5));
    std::cout << "rectangle 4x5: area " << shapes[0]->area() << '\n';
    std::cout << "     square 5: area " << shapes[1]->area() << '\n';
    std::cout << "        total: " << totalArea(shapes) << '\n';
    return 0;
}
