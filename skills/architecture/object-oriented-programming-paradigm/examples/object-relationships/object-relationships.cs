// Object relationships in C#.
//
// The GC erases the memory-level distinction — every field is a reference.
// Composition means the whole constructs the part and disposes it in Close();
// aggregation means the part arrives via constructor and is left alone at
// teardown. IDisposable's rule ("dispose only what you created") is exactly
// the composition/aggregation line.

using System;
using System.Collections.Generic;
using System.Linq;

record Book(string Title);

sealed class Library
{
    private readonly List<Book> _books;

    public Library(IEnumerable<Book> books) => _books = new List<Book>(books);

    public Book? Lookup(string title) =>
        _books.FirstOrDefault(b => b.Title == title);
}

sealed class Professor
{
    public string Name { get; }

    public Professor(string name) => Name = name;

    // Association: library is a method parameter, not a stored field.
    public string LookupBook(Library library, string title)
    {
        var book = library.Lookup(title);
        return book is null
            ? $"{Name}: '{title}' not in catalog"
            : $"{Name} looked up '{book.Title}' in the library";
    }
}

record Course(string Title);

sealed class Department : IDisposable
{
    private readonly string _name;
    private readonly List<Professor> _professors; // aggregation: injected
    private readonly List<Course> _courses = new(); // composition: created here
    private bool _disposed;

    public Department(string name, IEnumerable<Professor> professors)
    {
        _name = name;
        _professors = new List<Professor>(professors);
    }

    public void AddCourse(string title) => _courses.Add(new Course(title));

    public void PrintRoster()
    {
        Console.Write($"{_name} roster:");
        foreach (var p in _professors)
        {
            Console.Write($" {p.Name}");
        }
        Console.WriteLine();
    }

    public void PrintCourses()
    {
        if (_courses.Count == 0)
        {
            Console.WriteLine($"{_name} courses: (none)");
            return;
        }
        Console.Write($"{_name} courses:");
        foreach (var c in _courses)
        {
            Console.Write($" {c.Title}");
        }
        Console.WriteLine();
    }

    public void Dissolve()
    {
        _professors.Clear(); // drop references — never dispose professors
        _courses.Clear();    // composed parts die with the whole
    }

    public void Dispose()
    {
        if (_disposed) return;
        Dissolve();
        _disposed = true;
    }
}

class Program
{
    static void Main()
    {
        var library = new Library(new[]
        {
            new Book("Algorithms"),
            new Book("Calculus")
        });

        var alice = new Professor("Dr. Alice");
        var bob = new Professor("Dr. Bob");

        using var cs = new Department("Computer Science", new[] { alice, bob });
        cs.AddCourse("Algorithms");
        cs.AddCourse("Data Structures");

        var math = new Department("Mathematics", new[] { alice });
        math.AddCourse("Calculus");

        Console.WriteLine("=== Association (uses-a) ===");
        Console.WriteLine(alice.LookupBook(library, "Algorithms"));

        Console.WriteLine("\n=== Aggregation (has-a) ===");
        cs.PrintRoster();
        math.PrintRoster();
        cs.Dissolve();
        Console.WriteLine($"After dissolving CS — Alice still exists: {alice.Name}");
        math.PrintRoster();

        Console.WriteLine("\n=== Composition (owns-a) ===");
        math.PrintCourses();
        math.Dissolve();
        math.PrintCourses();
    }
}
