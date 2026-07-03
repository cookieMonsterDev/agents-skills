// State pattern in Swift.
//
// An enum with mutating methods is the idiomatic Swift state machine:
// exhaustive switch means the compiler flags unhandled (state, event)
// pairs, and associated values can carry per-state data. Use the
// protocol/class form only when states are open-ended.

enum MachineState {
    case idle
    case hasCoin
    case soldOut
}

struct VendingMachine {
    private(set) var state: MachineState
    private(set) var stock: Int

    init(stock: Int) {
        self.stock = stock
        self.state = stock > 0 ? .idle : .soldOut
    }

    mutating func insertCoin() {
        switch state {
        case .idle:
            print("coin accepted")
            state = .hasCoin
        case .hasCoin:
            print("coin already inserted, returning it")
        case .soldOut:
            print("sold out, returning coin")
        }
    }

    mutating func selectItem() {
        switch state {
        case .idle:
            print("insert a coin first")
        case .hasCoin:
            stock -= 1
            print("item dispensed (\(stock) left)")
            state = stock == 0 ? .soldOut : .idle
        case .soldOut:
            print("sold out")
        }
    }
}

var machine = VendingMachine(stock: 2)
machine.selectItem() // insert a coin first
machine.insertCoin()
machine.insertCoin() // coin already inserted
machine.selectItem() // item dispensed (1 left)
machine.insertCoin()
machine.selectItem() // item dispensed (0 left)
machine.insertCoin() // sold out, returning coin
