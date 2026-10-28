// Law of Demeter in Swift.
//
// order.customer.wallet.deduct(due) couples checkout to Customer's
// internals. customer.pay(due) is tell-don't-ask: Wallet stays private
// and the never-negative rule is enforced at the owner.

import Foundation

// --- Before (train wreck, sketched): ---
//
// final class Checkout {
//     func collect(order: Order, due: Decimal) throws {
//         try order.customer.wallet.deduct(due)
//     }
// }

// --- After: talk only to immediate collaborators ---

enum PaymentError: Error, CustomStringConvertible {
    case nonPositiveAmount
    case insufficientFunds

    var description: String {
        switch self {
        case .nonPositiveAmount: return "payment must be positive"
        case .insufficientFunds: return "insufficient funds"
        }
    }
}

private final class Wallet {
    private(set) var balance: Decimal

    init(opening: Decimal) throws {
        guard opening >= 0 else {
            throw PaymentError.nonPositiveAmount
        }
        balance = opening
    }

    func deduct(_ amount: Decimal) throws {
        guard amount > 0 else { throw PaymentError.nonPositiveAmount }
        guard amount <= balance else { throw PaymentError.insufficientFunds }
        balance -= amount
    }
}

final class Customer {
    let name: String
    private let wallet: Wallet

    init(name: String, opening: Decimal) throws {
        self.name = name
        self.wallet = try Wallet(opening: opening)
    }

    func pay(_ amount: Decimal) throws {
        try wallet.deduct(amount)
    }

    var balance: Decimal { wallet.balance }
}

struct Order {
    let id: String
    let customer: Customer
    let total: Decimal
}

final class Checkout {
    func collect(order: Order, due: Decimal) throws {
        try order.customer.pay(due)
    }
}

let ada = try Customer(name: "Ada", opening: 50)
let order = Order(id: "ORD-101", customer: ada, total: 12.5)
let checkout = Checkout()

print(String(format: "%@ wallet before: $%.2f", ada.name, NSDecimalNumber(decimal: ada.balance).doubleValue))
try checkout.collect(order: order, due: order.total)
print(String(format: "collected $%.2f for %@", NSDecimalNumber(decimal: order.total).doubleValue, order.id))
print(String(format: "%@ wallet after:  $%.2f  (invariant intact)", ada.name, NSDecimalNumber(decimal: ada.balance).doubleValue))
