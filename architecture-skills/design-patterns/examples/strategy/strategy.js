// Strategy pattern in JavaScript.
//
// Functions are first-class, so a strategy is usually just a function
// and a stateful strategy is a closure returned by a factory. A class
// hierarchy adds nothing here unless strategies need several methods.

// --- Stateless strategies: plain functions ---

const flatRate = () => 5.0;
const weightBased = (order) => 4.0 + 1.5 * order.weightKg;
const distanceBased = (order) => 2.0 + 0.05 * order.distanceKm;

// --- Stateful strategy: a closure captures the negotiated rates ---

function carrierRate(base, perKg) {
  return (order) => base + perKg * order.weightKg;
}

// Context: delegates the pricing decision to the current strategy.
class Checkout {
  #strategy;

  constructor(strategy) {
    this.#strategy = strategy;
  }

  setStrategy(strategy) {
    this.#strategy = strategy;
  }

  shippingFor(order) {
    return this.#strategy(order);
  }
}

const order = { weightKg: 2.4, distanceKm: 120 };

const strategies = [
  ["flat", flatRate],
  ["weight", weightBased],
  ["distance", distanceBased],
  ["carrier", carrierRate(3.0, 2.0)],
];

const checkout = new Checkout(flatRate);
for (const [name, strategy] of strategies) {
  checkout.setStrategy(strategy);
  console.log(`${name.padStart(8)}: $${checkout.shippingFor(order).toFixed(2)}`);
}
