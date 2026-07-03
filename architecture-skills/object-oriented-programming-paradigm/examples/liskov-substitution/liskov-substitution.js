/** Liskov Substitution Principle in JavaScript.
 *
 * Square-extends-Rectangle is the classic violation. The fix keeps
 * Rectangle and Square as separate immutable types behind duck typing.
 */

// --- Violation ---

class Rectangle {
  constructor(width, height) {
    this._width = width;
    this._height = height;
  }

  setWidth(w) { this._width = w; }
  setHeight(h) { this._height = h; }
  area() { return this._width * this._height; }
}

class Square extends Rectangle {
  constructor(side) { super(side, side); }

  setWidth(w) { this._width = this._height = w; }
  setHeight(h) { this._width = this._height = h; }
}

function stretchTo4x5(rect) {
  rect.setWidth(4);
  rect.setHeight(5);
  return rect.area();
}

// --- Fix: separate immutable types ---

class Rect {
  constructor(width, height) {
    Object.freeze({ width, height });
    this.width = width;
    this.height = height;
  }

  area() { return this.width * this.height; }
}

class Sq {
  constructor(side) {
    this.side = side;
  }

  area() { return this.side * this.side; }
}

function totalArea(shapes) {
  return shapes.reduce((sum, s) => sum + s.area(), 0);
}

console.log('-- Violation: Square substituted for Rectangle --');
for (const rect of [new Rectangle(2, 3), new Square(2)]) {
  const got = stretchTo4x5(rect);
  const verdict = got === 20 ? 'ok' : 'CONTRACT BROKEN';
  console.log(`${rect.constructor.name.padStart(9)}: expected 20, got ${got}  (${verdict})`);
}

console.log('\n-- Fix: separate types behind Shape --');
const shapes = [new Rect(4, 5), new Sq(5)];
for (const shape of shapes) {
  console.log(`${shape.constructor.name.padStart(9)}: area ${shape.area()}`);
}
console.log(`    total: ${totalArea(shapes)}`);
