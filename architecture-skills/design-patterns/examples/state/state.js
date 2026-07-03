// State pattern in JavaScript.
//
// States are plain objects in a lookup table — no classes needed.
// Handlers return the name of the next state, keeping transitions
// explicit and easy to log or test. (XState is the ecosystem's
// heavyweight version of this idea.)

const states = {
  idle: {
    insertCoin(machine) {
      console.log("coin accepted");
      return "hasCoin";
    },
    selectItem() {
      console.log("insert a coin first");
      return "idle";
    },
  },
  hasCoin: {
    insertCoin() {
      console.log("coin already inserted, returning it");
      return "hasCoin";
    },
    selectItem(machine) {
      machine.stock--;
      console.log(`item dispensed (${machine.stock} left)`);
      return machine.stock === 0 ? "soldOut" : "idle";
    },
  },
  soldOut: {
    insertCoin() {
      console.log("sold out, returning coin");
      return "soldOut";
    },
    selectItem() {
      console.log("sold out");
      return "soldOut";
    },
  },
};

class VendingMachine {
  constructor(stock) {
    this.stock = stock;
    this.state = stock > 0 ? "idle" : "soldOut";
  }

  insertCoin() {
    this.state = states[this.state].insertCoin(this);
  }

  selectItem() {
    this.state = states[this.state].selectItem(this);
  }
}

const machine = new VendingMachine(2);
machine.selectItem(); // insert a coin first
machine.insertCoin();
machine.insertCoin(); // coin already inserted
machine.selectItem(); // item dispensed (1 left)
machine.insertCoin();
machine.selectItem(); // item dispensed (0 left)
machine.insertCoin(); // sold out, returning coin
