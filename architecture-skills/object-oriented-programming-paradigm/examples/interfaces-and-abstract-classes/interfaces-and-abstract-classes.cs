// Interfaces & abstract classes in C#.
//
// An interface is a pure contract; an abstract class mixes implemented
// and abstract members. TabularExporter captures shared line-assembly
// logic once; JsonExporter satisfies the contract directly.

using System.Text;

record Metric(string Name, double Value);

interface IExporter
{
    string ContentType { get; }
    string ExportAll(IReadOnlyList<Metric> metrics);

    string FileName() => "report." + ContentType.Split('/').Last();
}

abstract class TabularExporter : IExporter
{
    public abstract string ContentType { get; }

    public string ExportAll(IReadOnlyList<Metric> metrics)
    {
        var lines = new List<string> { Header() };
        lines.AddRange(metrics.Select(Row));
        lines.Add($"# {metrics.Count} records");
        return string.Join('\n', lines);
    }

    protected abstract string Header();
    protected abstract string Row(Metric metric);
}

sealed class CsvExporter : TabularExporter
{
    public override string ContentType => "text/csv";
    protected override string Header() => "name,value";
    protected override string Row(Metric m) => $"{m.Name},{m.Value:F2}";
}

sealed class JsonExporter : IExporter
{
    public string ContentType => "application/json";

    public string ExportAll(IReadOnlyList<Metric> metrics)
    {
        var entries = string.Join(", ",
            metrics.Select(m => $"{{\"name\": \"{m.Name}\", \"value\": {m.Value:F2}}}"));
        return $"[{entries}]";
    }
}

static void Deliver(IExporter exporter, IReadOnlyList<Metric> metrics)
{
    Console.WriteLine($"--- {exporter.ContentType} -> {exporter.FileName()} ---");
    Console.WriteLine(exporter.ExportAll(metrics));
    Console.WriteLine();
}

var metrics = new List<Metric>
{
    new("cpu", 0.93),
    new("memory", 0.67),
    new("disk", 0.41),
};

Deliver(new CsvExporter(), metrics);
Deliver(new JsonExporter(), metrics);
