// Decorator pattern in C#.
//
// Add-ons wrap another IBeverage behind the same interface — the same
// shape as System.IO stream wrappers: new GZipStream(new FileStream(...)).

using System;

interface IBeverage
{
    string Description { get; }
    double Cost { get; }
}

class Espresso : IBeverage
{
    public string Description => "espresso";
    public double Cost => 2.00;
}

abstract class AddOn : IBeverage
{
    protected readonly IBeverage Inner;

    protected AddOn(IBeverage inner) => Inner = inner;

    public abstract string Description { get; }
    public abstract double Cost { get; }
}

class Milk : AddOn
{
    public Milk(IBeverage inner) : base(inner) {}
    public override string Description => Inner.Description + " + milk";
    public override double Cost => Inner.Cost + 0.30;
}

class Mocha : AddOn
{
    public Mocha(IBeverage inner) : base(inner) {}
    public override string Description => Inner.Description + " + mocha";
    public override double Cost => Inner.Cost + 0.50;
}

class WhippedCream : AddOn
{
    public WhippedCream(IBeverage inner) : base(inner) {}
    public override string Description => Inner.Description + " + whipped cream";
    public override double Cost => Inner.Cost + 0.40;
}

class Program
{
    static void Main()
    {
        var plain = new Espresso();
        var fancy = new WhippedCream(new Mocha(new Milk(new Espresso())));
        foreach (IBeverage drink in new IBeverage[] { plain, fancy })
        {
            Console.WriteLine($"{drink.Description}: ${drink.Cost:F2}");
        }
    }
}
