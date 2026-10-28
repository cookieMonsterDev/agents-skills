// Coupling and Cohesion in JavaScript.
//
// A god OrderProcessor that computes tax, validates, and ships couples
// three volatile concerns. Focused classes with high cohesion let a tax
// change touch only OrderCalculator.

// --- Before (tightly coupled, sketched): ---
//
// class OrderProcessor {
//   process(order) {
//     const total = order.subtotal * 1.20;  // tax
//     if (total <= 0) throw new Error();    // validation
//     console.log(`shipped ${order.id}`);   // shipping
//     return total;
//   }
// }

class Order {
  constructor(id, subtotal) {
    this.id = id;
    this.subtotal = subtotal;
  }
}

/** Finance's class: only tax-rule changes touch this file. */
class OrderCalculator {
  constructor(taxRate) {
    this.taxRate = taxRate;
  }

  total(order) {
    return order.subtotal * (1 + this.taxRate);
  }
}

/** Compliance's class: only validation rules change touch this file. */
class OrderValidator {
  validate(order, total) {
    if (order.subtotal <= 0) throw new RangeError("subtotal must be positive");
    if (total <= 0) throw new RangeError("total must be positive");
  }
}

/** Fulfillment's class: only carrier/API changes touch this file. */
class OrderShipper {
  ship(order) {
    return `shipped ${order.id}`;
  }
}

/** Thin orchestrator: wires cohesive pieces, owns no domain rules. */
class OrderService {
  constructor(calculator, validator, shipper) {
    this.calculator = calculator;
    this.validator = validator;
    this.shipper = shipper;
  }

  process(order) {
    const total = this.calculator.total(order);
    this.validator.validate(order, total);
    console.log(this.shipper.ship(order));
    return total;
  }
}

const order = new Order("ORD-204", 80);

const service = new OrderService(
  new OrderCalculator(0.20),
  new OrderValidator(),
  new OrderShipper(),
);
const total = service.process(order);
console.log(`total with 20% tax: $${total.toFixed(2)}`);

const newRateService = new OrderService(
  new OrderCalculator(0.08),
  new OrderValidator(),
  new OrderShipper(),
);
const newTotal = newRateService.process(order);
console.log(`total with 8% tax:  $${newTotal.toFixed(2)}  (only OrderCalculator changed)`);
