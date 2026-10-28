// Command pattern in Swift.
//
// Text editor with undo: a protocol with execute/undo, concrete commands
// capturing their own undo state, and a history array as the invoker.
// Foundation's UndoManager is the platform's built-in invoker; closures
// cover one-shot commands that need no undo.

final class Editor { // receiver
    var text = ""
}

protocol Command {
    func execute()
    func undo()
}

final class InsertText: Command {
    private let editor: Editor
    private let text: String

    init(editor: Editor, text: String) {
        self.editor = editor
        self.text = text
    }

    func execute() {
        editor.text += text
    }

    func undo() {
        editor.text.removeLast(text.count)
    }
}

final class DeleteLast: Command {
    private let editor: Editor
    private let count: Int
    private var deleted = "" // captured on execute so undo can restore it

    init(editor: Editor, count: Int) {
        self.editor = editor
        self.count = count
    }

    func execute() {
        deleted = String(editor.text.suffix(count))
        editor.text.removeLast(count)
    }

    func undo() {
        editor.text += deleted
    }
}

final class History { // invoker
    private var undoStack: [Command] = []

    func execute(_ command: Command) {
        command.execute()
        undoStack.append(command)
    }

    func undo() {
        undoStack.popLast()?.undo()
    }
}

let editor = Editor()
let history = History()

history.execute(InsertText(editor: editor, text: "Hello"))
history.execute(InsertText(editor: editor, text: ", world!"))
history.execute(DeleteLast(editor: editor, count: 1))
print("after edits: \"\(editor.text)\"")

history.undo()
history.undo()
print("after 2 undos: \"\(editor.text)\"")
