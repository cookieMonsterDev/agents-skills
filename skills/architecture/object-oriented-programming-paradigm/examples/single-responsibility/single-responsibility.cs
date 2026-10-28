// Single Responsibility Principle in C#.
//
// A god Invoice would compute totals, format itself, and persist
// itself — three actors sharing one file. The refactor gives each
// actor its own class; in a real project each lives in its own file
// under its own namespace, and the DI container wires them at the
// composition root.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

// --- Before (god class, sketched): three reasons to change ---
//
// class Invoice {
//     decimal Total()   { ... }  // changes when FINANCE changes tax
//     string ToText()   { ... }  // changes when LAYOUT changes
//     void SaveToDb()   { ... }  // changes when STORAGE changes
// }

// --- After: one collaborator per actor ---

public sealed record LineItem(string Description, decimal Amount);

/// <summary>Domain object: owns the data, nothing else.</summary>
public sealed class Invoice
{
    public string Id { get; }
    public string Customer { get; }
    public List<LineItem> Items { get; } = new();

    public Invoice(string id, string customer) => (Id, Customer) = (id, customer);

    public void AddItem(string description, decimal amount) =>
        Items.Add(new LineItem(description, amount));
}

/// <summary>Finance's class: only tax-rule changes touch this file.</summary>
public sealed class InvoiceCalculator
{
    private readonly decimal _taxRate;

    public InvoiceCalculator(decimal taxRate) => _taxRate = taxRate;

    public decimal Total(Invoice invoice) =>
        invoice.Items.Sum(i => i.Amount) * (1 + _taxRate);
}

/// <summary>Presentation's class: only layout changes touch this file.</summary>
public sealed class TextInvoiceFormatter
{
    public string Format(Invoice invoice, decimal total)
    {
        var sb = new StringBuilder($"Invoice {invoice.Id} for {invoice.Customer}");
        foreach (var item in invoice.Items)
        {
            sb.Append($"\n  {item.Description,-12} ${item.Amount,8:F2}");
        }
        return sb.Append($"\n  {"TOTAL",-12} ${total,8:F2}").ToString();
    }
}

/// <summary>Ops' class: only storage changes touch this file.</summary>
public sealed class InMemoryInvoiceRepository
{
    private readonly Dictionary<string, Invoice> _rows = new();

    public void Save(Invoice invoice) => _rows[invoice.Id] = invoice;

    public int Count => _rows.Count;
}

public static class Program
{
    public static void Main()
    {
        var invoice = new Invoice("INV-042", "ACME Corp");
        invoice.AddItem("Consulting", 1200.00m);
        invoice.AddItem("Hosting", 90.00m);

        var calculator = new InvoiceCalculator(0.20m);
        var formatter = new TextInvoiceFormatter();
        var repository = new InMemoryInvoiceRepository();

        decimal total = calculator.Total(invoice);
        Console.WriteLine(formatter.Format(invoice, total));

        repository.Save(invoice);
        Console.WriteLine($"saved {invoice.Id} ({repository.Count} record(s) stored)");
    }
}
