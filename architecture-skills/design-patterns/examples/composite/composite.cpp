// Composite pattern in C++.
//
// Files and directories share the Node interface; directories own
// their children through unique_ptr, mirroring real tree ownership.

#include <cstdio>
#include <memory>
#include <string>
#include <utility>
#include <vector>

class Node {
public:
    explicit Node(std::string name) : name_(std::move(name)) {}
    virtual ~Node() = default;
    virtual long size() const = 0;
    virtual void print(int indent) const = 0;

protected:
    std::string name_;
};

class File : public Node {
public:
    File(std::string name, long size) : Node(std::move(name)), size_(size) {}

    long size() const override { return size_; }

    void print(int indent) const override {
        std::printf("%*s%s (%ld B)\n", indent, "", name_.c_str(), size_);
    }

private:
    long size_;
};

class Directory : public Node {
public:
    explicit Directory(std::string name) : Node(std::move(name)) {}

    Directory& add(std::unique_ptr<Node> child) {
        children_.push_back(std::move(child));
        return *this;
    }

    long size() const override {
        long total = 0;
        for (const auto& child : children_) total += child->size();
        return total;
    }

    void print(int indent) const override {
        std::printf("%*s%s/ (%ld B)\n", indent, "", name_.c_str(), size());
        for (const auto& child : children_) child->print(indent + 2);
    }

private:
    std::vector<std::unique_ptr<Node>> children_;
};

int main() {
    auto src = std::make_unique<Directory>("src");
    src->add(std::make_unique<File>("main.py", 1200));
    src->add(std::make_unique<File>("util.py", 450));

    auto docs = std::make_unique<Directory>("docs");
    docs->add(std::make_unique<File>("readme.md", 800));

    Directory project("project");
    project.add(std::move(src));
    project.add(std::move(docs));
    project.add(std::make_unique<File>(".gitignore", 20));

    project.print(0);
    return 0;
}
