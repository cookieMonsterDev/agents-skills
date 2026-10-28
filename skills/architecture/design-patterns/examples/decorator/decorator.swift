// Decorator pattern in Swift.
//
// Add-ons wrap another Beverage behind the same protocol. Note the
// difference from protocol extensions, which add behavior to *every*
// conforming type at compile time; wrapping decorates individual
// instances at runtime.

import Foundation

protocol Beverage {
    var description: String { get }
    var cost: Double { get }
}

struct Espresso: Beverage {
    let description = "espresso"
    let cost = 2.00
}

struct AddOn: Beverage {
    let inner: Beverage
    let label: String
    let surcharge: Double

    var description: String { "\(inner.description) + \(label)" }
    var cost: Double { inner.cost + surcharge }
}

func milk(_ inner: Beverage) -> Beverage {
    AddOn(inner: inner, label: "milk", surcharge: 0.30)
}

func mocha(_ inner: Beverage) -> Beverage {
    AddOn(inner: inner, label: "mocha", surcharge: 0.50)
}

func whippedCream(_ inner: Beverage) -> Beverage {
    AddOn(inner: inner, label: "whipped cream", surcharge: 0.40)
}

let plain: Beverage = Espresso()
let fancy = whippedCream(mocha(milk(Espresso())))

for drink in [plain, fancy] {
    print("\(drink.description): $\(String(format: "%.2f", drink.cost))")
}
