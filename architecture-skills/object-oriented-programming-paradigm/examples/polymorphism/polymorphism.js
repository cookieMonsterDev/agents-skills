// Polymorphism in JavaScript.
//
// JS has no interfaces: duck typing over prototype-chain lookup *is*
// the dispatch mechanism. Any object with area() and describe() fits
// the loop — two `class` shapes and one plain object literal all work
// at the same call site.

class Circle {
  constructor(radius) {
    this.radius = radius;
  }

  area() {
    return Math.PI * this.radius ** 2;
  }

  describe() {
    return `circle r=${this.radius}`;
  }
}

class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  area() {
    return this.width * this.height;
  }

  describe() {
    return `rectangle ${this.width}x${this.height}`;
  }
}

// No class at all: a plain object quacks like a shape, so it *is* one.
function makeTriangle(base, height) {
  return {
    area: () => 0.5 * base * height,
    describe: () => `triangle b=${base} h=${height}`,
  };
}

// "Parametric" in spirit: works for anything iterable whose elements
// have area() — the duck-typed counterpart of a generic function.
function totalArea(shapes) {
  return shapes.reduce((sum, s) => sum + s.area(), 0);
}

const shapes = [new Circle(1.0), new Rectangle(3.0, 4.0), makeTriangle(6.0, 2.0)];

// One call site, three implementations: each object's own method runs.
for (const shape of shapes) {
  console.log(`${shape.describe().padStart(18)}: area ${shape.area().toFixed(2)}`);
}

console.log(`${"total".padStart(18)}: area ${totalArea(shapes).toFixed(2)}`);
