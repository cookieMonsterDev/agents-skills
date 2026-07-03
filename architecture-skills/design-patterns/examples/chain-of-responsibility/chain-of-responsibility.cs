// Chain of Responsibility pattern in C#.
//
// Support ticket escalation: an abstract handler holds the next link;
// each level resolves tickets up to its competence or forwards them.
// ASP.NET Core middleware is the same pattern built into the platform.

using System;
using System.Collections.Generic;

public sealed record Ticket(string Subject, int Severity); // severity 1..4

public abstract class Handler
{
    private Handler? _next;

    public Handler SetNext(Handler handler)
    {
        _next = handler;
        return handler; // enables a.SetNext(b).SetNext(c)
    }

    public virtual void Handle(Ticket ticket)
    {
        if (_next is not null)
        {
            _next.Handle(ticket);
        }
        else
        {
            Console.WriteLine(
                $"UNRESOLVED: \"{ticket.Subject}\" (severity {ticket.Severity}) -> escalate to engineering");
        }
    }
}

public sealed class SupportLevel : Handler
{
    private readonly string _name;
    private readonly int _maxSeverity;

    public SupportLevel(string name, int maxSeverity)
    {
        _name = name;
        _maxSeverity = maxSeverity;
    }

    public override void Handle(Ticket ticket)
    {
        if (ticket.Severity <= _maxSeverity)
        {
            Console.WriteLine($"{_name} resolved \"{ticket.Subject}\" (severity {ticket.Severity})");
        }
        else
        {
            base.Handle(ticket);
        }
    }
}

public static class Program
{
    public static void Main()
    {
        Handler chain = new SupportLevel("Help bot", 1);
        chain.SetNext(new SupportLevel("Frontline agent", 2))
             .SetNext(new SupportLevel("Support manager", 3));

        var tickets = new List<Ticket>
        {
            new("Reset my password", 1),
            new("Invoice shows wrong amount", 2),
            new("Account data corrupted", 3),
            new("Full region outage", 4),
        };

        foreach (var ticket in tickets)
        {
            chain.Handle(ticket);
        }
    }
}
