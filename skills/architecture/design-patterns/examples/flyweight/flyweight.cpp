// Flyweight pattern in C++.
//
// std::shared_ptr<const TreeType> expresses both aspects of the pattern
// in the type: the intrinsic state is shared (shared_ptr) and immutable
// (const). Each Tree context carries only its coordinates plus a cheap
// pointer copy.

#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>
#include <vector>

class TreeType {  // flyweight: immutable intrinsic state
public:
    TreeType(std::string name, std::string color)
        : name_(std::move(name)), color_(std::move(color)) {}

    void draw(int x, int y) const {
        std::cout << color_ << ' ' << name_ << " at (" << x << ", " << y << ")\n";
    }

private:
    std::string name_;
    std::string color_;
};

class TreeTypeFactory {
public:
    std::shared_ptr<const TreeType> get(const std::string& name, const std::string& color) {
        const std::string key = name + '/' + color;
        auto it = cache_.find(key);
        if (it == cache_.end()) {
            it = cache_.emplace(key, std::make_shared<const TreeType>(name, color)).first;
        }
        return it->second;
    }

    std::size_t size() const { return cache_.size(); }

private:
    std::unordered_map<std::string, std::shared_ptr<const TreeType>> cache_;
};

struct Tree {  // context: extrinsic state + shared flyweight
    int x;
    int y;
    std::shared_ptr<const TreeType> kind;
};

int main() {
    TreeTypeFactory factory;
    std::vector<Tree> forest = {
        {1, 1, factory.get("oak", "green")},
        {2, 4, factory.get("pine", "dark green")},
        {5, 2, factory.get("oak", "green")},
        {6, 6, factory.get("birch", "light green")},
        {8, 3, factory.get("pine", "dark green")},
        {9, 9, factory.get("oak", "green")},
    };

    for (const Tree& tree : forest) {
        tree.kind->draw(tree.x, tree.y);
    }

    std::cout << "trees planted: " << forest.size()
              << ", tree types in memory: " << factory.size() << '\n';
    return 0;
}
