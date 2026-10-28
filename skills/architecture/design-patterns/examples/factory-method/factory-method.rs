// Factory Method pattern in Rust.
//
// The creator is a trait whose default method (plan_delivery) is the shared
// workflow; implementors supply only create_transport. For a closed set of
// products, an enum with a constructor match is often preferred over
// boxed trait objects.

trait Transport {
    fn deliver(&self, cargo: &str) -> String;
}

struct Truck;
struct Ship;

impl Transport for Truck {
    fn deliver(&self, cargo: &str) -> String {
        format!("Truck delivers {cargo} by road in a box")
    }
}

impl Transport for Ship {
    fn deliver(&self, cargo: &str) -> String {
        format!("Ship delivers {cargo} by sea in a container")
    }
}

/// Creator: the default method is the shared workflow, the required
/// method is the factory step.
trait Logistics {
    fn name(&self) -> &'static str;
    fn create_transport(&self) -> Box<dyn Transport>;

    fn plan_delivery(&self, cargo: &str) -> String {
        let transport = self.create_transport();
        format!("[{}] {}", self.name(), transport.deliver(cargo))
    }
}

struct RoadLogistics;
struct SeaLogistics;

impl Logistics for RoadLogistics {
    fn name(&self) -> &'static str {
        "RoadLogistics"
    }
    fn create_transport(&self) -> Box<dyn Transport> {
        Box::new(Truck)
    }
}

impl Logistics for SeaLogistics {
    fn name(&self) -> &'static str {
        "SeaLogistics"
    }
    fn create_transport(&self) -> Box<dyn Transport> {
        Box::new(Ship)
    }
}

fn main() {
    let all: [&dyn Logistics; 2] = [&RoadLogistics, &SeaLogistics];
    for logistics in all {
        println!("{}", logistics.plan_delivery("machine parts"));
    }
}
