// Bridge pattern in Swift.
//
// Shapes hold a renderer as a protocol-typed property, keeping the two
// hierarchies independent. Value-type shapes with a protocol "handle"
// to the implementation are the natural Swift form of this pattern.

import Foundation

protocol Renderer {
    func circle(radius: Double) -> String
    func rectangle(width: Double, height: Double) -> String
}

struct VectorRenderer: Renderer {
    func circle(radius: Double) -> String {
        "<circle r=\(String(format: "%.1f", radius))/>"
    }
    func rectangle(width: Double, height: Double) -> String {
        "<rect w=\(String(format: "%.1f", width)) h=\(String(format: "%.1f", height))/>"
    }
}

struct RasterRenderer: Renderer {
    func circle(radius: Double) -> String {
        "pixels for a circle of radius \(String(format: "%.1f", radius))"
    }
    func rectangle(width: Double, height: Double) -> String {
        "pixels for a \(String(format: "%.1f", width))x\(String(format: "%.1f", height)) rectangle"
    }
}

protocol Shape {
    func draw() -> String
}

struct Circle: Shape {
    let renderer: Renderer
    let radius: Double

    func draw() -> String { renderer.circle(radius: radius) }
}

struct Rectangle: Shape {
    let renderer: Renderer
    let width: Double
    let height: Double

    func draw() -> String { renderer.rectangle(width: width, height: height) }
}

let renderers: [Renderer] = [VectorRenderer(), RasterRenderer()]
for renderer in renderers {
    let shapes: [Shape] = [
        Circle(renderer: renderer, radius: 5.0),
        Rectangle(renderer: renderer, width: 3.0, height: 4.0),
    ]
    for shape in shapes {
        print(shape.draw())
    }
}
