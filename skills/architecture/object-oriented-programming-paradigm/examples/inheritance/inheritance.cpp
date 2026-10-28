// Inheritance in C++.
//
// Overridable methods must be declared `virtual`; overrides say
// `override` so the compiler catches signature drift, and Contractor is
// `final`. A base class deleted through a base pointer needs a virtual
// destructor. Manager extends the base rule via Employee::monthlyPay();
// Contractor replaces it.

#include <iostream>
#include <iomanip>
#include <memory>
#include <string>
#include <vector>

class Employee {
public:
    Employee(std::string name, double baseSalary)
        : name_(std::move(name)), baseSalary_(baseSalary) {}
    virtual ~Employee() = default; // virtual: deleted via Employee*

    virtual std::string role() const { return "employee"; }
    virtual double monthlyPay() const { return baseSalary_; }

    void printPayslip() const {
        std::cout << std::left << std::setw(9) << name_
                  << std::setw(11) << role()
                  << "$" << std::right << std::setw(9) << std::fixed
                  << std::setprecision(2) << monthlyPay() << "\n";
    }

protected:
    std::string name_;
    double baseSalary_;
};

class Manager : public Employee {
public:
    Manager(std::string name, double baseSalary, int directReports)
        : Employee(std::move(name), baseSalary), directReports_(directReports) {}

    std::string role() const override { return "manager"; }

    double monthlyPay() const override {
        // Call the base implementation, then extend it.
        return Employee::monthlyPay() + 400.00 * directReports_;
    }

private:
    int directReports_;
};

class Contractor final : public Employee {
public:
    Contractor(std::string name, double hourlyRate, double hoursBilled)
        : Employee(std::move(name), 0.0),
          hourlyRate_(hourlyRate), hoursBilled_(hoursBilled) {}

    std::string role() const override { return "contractor"; }

    double monthlyPay() const override {
        return hourlyRate_ * hoursBilled_; // full replacement
    }

private:
    double hourlyRate_;
    double hoursBilled_;
};

int main() {
    // Payroll owns everyone through the base type; dispatch is virtual.
    std::vector<std::unique_ptr<Employee>> staff;
    staff.push_back(std::make_unique<Employee>("Ada", 4200.00));
    staff.push_back(std::make_unique<Manager>("Grace", 6500.00, 5));
    staff.push_back(std::make_unique<Contractor>("Linus", 95.00, 140.0));

    double total = 0.0;
    for (const auto& person : staff) {
        person->printPayslip();
        total += person->monthlyPay();
    }
    std::cout << std::left << std::setw(20) << "total"
              << "$" << std::right << std::setw(9) << total << "\n";
    return 0;
}
