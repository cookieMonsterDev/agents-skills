// Strategy pattern in Swift.
//
// Closures cover stateless strategies (sorted(by:) takes one), so the
// classic protocol form is only needed when a strategy carries state or
// several requirements. Both are shown; the struct plugs in by passing
// its method as a closure.

import Foundation

struct Order {
    let weightKg: Double
    let distanceKm: Double
}

// --- Closure form: idiomatic for stateless strategies ---

typealias ShippingStrategy = (Order) -> Double

let flatRate: ShippingStrategy = { _ in 5.00 }
let weightBased: ShippingStrategy = { 4.00 + 1.50 * $0.weightKg }
let distanceBased: ShippingStrategy = { 2.00 + 0.05 * $0.distanceKm }

// --- Protocol form: for stateful strategies ---

protocol ShippingCost {
    func cost(for order: Order) -> Double
}

/// A stateful strategy: the negotiated rates are its state.
struct CarrierRate: ShippingCost {
    let base: Double
    let perKg: Double

    func cost(for order: Order) -> Double {
        base + perKg * order.weightKg
    }
}

/// Context: delegates the pricing decision to the current strategy.
struct Checkout {
    var strategy: ShippingStrategy

    func shipping(for order: Order) -> Double {
        strategy(order)
    }
}

let order = Order(weightKg: 2.4, distanceKm: 120)
let carrier = CarrierRate(base: 3.00, perKg: 2.00)

let strategies: [(String, ShippingStrategy)] = [
    ("flat", flatRate),
    ("weight", weightBased),
    ("distance", distanceBased),
    ("carrier", carrier.cost(for:)),
]

var checkout = Checkout(strategy: flatRate)
for (name, strategy) in strategies {
    checkout.strategy = strategy
    let padded = String(repeating: " ", count: max(0, 8 - name.count)) + name
    print("\(padded): $\(String(format: "%.2f", checkout.shipping(for: order)))")
}
