// Observer pattern in Rust.
//
// The GoF form (subject holds &mut references to observers) fights the
// borrow checker. This example stores boxed closures, which the ticker
// owns outright — simple, but observers can't be shared elsewhere or
// unsubscribed by identity. The alternative is Rc<RefCell<dyn Observer>>
// (shared, mutable observers at the cost of runtime borrow checks);
// in practice most Rust code uses channels (std::sync::mpsc) instead.

type PriceObserver = Box<dyn Fn(&str, f64)>;

struct StockTicker {
    observers: Vec<PriceObserver>,
}

impl StockTicker {
    fn new() -> Self {
        Self { observers: Vec::new() }
    }

    fn subscribe(&mut self, observer: PriceObserver) {
        self.observers.push(observer);
    }

    fn update_price(&self, symbol: &str, price: f64) {
        for observer in &self.observers {
            observer(symbol, price);
        }
    }
}

struct PriceDisplay {
    name: String,
}

impl PriceDisplay {
    fn on_price(&self, symbol: &str, price: f64) {
        println!("{}: {} is now ${:.2}", self.name, symbol, price);
    }
}

fn make_alert(watched: &str, threshold: f64) -> PriceObserver {
    let watched = watched.to_string();
    Box::new(move |symbol, price| {
        if symbol == watched && price > threshold {
            println!("ALERT: {watched} crossed ${threshold:.2} (now ${price:.2})");
        }
    })
}

fn main() {
    let mut ticker = StockTicker::new();

    let display = PriceDisplay {
        name: "Lobby display".to_string(),
    };
    // The closure takes ownership of the display; the ticker now owns both.
    ticker.subscribe(Box::new(move |symbol, price| display.on_price(symbol, price)));
    ticker.subscribe(make_alert("ACME", 100.0));

    ticker.update_price("ACME", 98.5);
    ticker.update_price("ACME", 101.25);
    ticker.update_price("GLOBEX", 45.0);
}
