<?php
// State pattern in PHP.
//
// One class per state behind a shared interface; transitions assign a
// new state to the machine. PHP 8.1 enums with methods offer a lighter
// alternative when states carry no data.

declare(strict_types=1);

interface MachineState
{
    public function insertCoin(VendingMachine $m): void;
    public function selectItem(VendingMachine $m): void;
}

final class VendingMachine
{
    public MachineState $state;

    public function __construct(public int $stock)
    {
        $this->state = $stock > 0 ? new Idle() : new SoldOut();
    }

    public function insertCoin(): void
    {
        $this->state->insertCoin($this);
    }

    public function selectItem(): void
    {
        $this->state->selectItem($this);
    }
}

final class Idle implements MachineState
{
    public function insertCoin(VendingMachine $m): void
    {
        echo "coin accepted\n";
        $m->state = new HasCoin();
    }

    public function selectItem(VendingMachine $m): void
    {
        echo "insert a coin first\n";
    }
}

final class HasCoin implements MachineState
{
    public function insertCoin(VendingMachine $m): void
    {
        echo "coin already inserted, returning it\n";
    }

    public function selectItem(VendingMachine $m): void
    {
        $m->stock--;
        echo "item dispensed ({$m->stock} left)\n";
        $m->state = $m->stock === 0 ? new SoldOut() : new Idle();
    }
}

final class SoldOut implements MachineState
{
    public function insertCoin(VendingMachine $m): void
    {
        echo "sold out, returning coin\n";
    }

    public function selectItem(VendingMachine $m): void
    {
        echo "sold out\n";
    }
}

$machine = new VendingMachine(2);
$machine->selectItem(); // insert a coin first
$machine->insertCoin();
$machine->insertCoin(); // coin already inserted
$machine->selectItem(); // item dispensed (1 left)
$machine->insertCoin();
$machine->selectItem(); // item dispensed (0 left)
$machine->insertCoin(); // sold out, returning coin
