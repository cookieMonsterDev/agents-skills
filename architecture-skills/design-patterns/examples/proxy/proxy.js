// Proxy pattern in JavaScript (virtual proxy: lazy-loading image).
//
// JavaScript has a built-in Proxy object that intercepts property
// access on any target without hand-written delegation — the
// language-native form of this pattern. Both the classic form and the
// built-in Proxy are shown below.

class RealImage {
  constructor(filename) {
    this.filename = filename;
    console.log(`Loading ${filename} from disk (expensive)`);
  }

  display() {
    console.log(`Displaying ${this.filename}`);
  }
}

// --- Variant 1: classic hand-written virtual proxy ---

class ImageProxy {
  #filename;
  #real = null;

  constructor(filename) {
    this.#filename = filename;
  }

  display() {
    this.#real ??= new RealImage(this.#filename);
    this.#real.display();
  }
}

// --- Variant 2: built-in Proxy intercepting all access lazily ---

function lazyImage(filename) {
  let real = null;
  return new Proxy({}, {
    get(_target, prop) {
      real ??= new RealImage(filename);
      const value = real[prop];
      return typeof value === "function" ? value.bind(real) : value;
    },
  });
}

const holiday = new ImageProxy("holiday.png");
const unused = new ImageProxy("unused.png");
console.log("Proxies created; nothing loaded yet");

holiday.display();
holiday.display(); // loaded once, displayed twice

const native = lazyImage("native.png");
console.log("Built-in Proxy created; nothing loaded yet");
native.display(); // first property access triggers the load

console.log("unused.png was never loaded");
