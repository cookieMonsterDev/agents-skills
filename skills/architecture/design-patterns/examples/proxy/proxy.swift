// Proxy pattern in Swift (virtual proxy: lazy-loading image).
//
// A protocol is the subject interface; the proxy is a class holding an
// optional real subject created on first use. A stored `lazy var`
// covers the simpler case where property access alone should trigger
// creation.

protocol Image {
    func display()
}

/// Real subject: expensive to create.
final class RealImage: Image {
    private let filename: String

    init(filename: String) {
        self.filename = filename
        print("Loading \(filename) from disk (expensive)")
    }

    func display() {
        print("Displaying \(filename)")
    }
}

/// Virtual proxy: defers creating RealImage until first use.
final class ImageProxy: Image {
    private let filename: String
    private var real: RealImage?

    init(filename: String) {
        self.filename = filename
    }

    func display() {
        if real == nil {
            real = RealImage(filename: filename)
        }
        real?.display()
    }
}

let gallery: [Image] = [
    ImageProxy(filename: "holiday.png"),
    ImageProxy(filename: "unused.png"),
]
print("Proxies created; nothing loaded yet")

gallery[0].display()
gallery[0].display() // loaded once, displayed twice

print("unused.png was never loaded")
