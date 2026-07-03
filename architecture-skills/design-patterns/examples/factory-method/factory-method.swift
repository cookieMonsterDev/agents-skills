// Factory Method pattern in Swift.
//
// The creator is a protocol whose extension holds the shared workflow;
// conforming types supply only the factory method. This is the idiomatic
// Swift replacement for an abstract base class.

import Foundation

protocol Transport {
    func deliver(_ cargo: String) -> String
}

struct Truck: Transport {
    func deliver(_ cargo: String) -> String {
        "Truck delivers \(cargo) by road in a box"
    }
}

struct Ship: Transport {
    func deliver(_ cargo: String) -> String {
        "Ship delivers \(cargo) by sea in a container"
    }
}

/// Creator: conforming types supply only the factory method.
protocol Logistics {
    var name: String { get }
    func createTransport() -> Transport
}

extension Logistics {
    /// Shared workflow, written once for every creator.
    func planDelivery(of cargo: String) -> String {
        let transport = createTransport()
        return "[\(name)] \(transport.deliver(cargo))"
    }
}

struct RoadLogistics: Logistics {
    let name = "RoadLogistics"
    func createTransport() -> Transport { Truck() }
}

struct SeaLogistics: Logistics {
    let name = "SeaLogistics"
    func createTransport() -> Transport { Ship() }
}

let all: [Logistics] = [RoadLogistics(), SeaLogistics()]
for logistics in all {
    print(logistics.planDelivery(of: "machine parts"))
}
