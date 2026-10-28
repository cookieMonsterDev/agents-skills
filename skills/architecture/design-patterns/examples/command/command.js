// Command pattern in JavaScript.
//
// Text editor with undo. JS has first-class functions, so a command is
// naturally a { execute, undo } pair of closures over the state they
// need — no class hierarchy required. A class form works too; the
// closure form shown here is the more idiomatic JS.

const editor = { text: "" }; // receiver

function insertText(text) {
  return {
    execute() {
      editor.text += text;
    },
    undo() {
      editor.text = editor.text.slice(0, -text.length);
    },
  };
}

function deleteLast(count) {
  let deleted = ""; // captured on execute so undo can restore it
  return {
    execute() {
      deleted = editor.text.slice(-count);
      editor.text = editor.text.slice(0, -count);
    },
    undo() {
      editor.text += deleted;
    },
  };
}

// Invoker: runs commands and tracks them for undo.
const history = {
  undoStack: [],
  execute(command) {
    command.execute();
    this.undoStack.push(command);
  },
  undo() {
    const command = this.undoStack.pop();
    if (command) command.undo();
  },
};

history.execute(insertText("Hello"));
history.execute(insertText(", world!"));
history.execute(deleteLast(1));
console.log(`after edits: "${editor.text}"`);

history.undo();
history.undo();
console.log(`after 2 undos: "${editor.text}"`);
