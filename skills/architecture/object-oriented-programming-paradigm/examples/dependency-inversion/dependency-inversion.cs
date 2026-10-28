// Dependency Inversion Principle in C#.
//
// OrderService owns the INotifier interface and receives an implementation
// through its constructor — never `new SmtpNotifier(...)`. Main() is the
// composition root that wires ConsoleNotifier or RecordingNotifier.

using System;
using System.Collections.Generic;

public sealed record Order(string Id, string CustomerEmail);

/// <summary>Abstraction owned by policy: shaped to what Place() needs.</summary>
public interface INotifier
{
    void Notify(string email, string message);
}

public sealed class OrderService
{
    private readonly INotifier _notifier;

    public OrderService(INotifier notifier) => _notifier = notifier;

    public void Place(Order order)
    {
        Console.WriteLine($"placed {order.Id} for {order.CustomerEmail}");
        _notifier.Notify(order.CustomerEmail, $"order {order.Id} confirmed");
    }
}

// --- Low-level details: depend on the policy's interface ---

public sealed class ConsoleNotifier : INotifier
{
    public void Notify(string email, string message) =>
        Console.WriteLine($"notify {email}: {message}");
}

public sealed class RecordingNotifier : INotifier
{
    public List<(string Email, string Message)> Sent { get; } = new();

    public void Notify(string email, string message) => Sent.Add((email, message));
}

public static class Program
{
    public static void Main()
    {
        Console.WriteLine("-- ConsoleNotifier at composition root --");
        new OrderService(new ConsoleNotifier())
            .Place(new Order("ORD-001", "alice@example.com"));

        Console.WriteLine("\n-- RecordingNotifier: policy testable without I/O --");
        var recorder = new RecordingNotifier();
        new OrderService(recorder).Place(new Order("ORD-002", "bob@example.com"));
        Console.WriteLine($"{recorder.Sent.Count} notification(s) recorded");
    }
}
