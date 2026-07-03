// Interpreter pattern in C++.
//
// A tiny arithmetic grammar: literals, variables, +, -, *. The classic
// form: an abstract Expr with interpret(context) and one class per
// grammar rule, composed into a tree with unique_ptr. (A std::variant
// with std::visit is a modern alternative that avoids virtual dispatch.)

#include <iostream>
#include <map>
#include <memory>
#include <string>

using Context = std::map<std::string, int>;

class Expr {
public:
    virtual ~Expr() = default;
    virtual int interpret(const Context& context) const = 0;
};

using ExprPtr = std::unique_ptr<Expr>;

class Literal : public Expr {
public:
    explicit Literal(int value) : value_(value) {}
    int interpret(const Context&) const override { return value_; }

private:
    int value_;
};

class Variable : public Expr {
public:
    explicit Variable(std::string name) : name_(std::move(name)) {}
    int interpret(const Context& context) const override { return context.at(name_); }

private:
    std::string name_;
};

class BinaryOp : public Expr {
public:
    BinaryOp(char op, ExprPtr left, ExprPtr right)
        : op_(op), left_(std::move(left)), right_(std::move(right)) {}

    int interpret(const Context& context) const override {
        int l = left_->interpret(context);
        int r = right_->interpret(context);
        switch (op_) {
        case '+': return l + r;
        case '-': return l - r;
        default:  return l * r;
        }
    }

private:
    char op_;
    ExprPtr left_;
    ExprPtr right_;
};

ExprPtr add(ExprPtr l, ExprPtr r) { return std::make_unique<BinaryOp>('+', std::move(l), std::move(r)); }
ExprPtr sub(ExprPtr l, ExprPtr r) { return std::make_unique<BinaryOp>('-', std::move(l), std::move(r)); }
ExprPtr mul(ExprPtr l, ExprPtr r) { return std::make_unique<BinaryOp>('*', std::move(l), std::move(r)); }
ExprPtr lit(int v) { return std::make_unique<Literal>(v); }
ExprPtr var(std::string n) { return std::make_unique<Variable>(std::move(n)); }

int main() {
    // (x + y) * 2 - z
    ExprPtr expression = sub(mul(add(var("x"), var("y")), lit(2)), var("z"));

    const Context first = {{"x", 6}, {"y", 2}, {"z", 3}};
    const Context second = {{"x", 1}, {"y", 1}, {"z", 10}};

    std::cout << "(x + y) * 2 - z with x=6 y=2 z=3   = " << expression->interpret(first) << "\n";
    std::cout << "(x + y) * 2 - z with x=1 y=1 z=10  = " << expression->interpret(second) << "\n";
    return 0;
}
