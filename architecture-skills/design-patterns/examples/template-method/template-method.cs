// Template Method pattern in C#.
//
// An abstract class with a non-virtual template method and abstract
// steps (compare ASP.NET's middleware/lifecycle hooks). C# code often
// prefers composition — injecting Func<> steps — over inheritance; the
// classic inheritance form is shown here.

using System;
using System.Collections.Generic;
using System.Text;

public sealed record LineItem(string Product, int Units, double Price)
{
    public double Subtotal => Units * Price;
}

public abstract class SalesReport
{
    // The template method: non-virtual, so the skeleton cannot vary.
    public string Generate(IReadOnlyList<LineItem> items)
    {
        var outText = new StringBuilder(Header()).Append('\n');
        double total = 0;
        foreach (var item in items)
        {
            outText.Append(Row(item)).Append('\n');
            total += item.Subtotal;
        }
        return outText.Append(Footer(total)).ToString();
    }

    protected abstract string Header();
    protected abstract string Row(LineItem item);
    protected abstract string Footer(double total);
}

public sealed class CsvReport : SalesReport
{
    protected override string Header() => "product,units,price,subtotal";

    protected override string Row(LineItem item) =>
        $"{item.Product},{item.Units},{item.Price:F2},{item.Subtotal:F2}";

    protected override string Footer(double total) => $"total,,,{total:F2}";
}

public sealed class MarkdownReport : SalesReport
{
    protected override string Header() =>
        "| Product | Units | Subtotal |\n| --- | --- | --- |";

    protected override string Row(LineItem item) =>
        $"| {item.Product} | {item.Units} | ${item.Subtotal:F2} |";

    protected override string Footer(double total) => $"\n**Total: ${total:F2}**";
}

public static class Program
{
    public static void Main()
    {
        var items = new List<LineItem>
        {
            new("Keyboard", 2, 80.00),
            new("Mouse", 1, 25.50),
            new("Monitor", 3, 210.00),
        };

        foreach (SalesReport report in new SalesReport[] { new CsvReport(), new MarkdownReport() })
        {
            Console.WriteLine($"--- {report.GetType().Name} ---");
            Console.WriteLine(report.Generate(items));
            Console.WriteLine();
        }
    }
}
