// Memento pattern in Swift.
//
// A struct snapshot gets value semantics for free: handing it to the
// history is already an independent copy. Making it Codable (as here)
// also lets snapshots be persisted — the same shape NSUserActivity and
// state-restoration APIs use.

import Foundation

struct Snapshot: Codable { // memento
    fileprivate let text: String
    fileprivate let cursor: Int
}

final class TextEditor { // originator
    private var text = ""
    private var cursor = 0

    func type(_ insert: String) {
        let index = text.index(text.startIndex, offsetBy: cursor)
        text.insert(contentsOf: insert, at: index)
        cursor += insert.count
    }

    func save() -> Snapshot {
        Snapshot(text: text, cursor: cursor)
    }

    func restore(_ snapshot: Snapshot) {
        text = snapshot.text
        cursor = snapshot.cursor
    }

    var description: String {
        "'\(text)' (cursor at \(cursor))"
    }
}

final class History { // caretaker
    private var snapshots: [Snapshot] = []

    func push(_ snapshot: Snapshot) {
        snapshots.append(snapshot)
    }

    func pop() -> Snapshot? {
        snapshots.popLast()
    }
}

let editor = TextEditor()
let history = History()

editor.type("Hello")
history.push(editor.save())
editor.type(", world")
history.push(editor.save())
editor.type("!!!")
print("current: \(editor.description)")

for _ in 0..<2 {
    if let snapshot = history.pop() {
        editor.restore(snapshot)
        print("undo:    \(editor.description)")
    }
}
