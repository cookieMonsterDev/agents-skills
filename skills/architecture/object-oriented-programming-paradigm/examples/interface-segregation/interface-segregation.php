<?php
// Interface Segregation Principle in PHP.
//
// A fat IOfficeMachine interface forces SimplePrinter to stub scanDocument
// and faxDocument with exceptions. The fix splits IPrinter and IScanner
// so each client depends only on the methods it calls.

declare(strict_types=1);

// --- Violation: one fat interface every device must implement ---

interface IOfficeMachine
{
    public function printDocument(string $path): void;

    public function scanDocument(string $path): void;

    public function faxDocument(string $path): void;
}

final class SimplePrinter implements IOfficeMachine
{
    public function printDocument(string $path): void
    {
        echo "print {$path}\n";
    }

    public function scanDocument(string $path): void
    {
        throw new RuntimeException('scan');
    }

    public function faxDocument(string $path): void
    {
        throw new RuntimeException('fax');
    }
}

function runOfficeJob(IOfficeMachine $machine, string $path): void
{
    $machine->printDocument($path);
    foreach (['scan' => 'scanDocument', 'fax' => 'faxDocument'] as $action => $method) {
        try {
            $machine->{$method}($path);
        } catch (RuntimeException) {
            echo "{$action} attempt: NotSupported\n";
        }
    }
}

// --- Fix: small client-specific interfaces ---

interface IPrinter
{
    public function printDocument(string $path): void;
}

interface IScanner
{
    public function scanDocument(string $path): void;
}

final class BasicPrinter implements IPrinter
{
    public function printDocument(string $path): void
    {
        echo "print {$path}\n";
    }
}

final class FlatbedScanner implements IScanner
{
    public function scanDocument(string $path): void
    {
        echo "scan {$path}\n";
    }
}

final class MultiFunctionDevice implements IPrinter, IScanner
{
    public function printDocument(string $path): void
    {
        echo "print {$path}\n";
    }

    public function scanDocument(string $path): void
    {
        echo "scan {$path}\n";
    }
}

function printJob(IPrinter $printer, string $path): void
{
    $printer->printDocument($path);
}

function scanJob(IScanner $scanner, string $path): void
{
    $scanner->scanDocument($path);
}

function main(): void
{
    echo "-- Violation: SimplePrinter forced to stub scan/fax --\n";
    runOfficeJob(new SimplePrinter(), 'document.pdf');

    echo "\n-- Fix: clients depend only on what they need --\n";
    printJob(new BasicPrinter(), 'document.pdf');
    scanJob(new FlatbedScanner(), 'page.tif');
    printJob(new MultiFunctionDevice(), 'report.pdf');
}

main();
