// State pattern in C++.
//
// Stateless states are shared as singletons (no allocation per
// transition). An alternative modern-C++ form is std::variant over
// state structs with std::visit dispatch, which avoids virtual calls.

#include <iostream>

class VendingMachine;

class State {
public:
    virtual ~State() = default;
    virtual void insertCoin(VendingMachine& m) const = 0;
    virtual void selectItem(VendingMachine& m) const = 0;
};

class VendingMachine {  // context
public:
    explicit VendingMachine(int stock);

    void insertCoin() { state_->insertCoin(*this); }
    void selectItem() { state_->selectItem(*this); }

    void transitionTo(const State& state) { state_ = &state; }

    int stock = 0;

private:
    const State* state_;
};

class Idle : public State {
public:
    void insertCoin(VendingMachine& m) const override;
    void selectItem(VendingMachine&) const override {
        std::cout << "insert a coin first\n";
    }
    static const Idle instance;
};

class HasCoin : public State {
public:
    void insertCoin(VendingMachine&) const override {
        std::cout << "coin already inserted, returning it\n";
    }
    void selectItem(VendingMachine& m) const override;
    static const HasCoin instance;
};

class SoldOut : public State {
public:
    void insertCoin(VendingMachine&) const override {
        std::cout << "sold out, returning coin\n";
    }
    void selectItem(VendingMachine&) const override { std::cout << "sold out\n"; }
    static const SoldOut instance;
};

const Idle Idle::instance{};
const HasCoin HasCoin::instance{};
const SoldOut SoldOut::instance{};

void Idle::insertCoin(VendingMachine& m) const {
    std::cout << "coin accepted\n";
    m.transitionTo(HasCoin::instance);
}

void HasCoin::selectItem(VendingMachine& m) const {
    m.stock--;
    std::cout << "item dispensed (" << m.stock << " left)\n";
    if (m.stock == 0) {
        m.transitionTo(SoldOut::instance);
    } else {
        m.transitionTo(Idle::instance);
    }
}

VendingMachine::VendingMachine(int stock)
    : stock(stock),
      state_(stock > 0 ? static_cast<const State*>(&Idle::instance)
                       : &SoldOut::instance) {}

int main() {
    VendingMachine machine(2);
    machine.selectItem();  // insert a coin first
    machine.insertCoin();
    machine.insertCoin();  // coin already inserted
    machine.selectItem();  // item dispensed (1 left)
    machine.insertCoin();
    machine.selectItem();  // item dispensed (0 left)
    machine.insertCoin();  // sold out, returning coin
    return 0;
}
