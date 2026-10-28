<?php
/**
 * Interfaces & abstract classes in PHP.
 *
 * An interface is a pure contract; an abstract class mixes implemented
 * and abstract members. TabularExporter captures shared line-assembly
 * logic once; JsonExporter satisfies the contract directly.
 */

declare(strict_types=1);

final readonly class Metric
{
    public function __construct(
        public string $name,
        public float $value,
    ) {}
}

interface Exporter
{
    public function contentType(): string;
    public function exportAll(array $metrics): string;

    public function fileName(): string
    {
        $ct = $this->contentType();
        return 'report.' . substr($ct, strrpos($ct, '/') + 1);
    }
}

abstract class TabularExporter implements Exporter
{
    public function exportAll(array $metrics): string
    {
        $lines = [$this->header()];
        foreach ($metrics as $metric) {
            $lines[] = $this->row($metric);
        }
        $lines[] = '# ' . count($metrics) . ' records';
        return implode("\n", $lines);
    }

    abstract protected function header(): string;
    abstract protected function row(Metric $metric): string;
}

final class CsvExporter extends TabularExporter
{
    public function contentType(): string { return 'text/csv'; }
    protected function header(): string { return 'name,value'; }
    protected function row(Metric $m): string
    {
        return sprintf('%s,%.2f', $m->name, $m->value);
    }
}

final class JsonExporter implements Exporter
{
    public function contentType(): string { return 'application/json'; }

    public function exportAll(array $metrics): string
    {
        $entries = array_map(
            fn(Metric $m) => sprintf('{"name": "%s", "value": %.2f}', $m->name, $m->value),
            $metrics
        );
        return '[' . implode(', ', $entries) . ']';
    }
}

function deliver(Exporter $exporter, array $metrics): void
{
    echo "--- {$exporter->contentType()} -> {$exporter->fileName()} ---\n";
    echo $exporter->exportAll($metrics), "\n\n";
}

$metrics = [
    new Metric('cpu', 0.93),
    new Metric('memory', 0.67),
    new Metric('disk', 0.41),
];

deliver(new CsvExporter(), $metrics);
deliver(new JsonExporter(), $metrics);
