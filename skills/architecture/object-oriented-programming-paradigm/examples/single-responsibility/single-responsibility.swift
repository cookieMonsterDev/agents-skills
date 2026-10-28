// Single Responsibility Principle in Swift.
//
// An Invoice that computes totals, formats itself, AND persists itself
// serves three actors. The refactor gives each actor its own type.

import Foundation

struct LineItem {
    let description: String
    let amount: Double
}

final class Invoice {
    let id: String
    let customer: String
    var items: [LineItem] = []

    init(id: String, customer: String) {
        self.id = id
        self.customer = customer
    }

    func addItem(description: String, amount: Double) {
        items.append(LineItem(description: description, amount: amount))
    }
}

struct InvoiceCalculator {
    let taxRate: Double

    func total(invoice: Invoice) -> Double {
        let subtotal = invoice.items.reduce(0) { $0 + $1.amount }
        return subtotal * (1 + taxRate)
    }
}

struct TextInvoiceFormatter {
    func format(invoice: Invoice, total: Double) -> String {
        var lines = ["Invoice \(invoice.id) for \(invoice.customer)"]
        for item in invoice.items {
            lines.append(String(format: "  %-12@ $%8.2f", item.description, item.amount))
        }
        lines.append(String(format: "  %-12@ $%8.2f", "TOTAL", total))
        return lines.joined(separator: "\n")
    }
}

final class InMemoryInvoiceRepository {
    private var rows: [String: Invoice] = [:]

    func save(_ invoice: Invoice) { rows[invoice.id] = invoice }
    func count() -> Int { rows.count }
}

let invoice = Invoice(id: "INV-042", customer: "ACME Corp")
invoice.addItem(description: "Consulting", amount: 1200)
invoice.addItem(description: "Hosting", amount: 90)

let calculator = InvoiceCalculator(taxRate: 0.20)
let formatter = TextInvoiceFormatter()
let repository = InMemoryInvoiceRepository()

let total = calculator.total(invoice: invoice)
print(formatter.format(invoice: invoice, total: total))

repository.save(invoice)
print("saved \(invoice.id) (\(repository.count()) record(s) stored)")
