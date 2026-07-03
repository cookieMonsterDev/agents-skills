// Law of Demeter in JavaScript.
//
// order.getCustomer().getWallet().deduct(due) is a train wreck — checkout
// knows the customer's internals. customer.pay(due) is tell-don't-ask:
// payment logic stays with the wallet's owner.

// --- Before (train wreck, sketched): ---
//
// class Checkout {
//   collect(order, due) {
//     order.getCustomer().getWallet().deduct(due);
//   }
// }

// --- After: one hop from checkout to customer ---

class Wallet {
  #balance;

  constructor(opening) {
    if (opening < 0) throw new RangeError("opening balance cannot be negative");
    this.#balance = opening;
  }

  deduct(amount) {
    if (amount <= 0) throw new RangeError("payment must be positive");
    if (amount > this.#balance) throw new RangeError("insufficient funds");
    this.#balance -= amount;
  }

  balance() {
    return this.#balance;
  }
}

class Customer {
  #wallet;

  constructor(name, opening) {
    this.name = name;
    this.#wallet = new Wallet(opening);
  }

  pay(amount) {
    this.#wallet.deduct(amount);
  }

  balance() {
    return this.#wallet.balance();
  }
}

class Order {
  constructor(id, customer, total) {
    this.id = id;
    this.customer = customer;
    this.total = total;
  }
}

class Checkout {
  collect(order, due) {
    order.customer.pay(due);
  }
}

const ada = new Customer("Ada", 50);
const order = new Order("ORD-101", ada, 12.5);
const checkout = new Checkout();

console.log(`${ada.name} wallet before: $${ada.balance().toFixed(2)}`);
checkout.collect(order, order.total);
console.log(`collected $${order.total.toFixed(2)} for ${order.id}`);
console.log(`${ada.name} wallet after:  $${ada.balance().toFixed(2)}  (invariant intact)`);
