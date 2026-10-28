// Proxy pattern in C# (virtual proxy: lazy-loading image).
//
// The classic interface + delegating class form. Lazy<T> can replace
// the null check for thread-safe lazy creation, and DispatchProxy
// generates delegation for arbitrary interfaces at runtime (the
// mechanism behind many ORM and mocking libraries).

using System;

public interface IImage
{
    void Display();
}

// Real subject: expensive to create.
public sealed class RealImage : IImage
{
    private readonly string _filename;

    public RealImage(string filename)
    {
        _filename = filename;
        Console.WriteLine($"Loading {filename} from disk (expensive)");
    }

    public void Display() => Console.WriteLine($"Displaying {_filename}");
}

// Virtual proxy: defers creating RealImage until first use.
public sealed class ImageProxy : IImage
{
    private readonly Lazy<RealImage> _real;

    public ImageProxy(string filename)
    {
        _real = new Lazy<RealImage>(() => new RealImage(filename));
    }

    public void Display() => _real.Value.Display();
}

public static class Program
{
    public static void Main()
    {
        IImage holiday = new ImageProxy("holiday.png");
        IImage unused = new ImageProxy("unused.png");
        Console.WriteLine("Proxies created; nothing loaded yet");

        holiday.Display();
        holiday.Display(); // loaded once, displayed twice

        Console.WriteLine("unused.png was never loaded");
    }
}
