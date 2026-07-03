<?php
// Prototype pattern in PHP.
//
// The pattern is a language feature: the `clone` keyword copies an object,
// and the __clone hook fixes up fields that need a deep copy (object
// properties are otherwise shared between the original and the copy).

declare(strict_types=1);

final class Circle
{
    /** @param list<string> $tags */
    public function __construct(
        public float $x,
        public float $y,
        public readonly float $radius,
        public readonly string $color,
        public array $tags,
    ) {
    }

    public function __clone(): void
    {
        // Arrays already copy by value in PHP; if $tags were an object
        // (e.g. ArrayObject) it would need `clone` here. Shown for shape:
        $this->tags = [...$this->tags];
    }

    public function describe(): string
    {
        return sprintf(
            'Circle r=%.0f %s at (%.0f, %.0f) tags=[%s]',
            $this->radius,
            $this->color,
            $this->x,
            $this->y,
            implode(', ', $this->tags),
        );
    }
}

/** Catalog of pre-configured prototypes, cloned instead of constructed. */
final class ShapeRegistry
{
    /** @var array<string, Circle> */
    private array $prototypes = [];

    public function register(string $name, Circle $prototype): void
    {
        $this->prototypes[$name] = $prototype;
    }

    public function create(string $name): Circle
    {
        return clone $this->prototypes[$name];
    }
}

$registry = new ShapeRegistry();
$registry->register('warning-marker', new Circle(0, 0, 12, 'red', ['alert']));

$first = $registry->create('warning-marker');
$second = $registry->create('warning-marker');
$second->x = 40;
$second->y = 25;
$second->tags[] = 'muted';

echo $first->describe(), PHP_EOL;
echo $second->describe(), PHP_EOL;
echo 'independent copies: ', $first->tags !== $second->tags ? 'true' : 'false', PHP_EOL;
