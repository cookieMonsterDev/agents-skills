// Singleton pattern in Swift.
//
// `static let` is lazily initialized and thread-safe by language guarantee,
// so the whole pattern is one line — the same shape as URLSession.shared or
// FileManager.default. A private init enforces uniqueness. Prefer injecting
// the instance where feasible; `.shared` call sites are hard to fake in tests.

import Foundation

final class AppConfig {
    static let shared = AppConfig()

    private let settings: [String: String]

    private init() {
        // Stands in for reading a config file once.
        print("Loading configuration (expensive, happens once)")
        settings = [
            "app_name": "InventoryService",
            "db_url": "postgres://localhost/inventory",
            "log_level": "INFO",
        ]
    }

    func get(_ key: String) -> String {
        settings[key, default: ""]
    }
}

let a = AppConfig.shared
let b = AppConfig.shared

print("same instance: \(a === b)")
print("app_name: \(a.get("app_name"))")
print("db_url: \(b.get("db_url"))")
