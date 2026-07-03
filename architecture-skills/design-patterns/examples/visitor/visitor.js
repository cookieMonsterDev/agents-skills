// Visitor pattern in JavaScript.
//
// Classic double dispatch via accept(); the visitor is just a plain
// object with one method per shape type. JS being dynamically typed,
// many codebases skip accept() and dispatch on a type tag directly —
// the visitor object form still keeps operations grouped and complete.

class Circle {
  constructor(radius) {
    this.radius = radius;
  }

  accept(visitor) {
    return visitor.visitCircle(this);
  }
}

class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  accept(visitor) {
    return visitor.visitRectangle(this);
  }
}

class Triangle {
  constructor(base, height) {
    this.base = base;
    this.height = height;
  }

  accept(visitor) {
    return visitor.visitTriangle(this);
  }
}

// Visitors are plain objects: one method per concrete shape.

const areaVisitor = {
  visitCircle: (c) => Math.PI * c.radius ** 2,
  visitRectangle: (r) => r.width * r.height,
  visitTriangle: (t) => 0.5 * t.base * t.height,
};

const svgExportVisitor = {
  visitCircle: (c) => `<circle r="${c.radius}" />`,
  visitRectangle: (r) => `<rect width="${r.width}" height="${r.height}" />`,
  visitTriangle: (t) => `<polygon points="0,${t.height} ${t.base},${t.height} 0,0" />`,
};

const shapes = [new Circle(2), new Rectangle(3, 4), new Triangle(6, 2)];

let total = 0;
for (const shape of shapes) {
  const area = shape.accept(areaVisitor);
  console.log(`area=${area.toFixed(2).padStart(6)}  ${shape.accept(svgExportVisitor)}`);
  total += area;
}
console.log(`total area: ${total.toFixed(2)}`);
