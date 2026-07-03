// Singleton pattern in JavaScript.
//
// Note: module scope is the idiomatic singleton — `export default new
// AppConfig()` is cached by the module system, so every importer shares one
// instance with zero class machinery. The explicit static-instance form
// below is for when you can't rely on modules. Prefer passing the instance
// in (dependency injection); singletons leak state between tests.

class AppConfig {
  static #instance = null;

  #settings;

  constructor() {
    if (AppConfig.#instance) {
      return AppConfig.#instance; // constructor always yields the one instance
    }
    // Stands in for reading a config file once.
    console.log("Loading configuration (expensive, happens once)");
    this.#settings = {
      app_name: "InventoryService",
      db_url: "postgres://localhost/inventory",
      log_level: "INFO",
    };
    AppConfig.#instance = this;
  }

  static getInstance() {
    return new AppConfig();
  }

  get(key) {
    return this.#settings[key];
  }
}

const a = AppConfig.getInstance();
const b = new AppConfig(); // even direct construction returns the instance

console.log("same instance:", a === b);
console.log("app_name:", a.get("app_name"));
console.log("db_url:", b.get("db_url"));
