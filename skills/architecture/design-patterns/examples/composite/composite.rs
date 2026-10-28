// Composite pattern in Rust.
//
// A trait plus Box<dyn Node> children gives the open-ended GoF form.
// When the set of node kinds is closed, a recursive enum
// (enum Node { File(..), Dir(..) }) is often the more idiomatic choice.

trait Node {
    fn size(&self) -> u64;
    fn print(&self, indent: usize);
}

struct File {
    name: String,
    size: u64,
}

impl File {
    fn new(name: &str, size: u64) -> Box<Self> {
        Box::new(Self { name: name.to_string(), size })
    }
}

impl Node for File {
    fn size(&self) -> u64 {
        self.size
    }
    fn print(&self, indent: usize) {
        println!("{:indent$}{} ({} B)", "", self.name, self.size);
    }
}

struct Directory {
    name: String,
    children: Vec<Box<dyn Node>>,
}

impl Directory {
    fn new(name: &str) -> Self {
        Self { name: name.to_string(), children: Vec::new() }
    }

    fn add(mut self, child: Box<dyn Node>) -> Self {
        self.children.push(child);
        self
    }
}

impl Node for Directory {
    fn size(&self) -> u64 {
        self.children.iter().map(|child| child.size()).sum()
    }
    fn print(&self, indent: usize) {
        println!("{:indent$}{}/ ({} B)", "", self.name, self.size());
        for child in &self.children {
            child.print(indent + 2);
        }
    }
}

fn main() {
    let project = Directory::new("project")
        .add(Box::new(
            Directory::new("src")
                .add(File::new("main.py", 1200))
                .add(File::new("util.py", 450)),
        ))
        .add(Box::new(Directory::new("docs").add(File::new("readme.md", 800))))
        .add(File::new(".gitignore", 20));

    project.print(0);
}
