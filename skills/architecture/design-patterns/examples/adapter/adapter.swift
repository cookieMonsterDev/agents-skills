// Adapter pattern in Swift.
//
// Swift's idiomatic adapter is a retroactive protocol conformance: an
// extension makes an existing (even third-party) type conform to the
// target protocol with no wrapper type at all. Fall back to a wrapper
// struct when the conformance needs extra state or would clash with
// the type's own semantics.

import Foundation

protocol TemperatureSource {
    var name: String { get }
    var celsius: Double { get }
}

struct ModernSensor: TemperatureSource {
    let name: String
    let celsius: Double
}

// Adaptee: imagine this class comes from a third-party module.
final class LegacyFahrenheitSensor {
    let sensorId: String
    private let fahrenheit: Double

    init(sensorId: String, fahrenheit: Double) {
        self.sensorId = sensorId
        self.fahrenheit = fahrenheit
    }

    func readFahrenheit() -> Double { fahrenheit }
}

// The extension *is* the adapter.
extension LegacyFahrenheitSensor: TemperatureSource {
    var name: String { sensorId }
    var celsius: Double { (readFahrenheit() - 32.0) * 5.0 / 9.0 }
}

func report(_ sources: [TemperatureSource]) {
    for source in sources {
        print("\(source.name): \(String(format: "%.1f", source.celsius))°C")
    }
}

report([
    ModernSensor(name: "server-room", celsius: 21.5),
    LegacyFahrenheitSensor(sensorId: "warehouse-legacy", fahrenheit: 77.0),
])
