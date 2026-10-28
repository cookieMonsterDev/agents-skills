// Bridge pattern in Rust.
//
// The shape side holds a &dyn Renderer trait object so renderers are
// chosen at runtime. When the pairing is known at compile time, a
// generic parameter (Circle<R: Renderer>) gives the same split with
// static dispatch and no vtable.

trait Renderer {
    fn circle(&self, radius: f64) -> String;
    fn rectangle(&self, width: f64, height: f64) -> String;
}

struct VectorRenderer;

impl Renderer for VectorRenderer {
    fn circle(&self, radius: f64) -> String {
        format!("<circle r={radius:.1}/>")
    }
    fn rectangle(&self, width: f64, height: f64) -> String {
        format!("<rect w={width:.1} h={height:.1}/>")
    }
}

struct RasterRenderer;

impl Renderer for RasterRenderer {
    fn circle(&self, radius: f64) -> String {
        format!("pixels for a circle of radius {radius:.1}")
    }
    fn rectangle(&self, width: f64, height: f64) -> String {
        format!("pixels for a {width:.1}x{height:.1} rectangle")
    }
}

trait Shape {
    fn draw(&self) -> String;
}

struct Circle<'a> {
    renderer: &'a dyn Renderer,
    radius: f64,
}

impl Shape for Circle<'_> {
    fn draw(&self) -> String {
        self.renderer.circle(self.radius)
    }
}

struct Rectangle<'a> {
    renderer: &'a dyn Renderer,
    width: f64,
    height: f64,
}

impl Shape for Rectangle<'_> {
    fn draw(&self) -> String {
        self.renderer.rectangle(self.width, self.height)
    }
}

fn main() {
    let renderers: [&dyn Renderer; 2] = [&VectorRenderer, &RasterRenderer];
    for renderer in renderers {
        let circle = Circle { renderer, radius: 5.0 };
        let rectangle = Rectangle { renderer, width: 3.0, height: 4.0 };
        let shapes: [&dyn Shape; 2] = [&circle, &rectangle];
        for shape in shapes {
            println!("{}", shape.draw());
        }
    }
}
