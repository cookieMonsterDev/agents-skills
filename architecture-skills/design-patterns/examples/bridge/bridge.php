<?php
// Bridge pattern in PHP.
//
// Shapes (the abstraction) hold a Renderer (the implementation) so the
// two hierarchies vary independently.

interface Renderer
{
    public function circle(float $radius): string;
    public function rectangle(float $width, float $height): string;
}

class VectorRenderer implements Renderer
{
    public function circle(float $radius): string
    {
        return sprintf('<circle r=%.1f/>', $radius);
    }

    public function rectangle(float $width, float $height): string
    {
        return sprintf('<rect w=%.1f h=%.1f/>', $width, $height);
    }
}

class RasterRenderer implements Renderer
{
    public function circle(float $radius): string
    {
        return sprintf('pixels for a circle of radius %.1f', $radius);
    }

    public function rectangle(float $width, float $height): string
    {
        return sprintf('pixels for a %.1fx%.1f rectangle', $width, $height);
    }
}

abstract class Shape
{
    public function __construct(protected Renderer $renderer) {}

    abstract public function draw(): string;
}

class Circle extends Shape
{
    public function __construct(Renderer $renderer, private float $radius)
    {
        parent::__construct($renderer);
    }

    public function draw(): string
    {
        return $this->renderer->circle($this->radius);
    }
}

class Rectangle extends Shape
{
    public function __construct(Renderer $renderer, private float $width, private float $height)
    {
        parent::__construct($renderer);
    }

    public function draw(): string
    {
        return $this->renderer->rectangle($this->width, $this->height);
    }
}

foreach ([new VectorRenderer(), new RasterRenderer()] as $renderer) {
    foreach ([new Circle($renderer, 5.0), new Rectangle($renderer, 3.0, 4.0)] as $shape) {
        echo $shape->draw(), PHP_EOL;
    }
}
