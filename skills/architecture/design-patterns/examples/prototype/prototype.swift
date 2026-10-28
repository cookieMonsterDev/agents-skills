// Prototype pattern in Swift.
//
// Value types (structs) copy on assignment, so for them the pattern is a
// language feature — shown first. Reference types (classes) need an
// explicit clone() that copies mutable state, shown second.

import Foundation

// --- Variant 1: struct — copying is built in ---

struct Circle {
    var x: Double
    var y: Double
    let radius: Double
    let color: String
    var tags: [String]

    func describe() -> String {
        "Circle r=\(Int(radius)) \(color) at (\(Int(x)), \(Int(y))) tags=\(tags)"
    }
}

// --- Variant 2: class — clone() must be explicit ---

final class CircleRef {
    var x: Double
    var y: Double
    let radius: Double
    let color: String
    var tags: [String]

    init(x: Double, y: Double, radius: Double, color: String, tags: [String]) {
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.tags = tags
    }

    func clone() -> CircleRef {
        // Array is a value type, so assigning it here already copies it.
        CircleRef(x: x, y: y, radius: radius, color: color, tags: tags)
    }

    func describe() -> String {
        "CircleRef r=\(Int(radius)) \(color) at (\(Int(x)), \(Int(y))) tags=\(tags)"
    }
}

let prototypeMarker = Circle(x: 0, y: 0, radius: 12, color: "red", tags: ["alert"])
var movedMarker = prototypeMarker // struct assignment IS the clone
movedMarker.x = 40
movedMarker.y = 25
movedMarker.tags.append("muted")

print(prototypeMarker.describe())
print(movedMarker.describe())

let refPrototype = CircleRef(x: 0, y: 0, radius: 12, color: "red", tags: ["alert"])
let refCopy = refPrototype.clone()
refCopy.x = 40
refCopy.tags.append("muted")

print(refPrototype.describe())
print(refCopy.describe())
