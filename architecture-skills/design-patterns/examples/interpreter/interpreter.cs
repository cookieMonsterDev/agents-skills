// Interpreter pattern in C#.
//
// A tiny arithmetic grammar: literals, variables, +, -, *. Records
// implementing a small interface keep the class-per-rule structure
// compact; a sentence is a record tree evaluated against a dictionary
// of variable bindings.

using System;
using System.Collections.Generic;

public interface IExpr
{
    int Interpret(IReadOnlyDictionary<string, int> context);
}

public sealed record Literal(int Value) : IExpr
{
    public int Interpret(IReadOnlyDictionary<string, int> context) => Value;
}

public sealed record Variable(string Name) : IExpr
{
    public int Interpret(IReadOnlyDictionary<string, int> context) => context[Name];
}

public sealed record Add(IExpr Left, IExpr Right) : IExpr
{
    public int Interpret(IReadOnlyDictionary<string, int> context)
        => Left.Interpret(context) + Right.Interpret(context);
}

public sealed record Sub(IExpr Left, IExpr Right) : IExpr
{
    public int Interpret(IReadOnlyDictionary<string, int> context)
        => Left.Interpret(context) - Right.Interpret(context);
}

public sealed record Mul(IExpr Left, IExpr Right) : IExpr
{
    public int Interpret(IReadOnlyDictionary<string, int> context)
        => Left.Interpret(context) * Right.Interpret(context);
}

public static class Program
{
    public static void Main()
    {
        // (x + y) * 2 - z
        IExpr expression = new Sub(
            new Mul(new Add(new Variable("x"), new Variable("y")), new Literal(2)),
            new Variable("z"));

        var first = new Dictionary<string, int> { ["x"] = 6, ["y"] = 2, ["z"] = 3 };
        var second = new Dictionary<string, int> { ["x"] = 1, ["y"] = 1, ["z"] = 10 };

        Console.WriteLine($"(x + y) * 2 - z with x=6 y=2 z=3   = {expression.Interpret(first)}");
        Console.WriteLine($"(x + y) * 2 - z with x=1 y=1 z=10  = {expression.Interpret(second)}");
    }
}
