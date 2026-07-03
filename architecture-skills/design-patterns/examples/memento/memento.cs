// Memento pattern in C#.
//
// A record snapshot keeps the memento immutable. Nesting it inside the
// editor with a private constructor means only the originator can create
// or read one; the history just stacks opaque values.

using System;
using System.Collections.Generic;

public sealed class TextEditor
{
    private string _text = "";
    private int _cursor;

    // Memento: creatable and readable only by TextEditor.
    public sealed record Snapshot
    {
        internal string Text { get; }
        internal int Cursor { get; }

        internal Snapshot(string text, int cursor) => (Text, Cursor) = (text, cursor);
    }

    public void Type(string insert)
    {
        _text = _text.Insert(_cursor, insert);
        _cursor += insert.Length;
    }

    public Snapshot Save() => new(_text, _cursor);

    public void Restore(Snapshot s) => (_text, _cursor) = (s.Text, s.Cursor);

    public override string ToString() => $"'{_text}' (cursor at {_cursor})";
}

public sealed class History
{
    private readonly Stack<TextEditor.Snapshot> _snapshots = new();

    public void Push(TextEditor.Snapshot s) => _snapshots.Push(s);

    public bool TryPop(out TextEditor.Snapshot? s) => _snapshots.TryPop(out s);
}

public static class Program
{
    public static void Main()
    {
        var editor = new TextEditor();
        var history = new History();

        editor.Type("Hello");
        history.Push(editor.Save());
        editor.Type(", world");
        history.Push(editor.Save());
        editor.Type("!!!");
        Console.WriteLine($"current: {editor}");

        for (int i = 0; i < 2 && history.TryPop(out var s); i++)
        {
            editor.Restore(s!);
            Console.WriteLine($"undo:    {editor}");
        }
    }
}
