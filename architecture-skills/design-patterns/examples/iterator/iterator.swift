// Iterator pattern in Swift.
//
// A binary search tree traversed in sorted order. Swift builds the
// pattern in as Sequence/IteratorProtocol: conforming to them plugs a
// custom collection into for-in, map, filter, and reduce. Swift has no
// generators, so the iterator replaces the recursive walk with an
// explicit stack.

final class Node {
    let value: Int
    var left: Node?
    var right: Node?

    init(_ value: Int) {
        self.value = value
    }
}

struct SortedTree {
    private var root: Node?

    mutating func add(_ value: Int) {
        guard let root else {
            self.root = Node(value)
            return
        }
        var node = root
        while true {
            if value < node.value {
                if let left = node.left { node = left } else { node.left = Node(value); return }
            } else {
                if let right = node.right { node = right } else { node.right = Node(value); return }
            }
        }
    }

    struct InOrderIterator: IteratorProtocol {
        // Stack of nodes whose left subtrees are already done.
        private var stack: [Node] = []

        init(root: Node?) {
            pushLeftSpine(root)
        }

        private mutating func pushLeftSpine(_ start: Node?) {
            var node = start
            while let n = node {
                stack.append(n)
                node = n.left
            }
        }

        mutating func next() -> Int? {
            guard let node = stack.popLast() else { return nil }
            pushLeftSpine(node.right)
            return node.value
        }
    }
}

extension SortedTree: Sequence {
    func makeIterator() -> InOrderIterator {
        InOrderIterator(root: root)
    }
}

var tree = SortedTree()
for value in [5, 3, 8, 1, 4, 9, 7] {
    tree.add(value)
}

print("in order:", Array(tree))
print("sum:", tree.reduce(0, +))
print("evens:", tree.filter { $0 % 2 == 0 })
