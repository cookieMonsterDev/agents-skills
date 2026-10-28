<?php
// Adapter pattern in PHP.
//
// The adapter implements the target interface and delegates to the
// wrapped legacy instance, converting units at the boundary.

interface TemperatureSource
{
    public function name(): string;
    public function celsius(): float;
}

class ModernSensor implements TemperatureSource
{
    public function __construct(
        private string $name,
        private float $celsius,
    ) {}

    public function name(): string
    {
        return $this->name;
    }

    public function celsius(): float
    {
        return $this->celsius;
    }
}

// Adaptee: third-party class we cannot modify.
class LegacyFahrenheitSensor
{
    public function __construct(
        public readonly string $sensorId,
        private float $fahrenheit,
    ) {}

    public function readFahrenheit(): float
    {
        return $this->fahrenheit;
    }
}

class FahrenheitAdapter implements TemperatureSource
{
    public function __construct(private LegacyFahrenheitSensor $legacy) {}

    public function name(): string
    {
        return $this->legacy->sensorId;
    }

    public function celsius(): float
    {
        return ($this->legacy->readFahrenheit() - 32.0) * 5.0 / 9.0;
    }
}

/** @param TemperatureSource[] $sources */
function report(array $sources): void
{
    foreach ($sources as $source) {
        printf("%s: %.1f°C\n", $source->name(), $source->celsius());
    }
}

report([
    new ModernSensor('server-room', 21.5),
    new FahrenheitAdapter(new LegacyFahrenheitSensor('warehouse-legacy', 77.0)),
]);
