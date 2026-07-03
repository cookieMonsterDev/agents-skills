// Dependency Inversion Principle in C++.
//
// OrderService owns the Notifier abstract base class and receives an
// implementation through its constructor — never `new SmtpNotifier`.
// main() is the composition root that wires ConsoleNotifier or
// RecordingNotifier.

#include <iostream>
#include <memory>
#include <string>
#include <vector>

struct Order {
    std::string id;
    std::string customer_email;
};

/** Abstraction owned by policy: shaped to what place() needs. */
class Notifier {
public:
    virtual ~Notifier() = default;
    virtual void notify(const std::string& email, const std::string& message) = 0;
};

class OrderService {
public:
    explicit OrderService(std::shared_ptr<Notifier> notifier)
        : notifier_(std::move(notifier)) {}

    void place(const Order& order) const {
        std::cout << "placed " << order.id << " for " << order.customer_email << "\n";
        notifier_->notify(order.customer_email, "order " + order.id + " confirmed");
    }

private:
    std::shared_ptr<Notifier> notifier_;
};

// --- Low-level details: depend on the policy's interface ---

class ConsoleNotifier : public Notifier {
public:
    void notify(const std::string& email, const std::string& message) override {
        std::cout << "notify " << email << ": " << message << "\n";
    }
};

class RecordingNotifier : public Notifier {
public:
    void notify(const std::string& email, const std::string& message) override {
        sent_.emplace_back(email, message);
    }

    std::size_t count() const { return sent_.size(); }

private:
    std::vector<std::pair<std::string, std::string>> sent_;
};

int main() {
    std::cout << "-- ConsoleNotifier at composition root --\n";
    OrderService(std::make_shared<ConsoleNotifier>())
        .place({"ORD-001", "alice@example.com"});

    std::cout << "\n-- RecordingNotifier: policy testable without I/O --\n";
    auto recorder = std::make_shared<RecordingNotifier>();
    OrderService(recorder).place({"ORD-002", "bob@example.com"});
    std::cout << recorder->count() << " notification(s) recorded\n";
    return 0;
}
