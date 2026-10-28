// Proxy pattern in Rust (virtual proxy: lazy-loading image).
//
// A trait object gives the shared subject interface, and OnceCell
// provides interior-mutable lazy initialization behind &self. Note that
// Rust's smart pointers are proxy-like by design: Deref lets Box, Rc,
// and friends transparently interpose on access to their target.

use std::cell::OnceCell;

trait Image {
    fn display(&self);
}

/// Real subject: expensive to create.
struct RealImage {
    filename: String,
}

impl RealImage {
    fn load(filename: &str) -> Self {
        println!("Loading {filename} from disk (expensive)");
        Self { filename: filename.to_string() }
    }
}

impl Image for RealImage {
    fn display(&self) {
        println!("Displaying {}", self.filename);
    }
}

/// Virtual proxy: defers creating RealImage until first use.
struct ImageProxy {
    filename: String,
    real: OnceCell<RealImage>,
}

impl ImageProxy {
    fn new(filename: &str) -> Self {
        Self { filename: filename.to_string(), real: OnceCell::new() }
    }
}

impl Image for ImageProxy {
    fn display(&self) {
        self.real.get_or_init(|| RealImage::load(&self.filename)).display();
    }
}

fn main() {
    let gallery: Vec<Box<dyn Image>> = vec![
        Box::new(ImageProxy::new("holiday.png")),
        Box::new(ImageProxy::new("unused.png")),
    ];
    println!("Proxies created; nothing loaded yet");

    gallery[0].display();
    gallery[0].display(); // loaded once, displayed twice

    println!("unused.png was never loaded");
}
