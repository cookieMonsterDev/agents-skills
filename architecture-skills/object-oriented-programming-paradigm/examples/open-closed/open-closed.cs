// Open/Closed Principle in C#.
//
// PricingEngine is closed: it iterates registered DiscountRule
// implementations and never names a concrete rule. FlashSale is
// added later as a new class -- zero edits to the engine.

using System;
using System.Collections.Generic;

public sealed record Order(double Subtotal, int ItemCount, bool IsMember);

/// <summary>Extension point: one implementation per business rule.</summary>
public interface IDiscountRule
{
    string Name { get; }
    double Discount(Order order);
}

// --- Extensions: the engine never mentions these types ---

public sealed class BulkDiscount : IDiscountRule
{
    public string Name => "bulk";
    public double Discount(Order o) =>
        o.ItemCount >= 10 ? 0.05 * o.Subtotal : 0.0;
}

public sealed class MemberDiscount : IDiscountRule
{
    public string Name => "member";
    public double Discount(Order o) =>
        o.IsMember ? 0.10 * o.Subtotal : 0.0;
}

/// <summary>Closed core: computes a total over whatever rules it was given.</summary>
public sealed class PricingEngine
{
    private readonly List<IDiscountRule> _rules = new();

    public void Register(IDiscountRule rule) => _rules.Add(rule);

    public double Total(Order order)
    {
        double total = order.Subtotal;
        foreach (var rule in _rules)
        {
            double amount = rule.Discount(order);
            if (amount > 0.0)
                Console.WriteLine($"  {rule.Name,6}: -${amount:F2}");
            total -= amount;
        }
        return total;
    }
}

/// <summary>A NEW rule, written later -- nothing above is touched.</summary>
public sealed class FlashSale : IDiscountRule
{
    private readonly double _amount;
    private readonly double _threshold;

    public FlashSale(double amount, double threshold)
    {
        _amount = amount;
        _threshold = threshold;
    }

    public string Name => "flash";
    public double Discount(Order o) =>
        o.Subtotal > _threshold ? _amount : 0.0;
}

public static class Program
{
    public static void Main()
    {
        var order = new Order(120.00, 12, true);

        var engine = new PricingEngine();
        engine.Register(new BulkDiscount());
        engine.Register(new MemberDiscount());

        Console.WriteLine($"subtotal: ${order.Subtotal:F2}");
        Console.WriteLine($"total:    ${engine.Total(order):F2}");

        Console.WriteLine("-- registering FlashSale: no engine edits --");
        engine.Register(new FlashSale(15.00, 100.00));
        Console.WriteLine($"total:    ${engine.Total(order):F2}");
    }
}
