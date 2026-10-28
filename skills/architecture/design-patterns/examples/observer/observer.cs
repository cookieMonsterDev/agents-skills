// Observer pattern in C#.
//
// C# has the pattern built into the language: events (multicast
// delegates) are the idiomatic form, shown here. The interface-based
// IObservable<T>/IObserver<T> pair exists for reactive pipelines (Rx).

using System;

public sealed class StockTicker
{
    public event Action<string, double>? PriceChanged;

    public void UpdatePrice(string symbol, double price)
    {
        PriceChanged?.Invoke(symbol, price);
    }
}

public sealed class PriceDisplay
{
    private readonly string _name;

    public PriceDisplay(string name) => _name = name;

    public void OnPrice(string symbol, double price) =>
        Console.WriteLine($"{_name}: {symbol} is now ${price:F2}");
}

public static class Program
{
    public static void Main()
    {
        var ticker = new StockTicker();
        var display = new PriceDisplay("Lobby display");

        // Method-group subscription and a lambda subscription side by side.
        ticker.PriceChanged += display.OnPrice;
        ticker.PriceChanged += (symbol, price) =>
        {
            if (symbol == "ACME" && price > 100.0)
            {
                Console.WriteLine($"ALERT: ACME crossed $100.00 (now ${price:F2})");
            }
        };

        ticker.UpdatePrice("ACME", 98.5);
        ticker.UpdatePrice("ACME", 101.25);

        ticker.PriceChanged -= display.OnPrice;
        ticker.UpdatePrice("GLOBEX", 45.0); // only the alert remains
    }
}
