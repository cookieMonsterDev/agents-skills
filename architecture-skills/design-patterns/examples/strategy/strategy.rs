// Strategy pattern in Rust.
//
// Stateless strategies are idiomatically just closures or fn pointers
// (compare sort_by taking a comparator), so the context stores a boxed
// Fn. A trait is the right tool when a strategy carries state or
// several methods; the trait form plugs into the same context through
// a closure that captures the strategy value.

struct Order {
    weight_kg: f64,
    distance_km: f64,
}

// --- Closure form: idiomatic for stateless strategies ---

type ShippingStrategy = Box<dyn Fn(&Order) -> f64>;

/// Context: delegates the pricing decision to the current strategy.
struct Checkout {
    strategy: ShippingStrategy,
}

impl Checkout {
    fn new(strategy: ShippingStrategy) -> Self {
        Self { strategy }
    }

    fn set_strategy(&mut self, strategy: ShippingStrategy) {
        self.strategy = strategy;
    }

    fn shipping_for(&self, order: &Order) -> f64 {
        (self.strategy)(order)
    }
}

// --- Trait form: for stateful or multi-method strategies ---

trait ShippingCost {
    fn cost(&self, order: &Order) -> f64;
}

/// A stateful strategy: the negotiated rates are its state.
struct CarrierRate {
    base: f64,
    per_kg: f64,
}

impl ShippingCost for CarrierRate {
    fn cost(&self, order: &Order) -> f64 {
        self.base + self.per_kg * order.weight_kg
    }
}

fn main() {
    let order = Order {
        weight_kg: 2.4,
        distance_km: 120.0,
    };

    let carrier = CarrierRate {
        base: 3.00,
        per_kg: 2.00,
    };

    let strategies: Vec<(&str, ShippingStrategy)> = vec![
        ("flat", Box::new(|_: &Order| 5.00)),
        ("weight", Box::new(|o: &Order| 4.00 + 1.50 * o.weight_kg)),
        ("distance", Box::new(|o: &Order| 2.00 + 0.05 * o.distance_km)),
        ("carrier", Box::new(move |o: &Order| carrier.cost(o))),
    ];

    let mut checkout = Checkout::new(Box::new(|_: &Order| 5.00));
    for (name, strategy) in strategies {
        checkout.set_strategy(strategy);
        println!("{name:>8}: ${:.2}", checkout.shipping_for(&order));
    }
}
