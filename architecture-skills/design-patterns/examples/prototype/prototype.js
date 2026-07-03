// Prototype pattern in JavaScript.
//
// Note: structuredClone() deep-copies plain data, but drops methods and
// prototype chains, so class instances still want an explicit clone().
// (JavaScript's prototypal inheritance is a different mechanism despite
// the shared name.)

class Circle {
  constructor({ x, y, radius, color, tags }) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
    this.tags = tags;
  }

  clone() {
    // spread copies scalars; the tags array is duplicated so the copy
    // doesn't alias the prototype's list
    return new Circle({ ...this, tags: [...this.tags] });
  }

  describe() {
    return `Circle r=${this.radius} ${this.color} at (${this.x}, ${this.y}) tags=[${this.tags}]`;
  }
}

// Catalog of pre-configured prototypes, cloned instead of constructed.
class ShapeRegistry {
  #prototypes = new Map();

  register(name, prototypeShape) {
    this.#prototypes.set(name, prototypeShape);
  }

  create(name) {
    return this.#prototypes.get(name).clone();
  }
}

const registry = new ShapeRegistry();
registry.register(
  "warning-marker",
  new Circle({ x: 0, y: 0, radius: 12, color: "red", tags: ["alert"] }),
);

const first = registry.create("warning-marker");
const second = registry.create("warning-marker");
second.x = 40;
second.y = 25;
second.tags.push("muted");

console.log(first.describe());
console.log(second.describe());
console.log("independent copies:", first.tags !== second.tags);
