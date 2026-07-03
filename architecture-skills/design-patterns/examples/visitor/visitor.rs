// Visitor pattern in Rust.
//
// Idiomatic Rust usually replaces Visitor with an enum + match: the
// compiler enforces exhaustiveness and no accept() plumbing is needed
// (see area_by_match below). The trait-based double-dispatch form is
// worth it when the shape set must stay open to downstream crates.

use std::f64::consts::PI;

struct Circle {
    radius: f64,
}

struct Rectangle {
    width: f64,
    height: f64,
}

struct Triangle {
    base: f64,
    height: f64,
}

trait ShapeVisitor {
    fn visit_circle(&mut self, circle: &Circle);
    fn visit_rectangle(&mut self, rectangle: &Rectangle);
    fn visit_triangle(&mut self, triangle: &Triangle);
}

trait Shape {
    fn accept(&self, visitor: &mut dyn ShapeVisitor);
}

impl Shape for Circle {
    fn accept(&self, visitor: &mut dyn ShapeVisitor) {
        visitor.visit_circle(self);
    }
}

impl Shape for Rectangle {
    fn accept(&self, visitor: &mut dyn ShapeVisitor) {
        visitor.visit_rectangle(self);
    }
}

impl Shape for Triangle {
    fn accept(&self, visitor: &mut dyn ShapeVisitor) {
        visitor.visit_triangle(self);
    }
}

#[derive(Default)]
struct AreaVisitor {
    area: f64,
}

impl ShapeVisitor for AreaVisitor {
    fn visit_circle(&mut self, c: &Circle) {
        self.area = PI * c.radius * c.radius;
    }
    fn visit_rectangle(&mut self, r: &Rectangle) {
        self.area = r.width * r.height;
    }
    fn visit_triangle(&mut self, t: &Triangle) {
        self.area = 0.5 * t.base * t.height;
    }
}

#[derive(Default)]
struct SvgExportVisitor {
    markup: String,
}

impl ShapeVisitor for SvgExportVisitor {
    fn visit_circle(&mut self, c: &Circle) {
        self.markup = format!("<circle r=\"{}\" />", c.radius);
    }
    fn visit_rectangle(&mut self, r: &Rectangle) {
        self.markup = format!("<rect width=\"{}\" height=\"{}\" />", r.width, r.height);
    }
    fn visit_triangle(&mut self, t: &Triangle) {
        self.markup = format!("<polygon points=\"0,{h} {b},{h} 0,0\" />", h = t.height, b = t.base);
    }
}

// The enum + match alternative most Rust code reaches for first.
enum ShapeEnum {
    Circle { radius: f64 },
}

fn area_by_match(shape: &ShapeEnum) -> f64 {
    match shape {
        ShapeEnum::Circle { radius } => PI * radius * radius,
    }
}

fn main() {
    let shapes: Vec<Box<dyn Shape>> = vec![
        Box::new(Circle { radius: 2.0 }),
        Box::new(Rectangle { width: 3.0, height: 4.0 }),
        Box::new(Triangle { base: 6.0, height: 2.0 }),
    ];

    let mut area = AreaVisitor::default();
    let mut svg = SvgExportVisitor::default();
    let mut total = 0.0;

    for shape in &shapes {
        shape.accept(&mut area);
        shape.accept(&mut svg);
        println!("area={:6.2}  {}", area.area, svg.markup);
        total += area.area;
    }
    println!("total area: {total:.2}");

    let unit = ShapeEnum::Circle { radius: 1.0 };
    println!("enum+match circle area: {:.2}", area_by_match(&unit));
}
