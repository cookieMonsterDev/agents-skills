// Singleton pattern in C#.
//
// Lazy<T> gives thread-safe lazy initialization without hand-rolled
// locking. In real applications, prefer registering a singleton *lifetime*
// in the DI container (services.AddSingleton<AppConfig>()) — the type stays
// a plain class, testable and swappable, and only the wiring says "one".

using System;
using System.Collections.Generic;

public sealed class AppConfig
{
    private static readonly Lazy<AppConfig> _lazy = new(() => new AppConfig());

    public static AppConfig Instance => _lazy.Value;

    private readonly Dictionary<string, string> _settings;

    private AppConfig()
    {
        // Stands in for reading a config file once.
        Console.WriteLine("Loading configuration (expensive, happens once)");
        _settings = new Dictionary<string, string>
        {
            ["app_name"] = "InventoryService",
            ["db_url"] = "postgres://localhost/inventory",
            ["log_level"] = "INFO",
        };
    }

    public string Get(string key) => _settings[key];
}

public static class Program
{
    public static void Main()
    {
        AppConfig a = AppConfig.Instance;
        AppConfig b = AppConfig.Instance;

        Console.WriteLine($"same instance: {ReferenceEquals(a, b)}");
        Console.WriteLine($"app_name: {a.Get("app_name")}");
        Console.WriteLine($"db_url: {b.Get("db_url")}");
    }
}
