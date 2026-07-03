// Observer pattern in Swift.
//
// Closures with token-based unsubscription keep it simple. In real
// apps prefer the platform tools: Combine publishers, the Observation
// framework (@Observable), NotificationCenter, or KVO. Stored closures
// strongly capture what they reference — use [weak self] in observers
// that outlive their owner.

import Foundation

final class StockTicker {
    typealias PriceObserver = (String, Double) -> Void

    private var observers: [UUID: PriceObserver] = [:]

    @discardableResult
    func subscribe(_ observer: @escaping PriceObserver) -> UUID {
        let token = UUID()
        observers[token] = observer
        return token
    }

    func unsubscribe(_ token: UUID) {
        observers.removeValue(forKey: token)
    }

    func updatePrice(symbol: String, price: Double) {
        for observer in observers.values {
            observer(symbol, price)
        }
    }
}

final class PriceDisplay {
    let name: String

    init(name: String) {
        self.name = name
    }

    func onPrice(symbol: String, price: Double) {
        print("\(name): \(symbol) is now $\(String(format: "%.2f", price))")
    }
}

func makeAlert(watched: String, threshold: Double) -> StockTicker.PriceObserver {
    return { symbol, price in
        if symbol == watched && price > threshold {
            print("ALERT: \(watched) crossed $\(String(format: "%.2f", threshold)) "
                + "(now $\(String(format: "%.2f", price)))")
        }
    }
}

let ticker = StockTicker()
let display = PriceDisplay(name: "Lobby display")
let displayToken = ticker.subscribe { symbol, price in
    display.onPrice(symbol: symbol, price: price)
}
ticker.subscribe(makeAlert(watched: "ACME", threshold: 100))

ticker.updatePrice(symbol: "ACME", price: 98.5)
ticker.updatePrice(symbol: "ACME", price: 101.25)

ticker.unsubscribe(displayToken)
ticker.updatePrice(symbol: "GLOBEX", price: 45) // only the alert remains
