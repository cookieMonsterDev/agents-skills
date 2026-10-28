// Encapsulation in Swift.
//
// `private(set) var balance` gives public read and class-only write in
// one line — the idiomatic middle ground between a raw public var and a
// hand-written getter. Fallible operations use throws; the invariant
// (balance never negative) holds after every call.

import Foundation

enum AccountError: Error, CustomStringConvertible {
    case nonPositiveAmount
    case insufficientFunds

    var description: String {
        switch self {
        case .nonPositiveAmount: return "amount must be positive"
        case .insufficientFunds: return "insufficient funds"
        }
    }
}

final class BankAccount {
    // Anyone may read balance; only this class may write it.
    private(set) var balance: Double

    init(openingBalance: Double = 0) {
        precondition(openingBalance >= 0, "opening balance cannot be negative")
        self.balance = openingBalance
    }

    func deposit(_ amount: Double) throws {
        guard amount > 0 else { throw AccountError.nonPositiveAmount }
        balance += amount
    }

    func withdraw(_ amount: Double) throws {
        guard amount > 0 else { throw AccountError.nonPositiveAmount }
        guard amount <= balance else { throw AccountError.insufficientFunds }
        balance -= amount
    }
}

let account = BankAccount(openingBalance: 100)

try account.deposit(50)
print(String(format: "after deposit:  $%.2f", account.balance))

do {
    try account.withdraw(250)
} catch {
    print("withdraw $250 rejected: \(error)")
}

try account.withdraw(30)
print(String(format: "after withdraw: $%.2f  (invariant intact)", account.balance))

// account.balance = -500  // compile error: setter is private
