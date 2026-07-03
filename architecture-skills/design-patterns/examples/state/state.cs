// State pattern in C#.
//
// Classic class-per-state form; stateless states are shared singletons.
// For simple machines, a switch expression over an enum is often enough
// in modern C# — reach for classes when states carry behavior or data.

using System;

public abstract class MachineState
{
    public abstract void InsertCoin(VendingMachine m);
    public abstract void SelectItem(VendingMachine m);
}

public sealed class VendingMachine
{
    public int Stock { get; set; }
    public MachineState State { get; set; }

    public VendingMachine(int stock)
    {
        Stock = stock;
        State = stock > 0 ? Idle.Instance : SoldOut.Instance;
    }

    public void InsertCoin() => State.InsertCoin(this);
    public void SelectItem() => State.SelectItem(this);
}

public sealed class Idle : MachineState
{
    public static readonly Idle Instance = new();

    public override void InsertCoin(VendingMachine m)
    {
        Console.WriteLine("coin accepted");
        m.State = HasCoin.Instance;
    }

    public override void SelectItem(VendingMachine m) =>
        Console.WriteLine("insert a coin first");
}

public sealed class HasCoin : MachineState
{
    public static readonly HasCoin Instance = new();

    public override void InsertCoin(VendingMachine m) =>
        Console.WriteLine("coin already inserted, returning it");

    public override void SelectItem(VendingMachine m)
    {
        m.Stock--;
        Console.WriteLine($"item dispensed ({m.Stock} left)");
        m.State = m.Stock == 0 ? SoldOut.Instance : Idle.Instance;
    }
}

public sealed class SoldOut : MachineState
{
    public static readonly SoldOut Instance = new();

    public override void InsertCoin(VendingMachine m) =>
        Console.WriteLine("sold out, returning coin");

    public override void SelectItem(VendingMachine m) =>
        Console.WriteLine("sold out");
}

public static class Program
{
    public static void Main()
    {
        var machine = new VendingMachine(2);
        machine.SelectItem();  // insert a coin first
        machine.InsertCoin();
        machine.InsertCoin();  // coin already inserted
        machine.SelectItem();  // item dispensed (1 left)
        machine.InsertCoin();
        machine.SelectItem();  // item dispensed (0 left)
        machine.InsertCoin();  // sold out, returning coin
    }
}
