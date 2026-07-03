<?php
/**
 * Single Responsibility Principle in PHP.
 *
 * An Invoice that computes totals, formats itself, AND persists itself
 * serves three actors. The refactor gives each actor its own class.
 */

declare(strict_types=1);

final readonly class LineItem
{
    public function __construct(
        public string $description,
        public float $amount,
    ) {}
}

final class Invoice
{
    /** @var list<LineItem> */
    public array $items = [];

    public function __construct(
        public readonly string $id,
        public readonly string $customer,
    ) {}

    public function addItem(string $description, float $amount): void
    {
        $this->items[] = new LineItem($description, $amount);
    }
}

final class InvoiceCalculator
{
    public function __construct(private readonly float $taxRate) {}

    public function total(Invoice $invoice): float
    {
        $subtotal = array_sum(array_map(fn(LineItem $i) => $i->amount, $invoice->items));
        return $subtotal * (1 + $this->taxRate);
    }
}

final class TextInvoiceFormatter
{
    public function format(Invoice $invoice, float $total): string
    {
        $lines = ["Invoice {$invoice->id} for {$invoice->customer}"];
        foreach ($invoice->items as $item) {
            $lines[] = sprintf('  %-12s $%8.2f', $item->description, $item->amount);
        }
        $lines[] = sprintf('  %-12s $%8.2f', 'TOTAL', $total);
        return implode(PHP_EOL, $lines);
    }
}

final class InMemoryInvoiceRepository
{
    /** @var array<string, Invoice> */
    private array $rows = [];

    public function save(Invoice $invoice): void
    {
        $this->rows[$invoice->id] = $invoice;
    }

    public function count(): int
    {
        return count($this->rows);
    }
}

$invoice = new Invoice('INV-042', 'ACME Corp');
$invoice->addItem('Consulting', 1200.00);
$invoice->addItem('Hosting', 90.00);

$calculator = new InvoiceCalculator(0.20);
$formatter = new TextInvoiceFormatter();
$repository = new InMemoryInvoiceRepository();

$total = $calculator->total($invoice);
echo $formatter->format($invoice, $total), PHP_EOL;

$repository->save($invoice);
printf("saved %s (%d record(s) stored)\n", $invoice->id, $repository->count());
