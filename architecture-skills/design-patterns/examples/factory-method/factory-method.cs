// Factory Method pattern in C#.
//
// An abstract creator owns the shared workflow and defers one creation
// step to subclasses. For trivial cases, passing a Func<Transport>
// delegate is the lighter modern alternative.

using System;

public interface ITransport
{
    string Deliver(string cargo);
}

public sealed class Truck : ITransport
{
    public string Deliver(string cargo) => $"Truck delivers {cargo} by road in a box";
}

public sealed class Ship : ITransport
{
    public string Deliver(string cargo) => $"Ship delivers {cargo} by sea in a container";
}

/// <summary>Creator: shared workflow around one overridable creation step.</summary>
public abstract class Logistics
{
    protected abstract ITransport CreateTransport();

    public string PlanDelivery(string cargo)
    {
        ITransport transport = CreateTransport();
        return $"[{GetType().Name}] {transport.Deliver(cargo)}";
    }
}

public sealed class RoadLogistics : Logistics
{
    protected override ITransport CreateTransport() => new Truck();
}

public sealed class SeaLogistics : Logistics
{
    protected override ITransport CreateTransport() => new Ship();
}

public static class Program
{
    public static void Main()
    {
        Logistics[] all = { new RoadLogistics(), new SeaLogistics() };
        foreach (Logistics logistics in all)
        {
            Console.WriteLine(logistics.PlanDelivery("machine parts"));
        }
    }
}
