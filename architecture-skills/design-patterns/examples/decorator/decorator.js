// Decorator pattern in JavaScript.
//
// Wraps an object with another object of the same shape. Not the same
// thing as the TC39 @decorator syntax, which rewrites class members at
// definition time; this pattern stacks wrappers around instances at
// runtime. For functions, higher-order functions play the same role.

class Espresso {
  description() {
    return "espresso";
  }
  cost() {
    return 2.0;
  }
}

class AddOn {
  constructor(inner, label, surcharge) {
    this.inner = inner;
    this.label = label;
    this.surcharge = surcharge;
  }
  description() {
    return `${this.inner.description()} + ${this.label}`;
  }
  cost() {
    return this.inner.cost() + this.surcharge;
  }
}

const milk = (inner) => new AddOn(inner, "milk", 0.3);
const mocha = (inner) => new AddOn(inner, "mocha", 0.5);
const whippedCream = (inner) => new AddOn(inner, "whipped cream", 0.4);

const plain = new Espresso();
const fancy = whippedCream(mocha(milk(new Espresso())));

for (const drink of [plain, fancy]) {
  console.log(`${drink.description()}: $${drink.cost().toFixed(2)}`);
}
