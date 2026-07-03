<?php
// Template Method pattern in PHP.
//
// The classic form: an abstract class whose final template method fixes
// the skeleton and calls abstract steps that subclasses supply. For
// simple cases modern PHP often prefers passing closures instead of
// subclassing.

declare(strict_types=1);

final class LineItem
{
    public function __construct(
        public readonly string $product,
        public readonly int $units,
        public readonly float $price,
    ) {
    }

    public function subtotal(): float
    {
        return $this->units * $this->price;
    }
}

abstract class SalesReport
{
    /**
     * The template method: final, so the skeleton — iteration and
     * totalling — cannot vary.
     *
     * @param LineItem[] $items
     */
    final public function generate(array $items): string
    {
        $lines = [$this->header()];
        $total = 0.0;
        foreach ($items as $item) {
            $lines[] = $this->row($item);
            $total += $item->subtotal();
        }
        $lines[] = $this->footer($total);

        return implode("\n", $lines);
    }

    abstract protected function header(): string;

    abstract protected function row(LineItem $item): string;

    abstract protected function footer(float $total): string;
}

final class CsvReport extends SalesReport
{
    protected function header(): string
    {
        return 'product,units,price,subtotal';
    }

    protected function row(LineItem $item): string
    {
        return sprintf('%s,%d,%.2f,%.2f', $item->product, $item->units, $item->price, $item->subtotal());
    }

    protected function footer(float $total): string
    {
        return sprintf('total,,,%.2f', $total);
    }
}

final class MarkdownReport extends SalesReport
{
    protected function header(): string
    {
        return "| Product | Units | Subtotal |\n| --- | --- | --- |";
    }

    protected function row(LineItem $item): string
    {
        return sprintf('| %s | %d | $%.2f |', $item->product, $item->units, $item->subtotal());
    }

    protected function footer(float $total): string
    {
        return sprintf("\n**Total: $%.2f**", $total);
    }
}

$items = [
    new LineItem('Keyboard', 2, 80.00),
    new LineItem('Mouse', 1, 25.50),
    new LineItem('Monitor', 3, 210.00),
];

foreach ([new CsvReport(), new MarkdownReport()] as $report) {
    printf("--- %s ---\n%s\n\n", $report::class, $report->generate($items));
}
