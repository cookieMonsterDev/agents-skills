<?php
// Factory Method pattern in PHP.
//
// An abstract creator owns the shared workflow and defers one creation
// step to subclasses. For trivial cases, passing a closure or a
// first-class callable (PHP 8.1+) is the lighter alternative.

declare(strict_types=1);

interface Transport
{
    public function deliver(string $cargo): string;
}

final class Truck implements Transport
{
    public function deliver(string $cargo): string
    {
        return "Truck delivers $cargo by road in a box";
    }
}

final class Ship implements Transport
{
    public function deliver(string $cargo): string
    {
        return "Ship delivers $cargo by sea in a container";
    }
}

/** Creator: shared workflow around one overridable creation step. */
abstract class Logistics
{
    abstract protected function createTransport(): Transport;

    public function planDelivery(string $cargo): string
    {
        $transport = $this->createTransport();
        return '[' . static::class . '] ' . $transport->deliver($cargo);
    }
}

final class RoadLogistics extends Logistics
{
    protected function createTransport(): Transport
    {
        return new Truck();
    }
}

final class SeaLogistics extends Logistics
{
    protected function createTransport(): Transport
    {
        return new Ship();
    }
}

foreach ([new RoadLogistics(), new SeaLogistics()] as $logistics) {
    echo $logistics->planDelivery('machine parts'), PHP_EOL;
}
