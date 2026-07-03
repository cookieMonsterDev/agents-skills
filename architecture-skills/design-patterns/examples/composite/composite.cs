// Composite pattern in C#.
//
// Files and directories implement one INode interface, so callers can
// total sizes or print trees without distinguishing leaf from branch —
// the same shape as WPF's visual tree. Node classes carry a "Node"
// suffix to avoid clashing with System.IO.File/Directory.

using System;
using System.Collections.Generic;
using System.Linq;

interface INode
{
    long Size { get; }
    void Print(int indent = 0);
}

class FileNode : INode
{
    private readonly string _name;

    public FileNode(string name, long size)
    {
        _name = name;
        Size = size;
    }

    public long Size { get; }

    public void Print(int indent = 0) =>
        Console.WriteLine($"{new string(' ', indent)}{_name} ({Size} B)");
}

class DirectoryNode : INode
{
    private readonly string _name;
    private readonly List<INode> _children = new();

    public DirectoryNode(string name) => _name = name;

    public DirectoryNode Add(INode child)
    {
        _children.Add(child);
        return this;
    }

    public long Size => _children.Sum(child => child.Size);

    public void Print(int indent = 0)
    {
        Console.WriteLine($"{new string(' ', indent)}{_name}/ ({Size} B)");
        foreach (var child in _children)
        {
            child.Print(indent + 2);
        }
    }
}

class Program
{
    static void Main()
    {
        var project = new DirectoryNode("project")
            .Add(new DirectoryNode("src")
                .Add(new FileNode("main.py", 1200))
                .Add(new FileNode("util.py", 450)))
            .Add(new DirectoryNode("docs")
                .Add(new FileNode("readme.md", 800)))
            .Add(new FileNode(".gitignore", 20));
        project.Print();
    }
}
