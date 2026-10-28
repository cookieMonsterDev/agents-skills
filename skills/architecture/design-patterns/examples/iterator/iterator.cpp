// Iterator pattern in C++.
//
// A binary search tree traversed in sorted order. Iterators are the
// STL's core abstraction: rather than a GoF hasNext/next class, a
// custom collection provides begin()/end() and an iterator with
// operator++/operator*/operator!=, which is all range-based for needs.
// The iterator carries an explicit stack replacing the recursive walk.

#include <iostream>
#include <memory>
#include <vector>

class SortedTree {
    struct Node {
        int value;
        std::unique_ptr<Node> left, right;
        explicit Node(int v) : value(v) {}
    };

    std::unique_ptr<Node> root_;

public:
    void add(int value) {
        std::unique_ptr<Node>* slot = &root_;
        while (*slot) {
            slot = value < (*slot)->value ? &(*slot)->left : &(*slot)->right;
        }
        *slot = std::make_unique<Node>(value);
    }

    class iterator {
        std::vector<const Node*> stack_; // nodes whose left subtrees are done

        void pushLeftSpine(const Node* node) {
            for (; node != nullptr; node = node->left.get()) {
                stack_.push_back(node);
            }
        }

    public:
        explicit iterator(const Node* root) { pushLeftSpine(root); }

        int operator*() const { return stack_.back()->value; }

        iterator& operator++() {
            const Node* node = stack_.back();
            stack_.pop_back();
            pushLeftSpine(node->right.get());
            return *this;
        }

        bool operator!=(const iterator& other) const {
            return stack_ != other.stack_;
        }
    };

    iterator begin() const { return iterator(root_.get()); }
    iterator end() const { return iterator(nullptr); }
};

int main() {
    SortedTree tree;
    for (int value : {5, 3, 8, 1, 4, 9, 7}) {
        tree.add(value);
    }

    int sum = 0;
    std::cout << "in order:";
    for (int value : tree) {
        std::cout << " " << value;
        sum += value;
    }
    std::cout << "\nsum: " << sum << "\n";
    return 0;
}
