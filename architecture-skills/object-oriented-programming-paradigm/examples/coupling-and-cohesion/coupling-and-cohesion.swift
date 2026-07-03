// Coupling and Cohesion in Swift.
//
// A god OrderProcessor that computes tax, validates, and ships couples
// three volatile concerns. Focused types with high cohesion let a tax
// change touch only OrderCalculator.

import Foundation

// --- Before (tightly coupled, sketched): ---
//
// final class OrderProcessor {
//     func process(_ order: Order) throws -> Decimal {
//         let total = order.subtotal * 1.20  // tax
//         guard total > 0 else { throw ... } // validation
//         print("shipped \(order.id)")        // shipping
//         return total
//     }
// }

struct Order {
    let id: String
    let subtotal: Decimal
}

/// Finance's type: only tax-rule changes touch this file.
struct OrderCalculator {
    let taxRate: Decimal

    func total(for order: Order) -> Decimal {
        order.subtotal * (1 + taxRate)
    }
}

/// Compliance's type: only validation rules change touch this file.
struct OrderValidator {
    func validate(order: Order, total: Decimal) throws {
        guard order.subtotal > 0 else {
            throw NSError(domain: "Order", code: 1, userInfo: [NSLocalizedDescriptionKey: "subtotal must be positive"])
        }
        guard total > 0 else {
            throw NSError(domain: "Order", code: 2, userInfo: [NSLocalizedDescriptionKey: "total must be positive"])
        }
    }
}

/// Fulfillment's type: only carrier/API changes touch this file.
struct OrderShipper {
    func ship(order: Order) -> String {
        "shipped \(order.id)"
    }
}

/// Thin orchestrator: wires cohesive pieces, owns no domain rules.
struct OrderService {
    let calculator: OrderCalculator
    let validator: OrderValidator
    let shipper: OrderShipper

    func process(_ order: Order) throws -> Decimal {
        let total = calculator.total(for: order)
        try validator.validate(order: order, total: total)
        print(shipper.ship(order: order))
        return total
    }
}

let order = Order(id: "ORD-204", subtotal: 80)

let service = OrderService(
    calculator: OrderCalculator(taxRate: 0.20),
    validator: OrderValidator(),
    shipper: OrderShipper()
)
let total = try service.process(order)
print(String(format: "total with 20%% tax: $%.2f", NSDecimalNumber(decimal: total).doubleValue))

let newRateService = OrderService(
    calculator: OrderCalculator(taxRate: 0.08),
    validator: OrderValidator(),
    shipper: OrderShipper()
)
let newTotal = try newRateService.process(order)
print(String(format: "total with 8%% tax:  $%.2f  (only OrderCalculator changed)", NSDecimalNumber(decimal: newTotal).doubleValue))
