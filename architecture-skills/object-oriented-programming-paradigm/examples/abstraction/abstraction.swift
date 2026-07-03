// Abstraction in Swift.
//
// Callers see the essential model of a note store — save and load —
// while each implementation hides its operational detail (a dictionary
// vs a file on disk). A protocol names the contract explicitly.

import Foundation

protocol NoteStore {
    func save(key: String, text: String)
    func load(key: String) -> String?
}

final class MemoryStore: NoteStore {
    private var notes: [String: String] = [:]

    func save(key: String, text: String) { notes[key] = text }

    func load(key: String) -> String? { notes[key] }
}

final class FileStore: NoteStore {
    private let path: String

    init(path: String) { self.path = path }

    func save(key: String, text: String) {
        let line = "\(key)\t\(text)\n"
        if FileManager.default.fileExists(atPath: path) {
            if let handle = FileHandle(forWritingAtPath: path) {
                handle.seekToEndOfFile()
                handle.write(line.data(using: .utf8)!)
                handle.closeFile()
            }
        } else {
            try? line.write(toFile: path, atomically: true, encoding: .utf8)
        }
    }

    func load(key: String) -> String? {
        guard let content = try? String(contentsOfFile: path, encoding: .utf8) else {
            return nil
        }
        var found: String?
        for line in content.split(separator: "\n") {
            let parts = line.split(separator: "\t", maxSplits: 1)
            if parts.count == 2, parts[0] == Substring(key) {
                found = String(parts[1])
            }
        }
        return found
    }
}

func runSession(store: NoteStore) {
    store.save(key: "groceries", text: "eggs, flour")
    store.save(key: "groceries", text: "eggs, flour, milk")
    store.save(key: "idea", text: "hide the how, expose the what")
    print("  groceries:", store.load(key: "groceries") ?? "")
    print("  idea:     ", store.load(key: "idea") ?? "")
    print("  missing:  ", store.load(key: "missing") as Any)
}

print("memory-backed store:")
runSession(store: MemoryStore())

let path = "abstraction_demo.txt"
defer { try? FileManager.default.removeItem(atPath: path) }
print("file-backed store:")
runSession(store: FileStore(path: path))
