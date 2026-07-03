<?php
// Proxy pattern in PHP (virtual proxy: lazy-loading image).
//
// The classic interface + delegating class form. PHP's __call/__get
// magic methods can forward arbitrary access to the real subject
// (Doctrine generates entity proxies this way for lazy loading).

declare(strict_types=1);

interface Image
{
    public function display(): void;
}

/** Real subject: expensive to create. */
final class RealImage implements Image
{
    public function __construct(private readonly string $filename)
    {
        echo "Loading {$filename} from disk (expensive)\n";
    }

    public function display(): void
    {
        echo "Displaying {$this->filename}\n";
    }
}

/** Virtual proxy: defers creating RealImage until first use. */
final class ImageProxy implements Image
{
    private ?RealImage $real = null;

    public function __construct(private readonly string $filename)
    {
    }

    public function display(): void
    {
        $this->real ??= new RealImage($this->filename);
        $this->real->display();
    }
}

$holiday = new ImageProxy('holiday.png');
$unused = new ImageProxy('unused.png');
echo "Proxies created; nothing loaded yet\n";

$holiday->display();
$holiday->display(); // loaded once, displayed twice

echo "unused.png was never loaded\n";
