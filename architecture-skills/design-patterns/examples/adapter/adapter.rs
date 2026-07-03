// Adapter pattern in Rust.
//
// The newtype idiom is the natural adapter: wrap the foreign type in a
// local struct and implement the local trait on the wrapper. This also
// sidesteps the orphan rule, which forbids implementing a foreign trait
// for a foreign type directly.

trait TemperatureSource {
    fn name(&self) -> &str;
    fn celsius(&self) -> f64;
}

struct ModernSensor {
    name: String,
    celsius: f64,
}

impl TemperatureSource for ModernSensor {
    fn name(&self) -> &str {
        &self.name
    }
    fn celsius(&self) -> f64 {
        self.celsius
    }
}

/// Adaptee: imagine this type comes from another crate.
struct LegacyFahrenheitSensor {
    sensor_id: String,
    fahrenheit: f64,
}

impl LegacyFahrenheitSensor {
    fn read_fahrenheit(&self) -> f64 {
        self.fahrenheit
    }
}

/// Newtype adapter around the legacy sensor.
struct FahrenheitAdapter(LegacyFahrenheitSensor);

impl TemperatureSource for FahrenheitAdapter {
    fn name(&self) -> &str {
        &self.0.sensor_id
    }
    fn celsius(&self) -> f64 {
        (self.0.read_fahrenheit() - 32.0) * 5.0 / 9.0
    }
}

fn report(sources: &[&dyn TemperatureSource]) {
    for source in sources {
        println!("{}: {:.1}°C", source.name(), source.celsius());
    }
}

fn main() {
    let modern = ModernSensor {
        name: "server-room".to_string(),
        celsius: 21.5,
    };
    let adapter = FahrenheitAdapter(LegacyFahrenheitSensor {
        sensor_id: "warehouse-legacy".to_string(),
        fahrenheit: 77.0,
    });
    report(&[&modern, &adapter]);
}
