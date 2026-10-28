<?php
// Classes & objects in PHP.
//
// PHP 8 constructor property promotion declares and assigns instance
// fields directly in the constructor signature; readonly locks them
// after construction. `static` properties/methods are the class-level
// members, and transfer() stays a plain namespaced function because it
// belongs to no single account.

declare(strict_types=1);

final class BankAccount
{
    // Static property: one counter shared by all instances.
    private static int $accountsOpened = 0;

    public readonly string $number;
    private float $balance;

    // Constructor: promotion declares $owner as an instance field.
    public function __construct(
        public readonly string $owner,
        float $openingBalance = 0.0,
    ) {
        if ($openingBalance < 0) {
            throw new InvalidArgumentException('opening balance cannot be negative');
        }
        $this->number = sprintf('ACC-%04d', ++self::$accountsOpened);
        $this->balance = $openingBalance;
    }

    // Instance methods: $this binds them to one object.
    public function deposit(float $amount): void
    {
        if ($amount <= 0) {
            throw new InvalidArgumentException('deposit must be positive');
        }
        $this->balance += $amount;
    }

    public function withdraw(float $amount): void
    {
        if ($amount > $this->balance) {
            throw new RuntimeException("{$this->number}: insufficient funds");
        }
        $this->balance -= $amount;
    }

    public function __toString(): string
    {
        return sprintf('%s (%s): $%.2f', $this->number, $this->owner, $this->balance);
    }

    // Static method: bound to the class, callable with no instance.
    public static function totalOpened(): int
    {
        return self::$accountsOpened;
    }
}

// Free function: coordinates two objects, owns neither.
function transfer(BankAccount $from, BankAccount $to, float $amount): void
{
    $from->withdraw($amount);
    $to->deposit($amount);
}

// Two objects from one blueprint, each with independent state.
$alice = new BankAccount('Alice', 100.0);
$bob = new BankAccount('Bob');

$alice->deposit(50.0);
$bob->deposit(20.0);
$alice->withdraw(30.0);

echo $alice, PHP_EOL; // Bob's balance is untouched
echo $bob, PHP_EOL;

transfer($alice, $bob, 40.0);
echo 'after transfer:', PHP_EOL;
echo $alice, PHP_EOL;
echo $bob, PHP_EOL;

echo 'accounts opened: ', BankAccount::totalOpened(), PHP_EOL;
