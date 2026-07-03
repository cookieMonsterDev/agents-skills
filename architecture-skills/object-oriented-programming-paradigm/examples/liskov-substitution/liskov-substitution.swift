// Liskov Substitution Principle in Swift.
//
// Square-extends-Rectangle is the classic violation. The fix keeps
// Rectangle and Square as separate immutable types behind a Shape protocol.

import Foundation

// --- Violation ---

class Rectangle {
    var width: Double
    var height: Double

    init(width: Double, height: Double) {
        self.width = width
        self.height = height
    }

    func setWidth(_ w: Double) { width = w }
    func setHeight(_ h: Double) { height = h }
    func area() -> Double { width * height }
}

final class Square: Rectangle {
    init(side: Double) { super.init(width: side, height: side) }

    override func setWidth(_ w: Double) { width = height = w }
    override func setHeight(_ h: Double) { width = height = h }
}

func stretchTo4x5(_ rect: Rectangle) -> Double {
    rect.setWidth(4)
    rect.setHeight(5)
    return rect.area()
}

// --- Fix ---

protocol Shape {
    func area() -> Double
}

struct Rect: Shape {
    let width: Double
    let height: Double
    func area() -> Double { width * height }
}

struct Sq: Shape {
    let side: Double
    func area() -> Double { side * side }
}

func totalArea(_ shapes: [Shape]) -> Double {
    shapes.reduce(0) { $0 + $1.area() }
}

print("-- Violation: Square substituted for Rectangle --")
for rect: Rectangle in [Rectangle(width: 2, height: 3), Square(side: 2)] {
    let got = stretchTo4x5(rect)
    let verdict = got == 20 ? "ok" : "CONTRACT BROKEN"
    print(String(format: "%9@: expected 20, got %g  (%@)", String(describing: type(of: rect)), got, verdict))
}

print("\n-- Fix: separate types behind Shape --")
let shapes: [Shape] = [Rect(width: 4, height: 5), Sq(side: 5)]
for shape in shapes {
    print(String(format: "%9@: area %g", String(describing: type(of: shape)), shape.area()))
}
print(String(format: "    total: %g", totalArea(shapes)))
