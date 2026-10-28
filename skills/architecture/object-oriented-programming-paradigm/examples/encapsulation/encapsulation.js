// Encapsulation in JavaScript.
//
// #private class fields are enforced by the engine: `account.#balance`
// outside the class is a syntax error, not just a convention. (Before
// class fields, closures did the same job — see makeAccount.) A getter
// exposes the value read-only; deposit/withdraw enforce the invariant:
// balance never goes negative.

class BankAccount {
  #balance; // truly private: inaccessible outside this class body

  constructor(openingBalance = 0) {
    if (openingBalance < 0) throw new RangeError("opening balance cannot be negative");
    this.#balance = openingBalance;
  }

  get balance() {
    return this.#balance; // read access only: no setter defined
  }

  deposit(amount) {
    if (amount <= 0) throw new RangeError("deposit must be positive");
    this.#balance += amount;
  }

  withdraw(amount) {
    if (amount <= 0) throw new RangeError("withdrawal must be positive");
    if (amount > this.#balance) throw new RangeError("insufficient funds");
    this.#balance -= amount;
  }
}

// The pre-class-fields form: a closure hides `balance` completely.
function makeAccount(openingBalance) {
  let balance = openingBalance; // unreachable except through the methods below
  return {
    balance: () => balance,
    deposit(amount) {
      if (amount <= 0) throw new RangeError("deposit must be positive");
      balance += amount;
    },
    withdraw(amount) {
      if (amount <= 0 || amount > balance) throw new RangeError("insufficient funds");
      balance -= amount;
    },
  };
}

const account = new BankAccount(100);
account.deposit(50);
console.log(`after deposit:  $${account.balance.toFixed(2)}`);

try {
  account.withdraw(250);
} catch (err) {
  console.log(`withdraw $250 rejected: ${err.message}`);
}

account.withdraw(30);
console.log(`after withdraw: $${account.balance.toFixed(2)}  (invariant intact)`);

const closed = makeAccount(100);
closed.withdraw(40);
console.log(`closure account: $${closed.balance().toFixed(2)}`);
// account.#balance = -500;  // SyntaxError: private field outside class body
