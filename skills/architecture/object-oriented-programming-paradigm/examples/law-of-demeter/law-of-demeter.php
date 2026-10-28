<?php
// Law of Demeter in PHP.
//
// $order->getCustomer()->getWallet()->deduct($due) is the classic train
// wreck in getter-heavy PHP. $customer->pay($due) is tell-don't-ask:
// the wallet stays private and payment rules live with Customer.

declare(strict_types=1);

// --- Before (train wreck, sketched): ---
//
// final class Checkout {
//     public function collect(Order $order, float $due): void {
//         $order->getCustomer()->getWallet()->deduct($due);
//     }
// }

// --- After: one hop from checkout to customer ---

final class Wallet
{
    private float $balance;

    public function __construct(float $opening)
    {
        if ($opening < 0) {
            throw new InvalidArgumentException('opening balance cannot be negative');
        }
        $this->balance = $opening;
    }

    public function deduct(float $amount): void
    {
        if ($amount <= 0) {
            throw new InvalidArgumentException('payment must be positive');
        }
        if ($amount > $this->balance) {
            throw new InvalidArgumentException('insufficient funds');
        }
        $this->balance -= $amount;
    }

    public function balance(): float
    {
        return $this->balance;
    }
}

final class Customer
{
    public readonly string $name;
    private Wallet $wallet; // no getWallet() — outsiders must not reach in

    public function __construct(string $name, float $opening)
    {
        $this->name = $name;
        $this->wallet = new Wallet($opening);
    }

    public function pay(float $amount): void
    {
        $this->wallet->deduct($amount);
    }

    public function balance(): float
    {
        return $this->wallet->balance();
    }
}

final class Order
{
    public function __construct(
        public readonly string $id,
        public readonly Customer $customer,
        public readonly float $total,
    ) {}
}

final class Checkout
{
    public function collect(Order $order, float $due): void
    {
        $order->customer->pay($due);
    }
}

$ada = new Customer('Ada', 50.00);
$order = new Order('ORD-101', $ada, 12.50);
$checkout = new Checkout();

printf("%s wallet before: $%.2f\n", $ada->name, $ada->balance());
$checkout->collect($order, $order->total);
printf("collected $%.2f for %s\n", $order->total, $order->id);
printf("%s wallet after:  $%.2f  (invariant intact)\n", $ada->name, $ada->balance());
