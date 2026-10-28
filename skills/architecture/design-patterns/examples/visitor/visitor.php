<?php
// Visitor pattern in PHP.
//
// Classic double dispatch: accept() resolves the concrete shape, the
// visitor method resolves the operation. PHP 8 enums + match cover
// simple closed sets, but for a class hierarchy the visitor interface
// keeps every operation total: adding a shape breaks all visitors at
// once instead of failing silently.

declare(strict_types=1);

interface ShapeVisitor
{
    public function visitCircle(Circle $circle): mixed;

    public function visitRectangle(Rectangle $rectangle): mixed;

    public function visitTriangle(Triangle $triangle): mixed;
}

interface Shape
{
    public function accept(ShapeVisitor $visitor): mixed;
}

final class Circle implements Shape
{
    public function __construct(public readonly float $radius)
    {
    }

    public function accept(ShapeVisitor $visitor): mixed
    {
        return $visitor->visitCircle($this);
    }
}

final class Rectangle implements Shape
{
    public function __construct(
        public readonly float $width,
        public readonly float $height,
    ) {
    }

    public function accept(ShapeVisitor $visitor): mixed
    {
        return $visitor->visitRectangle($this);
    }
}

final class Triangle implements Shape
{
    public function __construct(
        public readonly float $base,
        public readonly float $height,
    ) {
    }

    public function accept(ShapeVisitor $visitor): mixed
    {
        return $visitor->visitTriangle($this);
    }
}

final class AreaVisitor implements ShapeVisitor
{
    public function visitCircle(Circle $c): float
    {
        return M_PI * $c->radius ** 2;
    }

    public function visitRectangle(Rectangle $r): float
    {
        return $r->width * $r->height;
    }

    public function visitTriangle(Triangle $t): float
    {
        return 0.5 * $t->base * $t->height;
    }
}

final class SvgExportVisitor implements ShapeVisitor
{
    public function visitCircle(Circle $c): string
    {
        return sprintf('<circle r="%g" />', $c->radius);
    }

    public function visitRectangle(Rectangle $r): string
    {
        return sprintf('<rect width="%g" height="%g" />', $r->width, $r->height);
    }

    public function visitTriangle(Triangle $t): string
    {
        return sprintf('<polygon points="0,%g %g,%g 0,0" />', $t->height, $t->base, $t->height);
    }
}

$shapes = [new Circle(2), new Rectangle(3, 4), new Triangle(6, 2)];
$area = new AreaVisitor();
$svg = new SvgExportVisitor();

$total = 0.0;
foreach ($shapes as $shape) {
    $a = $shape->accept($area);
    printf("area=%6.2f  %s\n", $a, $shape->accept($svg));
    $total += $a;
}
printf("total area: %.2f\n", $total);
