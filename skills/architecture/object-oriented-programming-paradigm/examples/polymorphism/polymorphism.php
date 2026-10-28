<?php
// Polymorphism in PHP.
//
// PHP works like Java here: an interface is the abstraction and every
// method call dispatches dynamically on the object's class. PHP has no
// generics, so totalArea relies on the interface type check per
// element — the docblock template syntax is convention only.

declare(strict_types=1);

// The abstraction: the only type the client mentions.
interface Shape
{
    public function area(): float;

    public function describe(): string;
}

final class Circle implements Shape
{
    public function __construct(private readonly float $radius) {}

    public function area(): float
    {
        return M_PI * $this->radius ** 2;
    }

    public function describe(): string
    {
        return "circle r={$this->radius}";
    }
}

final class Rectangle implements Shape
{
    public function __construct(
        private readonly float $width,
        private readonly float $height,
    ) {}

    public function area(): float
    {
        return $this->width * $this->height;
    }

    public function describe(): string
    {
        return "rectangle {$this->width}x{$this->height}";
    }
}

final class Triangle implements Shape
{
    public function __construct(
        private readonly float $base,
        private readonly float $height,
    ) {}

    public function area(): float
    {
        return 0.5 * $this->base * $this->height;
    }

    public function describe(): string
    {
        return "triangle b={$this->base} h={$this->height}";
    }
}

/**
 * @param list<Shape> $shapes  (docblock "generics" — convention, not enforced)
 */
function totalArea(array $shapes): float
{
    return array_sum(array_map(fn (Shape $s): float => $s->area(), $shapes));
}

$shapes = [new Circle(1.0), new Rectangle(3.0, 4.0), new Triangle(6.0, 2.0)];

// One call site, three implementations: the object's class decides.
foreach ($shapes as $shape) {
    printf("%18s: area %.2f\n", $shape->describe(), $shape->area());
}

printf("%18s: area %.2f\n", 'total', totalArea($shapes));
