<?php
// Encapsulation in PHP.
//
// `private` on the property makes the boundary real: outside writes are
// a fatal error, so the only mutations go through deposit/withdraw,
// which enforce the invariant (balance never negative). PHP 8.4 property
// hooks (get/set blocks) can validate on assignment; a plain private
// property plus methods stays the most common form.

declare(strict_types=1);

final class BankAccount
{
    private float $balance; // only this class's methods may touch it

    public function __construct(float $openingBalance = 0.0)
    {
        if ($openingBalance < 0) {
            throw new InvalidArgumentException('opening balance cannot be negative');
        }
        $this->balance = $openingBalance;
    }

    public function balance(): float
    {
        return $this->balance; // read access only: no setter exists
    }

    public function deposit(float $amount): void
    {
        if ($amount <= 0) {
            throw new InvalidArgumentException('deposit must be positive');
        }
        $this->balance += $amount;
    }

    public function withdraw(float $amount): void
    {
        if ($amount <= 0) {
            throw new InvalidArgumentException('withdrawal must be positive');
        }
        if ($amount > $this->balance) {
            throw new InvalidArgumentException('insufficient funds');
        }
        $this->balance -= $amount;
    }
}

$account = new BankAccount(100.00);

$account->deposit(50.00);
printf("after deposit:  $%.2f\n", $account->balance());

try {
    $account->withdraw(250.00);
} catch (InvalidArgumentException $err) {
    printf("withdraw \$250 rejected: %s\n", $err->getMessage());
}

$account->withdraw(30.00);
printf("after withdraw: $%.2f  (invariant intact)\n", $account->balance());

// $account->balance = -500;  // fatal error: cannot access private property
