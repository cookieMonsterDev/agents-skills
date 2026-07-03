// Polymorphism in Swift.
//
// One loop calls area()/describe() on a mixed list and each object
// answers with its own implementation. Protocols + structs are the
// idiomatic form; Square conforms to Shape explicitly.

import Foundation

protocol Shape {
    func area() -> Double
    func describe() -> String
}

struct Circle: Shape {
    let radius: Double

    func area() -> Double { Double.pi * radius * radius }
    func describe() -> String { "circle r=\(radius)" }
}

struct Rectangle: Shape {
    let width: Double
    let height: Double

    func area() -> Double { width * height }
    func describe() -> String { "rectangle \(width)x\(height)" }
}

struct Square: Shape {
    let side: Double

    func area() -> Double { side * side }
    func describe() -> String { "square \(side)x\(side)" }
}

func totalArea(_ shapes: [Shape]) -> Double {
    shapes.reduce(0) { $0 + $1.area() }
}

let shapes: [Shape] = [Circle(radius: 1.0), Rectangle(width: 3, height: 4), Square(side: 2.0)]

for shape in shapes {
    print(String(format: "%18@: area %.2f", shape.describe(), shape.area()))
}
print(String(format: "%18@: area %.2f", "total", totalArea(shapes)))
