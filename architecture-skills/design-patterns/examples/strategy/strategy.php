<?php
// Strategy pattern in PHP.
//
// PHP closures and first-class callables cover stateless strategies
// (usort's comparator is a strategy). An interface earns its keep when
// the strategy carries state or several methods; both forms are shown.

declare(strict_types=1);

final class Order
{
    public function __construct(
        public readonly float $weightKg,
        public readonly float $distanceKm,
    ) {
    }
}

interface ShippingStrategy
{
    public function cost(Order $order): float;
}

// A stateful strategy: the negotiated rates are its state.
final class CarrierRate implements ShippingStrategy
{
    public function __construct(
        private readonly float $base,
        private readonly float $perKg,
    ) {
    }

    public function cost(Order $order): float
    {
        return $this->base + $this->perKg * $order->weightKg;
    }
}

// Context: accepts a closure or an object; delegates pricing to it.
final class Checkout
{
    /** @var callable(Order): float */
    private $strategy;

    public function __construct(callable $strategy)
    {
        $this->strategy = $strategy;
    }

    public function setStrategy(callable $strategy): void
    {
        $this->strategy = $strategy;
    }

    public function shippingFor(Order $order): float
    {
        return ($this->strategy)($order);
    }
}

$order = new Order(weightKg: 2.4, distanceKm: 120);

$strategies = [
    'flat' => fn (Order $o): float => 5.00,
    'weight' => fn (Order $o): float => 4.00 + 1.50 * $o->weightKg,
    'distance' => fn (Order $o): float => 2.00 + 0.05 * $o->distanceKm,
    'carrier' => (new CarrierRate(base: 3.00, perKg: 2.00))->cost(...),
];

$checkout = new Checkout($strategies['flat']);
foreach ($strategies as $name => $strategy) {
    $checkout->setStrategy($strategy);
    printf("%8s: $%.2f\n", $name, $checkout->shippingFor($order));
}
