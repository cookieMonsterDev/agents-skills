// Prototype pattern in Rust.
//
// #[derive(Clone)] is the pattern as a compiler-checked language feature:
// every field (including the Vec) is deep-copied. The registry shows the
// classic use — clone pre-configured exemplars instead of constructing.

use std::collections::HashMap;

#[derive(Clone, Debug)]
struct Circle {
    x: f64,
    y: f64,
    radius: f64,
    color: String,
    tags: Vec<String>,
}

impl Circle {
    fn describe(&self) -> String {
        format!(
            "Circle r={} {} at ({}, {}) tags={:?}",
            self.radius, self.color, self.x, self.y, self.tags
        )
    }
}

/// Catalog of pre-configured prototypes, cloned instead of constructed.
struct ShapeRegistry {
    prototypes: HashMap<String, Circle>,
}

impl ShapeRegistry {
    fn new() -> Self {
        Self {
            prototypes: HashMap::new(),
        }
    }

    fn register(&mut self, name: &str, prototype: Circle) {
        self.prototypes.insert(name.to_string(), prototype);
    }

    fn create(&self, name: &str) -> Circle {
        self.prototypes[name].clone()
    }
}

fn main() {
    let mut registry = ShapeRegistry::new();
    registry.register(
        "warning-marker",
        Circle {
            x: 0.0,
            y: 0.0,
            radius: 12.0,
            color: "red".to_string(),
            tags: vec!["alert".to_string()],
        },
    );

    let first = registry.create("warning-marker");
    let mut second = registry.create("warning-marker");
    second.x = 40.0;
    second.y = 25.0;
    second.tags.push("muted".to_string());

    println!("{}", first.describe());
    println!("{}", second.describe());
    // Ownership already guarantees the copies are independent: mutating
    // `second.tags` above could not have touched `first`.
}
