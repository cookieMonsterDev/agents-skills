<?php
// Coupling and Cohesion in PHP.
//
// A god OrderProcessor that computes tax, validates, and ships couples
// three volatile concerns. Focused classes with high cohesion let a tax
// change touch only OrderCalculator.

declare(strict_types=1);

// --- Before (tightly coupled, sketched): ---
//
// final class OrderProcessor {
//     public function process(Order $order): float {
//         $total = $order->subtotal * 1.20;  // tax
//         if ($total <= 0) throw ...;        // validation
//         echo "shipped {$order->id}";       // shipping
//         return $total;
//     }
// }

final class Order
{
    public function __construct(
        public readonly string $id,
        public readonly float $subtotal,
    ) {}
}

/** Finance's class: only tax-rule changes touch this file. */
final class OrderCalculator
{
    public function __construct(private readonly float $taxRate) {}

    public function total(Order $order): float
    {
        return $order->subtotal * (1 + $this->taxRate);
    }
}

/** Compliance's class: only validation rules change touch this file. */
final class OrderValidator
{
    public function validate(Order $order, float $total): void
    {
        if ($order->subtotal <= 0) {
            throw new InvalidArgumentException('subtotal must be positive');
        }
        if ($total <= 0) {
            throw new InvalidArgumentException('total must be positive');
        }
    }
}

/** Fulfillment's class: only carrier/API changes touch this file. */
final class OrderShipper
{
    public function ship(Order $order): string
    {
        return "shipped {$order->id}";
    }
}

/** Thin orchestrator: wires cohesive pieces, owns no domain rules. */
final class OrderService
{
    public function __construct(
        private readonly OrderCalculator $calculator,
        private readonly OrderValidator $validator,
        private readonly OrderShipper $shipper,
    ) {}

    public function process(Order $order): float
    {
        $total = $this->calculator->total($order);
        $this->validator->validate($order, $total);
        echo $this->shipper->ship($order) . PHP_EOL;
        return $total;
    }
}

$order = new Order('ORD-204', 80.00);

$service = new OrderService(
    new OrderCalculator(0.20),
    new OrderValidator(),
    new OrderShipper(),
);
$total = $service->process($order);
printf("total with 20%% tax: $%.2f\n", $total);

$newRateService = new OrderService(
    new OrderCalculator(0.08),
    new OrderValidator(),
    new OrderShipper(),
);
$newTotal = $newRateService->process($order);
printf("total with 8%% tax:  $%.2f  (only OrderCalculator changed)\n", $newTotal);
