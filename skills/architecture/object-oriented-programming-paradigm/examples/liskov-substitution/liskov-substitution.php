<?php
/**
 * Liskov Substitution Principle in PHP.
 *
 * Square-extends-Rectangle is the classic violation. The fix keeps
 * Rectangle and Square as separate immutable types behind a Shape interface.
 */

declare(strict_types=1);

// --- Violation ---

class Rectangle
{
    public function __construct(
        protected float $width,
        protected float $height,
    ) {}

    public function setWidth(float $w): void { $this->width = $w; }
    public function setHeight(float $h): void { $this->height = $h; }
    public function area(): float { return $this->width * $this->height; }
}

final class Square extends Rectangle
{
    public function __construct(float $side)
    {
        parent::__construct($side, $side);
    }

    public function setWidth(float $w): void { $this->width = $this->height = $w; }
    public function setHeight(float $h): void { $this->width = $this->height = $h; }
}

function stretchTo4x5(Rectangle $rect): float
{
    $rect->setWidth(4);
    $rect->setHeight(5);
    return $rect->area();
}

// --- Fix ---

interface Shape
{
    public function area(): float;
}

final readonly class Rect implements Shape
{
    public function __construct(
        public float $width,
        public float $height,
    ) {}

    public function area(): float { return $this->width * $this->height; }
}

final readonly class Sq implements Shape
{
    public function __construct(public float $side) {}

    public function area(): float { return $this->side * $this->side; }
}

/** @param Shape[] $shapes */
function totalArea(array $shapes): float
{
    return array_sum(array_map(fn(Shape $s) => $s->area(), $shapes));
}

echo "-- Violation: Square substituted for Rectangle --\n";
foreach ([new Rectangle(2, 3), new Square(2)] as $rect) {
    $got = stretchTo4x5($rect);
    $verdict = $got === 20.0 ? 'ok' : 'CONTRACT BROKEN';
    printf("%9s: expected 20, got %g  (%s)\n", $rect::class, $got, $verdict);
}

echo "\n-- Fix: separate types behind Shape --\n";
$shapes = [new Rect(4, 5), new Sq(5)];
foreach ($shapes as $shape) {
    printf("%9s: area %g\n", $shape::class, $shape->area());
}
printf("    total: %g\n", totalArea($shapes));
