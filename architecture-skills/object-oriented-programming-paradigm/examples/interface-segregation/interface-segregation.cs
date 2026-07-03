// Interface Segregation Principle in C#.
//
// A fat IOfficeMachine interface forces SimplePrinter to stub scan()
// and fax() with NotSupportedException. The fix splits IPrinter and
// IScanner so each client depends only on the methods it calls.

using System;

// --- Violation: one fat interface every device must implement ---

public interface IOfficeMachine
{
    void PrintDocument(string path);
    void ScanDocument(string path);
    void FaxDocument(string path);
}

public sealed class SimplePrinter : IOfficeMachine
{
    public void PrintDocument(string path) => Console.WriteLine($"print {path}");

    public void ScanDocument(string path) => throw new NotSupportedException("scan");

    public void FaxDocument(string path) => throw new NotSupportedException("fax");
}

static void RunOfficeJob(IOfficeMachine machine, string path)
{
    machine.PrintDocument(path);
    foreach (var (action, fn) in new (string, Action)[]
             {
                 ("scan", () => machine.ScanDocument(path)),
                 ("fax", () => machine.FaxDocument(path)),
             })
    {
        try { fn(); }
        catch (NotSupportedException) { Console.WriteLine($"{action} attempt: NotSupported"); }
    }
}

// --- Fix: small client-specific interfaces ---

public interface IPrinter
{
    void PrintDocument(string path);
}

public interface IScanner
{
    void ScanDocument(string path);
}

public sealed class BasicPrinter : IPrinter
{
    public void PrintDocument(string path) => Console.WriteLine($"print {path}");
}

public sealed class FlatbedScanner : IScanner
{
    public void ScanDocument(string path) => Console.WriteLine($"scan {path}");
}

public sealed class MultiFunctionDevice : IPrinter, IScanner
{
    public void PrintDocument(string path) => Console.WriteLine($"print {path}");
    public void ScanDocument(string path) => Console.WriteLine($"scan {path}");
}

static void PrintJob(IPrinter printer, string path) => printer.PrintDocument(path);
static void ScanJob(IScanner scanner, string path) => scanner.ScanDocument(path);

public static class Program
{
    public static void Main()
    {
        Console.WriteLine("-- Violation: SimplePrinter forced to stub scan/fax --");
        RunOfficeJob(new SimplePrinter(), "document.pdf");

        Console.WriteLine("\n-- Fix: clients depend only on what they need --");
        PrintJob(new BasicPrinter(), "document.pdf");
        ScanJob(new FlatbedScanner(), "page.tif");
        PrintJob(new MultiFunctionDevice(), "report.pdf");
    }
}
