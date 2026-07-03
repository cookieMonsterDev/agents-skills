// Flyweight pattern in C#.
//
// string.Intern is the built-in example of this pattern. Here a
// Dictionary-backed factory shares immutable TreeType records among
// many Tree contexts; records give value equality and immutability
// for free.

using System;
using System.Collections.Generic;

// Flyweight: immutable intrinsic state shared by many trees.
public sealed record TreeType(string Name, string Color)
{
    public void Draw(int x, int y) => Console.WriteLine($"{Color} {Name} at ({x}, {y})");
}

public sealed class TreeTypeFactory
{
    private readonly Dictionary<string, TreeType> _cache = new();

    public TreeType Get(string name, string color)
    {
        string key = $"{name}/{color}";
        if (!_cache.TryGetValue(key, out TreeType? type))
        {
            type = new TreeType(name, color);
            _cache[key] = type;
        }
        return type;
    }

    public int Count => _cache.Count;
}

// Context: extrinsic state plus a reference to the shared flyweight.
public sealed record Tree(int X, int Y, TreeType Kind)
{
    public void Draw() => Kind.Draw(X, Y);
}

public static class Program
{
    public static void Main()
    {
        var factory = new TreeTypeFactory();
        var forest = new List<Tree>
        {
            new(1, 1, factory.Get("oak", "green")),
            new(2, 4, factory.Get("pine", "dark green")),
            new(5, 2, factory.Get("oak", "green")),
            new(6, 6, factory.Get("birch", "light green")),
            new(8, 3, factory.Get("pine", "dark green")),
            new(9, 9, factory.Get("oak", "green")),
        };

        foreach (Tree tree in forest)
        {
            tree.Draw();
        }

        Console.WriteLine($"trees planted: {forest.Count}, tree types in memory: {factory.Count}");
    }
}
