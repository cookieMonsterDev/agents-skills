// Iterator pattern in C#.
//
// A binary search tree traversed in sorted order. C# builds the pattern
// in as IEnumerable<T>: an iterator method with yield return generates
// the iterator object, so no hand-rolled MoveNext/Current class is
// needed — and LINQ works on the collection for free.

using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class SortedTree : IEnumerable<int>
{
    private sealed class Node
    {
        public int Value;
        public Node? Left, Right;
    }

    private Node? _root;

    public void Add(int value)
    {
        if (_root is null)
        {
            _root = new Node { Value = value };
            return;
        }
        var node = _root;
        while (true)
        {
            if (value < node.Value)
            {
                if (node.Left is null) { node.Left = new Node { Value = value }; return; }
                node = node.Left;
            }
            else
            {
                if (node.Right is null) { node.Right = new Node { Value = value }; return; }
                node = node.Right;
            }
        }
    }

    public IEnumerator<int> GetEnumerator() => Walk(_root).GetEnumerator();

    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();

    private static IEnumerable<int> Walk(Node? node)
    {
        if (node is null)
        {
            yield break;
        }
        foreach (int value in Walk(node.Left)) yield return value;
        yield return node.Value;
        foreach (int value in Walk(node.Right)) yield return value;
    }
}

public static class Program
{
    public static void Main()
    {
        var tree = new SortedTree();
        foreach (int value in new[] { 5, 3, 8, 1, 4, 9, 7 })
        {
            tree.Add(value);
        }

        Console.WriteLine("in order: " + string.Join(" ", tree));
        Console.WriteLine("sum: " + tree.Sum());
        Console.WriteLine("evens: " + string.Join(" ", tree.Where(v => v % 2 == 0)));
    }
}
