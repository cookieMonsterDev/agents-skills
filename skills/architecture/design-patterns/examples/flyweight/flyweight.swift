// Flyweight pattern in Swift.
//
// The flyweight must be a class: reference semantics let many trees
// share one instance, where a struct would be copied on every
// assignment and defeat the pattern. The stored properties are `let`,
// so the shared state is immutable.

/// Flyweight: immutable intrinsic state shared by many trees.
final class TreeType {
    let name: String
    let color: String

    init(name: String, color: String) {
        self.name = name
        self.color = color
    }

    func draw(x: Int, y: Int) {
        print("\(color) \(name) at (\(x), \(y))")
    }
}

final class TreeTypeFactory {
    private var cache: [String: TreeType] = [:]

    func get(name: String, color: String) -> TreeType {
        let key = "\(name)/\(color)"
        if let existing = cache[key] {
            return existing
        }
        let type = TreeType(name: name, color: color)
        cache[key] = type
        return type
    }

    var count: Int { cache.count }
}

/// Context: extrinsic state plus a reference to the shared flyweight.
struct Tree {
    let x: Int
    let y: Int
    let kind: TreeType
}

let factory = TreeTypeFactory()
let forest: [Tree] = [
    Tree(x: 1, y: 1, kind: factory.get(name: "oak", color: "green")),
    Tree(x: 2, y: 4, kind: factory.get(name: "pine", color: "dark green")),
    Tree(x: 5, y: 2, kind: factory.get(name: "oak", color: "green")),
    Tree(x: 6, y: 6, kind: factory.get(name: "birch", color: "light green")),
    Tree(x: 8, y: 3, kind: factory.get(name: "pine", color: "dark green")),
    Tree(x: 9, y: 9, kind: factory.get(name: "oak", color: "green")),
]

for tree in forest {
    tree.kind.draw(x: tree.x, y: tree.y)
}

print("trees planted: \(forest.count), tree types in memory: \(factory.count)")
