// Classes & objects in JavaScript.
//
// `class` is sugar over prototypes: methods live once on the
// prototype, fields live on each instance. #private fields keep the
// balance inaccessible from outside, `static` members hang off the
// class itself, and transfer() stays a plain function because it
// belongs to no single account.

class BankAccount {
  // Static field: one counter shared by all instances.
  static #accountsOpened = 0;

  // Private instance fields: one copy per object, never shared.
  #balance;

  // Constructor: the only way in; if it returns, state is valid.
  constructor(owner, openingBalance = 0) {
    if (openingBalance < 0) {
      throw new RangeError("opening balance cannot be negative");
    }
    BankAccount.#accountsOpened += 1;
    this.number = `ACC-${String(BankAccount.#accountsOpened).padStart(4, "0")}`;
    this.owner = owner;
    this.#balance = openingBalance;
  }

  // Instance methods: `this` binds them to one object.
  deposit(amount) {
    if (amount <= 0) {
      throw new RangeError("deposit must be positive");
    }
    this.#balance += amount;
  }

  withdraw(amount) {
    if (amount > this.#balance) {
      throw new Error(`${this.number}: insufficient funds`);
    }
    this.#balance -= amount;
  }

  get balance() {
    return this.#balance;
  }

  toString() {
    return `${this.number} (${this.owner}): $${this.#balance.toFixed(2)}`;
  }

  // Static method: bound to the class, callable with no instance.
  static totalOpened() {
    return BankAccount.#accountsOpened;
  }
}

// Free function: coordinates two objects, owns neither.
function transfer(from, to, amount) {
  from.withdraw(amount);
  to.deposit(amount);
}

// Two objects from one blueprint, each with independent state.
const alice = new BankAccount("Alice", 100);
const bob = new BankAccount("Bob");

alice.deposit(50);
bob.deposit(20);
alice.withdraw(30);

console.log(alice.toString()); // Bob's balance is untouched
console.log(bob.toString());

transfer(alice, bob, 40);
console.log("after transfer:");
console.log(alice.toString());
console.log(bob.toString());

console.log(`accounts opened: ${BankAccount.totalOpened()}`);
