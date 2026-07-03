// Observer pattern in C++.
//
// std::function is the modern C++ observer: any lambda, functor, or
// bound member can subscribe without an interface hierarchy. subscribe()
// returns an id so callers can unsubscribe (avoiding the classic
// dangling-observer bug).

#include <functional>
#include <iostream>
#include <string>
#include <vector>

using PriceObserver = std::function<void(const std::string&, double)>;

class StockTicker {  // subject
public:
    int subscribe(PriceObserver observer) {
        observers_.push_back({next_id_, std::move(observer)});
        return next_id_++;
    }

    void unsubscribe(int id) {
        std::erase_if(observers_, [id](const auto& entry) { return entry.first == id; });
    }

    void updatePrice(const std::string& symbol, double price) {
        for (const auto& [id, observer] : observers_) {
            observer(symbol, price);
        }
    }

private:
    std::vector<std::pair<int, PriceObserver>> observers_;
    int next_id_ = 0;
};

class PriceDisplay {
public:
    explicit PriceDisplay(std::string name) : name_(std::move(name)) {}

    void onPrice(const std::string& symbol, double price) const {
        std::cout << name_ << ": " << symbol << " is now $" << price << '\n';
    }

private:
    std::string name_;
};

int main() {
    std::cout.precision(2);
    std::cout << std::fixed;

    StockTicker ticker;
    PriceDisplay display("Lobby display");

    int displayId = ticker.subscribe(
        [&display](const std::string& symbol, double price) {
            display.onPrice(symbol, price);
        });

    ticker.subscribe([](const std::string& symbol, double price) {
        if (symbol == "ACME" && price > 100.0) {
            std::cout << "ALERT: ACME crossed $100.00 (now $" << price << ")\n";
        }
    });

    ticker.updatePrice("ACME", 98.5);
    ticker.updatePrice("ACME", 101.25);

    ticker.unsubscribe(displayId);
    ticker.updatePrice("GLOBEX", 45.0);  // only the alert remains
    return 0;
}
