// Bridge pattern in C++.
//
// Shapes (the abstraction) hold a reference to a renderer (the
// implementation) so the two hierarchies vary independently. Ownership
// stays with the caller; shapes only observe the renderer.

#include <cstdio>
#include <string>

namespace {

std::string num(double value) {
    char buf[32];
    std::snprintf(buf, sizeof(buf), "%.1f", value);
    return buf;
}

}  // namespace

class Renderer {
public:
    virtual ~Renderer() = default;
    virtual std::string circle(double radius) const = 0;
    virtual std::string rectangle(double width, double height) const = 0;
};

class VectorRenderer : public Renderer {
public:
    std::string circle(double radius) const override {
        return "<circle r=" + num(radius) + "/>";
    }
    std::string rectangle(double width, double height) const override {
        return "<rect w=" + num(width) + " h=" + num(height) + "/>";
    }
};

class RasterRenderer : public Renderer {
public:
    std::string circle(double radius) const override {
        return "pixels for a circle of radius " + num(radius);
    }
    std::string rectangle(double width, double height) const override {
        return "pixels for a " + num(width) + "x" + num(height) + " rectangle";
    }
};

class Shape {
public:
    explicit Shape(const Renderer& renderer) : renderer_(renderer) {}
    virtual ~Shape() = default;
    virtual std::string draw() const = 0;

protected:
    const Renderer& renderer_;
};

class Circle : public Shape {
public:
    Circle(const Renderer& renderer, double radius)
        : Shape(renderer), radius_(radius) {}
    std::string draw() const override { return renderer_.circle(radius_); }

private:
    double radius_;
};

class Rectangle : public Shape {
public:
    Rectangle(const Renderer& renderer, double width, double height)
        : Shape(renderer), width_(width), height_(height) {}
    std::string draw() const override {
        return renderer_.rectangle(width_, height_);
    }

private:
    double width_;
    double height_;
};

int main() {
    VectorRenderer vector;
    RasterRenderer raster;
    const Renderer* renderers[] = {&vector, &raster};

    for (const Renderer* renderer : renderers) {
        Circle circle(*renderer, 5.0);
        Rectangle rectangle(*renderer, 3.0, 4.0);
        std::printf("%s\n%s\n", circle.draw().c_str(), rectangle.draw().c_str());
    }
    return 0;
}
