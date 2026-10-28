// Single Responsibility Principle in C++.
//
// The god Invoice would mix domain math, iostream formatting, and
// storage — and its header would drag all three dependency sets into
// every client, so any concern's change recompiles everything. The
// refactor gives each actor its own class (own header in a real
// project); the Invoice keeps only its data.

#include <iostream>
#include <sstream>
#include <string>
#include <vector>

// --- Before (god class, sketched): three reasons to change ---
//
// class Invoice {
//     double total();          // changes when FINANCE changes tax
//     std::string toText();    // changes when LAYOUT changes
//     void saveToDb();         // changes when STORAGE changes
// };

// --- After: one collaborator per actor ---

struct LineItem {
    std::string description;
    double amount;
};

// Domain object: owns the data, nothing else.
class Invoice {
public:
    Invoice(std::string id, std::string customer)
        : id_(std::move(id)), customer_(std::move(customer)) {}

    void addItem(std::string desc, double amount) {
        items_.push_back({std::move(desc), amount});
    }

    const std::string& id() const { return id_; }
    const std::string& customer() const { return customer_; }
    const std::vector<LineItem>& items() const { return items_; }

private:
    std::string id_;
    std::string customer_;
    std::vector<LineItem> items_;
};

// Finance's class: only tax-rule changes touch this file.
class InvoiceCalculator {
public:
    explicit InvoiceCalculator(double taxRate) : taxRate_(taxRate) {}

    double total(const Invoice& invoice) const {
        double subtotal = 0.0;
        for (const auto& item : invoice.items()) subtotal += item.amount;
        return subtotal * (1.0 + taxRate_);
    }

private:
    double taxRate_;
};

// Presentation's class: only layout changes touch this file.
class TextInvoiceFormatter {
public:
    std::string format(const Invoice& invoice, double total) const {
        std::ostringstream out;
        out << "Invoice " << invoice.id() << " for " << invoice.customer();
        for (const auto& item : invoice.items()) {
            out << "\n  " << item.description << "  $" << item.amount;
        }
        out << "\n  TOTAL  $" << total;
        return out.str();
    }
};

// Ops' class: only storage changes touch this file.
class InMemoryInvoiceRepository {
public:
    void save(const Invoice& invoice) { savedIds_.push_back(invoice.id()); }
    std::size_t count() const { return savedIds_.size(); }

private:
    std::vector<std::string> savedIds_;
};

int main() {
    Invoice invoice("INV-042", "ACME Corp");
    invoice.addItem("Consulting", 1200.00);
    invoice.addItem("Hosting", 90.00);

    InvoiceCalculator calculator(0.20);
    TextInvoiceFormatter formatter;
    InMemoryInvoiceRepository repository;

    double total = calculator.total(invoice);
    std::cout << formatter.format(invoice, total) << "\n";

    repository.save(invoice);
    std::cout << "saved " << invoice.id() << " (" << repository.count()
              << " record(s) stored)\n";
    return 0;
}
