// Memento pattern in Rust.
//
// Ownership makes the pattern natural: save() clones state into a value
// the history owns outright, and private fields make the snapshot opaque
// outside this module. For whole-state snapshots, deriving Clone on the
// originator and stacking full copies is often all you need.

struct Snapshot {
    text: String,
    cursor: usize,
}

struct TextEditor {
    text: String,
    cursor: usize,
}

impl TextEditor {
    fn new() -> Self {
        Self {
            text: String::new(),
            cursor: 0,
        }
    }

    fn type_text(&mut self, insert: &str) {
        self.text.insert_str(self.cursor, insert);
        self.cursor += insert.len();
    }

    fn save(&self) -> Snapshot {
        Snapshot {
            text: self.text.clone(),
            cursor: self.cursor,
        }
    }

    fn restore(&mut self, snapshot: Snapshot) {
        self.text = snapshot.text;
        self.cursor = snapshot.cursor;
    }

    fn describe(&self) -> String {
        format!("'{}' (cursor at {})", self.text, self.cursor)
    }
}

struct History {
    snapshots: Vec<Snapshot>,
}

impl History {
    fn new() -> Self {
        Self { snapshots: Vec::new() }
    }

    fn push(&mut self, snapshot: Snapshot) {
        self.snapshots.push(snapshot);
    }

    fn pop(&mut self) -> Option<Snapshot> {
        self.snapshots.pop()
    }
}

fn main() {
    let mut editor = TextEditor::new();
    let mut history = History::new();

    editor.type_text("Hello");
    history.push(editor.save());
    editor.type_text(", world");
    history.push(editor.save());
    editor.type_text("!!!");
    println!("current: {}", editor.describe());

    for _ in 0..2 {
        if let Some(snapshot) = history.pop() {
            editor.restore(snapshot);
            println!("undo:    {}", editor.describe());
        }
    }
}
