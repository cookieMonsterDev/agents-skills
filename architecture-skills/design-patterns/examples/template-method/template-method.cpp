// Template Method pattern in C++.
//
// Shown as the NVI idiom (non-virtual interface): the public generate()
// is non-virtual and fixes the skeleton; the varying steps are private
// virtuals. Modern C++ often prefers composition — passing lambdas or a
// strategy-like steps object — over inheritance for this.

#include <iostream>
#include <memory>
#include <sstream>
#include <string>
#include <vector>

struct LineItem {
    std::string product;
    int units;
    double price;

    double subtotal() const { return units * price; }
};

class SalesReport {
public:
    virtual ~SalesReport() = default;

    // The template method: iteration and totalling never vary.
    std::string generate(const std::vector<LineItem>& items) const {
        std::ostringstream out;
        out << header() << "\n";
        double total = 0.0;
        for (const auto& item : items) {
            out << row(item) << "\n";
            total += item.subtotal();
        }
        out << footer(total) << "\n";
        return out.str();
    }

private:
    virtual std::string header() const = 0;
    virtual std::string row(const LineItem& item) const = 0;
    virtual std::string footer(double total) const = 0;
};

class CsvReport : public SalesReport {
    std::string header() const override { return "product,units,price,subtotal"; }

    std::string row(const LineItem& item) const override {
        char buf[128];
        std::snprintf(buf, sizeof(buf), "%s,%d,%.2f,%.2f", item.product.c_str(),
                      item.units, item.price, item.subtotal());
        return buf;
    }

    std::string footer(double total) const override {
        char buf[64];
        std::snprintf(buf, sizeof(buf), "total,,,%.2f", total);
        return buf;
    }
};

class MarkdownReport : public SalesReport {
    std::string header() const override {
        return "| Product | Units | Subtotal |\n| --- | --- | --- |";
    }

    std::string row(const LineItem& item) const override {
        char buf[128];
        std::snprintf(buf, sizeof(buf), "| %s | %d | $%.2f |", item.product.c_str(),
                      item.units, item.subtotal());
        return buf;
    }

    std::string footer(double total) const override {
        char buf[64];
        std::snprintf(buf, sizeof(buf), "\n**Total: $%.2f**", total);
        return buf;
    }
};

int main() {
    const std::vector<LineItem> items = {
        {"Keyboard", 2, 80.00},
        {"Mouse", 1, 25.50},
        {"Monitor", 3, 210.00},
    };

    std::vector<std::unique_ptr<SalesReport>> reports;
    reports.push_back(std::make_unique<CsvReport>());
    reports.push_back(std::make_unique<MarkdownReport>());

    for (const auto& report : reports) {
        std::cout << report->generate(items) << "\n";
    }
    return 0;
}
