// Adapter pattern in JavaScript.
//
// With duck typing there is no interface keyword: the adapter just
// exposes the methods callers expect and forwards to the legacy object.
// A formal adapter class pays off when the mismatched object is
// third-party and used in many places.

class ModernSensor {
  constructor(name, celsius) {
    this._name = name;
    this._celsius = celsius;
  }
  name() {
    return this._name;
  }
  celsius() {
    return this._celsius;
  }
}

// Adaptee: third-party class we cannot modify.
class LegacyFahrenheitSensor {
  constructor(sensorId, fahrenheit) {
    this.sensorId = sensorId;
    this._fahrenheit = fahrenheit;
  }
  readFahrenheit() {
    return this._fahrenheit;
  }
}

class FahrenheitAdapter {
  constructor(legacy) {
    this._legacy = legacy;
  }
  name() {
    return this._legacy.sensorId;
  }
  celsius() {
    return ((this._legacy.readFahrenheit() - 32) * 5) / 9;
  }
}

function report(sources) {
  for (const source of sources) {
    console.log(`${source.name()}: ${source.celsius().toFixed(1)}°C`);
  }
}

report([
  new ModernSensor("server-room", 21.5),
  new FahrenheitAdapter(new LegacyFahrenheitSensor("warehouse-legacy", 77)),
]);
