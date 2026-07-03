// Abstract Factory pattern in C#.
//
// Interfaces model products and the factory; in real applications the
// concrete factory is usually chosen once and registered in a dependency
// injection container.

using System;

public interface IButton
{
    string Render();
}

public interface ICheckbox
{
    string Render();
}

public sealed class MacButton : IButton
{
    public string Render() => "( OK )  // rounded macOS button";
}

public sealed class MacCheckbox : ICheckbox
{
    public string Render() => "◉ Remember me  // macOS checkbox";
}

public sealed class WindowsButton : IButton
{
    public string Render() => "[ OK ]  // rectangular Windows button";
}

public sealed class WindowsCheckbox : ICheckbox
{
    public string Render() => "[x] Remember me  // Windows checkbox";
}

/// <summary>One creation method per product kind; products always match.</summary>
public interface IWidgetFactory
{
    IButton CreateButton();
    ICheckbox CreateCheckbox();
}

public sealed class MacFactory : IWidgetFactory
{
    public IButton CreateButton() => new MacButton();
    public ICheckbox CreateCheckbox() => new MacCheckbox();
}

public sealed class WindowsFactory : IWidgetFactory
{
    public IButton CreateButton() => new WindowsButton();
    public ICheckbox CreateCheckbox() => new WindowsCheckbox();
}

public static class Program
{
    // Client code: depends only on the abstract factory and products.
    private static void RenderDialog(IWidgetFactory factory)
    {
        Console.WriteLine(factory.CreateButton().Render());
        Console.WriteLine(factory.CreateCheckbox().Render());
    }

    public static void Main()
    {
        Console.WriteLine("-- macOS theme --");
        RenderDialog(new MacFactory());

        Console.WriteLine("-- Windows theme --");
        RenderDialog(new WindowsFactory());
    }
}
