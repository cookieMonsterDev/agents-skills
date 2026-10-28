// Factory Method pattern in JavaScript.
//
// Note: with first-class functions, passing a constructor or closure
// (`planDelivery(() => new Truck())`) often replaces the pattern. The
// class form below is worth it when the creator has real shared logic.

class Truck {
  deliver(cargo) {
    return `Truck delivers ${cargo} by road in a box`;
  }
}

class Ship {
  deliver(cargo) {
    return `Ship delivers ${cargo} by sea in a container`;
  }
}

// Creator: shared workflow around one overridable creation step.
class Logistics {
  createTransport() {
    throw new Error("Subclass must implement createTransport()");
  }

  planDelivery(cargo) {
    const transport = this.createTransport();
    return `[${this.constructor.name}] ${transport.deliver(cargo)}`;
  }
}

class RoadLogistics extends Logistics {
  createTransport() {
    return new Truck();
  }
}

class SeaLogistics extends Logistics {
  createTransport() {
    return new Ship();
  }
}

for (const logistics of [new RoadLogistics(), new SeaLogistics()]) {
  console.log(logistics.planDelivery("machine parts"));
}

// The functional alternative: the "factory method" is just a parameter.
function planDelivery(createTransport, cargo) {
  return createTransport().deliver(cargo);
}
console.log(planDelivery(() => new Ship(), "spare tires"));
