// Prototype pattern in C#.
//
// Records make the pattern a language feature: `with` expressions produce
// nondestructive copies. Reference-typed members are still shared by the
// default copy, so a Clone method deep-copies them explicitly.

using System;
using System.Collections.Generic;

public sealed record Circle(double X, double Y, double Radius, string Color, List<string> Tags)
{
    // `with` copies references, so Tags would be aliased; Clone deep-copies it.
    public Circle Clone() => this with { Tags = new List<string>(Tags) };

    public string Describe() =>
        $"Circle r={Radius} {Color} at ({X}, {Y}) tags=[{string.Join(", ", Tags)}]";
}

/// <summary>Catalog of pre-configured prototypes, cloned instead of constructed.</summary>
public sealed class ShapeRegistry
{
    private readonly Dictionary<string, Circle> _prototypes = new();

    public void Register(string name, Circle prototypeShape) => _prototypes[name] = prototypeShape;

    public Circle Create(string name) => _prototypes[name].Clone();
}

public static class Program
{
    public static void Main()
    {
        var registry = new ShapeRegistry();
        registry.Register("warning-marker", new Circle(0, 0, 12, "red", new List<string> { "alert" }));

        Circle first = registry.Create("warning-marker");
        Circle second = registry.Create("warning-marker") with { X = 40, Y = 25 };
        second.Tags.Add("muted");

        Console.WriteLine(first.Describe());
        Console.WriteLine(second.Describe());
        Console.WriteLine($"independent copies: {!ReferenceEquals(first.Tags, second.Tags)}");
    }
}
