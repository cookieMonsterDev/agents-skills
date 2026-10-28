// Abstraction in JavaScript (Node).
//
// Duck typing means the abstraction is a shape, not a keyword: any
// object with save/load fits. The contract lives in documentation (or
// a TypeScript interface); private fields (#) keep each implementation's
// operational detail — a Map vs a file — out of the callers' reach.

const fs = require("node:fs");

/**
 * The abstraction (by convention): { save(key, text), load(key) -> string|null }
 */

// Operational detail: a Map. Callers never see it.
class MemoryStore {
  #notes = new Map();

  save(key, text) {
    this.#notes.set(key, text);
  }

  load(key) {
    return this.#notes.get(key) ?? null;
  }
}

// Operational detail: append-only lines in a file, last write wins.
class FileStore {
  #path;

  constructor(path) {
    this.#path = path;
  }

  save(key, text) {
    fs.appendFileSync(this.#path, `${key}\t${text}\n`);
  }

  load(key) {
    if (!fs.existsSync(this.#path)) return null;
    let found = null;
    for (const line of fs.readFileSync(this.#path, "utf8").split("\n")) {
      const tab = line.indexOf("\t");
      if (tab !== -1 && line.slice(0, tab) === key) {
        found = line.slice(tab + 1); // keep scanning: last write wins
      }
    }
    return found;
  }
}

// Client: written once against the abstraction, never edited when the
// implementation behind it swaps.
function runSession(store) {
  store.save("groceries", "eggs, flour");
  store.save("groceries", "eggs, flour, milk"); // overwrite
  store.save("idea", "hide the how, expose the what");
  console.log("  groceries:", store.load("groceries"));
  console.log("  idea:     ", store.load("idea"));
  console.log("  missing:  ", store.load("missing"));
}

console.log("memory-backed store:");
runSession(new MemoryStore());

const path = "abstraction_demo.txt";
console.log("file-backed store:");
runSession(new FileStore(path));
fs.rmSync(path, { force: true });
