// Proxy pattern in C++ (virtual proxy: lazy-loading image).
//
// A unique_ptr created on first call implements the lazy load. Note
// that smart pointers themselves are the standard library's proxy-like
// constructs: they overload * and -> to interpose on every access to
// the underlying object.

#include <iostream>
#include <memory>
#include <string>

class Image {  // subject interface
public:
    virtual ~Image() = default;
    virtual void display() = 0;
};

class RealImage : public Image {  // real subject: expensive to create
public:
    explicit RealImage(std::string filename) : filename_(std::move(filename)) {
        std::cout << "Loading " << filename_ << " from disk (expensive)\n";
    }

    void display() override { std::cout << "Displaying " << filename_ << '\n'; }

private:
    std::string filename_;
};

class ImageProxy : public Image {  // defers creating RealImage until first use
public:
    explicit ImageProxy(std::string filename) : filename_(std::move(filename)) {}

    void display() override {
        if (!real_) {
            real_ = std::make_unique<RealImage>(filename_);
        }
        real_->display();
    }

private:
    std::string filename_;
    std::unique_ptr<RealImage> real_;
};

int main() {
    ImageProxy holiday("holiday.png");
    ImageProxy unused("unused.png");
    std::cout << "Proxies created; nothing loaded yet\n";

    holiday.display();
    holiday.display();  // loaded once, displayed twice

    std::cout << "unused.png was never loaded\n";
    return 0;
}
