// Decorator pattern in Rust.
//
// Wrappers implement the same trait as the value they wrap — the same
// shape as std's io::BufReader over any Read, or iterator adapters.
// Generic wrappers compose statically with zero cost; switch to
// Box<dyn Beverage> when the stack must be assembled at runtime.

trait Beverage {
    fn description(&self) -> String;
    fn cost(&self) -> f64;
}

struct Espresso;

impl Beverage for Espresso {
    fn description(&self) -> String {
        "espresso".to_string()
    }
    fn cost(&self) -> f64 {
        2.00
    }
}

struct Milk<B: Beverage>(B);

impl<B: Beverage> Beverage for Milk<B> {
    fn description(&self) -> String {
        format!("{} + milk", self.0.description())
    }
    fn cost(&self) -> f64 {
        self.0.cost() + 0.30
    }
}

struct Mocha<B: Beverage>(B);

impl<B: Beverage> Beverage for Mocha<B> {
    fn description(&self) -> String {
        format!("{} + mocha", self.0.description())
    }
    fn cost(&self) -> f64 {
        self.0.cost() + 0.50
    }
}

struct WhippedCream<B: Beverage>(B);

impl<B: Beverage> Beverage for WhippedCream<B> {
    fn description(&self) -> String {
        format!("{} + whipped cream", self.0.description())
    }
    fn cost(&self) -> f64 {
        self.0.cost() + 0.40
    }
}

fn main() {
    let drinks: Vec<Box<dyn Beverage>> = vec![
        Box::new(Espresso),
        Box::new(WhippedCream(Mocha(Milk(Espresso)))),
    ];
    for drink in &drinks {
        println!("{}: ${:.2}", drink.description(), drink.cost());
    }
}
