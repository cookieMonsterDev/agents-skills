// Bridge pattern in C#.
//
// Shapes (the abstraction) hold an IRenderer (the implementation) so
// both hierarchies grow independently — the same split ADO.NET uses
// between DbConnection and each provider's implementation.

using System;

interface IRenderer
{
    string Circle(double radius);
    string Rectangle(double width, double height);
}

class VectorRenderer : IRenderer
{
    public string Circle(double radius) => $"<circle r={radius:F1}/>";
    public string Rectangle(double width, double height) => $"<rect w={width:F1} h={height:F1}/>";
}

class RasterRenderer : IRenderer
{
    public string Circle(double radius) => $"pixels for a circle of radius {radius:F1}";
    public string Rectangle(double width, double height) => $"pixels for a {width:F1}x{height:F1} rectangle";
}

abstract class Shape
{
    protected readonly IRenderer Renderer;

    protected Shape(IRenderer renderer) => Renderer = renderer;

    public abstract string Draw();
}

class Circle : Shape
{
    private readonly double _radius;

    public Circle(IRenderer renderer, double radius) : base(renderer) => _radius = radius;

    public override string Draw() => Renderer.Circle(_radius);
}

class Rectangle : Shape
{
    private readonly double _width;
    private readonly double _height;

    public Rectangle(IRenderer renderer, double width, double height) : base(renderer)
    {
        _width = width;
        _height = height;
    }

    public override string Draw() => Renderer.Rectangle(_width, _height);
}

class Program
{
    static void Main()
    {
        var renderers = new IRenderer[] { new VectorRenderer(), new RasterRenderer() };
        foreach (var renderer in renderers)
        {
            var shapes = new Shape[] { new Circle(renderer, 5.0), new Rectangle(renderer, 3.0, 4.0) };
            foreach (var shape in shapes)
            {
                Console.WriteLine(shape.Draw());
            }
        }
    }
}
