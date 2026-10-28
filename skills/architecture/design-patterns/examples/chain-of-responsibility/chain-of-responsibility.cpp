// Chain of Responsibility pattern in C++.
//
// Support ticket escalation: a virtual handler base class holds the
// next link; each level resolves tickets up to its competence or
// forwards them along the chain.

#include <iostream>
#include <memory>
#include <string>
#include <vector>

struct Ticket {
    std::string subject;
    int severity; // 1 (trivial) .. 4 (critical)
};

class Handler {
public:
    virtual ~Handler() = default;

    Handler* setNext(std::unique_ptr<Handler> next) {
        next_ = std::move(next);
        return next_.get(); // enables a->setNext(b)->setNext(c)
    }

    virtual void handle(const Ticket& ticket) {
        if (next_) {
            next_->handle(ticket);
        } else {
            std::cout << "UNRESOLVED: \"" << ticket.subject << "\" (severity "
                      << ticket.severity << ") -> escalate to engineering\n";
        }
    }

private:
    std::unique_ptr<Handler> next_;
};

class SupportLevel : public Handler {
public:
    SupportLevel(std::string name, int maxSeverity)
        : name_(std::move(name)), maxSeverity_(maxSeverity) {}

    void handle(const Ticket& ticket) override {
        if (ticket.severity <= maxSeverity_) {
            std::cout << name_ << " resolved \"" << ticket.subject
                      << "\" (severity " << ticket.severity << ")\n";
        } else {
            Handler::handle(ticket);
        }
    }

private:
    std::string name_;
    int maxSeverity_;
};

int main() {
    auto chain = std::make_unique<SupportLevel>("Help bot", 1);
    chain->setNext(std::make_unique<SupportLevel>("Frontline agent", 2))
        ->setNext(std::make_unique<SupportLevel>("Support manager", 3));

    const std::vector<Ticket> tickets = {
        {"Reset my password", 1},
        {"Invoice shows wrong amount", 2},
        {"Account data corrupted", 3},
        {"Full region outage", 4},
    };
    for (const auto& ticket : tickets) {
        chain->handle(ticket);
    }
    return 0;
}
