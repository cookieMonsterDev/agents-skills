// Iterator pattern in JavaScript.
//
// A binary search tree traversed in sorted order. JS builds the pattern
// in via the iteration protocol: implementing [Symbol.iterator] — most
// easily with a generator function* — plugs a custom collection into
// for...of, spread, and destructuring. No GoF iterator class needed.

class SortedTree {
  #root = null;

  add(value) {
    const node = { value, left: null, right: null };
    if (this.#root === null) {
      this.#root = node;
      return;
    }
    let current = this.#root;
    for (;;) {
      const side = value < current.value ? "left" : "right";
      if (current[side] === null) {
        current[side] = node;
        return;
      }
      current = current[side];
    }
  }

  // Each call produces a fresh, independent iterator.
  *[Symbol.iterator]() {
    yield* this.#walk(this.#root);
  }

  *#walk(node) {
    if (node !== null) {
      yield* this.#walk(node.left);
      yield node.value;
      yield* this.#walk(node.right);
    }
  }
}

const tree = new SortedTree();
for (const value of [5, 3, 8, 1, 4, 9, 7]) {
  tree.add(value);
}

console.log("in order:", [...tree]);
console.log("sum:", [...tree].reduce((a, b) => a + b, 0));

const [smallest, secondSmallest] = tree;
console.log("two smallest:", smallest, secondSmallest);
