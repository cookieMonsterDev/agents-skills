// Open/Closed Principle in JavaScript.
//
// PricingEngine is closed: it iterates registered rules through the
// discount duck contract and never names a concrete rule. FlashSale
// is added later as a new class -- zero edits to the engine.

class PricingEngine {
  constructor() {
    this._rules = [];
  }

  register(rule) {
    this._rules.push(rule);
  }

  total(order) {
    let total = order.subtotal;
    for (const rule of this._rules) {
      const amount = rule.discount(order);
      if (amount > 0) {
        console.log(`  ${rule.name.padStart(6)}: -$${amount.toFixed(2)}`);
      }
      total -= amount;
    }
    return total;
  }
}

// --- Extensions: the engine never mentions these types ---

class BulkDiscount {
  get name() {
    return 'bulk';
  }

  discount(order) {
    return order.itemCount >= 10 ? 0.05 * order.subtotal : 0.0;
  }
}

class MemberDiscount {
  get name() {
    return 'member';
  }

  discount(order) {
    return order.isMember ? 0.10 * order.subtotal : 0.0;
  }
}

// A NEW rule, written later -- nothing above is touched.
class FlashSale {
  constructor(amount, threshold) {
    this._amount = amount;
    this._threshold = threshold;
  }

  get name() {
    return 'flash';
  }

  discount(order) {
    return order.subtotal > this._threshold ? this._amount : 0.0;
  }
}

function main() {
  const order = { subtotal: 120.0, itemCount: 12, isMember: true };

  const engine = new PricingEngine();
  engine.register(new BulkDiscount());
  engine.register(new MemberDiscount());

  console.log(`subtotal: $${order.subtotal.toFixed(2)}`);
  console.log(`total:    $${engine.total(order).toFixed(2)}`);

  console.log('-- registering FlashSale: no engine edits --');
  engine.register(new FlashSale(15.0, 100.0));
  console.log(`total:    $${engine.total(order).toFixed(2)}`);
}

main();
