// Inheritance in C#.
//
// C# allows a single base class, and methods are non-virtual by
// default: the base must opt in with `virtual` and subclasses override
// with `override` (hiding with `new` is almost always a mistake).
// Manager extends the base rule via base.MonthlyPay(); Contractor is
// `sealed`, closing it to further derivation.

using System;
using System.Collections.Generic;

// Base class: the common payroll contract and default pay rule.
public class Employee
{
    protected string Name { get; }
    protected double BaseSalary { get; }

    public Employee(string name, double baseSalary)
    {
        Name = name;
        BaseSalary = baseSalary;
    }

    public virtual string Role => "employee";

    public virtual double MonthlyPay() => BaseSalary;

    public void PrintPayslip() =>
        Console.WriteLine($"{Name,-8} {Role,-10} ${MonthlyPay(),9:N2}");
}

// Extends the base rule: standard salary plus a per-report bonus.
public class Manager : Employee
{
    private readonly int _directReports;

    public Manager(string name, double baseSalary, int directReports)
        : base(name, baseSalary) => _directReports = directReports;

    public override string Role => "manager";

    // Call the base implementation, then extend it.
    public override double MonthlyPay() =>
        base.MonthlyPay() + 400.00 * _directReports;
}

// Replaces the base rule outright: billed hours, no base salary.
public sealed class Contractor : Employee
{
    private readonly double _hourlyRate;
    private readonly double _hoursBilled;

    public Contractor(string name, double hourlyRate, double hoursBilled)
        : base(name, 0.0)
    {
        _hourlyRate = hourlyRate;
        _hoursBilled = hoursBilled;
    }

    public override string Role => "contractor";

    public override double MonthlyPay() => _hourlyRate * _hoursBilled;
}

public static class Program
{
    public static void Main()
    {
        // Payroll treats everyone as an Employee; dispatch picks the override.
        var staff = new List<Employee>
        {
            new Employee("Ada", 4200.00),
            new Manager("Grace", 6500.00, 5),
            new Contractor("Linus", 95.00, 140.0),
        };

        var total = 0.0;
        foreach (var person in staff)
        {
            person.PrintPayslip();
            total += person.MonthlyPay();
        }
        Console.WriteLine($"{"total",-19} ${total,9:N2}");
    }
}
