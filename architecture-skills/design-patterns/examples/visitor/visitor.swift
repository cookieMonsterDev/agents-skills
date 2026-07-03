// Visitor pattern in Swift.
//
// Classic double dispatch via accept(). Idiomatic Swift often models a
// closed shape set as an enum and switches over it — exhaustive at
// compile time with no accept() plumbing (shown at the bottom). The
// protocol form keeps the hierarchy open for new conforming types.

import Foundation

protocol ShapeVisitor {
    associatedtype Result
    func visit(_ circle: Circle) -> Result
    func visit(_ rectangle: Rectangle) -> Result
    func visit(_ triangle: Triangle) -> Result
}

protocol Shape {
    func accept<V: ShapeVisitor>(_ visitor: V) -> V.Result
}

struct Circle: Shape {
    let radius: Double

    func accept<V: ShapeVisitor>(_ visitor: V) -> V.Result {
        visitor.visit(self)
    }
}

struct Rectangle: Shape {
    let width: Double
    let height: Double

    func accept<V: ShapeVisitor>(_ visitor: V) -> V.Result {
        visitor.visit(self)
    }
}

struct Triangle: Shape {
    let base: Double
    let height: Double

    func accept<V: ShapeVisitor>(_ visitor: V) -> V.Result {
        visitor.visit(self)
    }
}

struct AreaVisitor: ShapeVisitor {
    func visit(_ c: Circle) -> Double { .pi * c.radius * c.radius }
    func visit(_ r: Rectangle) -> Double { r.width * r.height }
    func visit(_ t: Triangle) -> Double { 0.5 * t.base * t.height }
}

struct SvgExportVisitor: ShapeVisitor {
    func visit(_ c: Circle) -> String { "<circle r=\"\(c.radius)\" />" }
    func visit(_ r: Rectangle) -> String { "<rect width=\"\(r.width)\" height=\"\(r.height)\" />" }
    func visit(_ t: Triangle) -> String {
        "<polygon points=\"0,\(t.height) \(t.base),\(t.height) 0,0\" />"
    }
}

let shapes: [Shape] = [Circle(radius: 2), Rectangle(width: 3, height: 4), Triangle(base: 6, height: 2)]
let area = AreaVisitor()
let svg = SvgExportVisitor()

var total = 0.0
for shape in shapes {
    let a = shape.accept(area)
    print(String(format: "area=%6.2f  %@", a, shape.accept(svg)))
    total += a
}
print(String(format: "total area: %.2f", total))

// The enum + switch alternative most Swift code reaches for first.
enum ShapeCase {
    case circle(radius: Double)
    case rectangle(width: Double, height: Double)
}

func areaOf(_ shape: ShapeCase) -> Double {
    switch shape {
    case .circle(let radius): return .pi * radius * radius
    case .rectangle(let width, let height): return width * height
    }
}

print(String(format: "enum+switch circle area: %.2f", areaOf(.circle(radius: 1))))
