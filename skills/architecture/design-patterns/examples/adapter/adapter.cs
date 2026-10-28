// Adapter pattern in C#.
//
// An object adapter: the adapter implements the target interface and
// delegates to the wrapped legacy instance. System.IO.StreamReader
// (stream -> text) plays the same role in the base class library.

using System;
using System.Collections.Generic;

interface ITemperatureSource
{
    string Name { get; }
    double Celsius { get; }
}

class ModernSensor : ITemperatureSource
{
    public string Name { get; }
    public double Celsius { get; }

    public ModernSensor(string name, double celsius)
    {
        Name = name;
        Celsius = celsius;
    }
}

// Adaptee: third-party class we cannot modify.
class LegacyFahrenheitSensor
{
    public string SensorId { get; }
    private readonly double _fahrenheit;

    public LegacyFahrenheitSensor(string sensorId, double fahrenheit)
    {
        SensorId = sensorId;
        _fahrenheit = fahrenheit;
    }

    public double ReadFahrenheit() => _fahrenheit;
}

class FahrenheitAdapter : ITemperatureSource
{
    private readonly LegacyFahrenheitSensor _legacy;

    public FahrenheitAdapter(LegacyFahrenheitSensor legacy) => _legacy = legacy;

    public string Name => _legacy.SensorId;
    public double Celsius => (_legacy.ReadFahrenheit() - 32.0) * 5.0 / 9.0;
}

class Program
{
    static void Main()
    {
        var sources = new List<ITemperatureSource>
        {
            new ModernSensor("server-room", 21.5),
            new FahrenheitAdapter(new LegacyFahrenheitSensor("warehouse-legacy", 77.0)),
        };
        foreach (var source in sources)
        {
            Console.WriteLine($"{source.Name}: {source.Celsius:F1}°C");
        }
    }
}
