// Iterator pattern in Rust.
//
// A binary search tree traversed in sorted order. Rust builds the
// pattern in as the Iterator trait: implementing next() -> Option<T>
// plugs a custom collection into for loops and the whole adapter
// ecosystem (map, filter, sum). The iterator replaces the recursive
// walk with an explicit stack of borrowed nodes.

struct Node {
    value: i32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

#[derive(Default)]
struct SortedTree {
    root: Option<Box<Node>>,
}

impl SortedTree {
    fn add(&mut self, value: i32) {
        let mut slot = &mut self.root;
        while let Some(node) = slot {
            slot = if value < node.value { &mut node.left } else { &mut node.right };
        }
        *slot = Some(Box::new(Node { value, left: None, right: None }));
    }

    fn iter(&self) -> InOrder<'_> {
        let mut iter = InOrder { stack: Vec::new() };
        iter.push_left_spine(self.root.as_deref());
        iter
    }
}

/// Stack of nodes whose left subtrees are already done.
struct InOrder<'a> {
    stack: Vec<&'a Node>,
}

impl<'a> InOrder<'a> {
    fn push_left_spine(&mut self, mut node: Option<&'a Node>) {
        while let Some(n) = node {
            self.stack.push(n);
            node = n.left.as_deref();
        }
    }
}

impl<'a> Iterator for InOrder<'a> {
    type Item = i32;

    fn next(&mut self) -> Option<i32> {
        let node = self.stack.pop()?;
        self.push_left_spine(node.right.as_deref());
        Some(node.value)
    }
}

impl<'a> IntoIterator for &'a SortedTree {
    type Item = i32;
    type IntoIter = InOrder<'a>;

    fn into_iter(self) -> InOrder<'a> {
        self.iter()
    }
}

fn main() {
    let mut tree = SortedTree::default();
    for value in [5, 3, 8, 1, 4, 9, 7] {
        tree.add(value);
    }

    let in_order: Vec<i32> = tree.iter().collect();
    println!("in order: {in_order:?}");
    println!("sum: {}", tree.iter().sum::<i32>());
    println!("evens: {:?}", tree.iter().filter(|v| v % 2 == 0).collect::<Vec<_>>());
}
