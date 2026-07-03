<?php
// Flyweight pattern in PHP.
//
// PHP copies objects by handle, not by value, so sharing is natural:
// an array-backed factory returns the same immutable (readonly)
// TreeType instance for every repeated species.

declare(strict_types=1);

/** Flyweight: immutable intrinsic state shared by many trees. */
final class TreeType
{
    public function __construct(
        public readonly string $name,
        public readonly string $color,
    ) {
    }

    public function draw(int $x, int $y): void
    {
        echo "{$this->color} {$this->name} at ($x, $y)\n";
    }
}

final class TreeTypeFactory
{
    /** @var array<string, TreeType> */
    private array $cache = [];

    public function get(string $name, string $color): TreeType
    {
        $key = "$name/$color";
        return $this->cache[$key] ??= new TreeType($name, $color);
    }

    public function count(): int
    {
        return count($this->cache);
    }
}

/** Context: extrinsic state plus a reference to the shared flyweight. */
final class Tree
{
    public function __construct(
        public readonly int $x,
        public readonly int $y,
        public readonly TreeType $kind,
    ) {
    }

    public function draw(): void
    {
        $this->kind->draw($this->x, $this->y);
    }
}

$factory = new TreeTypeFactory();
$forest = [
    new Tree(1, 1, $factory->get('oak', 'green')),
    new Tree(2, 4, $factory->get('pine', 'dark green')),
    new Tree(5, 2, $factory->get('oak', 'green')),
    new Tree(6, 6, $factory->get('birch', 'light green')),
    new Tree(8, 3, $factory->get('pine', 'dark green')),
    new Tree(9, 9, $factory->get('oak', 'green')),
];

foreach ($forest as $tree) {
    $tree->draw();
}

echo 'trees planted: ' . count($forest) . ', tree types in memory: ' . $factory->count() . "\n";
