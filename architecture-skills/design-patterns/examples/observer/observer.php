<?php
// Observer pattern in PHP.
//
// PHP ships SplSubject/SplObserver in the standard library, but their
// notify() carries no payload, so real code usually rolls its own with
// closures — as here. subscribe() returns an unsubscribe closure.

declare(strict_types=1);

final class StockTicker
{
    /** @var array<int, Closure(string, float): void> */
    private array $observers = [];
    private int $nextId = 0;

    /** @param Closure(string, float): void $observer */
    public function subscribe(Closure $observer): Closure
    {
        $id = $this->nextId++;
        $this->observers[$id] = $observer;
        return function () use ($id): void {
            unset($this->observers[$id]);
        };
    }

    public function updatePrice(string $symbol, float $price): void
    {
        foreach ($this->observers as $observer) {
            $observer($symbol, $price);
        }
    }
}

final class PriceDisplay
{
    public function __construct(private readonly string $name)
    {
    }

    public function onPrice(string $symbol, float $price): void
    {
        printf("%s: %s is now $%.2f\n", $this->name, $symbol, $price);
    }
}

function makeAlert(string $watched, float $threshold): Closure
{
    return function (string $symbol, float $price) use ($watched, $threshold): void {
        if ($symbol === $watched && $price > $threshold) {
            printf("ALERT: %s crossed $%.2f (now $%.2f)\n", $watched, $threshold, $price);
        }
    };
}

$ticker = new StockTicker();
$display = new PriceDisplay('Lobby display');
$unsubscribe = $ticker->subscribe($display->onPrice(...));
$ticker->subscribe(makeAlert('ACME', 100.0));

$ticker->updatePrice('ACME', 98.5);
$ticker->updatePrice('ACME', 101.25);

$unsubscribe();
$ticker->updatePrice('GLOBEX', 45.0); // only the alert remains
