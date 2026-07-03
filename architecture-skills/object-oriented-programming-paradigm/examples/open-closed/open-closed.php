<?php
/**
 * Open/Closed Principle in PHP.
 *
 * PricingEngine is closed: it iterates registered discount rules and
 * never names a concrete rule. FlashSale is added later with zero edits
 * to the engine.
 */

declare(strict_types=1);

final readonly class Order
{
    public function __construct(
        public float $subtotal,
        public int $itemCount,
        public bool $isMember,
    ) {}
}

interface DiscountRule
{
    public function name(): string;
    public function discount(Order $order): float;
}

final class BulkDiscount implements DiscountRule
{
    public function name(): string { return 'bulk'; }

    public function discount(Order $order): float
    {
        return $order->itemCount >= 10 ? 0.05 * $order->subtotal : 0.0;
    }
}

final class MemberDiscount implements DiscountRule
{
    public function name(): string { return 'member'; }

    public function discount(Order $order): float
    {
        return $order->isMember ? 0.10 * $order->subtotal : 0.0;
    }
}

final class PricingEngine
{
    /** @var list<DiscountRule> */
    private array $rules = [];

    public function register(DiscountRule $rule): void
    {
        $this->rules[] = $rule;
    }

    public function total(Order $order): float
    {
        $total = $order->subtotal;
        foreach ($this->rules as $rule) {
            $amount = $rule->discount($order);
            if ($amount > 0.0) {
                printf("  %6s: -$%.2f\n", $rule->name(), $amount);
            }
            $total -= $amount;
        }
        return $total;
    }
}

final class FlashSale implements DiscountRule
{
    public function __construct(
        private readonly float $amount,
        private readonly float $threshold,
    ) {}

    public function name(): string { return 'flash'; }

    public function discount(Order $order): float
    {
        return $order->subtotal > $this->threshold ? $this->amount : 0.0;
    }
}

$order = new Order(120.00, 12, true);
$engine = new PricingEngine();
$engine->register(new BulkDiscount());
$engine->register(new MemberDiscount());

printf("subtotal: $%.2f\n", $order->subtotal);
printf("total:    $%.2f\n", $engine->total($order));

echo "-- registering FlashSale: no engine edits --\n";
$engine->register(new FlashSale(15.00, 100.00));
printf("total:    $%.2f\n", $engine->total($order));
