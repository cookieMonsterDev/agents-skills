// Open/Closed Principle in Swift.
//
// PricingEngine is closed: it iterates registered discount rules and
// never names a concrete rule. FlashSale is added later with zero edits
// to the engine.

import Foundation

struct Order {
    let subtotal: Double
    let itemCount: Int
    let isMember: Bool
}

protocol DiscountRule {
    var name: String { get }
    func discount(order: Order) -> Double
}

struct BulkDiscount: DiscountRule {
    let name = "bulk"
    func discount(order: Order) -> Double {
        order.itemCount >= 10 ? 0.05 * order.subtotal : 0
    }
}

struct MemberDiscount: DiscountRule {
    let name = "member"
    func discount(order: Order) -> Double {
        order.isMember ? 0.10 * order.subtotal : 0
    }
}

final class PricingEngine {
    private var rules: [DiscountRule] = []

    func register(_ rule: DiscountRule) { rules.append(rule) }

    func total(order: Order) -> Double {
        var total = order.subtotal
        for rule in rules {
            let amount = rule.discount(order: order)
            if amount > 0 {
                print(String(format: "  %6@: -$%.2f", rule.name, amount))
            }
            total -= amount
        }
        return total
    }
}

struct FlashSale: DiscountRule {
    let name = "flash"
    let amount: Double
    let threshold: Double

    func discount(order: Order) -> Double {
        order.subtotal > threshold ? amount : 0
    }
}

let order = Order(subtotal: 120, itemCount: 12, isMember: true)
let engine = PricingEngine()
engine.register(BulkDiscount())
engine.register(MemberDiscount())

print(String(format: "subtotal: $%.2f", order.subtotal))
print(String(format: "total:    $%.2f", engine.total(order: order)))

print("-- registering FlashSale: no engine edits --")
engine.register(FlashSale(amount: 15, threshold: 100))
print(String(format: "total:    $%.2f", engine.total(order: order)))
