// Strategy pattern in C#.
//
// C# has both forms: Func<,> delegates/lambdas for stateless strategies
// (Comparison<T> and LINQ selectors are strategies in disguise), and a
// class when the strategy carries state (CarrierRate). The context
// accepts a delegate, so both plug in the same way.

using System;

public sealed record Order(double WeightKg, double DistanceKm);

// A stateful strategy: the negotiated rates are its state.
public sealed class CarrierRate
{
    private readonly double _base;
    private readonly double _perKg;

    public CarrierRate(double baseCost, double perKg)
    {
        _base = baseCost;
        _perKg = perKg;
    }

    public double Cost(Order order) => _base + _perKg * order.WeightKg;
}

// Context: delegates the pricing decision to the current strategy.
public sealed class Checkout
{
    private Func<Order, double> _strategy;

    public Checkout(Func<Order, double> strategy) => _strategy = strategy;

    public void SetStrategy(Func<Order, double> strategy) => _strategy = strategy;

    public double ShippingFor(Order order) => _strategy(order);
}

public static class Program
{
    public static void Main()
    {
        var order = new Order(2.4, 120);

        var strategies = new (string Name, Func<Order, double> Strategy)[]
        {
            ("flat", _ => 5.00),
            ("weight", o => 4.00 + 1.50 * o.WeightKg),
            ("distance", o => 2.00 + 0.05 * o.DistanceKm),
            ("carrier", new CarrierRate(3.00, 2.00).Cost),
        };

        var checkout = new Checkout(strategies[0].Strategy);
        foreach (var (name, s) in strategies)
        {
            checkout.SetStrategy(s);
            Console.WriteLine($"{name,8}: ${checkout.ShippingFor(order):F2}");
        }
    }
}
