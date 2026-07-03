// Memento pattern in JavaScript.
//
// A frozen plain object is the snapshot; JS has no way to hide its
// fields from the caretaker, so opacity is by convention. For simple
// cases, structuredClone() of the whole state object does the same job.

class TextEditor {
  #text = "";
  #cursor = 0;

  type(insert) {
    this.#text =
      this.#text.slice(0, this.#cursor) + insert + this.#text.slice(this.#cursor);
    this.#cursor += insert.length;
  }

  save() {
    return Object.freeze({ text: this.#text, cursor: this.#cursor });
  }

  restore(snapshot) {
    this.#text = snapshot.text;
    this.#cursor = snapshot.cursor;
  }

  toString() {
    return `'${this.#text}' (cursor at ${this.#cursor})`;
  }
}

class History {
  #snapshots = [];

  push(snapshot) {
    this.#snapshots.push(snapshot);
  }

  pop() {
    return this.#snapshots.pop() ?? null;
  }
}

const editor = new TextEditor();
const history = new History();

editor.type("Hello");
history.push(editor.save());
editor.type(", world");
history.push(editor.save());
editor.type("!!!");
console.log(`current: ${editor}`);

for (let i = 0; i < 2; i++) {
  const snapshot = history.pop();
  if (snapshot) {
    editor.restore(snapshot);
    console.log(`undo:    ${editor}`);
  }
}
