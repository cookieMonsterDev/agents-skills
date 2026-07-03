// Flyweight pattern in Rust.
//
// Rc makes the sharing explicit: cloning an Rc<TreeType> copies a
// pointer, not the data, and the type system guarantees the shared
// state cannot be mutated behind other owners' backs. Use Arc instead
// of Rc when contexts cross threads.

use std::collections::HashMap;
use std::rc::Rc;

/// Flyweight: immutable intrinsic state shared by many trees.
struct TreeType {
    name: String,
    color: String,
}

impl TreeType {
    fn draw(&self, x: i32, y: i32) {
        println!("{} {} at ({}, {})", self.color, self.name, x, y);
    }
}

#[derive(Default)]
struct TreeTypeFactory {
    cache: HashMap<String, Rc<TreeType>>,
}

impl TreeTypeFactory {
    fn get(&mut self, name: &str, color: &str) -> Rc<TreeType> {
        let key = format!("{name}/{color}");
        Rc::clone(self.cache.entry(key).or_insert_with(|| {
            Rc::new(TreeType {
                name: name.to_string(),
                color: color.to_string(),
            })
        }))
    }

    fn len(&self) -> usize {
        self.cache.len()
    }
}

/// Context: extrinsic state plus a cheap handle to the shared flyweight.
struct Tree {
    x: i32,
    y: i32,
    kind: Rc<TreeType>,
}

fn main() {
    let mut factory = TreeTypeFactory::default();
    let plan = [
        (1, 1, "oak", "green"),
        (2, 4, "pine", "dark green"),
        (5, 2, "oak", "green"),
        (6, 6, "birch", "light green"),
        (8, 3, "pine", "dark green"),
        (9, 9, "oak", "green"),
    ];

    let forest: Vec<Tree> = plan
        .iter()
        .map(|&(x, y, name, color)| Tree { x, y, kind: factory.get(name, color) })
        .collect();

    for tree in &forest {
        tree.kind.draw(tree.x, tree.y);
    }

    println!("trees planted: {}, tree types in memory: {}", forest.len(), factory.len());
}
