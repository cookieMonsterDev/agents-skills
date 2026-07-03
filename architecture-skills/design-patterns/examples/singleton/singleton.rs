// Singleton pattern in Rust.
//
// std::sync::OnceLock initializes a static exactly once, thread-safely
// (LazyLock and the older lazy_static/once_cell crates are equivalent).
// Rust makes the costs explicit: a mutable singleton would need a Mutex.
// Prefer passing &AppConfig down from main where feasible; globals hide
// dependencies from function signatures.

use std::collections::HashMap;
use std::sync::OnceLock;

#[derive(Debug)]
struct AppConfig {
    settings: HashMap<&'static str, &'static str>,
}

impl AppConfig {
    fn load() -> Self {
        // Stands in for reading a config file once.
        println!("Loading configuration (expensive, happens once)");
        Self {
            settings: HashMap::from([
                ("app_name", "InventoryService"),
                ("db_url", "postgres://localhost/inventory"),
                ("log_level", "INFO"),
            ]),
        }
    }

    fn get(&self, key: &str) -> &str {
        self.settings[key]
    }
}

fn app_config() -> &'static AppConfig {
    static INSTANCE: OnceLock<AppConfig> = OnceLock::new();
    INSTANCE.get_or_init(AppConfig::load)
}

fn main() {
    let a = app_config();
    let b = app_config();

    println!("same instance: {}", std::ptr::eq(a, b));
    println!("app_name: {}", a.get("app_name"));
    println!("db_url: {}", b.get("db_url"));
}
