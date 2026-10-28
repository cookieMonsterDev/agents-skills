// Command pattern in Rust.
//
// Text editor with undo: a Command trait with execute/undo, boxed
// commands in a history vector. Commands borrow nothing — they receive
// the editor at call time — which keeps the borrow checker happy. For
// one-shot commands without undo, Box<dyn FnOnce(&mut Editor)> suffices.

struct Editor {
    text: String, // receiver
}

trait Command {
    fn execute(&mut self, editor: &mut Editor);
    fn undo(&mut self, editor: &mut Editor);
}

struct InsertText {
    text: String,
}

impl Command for InsertText {
    fn execute(&mut self, editor: &mut Editor) {
        editor.text.push_str(&self.text);
    }

    fn undo(&mut self, editor: &mut Editor) {
        let new_len = editor.text.len() - self.text.len();
        editor.text.truncate(new_len);
    }
}

struct DeleteLast {
    count: usize,
    deleted: String, // captured on execute so undo can restore it
}

impl Command for DeleteLast {
    fn execute(&mut self, editor: &mut Editor) {
        let split = editor.text.len() - self.count;
        self.deleted = editor.text.split_off(split);
    }

    fn undo(&mut self, editor: &mut Editor) {
        editor.text.push_str(&self.deleted);
    }
}

struct History {
    undo_stack: Vec<Box<dyn Command>>,
}

impl History {
    fn execute(&mut self, mut command: Box<dyn Command>, editor: &mut Editor) {
        command.execute(editor);
        self.undo_stack.push(command);
    }

    fn undo(&mut self, editor: &mut Editor) {
        if let Some(mut command) = self.undo_stack.pop() {
            command.undo(editor);
        }
    }
}

fn main() {
    let mut editor = Editor { text: String::new() };
    let mut history = History { undo_stack: Vec::new() };

    history.execute(Box::new(InsertText { text: "Hello".into() }), &mut editor);
    history.execute(Box::new(InsertText { text: ", world!".into() }), &mut editor);
    history.execute(Box::new(DeleteLast { count: 1, deleted: String::new() }), &mut editor);
    println!("after edits: {:?}", editor.text);

    history.undo(&mut editor);
    history.undo(&mut editor);
    println!("after 2 undos: {:?}", editor.text);
}
