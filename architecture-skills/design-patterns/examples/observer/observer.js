// Observer pattern in JavaScript.
//
// Closures are the natural observer in JS; subscribe() returns an
// unsubscribe function (the convention used by RxJS, Redux, etc.).
// The platform equivalents are EventTarget in the browser and
// EventEmitter in Node — reach for those before rolling your own.

class StockTicker {
  #observers = new Set();

  subscribe(observer) {
    this.#observers.add(observer);
    return () => this.#observers.delete(observer);
  }

  updatePrice(symbol, price) {
    for (const observer of this.#observers) {
      observer(symbol, price);
    }
  }
}

class PriceDisplay {
  constructor(name) {
    this.name = name;
  }

  onPrice = (symbol, price) => {
    console.log(`${this.name}: ${symbol} is now $${price.toFixed(2)}`);
  };
}

function makeAlert(watchedSymbol, threshold) {
  return (symbol, price) => {
    if (symbol === watchedSymbol && price > threshold) {
      console.log(
        `ALERT: ${watchedSymbol} crossed $${threshold.toFixed(2)} (now $${price.toFixed(2)})`,
      );
    }
  };
}

const ticker = new StockTicker();
const display = new PriceDisplay("Lobby display");
const unsubscribe = ticker.subscribe(display.onPrice);
ticker.subscribe(makeAlert("ACME", 100));

ticker.updatePrice("ACME", 98.5);
ticker.updatePrice("ACME", 101.25);

unsubscribe();
ticker.updatePrice("GLOBEX", 45); // only the alert remains
