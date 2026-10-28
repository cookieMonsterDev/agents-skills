// Abstraction in C#.
//
// The abstraction is an interface (I-prefixed by convention): callers
// see Save/Load and nothing else, while each implementation hides its
// operational detail (a Dictionary vs a file). The client method takes
// INoteStore and runs unchanged when the implementation swaps.

using System;
using System.Collections.Generic;
using System.IO;

// The abstraction: the only surface callers may rely on.
public interface INoteStore
{
    void Save(string key, string text);
    string? Load(string key);
}

// Operational detail: a Dictionary. Callers never see it.
public sealed class MemoryStore : INoteStore
{
    private readonly Dictionary<string, string> _notes = new();

    public void Save(string key, string text) => _notes[key] = text;

    public string? Load(string key) => _notes.GetValueOrDefault(key);
}

// Operational detail: append-only lines in a file, last write wins.
public sealed class FileStore : INoteStore
{
    private readonly string _path;

    public FileStore(string path) => _path = path;

    public void Save(string key, string text) =>
        File.AppendAllText(_path, $"{key}\t{text}\n");

    public string? Load(string key)
    {
        if (!File.Exists(_path)) return null;
        string? found = null;
        foreach (var line in File.ReadAllLines(_path))
        {
            var parts = line.Split('\t', 2);
            if (parts.Length == 2 && parts[0] == key)
            {
                found = parts[1]; // keep scanning: last write wins
            }
        }
        return found;
    }
}

public static class Program
{
    // Client: written once against the abstraction, never edited when
    // the implementation behind it swaps.
    private static void RunSession(INoteStore store)
    {
        store.Save("groceries", "eggs, flour");
        store.Save("groceries", "eggs, flour, milk"); // overwrite
        store.Save("idea", "hide the how, expose the what");
        Console.WriteLine($"  groceries: {store.Load("groceries") ?? "(missing)"}");
        Console.WriteLine($"  idea:      {store.Load("idea") ?? "(missing)"}");
        Console.WriteLine($"  missing:   {store.Load("missing") ?? "(missing)"}");
    }

    public static void Main()
    {
        Console.WriteLine("memory-backed store:");
        RunSession(new MemoryStore());

        const string path = "abstraction_demo.txt";
        Console.WriteLine("file-backed store:");
        RunSession(new FileStore(path));
        File.Delete(path);
    }
}
