// Polymorphism in C#.
//
// Interface methods dispatch dynamically, so one loop over a
// List<IShape> calls each record's own implementation. TotalArea is a
// generic method (parametric polymorphism, reified at runtime), and
// the overloaded Label methods show ad-hoc polymorphism resolved
// statically by the declared argument type.

using System;
using System.Collections.Generic;
using System.Linq;

// The abstraction: the only type the client mentions.
interface IShape
{
    double Area();
    string Describe();
}

record Circle(double Radius) : IShape
{
    public double Area() => Math.PI * Radius * Radius;
    public string Describe() => $"circle r={Radius}";
}

record Rectangle(double Width, double Height) : IShape
{
    public double Area() => Width * Height;
    public string Describe() => $"rectangle {Width}x{Height}";
}

record Triangle(double Base, double Height) : IShape
{
    public double Area() => 0.5 * Base * Height;
    public string Describe() => $"triangle b={Base} h={Height}";
}

static class Program
{
    // Parametric polymorphism: one method, any list of shapes.
    static double TotalArea<T>(IReadOnlyList<T> shapes) where T : IShape =>
        shapes.Sum(s => s.Area());

    // Ad-hoc polymorphism: the overload is picked at compile time by
    // the static argument type — not by the runtime type.
    static string Label(Circle c) => $"round: {c.Describe()}";
    static string Label(IShape s) => $"shape: {s.Describe()}";

    static void Main()
    {
        var shapes = new List<IShape>
        {
            new Circle(1.0),
            new Rectangle(3.0, 4.0),
            new Triangle(6.0, 2.0),
        };

        // One call site, three implementations (dynamic dispatch).
        foreach (var shape in shapes)
        {
            Console.WriteLine($"{shape.Describe(),22}: area {shape.Area():F2}");
        }
        Console.WriteLine($"{"total",22}: area {TotalArea(shapes):F2}");

        // Overload resolution is static: same object, different overloads.
        Circle asCircle = new Circle(2.0);
        IShape asShape = asCircle;
        Console.WriteLine(Label(asCircle)); // round: ...
        Console.WriteLine(Label(asShape));  // shape: ... (same object!)
    }
}
