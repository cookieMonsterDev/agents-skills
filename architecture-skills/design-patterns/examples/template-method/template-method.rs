// Template Method pattern in Rust.
//
// Rust has no inheritance; the idiomatic equivalent is a trait whose
// default method is the template — it fixes the skeleton and calls the
// required methods that implementors supply (Iterator works this way:
// dozens of default methods built on one required next()).

struct LineItem {
    product: &'static str,
    units: u32,
    price: f64,
}

impl LineItem {
    fn subtotal(&self) -> f64 {
        self.units as f64 * self.price
    }
}

trait SalesReport {
    /// The template method: a default impl fixes the skeleton, so
    /// iteration and totalling never vary.
    fn generate(&self, items: &[LineItem]) -> String {
        let mut lines = vec![self.header()];
        let mut total = 0.0;
        for item in items {
            lines.push(self.row(item));
            total += item.subtotal();
        }
        lines.push(self.footer(total));
        lines.join("\n")
    }

    fn header(&self) -> String;
    fn row(&self, item: &LineItem) -> String;
    fn footer(&self, total: f64) -> String;
}

struct CsvReport;

impl SalesReport for CsvReport {
    fn header(&self) -> String {
        "product,units,price,subtotal".to_string()
    }

    fn row(&self, item: &LineItem) -> String {
        format!(
            "{},{},{:.2},{:.2}",
            item.product,
            item.units,
            item.price,
            item.subtotal()
        )
    }

    fn footer(&self, total: f64) -> String {
        format!("total,,,{total:.2}")
    }
}

struct MarkdownReport;

impl SalesReport for MarkdownReport {
    fn header(&self) -> String {
        "| Product | Units | Subtotal |\n| --- | --- | --- |".to_string()
    }

    fn row(&self, item: &LineItem) -> String {
        format!("| {} | {} | ${:.2} |", item.product, item.units, item.subtotal())
    }

    fn footer(&self, total: f64) -> String {
        format!("\n**Total: ${total:.2}**")
    }
}

fn main() {
    let items = [
        LineItem { product: "Keyboard", units: 2, price: 80.00 },
        LineItem { product: "Mouse", units: 1, price: 25.50 },
        LineItem { product: "Monitor", units: 3, price: 210.00 },
    ];

    let reports: Vec<(&str, Box<dyn SalesReport>)> = vec![
        ("CsvReport", Box::new(CsvReport)),
        ("MarkdownReport", Box::new(MarkdownReport)),
    ];

    for (name, report) in &reports {
        println!("--- {name} ---");
        println!("{}\n", report.generate(&items));
    }
}
