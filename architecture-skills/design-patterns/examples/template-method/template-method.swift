// Template Method pattern in Swift.
//
// Swift's idiomatic form is a protocol extension: the extension's
// default method is the template and the protocol requirements are the
// varying steps — no base class needed, and it works for structs.
// Composition (passing the steps as closures) is often preferred over
// any inheritance-based form.

import Foundation

struct LineItem {
    let product: String
    let units: Int
    let price: Double

    var subtotal: Double { Double(units) * price }
}

protocol SalesReport {
    func header() -> String
    func row(_ item: LineItem) -> String
    func footer(total: Double) -> String
}

extension SalesReport {
    /// The template method: iteration and totalling never vary.
    func generate(_ items: [LineItem]) -> String {
        var lines = [header()]
        var total = 0.0
        for item in items {
            lines.append(row(item))
            total += item.subtotal
        }
        lines.append(footer(total: total))
        return lines.joined(separator: "\n")
    }
}

struct CsvReport: SalesReport {
    func header() -> String {
        "product,units,price,subtotal"
    }

    func row(_ item: LineItem) -> String {
        String(format: "%@,%d,%.2f,%.2f", item.product, item.units, item.price, item.subtotal)
    }

    func footer(total: Double) -> String {
        String(format: "total,,,%.2f", total)
    }
}

struct MarkdownReport: SalesReport {
    func header() -> String {
        "| Product | Units | Subtotal |\n| --- | --- | --- |"
    }

    func row(_ item: LineItem) -> String {
        String(format: "| %@ | %d | $%.2f |", item.product, item.units, item.subtotal)
    }

    func footer(total: Double) -> String {
        String(format: "\n**Total: $%.2f**", total)
    }
}

let items = [
    LineItem(product: "Keyboard", units: 2, price: 80.00),
    LineItem(product: "Mouse", units: 1, price: 25.50),
    LineItem(product: "Monitor", units: 3, price: 210.00),
]

let reports: [(String, SalesReport)] = [
    ("CsvReport", CsvReport()),
    ("MarkdownReport", MarkdownReport()),
]

for (name, report) in reports {
    print("--- \(name) ---")
    print(report.generate(items))
    print()
}
