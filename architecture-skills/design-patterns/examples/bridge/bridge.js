// Bridge pattern in JavaScript.
//
// Shapes hold a renderer object and delegate to it. With duck typing
// the "implementation interface" is just a convention: any object with
// circle() and rectangle() methods works as a renderer.

class VectorRenderer {
  circle(radius) {
    return `<circle r=${radius.toFixed(1)}/>`;
  }
  rectangle(width, height) {
    return `<rect w=${width.toFixed(1)} h=${height.toFixed(1)}/>`;
  }
}

class RasterRenderer {
  circle(radius) {
    return `pixels for a circle of radius ${radius.toFixed(1)}`;
  }
  rectangle(width, height) {
    return `pixels for a ${width.toFixed(1)}x${height.toFixed(1)} rectangle`;
  }
}

class Shape {
  constructor(renderer) {
    this.renderer = renderer;
  }
}

class Circle extends Shape {
  constructor(renderer, radius) {
    super(renderer);
    this.radius = radius;
  }
  draw() {
    return this.renderer.circle(this.radius);
  }
}

class Rectangle extends Shape {
  constructor(renderer, width, height) {
    super(renderer);
    this.width = width;
    this.height = height;
  }
  draw() {
    return this.renderer.rectangle(this.width, this.height);
  }
}

for (const renderer of [new VectorRenderer(), new RasterRenderer()]) {
  for (const shape of [new Circle(renderer, 5.0), new Rectangle(renderer, 3.0, 4.0)]) {
    console.log(shape.draw());
  }
}
