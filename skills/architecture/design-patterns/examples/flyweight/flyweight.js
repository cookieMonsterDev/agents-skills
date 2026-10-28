// Flyweight pattern in JavaScript.
//
// Engines already intern strings, so string-heavy data shares storage
// for free. The explicit form is a Map-backed factory handing out
// frozen shared objects; Object.freeze keeps the intrinsic state safe
// to share.

class TreeType {
  constructor(name, color) {
    this.name = name;
    this.color = color;
    Object.freeze(this); // shared state must be immutable
  }

  draw(x, y) {
    console.log(`${this.color} ${this.name} at (${x}, ${y})`);
  }
}

class TreeTypeFactory {
  #cache = new Map();

  get(name, color) {
    const key = `${name}/${color}`;
    if (!this.#cache.has(key)) {
      this.#cache.set(key, new TreeType(name, color));
    }
    return this.#cache.get(key);
  }

  get size() {
    return this.#cache.size;
  }
}

class Forest {
  #trees = [];
  #factory;

  constructor(factory) {
    this.#factory = factory;
  }

  plant(x, y, name, color) {
    this.#trees.push({ x, y, kind: this.#factory.get(name, color) });
  }

  draw() {
    for (const { x, y, kind } of this.#trees) {
      kind.draw(x, y);
    }
  }

  get size() {
    return this.#trees.length;
  }
}

const factory = new TreeTypeFactory();
const forest = new Forest(factory);
forest.plant(1, 1, "oak", "green");
forest.plant(2, 4, "pine", "dark green");
forest.plant(5, 2, "oak", "green");
forest.plant(6, 6, "birch", "light green");
forest.plant(8, 3, "pine", "dark green");
forest.plant(9, 9, "oak", "green");
forest.draw();

console.log(`trees planted: ${forest.size}, tree types in memory: ${factory.size}`);
