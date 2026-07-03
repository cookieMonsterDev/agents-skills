// Command pattern in C#.
//
// Text editor with undo: an ICommand-style interface with Execute/Undo,
// concrete commands capturing their own undo state, and a history stack
// as the invoker. For one-shot commands without undo, an Action delegate
// is the lighter idiom (WPF's ICommand is this pattern in the framework).

using System;
using System.Collections.Generic;
using System.Text;

public sealed class Editor // receiver
{
    public StringBuilder Text { get; } = new();
}

public interface ICommand
{
    void Execute();
    void Undo();
}

public sealed class InsertText : ICommand
{
    private readonly Editor _editor;
    private readonly string _text;

    public InsertText(Editor editor, string text)
    {
        _editor = editor;
        _text = text;
    }

    public void Execute() => _editor.Text.Append(_text);

    public void Undo() => _editor.Text.Length -= _text.Length;
}

public sealed class DeleteLast : ICommand
{
    private readonly Editor _editor;
    private readonly int _count;
    private string _deleted = ""; // captured on Execute so Undo can restore it

    public DeleteLast(Editor editor, int count)
    {
        _editor = editor;
        _count = count;
    }

    public void Execute()
    {
        int start = _editor.Text.Length - _count;
        _deleted = _editor.Text.ToString(start, _count);
        _editor.Text.Length = start;
    }

    public void Undo() => _editor.Text.Append(_deleted);
}

public sealed class History // invoker
{
    private readonly Stack<ICommand> _undoStack = new();

    public void Execute(ICommand command)
    {
        command.Execute();
        _undoStack.Push(command);
    }

    public void Undo()
    {
        if (_undoStack.Count > 0)
        {
            _undoStack.Pop().Undo();
        }
    }
}

public static class Program
{
    public static void Main()
    {
        var editor = new Editor();
        var history = new History();

        history.Execute(new InsertText(editor, "Hello"));
        history.Execute(new InsertText(editor, ", world!"));
        history.Execute(new DeleteLast(editor, 1));
        Console.WriteLine($"after edits: \"{editor.Text}\"");

        history.Undo();
        history.Undo();
        Console.WriteLine($"after 2 undos: \"{editor.Text}\"");
    }
}
