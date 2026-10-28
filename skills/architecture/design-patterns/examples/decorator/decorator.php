<?php
// Decorator pattern in PHP.
//
// Add-ons wrap another Beverage behind the same interface — the same
// idea as PSR-15 middleware wrapping request handlers.

interface Beverage
{
    public function description(): string;
    public function cost(): float;
}

class Espresso implements Beverage
{
    public function description(): string
    {
        return 'espresso';
    }

    public function cost(): float
    {
        return 2.00;
    }
}

abstract class AddOn implements Beverage
{
    public function __construct(protected Beverage $inner) {}
}

class Milk extends AddOn
{
    public function description(): string
    {
        return $this->inner->description() . ' + milk';
    }

    public function cost(): float
    {
        return $this->inner->cost() + 0.30;
    }
}

class Mocha extends AddOn
{
    public function description(): string
    {
        return $this->inner->description() . ' + mocha';
    }

    public function cost(): float
    {
        return $this->inner->cost() + 0.50;
    }
}

class WhippedCream extends AddOn
{
    public function description(): string
    {
        return $this->inner->description() . ' + whipped cream';
    }

    public function cost(): float
    {
        return $this->inner->cost() + 0.40;
    }
}

$plain = new Espresso();
$fancy = new WhippedCream(new Mocha(new Milk(new Espresso())));

foreach ([$plain, $fancy] as $drink) {
    printf("%s: $%.2f\n", $drink->description(), $drink->cost());
}
