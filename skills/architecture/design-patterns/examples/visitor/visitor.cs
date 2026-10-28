// Visitor pattern in C#.
//
// Classic double dispatch: Accept() resolves the concrete shape, the
// Visit overload resolves the operation. Modern C# can instead use
// pattern-matching switch expressions on a sealed hierarchy, which is
// lighter when the shape set is closed; the classic form is shown here.

using System;
using System.Collections.Generic;

public interface IShapeVisitor<out TResult>
{
    TResult Visit(Circle circle);
    TResult Visit(Rectangle rectangle);
    TResult Visit(Triangle triangle);
}

public interface IShape
{
    TResult Accept<TResult>(IShapeVisitor<TResult> visitor);
}

public sealed record Circle(double Radius) : IShape
{
    public TResult Accept<TResult>(IShapeVisitor<TResult> visitor) => visitor.Visit(this);
}

public sealed record Rectangle(double Width, double Height) : IShape
{
    public TResult Accept<TResult>(IShapeVisitor<TResult> visitor) => visitor.Visit(this);
}

public sealed record Triangle(double Base, double Height) : IShape
{
    public TResult Accept<TResult>(IShapeVisitor<TResult> visitor) => visitor.Visit(this);
}

public sealed class AreaVisitor : IShapeVisitor<double>
{
    public double Visit(Circle c) => Math.PI * c.Radius * c.Radius;
    public double Visit(Rectangle r) => r.Width * r.Height;
    public double Visit(Triangle t) => 0.5 * t.Base * t.Height;
}

public sealed class SvgExportVisitor : IShapeVisitor<string>
{
    public string Visit(Circle c) => $"<circle r=\"{c.Radius}\" />";
    public string Visit(Rectangle r) => $"<rect width=\"{r.Width}\" height=\"{r.Height}\" />";
    public string Visit(Triangle t) => $"<polygon points=\"0,{t.Height} {t.Base},{t.Height} 0,0\" />";
}

public static class Program
{
    public static void Main()
    {
        var shapes = new List<IShape> { new Circle(2), new Rectangle(3, 4), new Triangle(6, 2) };
        var area = new AreaVisitor();
        var svg = new SvgExportVisitor();

        double total = 0;
        foreach (var shape in shapes)
        {
            double a = shape.Accept(area);
            Console.WriteLine($"area={a,6:F2}  {shape.Accept(svg)}");
            total += a;
        }
        Console.WriteLine($"total area: {total:F2}");
    }
}
