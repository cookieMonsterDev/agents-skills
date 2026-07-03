// Classes & objects in Swift.
//
// Swift bundles state and behavior in both struct (value, copied) and
// class (reference, shared identity). A bank account is a natural
// class: two references must observe the same mutation. `init` is the
// constructor, `static` members belong to the type, and transfer()
// stays a free function because it owns neither account.

import Foundation

final class BankAccount {
    // Static member: one counter shared by all instances.
    private static var accountsOpened = 0

    // Instance state: one copy per object, never shared.
    let number: String
    let owner: String
    private(set) var balance: Double

    // Initializer: the only way in; if it returns, state is valid.
    init(owner: String, openingBalance: Double = 0) {
        precondition(openingBalance >= 0, "opening balance cannot be negative")
        BankAccount.accountsOpened += 1
        self.number = String(format: "ACC-%04d", BankAccount.accountsOpened)
        self.owner = owner
        self.balance = openingBalance
    }

    // Instance methods: implicit `self` binds them to one object.
    func deposit(_ amount: Double) {
        precondition(amount > 0, "deposit must be positive")
        balance += amount
    }

    func withdraw(_ amount: Double) {
        precondition(amount <= balance, "\(number): insufficient funds")
        balance -= amount
    }

    var description: String {
        String(format: "%@ (%@): $%.2f", number, owner, balance)
    }

    // Static method: bound to the type, callable with no instance.
    static func totalOpened() -> Int {
        accountsOpened
    }
}

// Free function: coordinates two objects, owns neither.
func transfer(from source: BankAccount, to target: BankAccount, amount: Double) {
    source.withdraw(amount)
    target.deposit(amount)
}

// Two objects from one blueprint, each with independent state.
let alice = BankAccount(owner: "Alice", openingBalance: 100)
let bob = BankAccount(owner: "Bob")

alice.deposit(50)
bob.deposit(20)
alice.withdraw(30)

print(alice.description) // Bob's balance is untouched
print(bob.description)

transfer(from: alice, to: bob, amount: 40)
print("after transfer:")
print(alice.description)
print(bob.description)

print("accounts opened: \(BankAccount.totalOpened())")
