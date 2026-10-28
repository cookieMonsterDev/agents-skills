// Inheritance in Swift.
//
// Manager and Contractor are genuinely is-a Employee: payroll can pay
// any of them through the base class. Manager extends the base pay rule
// via super.monthlyPay(); Contractor replaces it. Protocols + structs
// are preferred in Swift, but class inheritance fits open hierarchies.

import Foundation

class Employee {
    let name: String
    let baseSalary: Double

    init(name: String, baseSalary: Double) {
        self.name = name
        self.baseSalary = baseSalary
    }

    var role: String { "employee" }

    func monthlyPay() -> Double { baseSalary }

    func payslip() -> String {
        String(format: "%-8@ %-10@ $%9.2f", name, role, monthlyPay())
    }
}

final class Manager: Employee {
    let directReports: Int

    init(name: String, baseSalary: Double, directReports: Int) {
        self.directReports = directReports
        super.init(name: name, baseSalary: baseSalary)
    }

    override var role: String { "manager" }

    override func monthlyPay() -> Double {
        super.monthlyPay() + 400.0 * Double(directReports)
    }
}

final class Contractor: Employee {
    let hourlyRate: Double
    let hoursBilled: Double

    init(name: String, hourlyRate: Double, hoursBilled: Double) {
        self.hourlyRate = hourlyRate
        self.hoursBilled = hoursBilled
        super.init(name: name, baseSalary: 0)
    }

    override var role: String { "contractor" }

    override func monthlyPay() -> Double { hourlyRate * hoursBilled }
}

let staff: [Employee] = [
    Employee(name: "Ada", baseSalary: 4200),
    Manager(name: "Grace", baseSalary: 6500, directReports: 5),
    Contractor(name: "Linus", hourlyRate: 95, hoursBilled: 140),
]

var total = 0.0
for person in staff {
    print(person.payslip())
    total += person.monthlyPay()
}
print(String(format: "%-19@ $%9.2f", "total", total))
