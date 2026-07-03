// Composite pattern in Swift.
//
// Files and directories conform to one Node protocol. The directory is
// a class because the tree is recursive, reference-shaped data; a
// closed set of node kinds could instead be an indirect enum.

protocol Node {
    var size: Int { get }
    func printTree(indent: Int)
}

struct File: Node {
    let name: String
    let size: Int

    func printTree(indent: Int) {
        print("\(String(repeating: " ", count: indent))\(name) (\(size) B)")
    }
}

final class Directory: Node {
    let name: String
    private var children: [Node] = []

    init(_ name: String) {
        self.name = name
    }

    @discardableResult
    func add(_ child: Node) -> Directory {
        children.append(child)
        return self
    }

    var size: Int {
        children.reduce(0) { $0 + $1.size }
    }

    func printTree(indent: Int) {
        print("\(String(repeating: " ", count: indent))\(name)/ (\(size) B)")
        for child in children {
            child.printTree(indent: indent + 2)
        }
    }
}

let project = Directory("project")
    .add(Directory("src")
        .add(File(name: "main.py", size: 1200))
        .add(File(name: "util.py", size: 450)))
    .add(Directory("docs").add(File(name: "readme.md", size: 800)))
    .add(File(name: ".gitignore", size: 20))

project.printTree(indent: 0)
