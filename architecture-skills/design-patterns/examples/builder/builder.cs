// Builder pattern in C#.
//
// Note: C# object initializers and records with `init` setters cover simple
// cases; use a builder for multi-stage construction with validation.

using System;
using System.Collections.Generic;

// Immutable product.
public sealed record HttpRequest(
    string Method,
    string Url,
    IReadOnlyDictionary<string, string> Headers,
    string? Body,
    double TimeoutSeconds);

public sealed class HttpRequestBuilder
{
    private readonly string _method;
    private readonly string _url;
    private readonly Dictionary<string, string> _headers = new();
    private string? _body;
    private double _timeoutSeconds = 30.0;

    public HttpRequestBuilder(string method, string url)
    {
        _method = method.ToUpperInvariant();
        _url = url;
    }

    public HttpRequestBuilder Header(string name, string value)
    {
        _headers[name] = value;
        return this;
    }

    public HttpRequestBuilder Body(string body)
    {
        _body = body;
        return this;
    }

    public HttpRequestBuilder Timeout(double seconds)
    {
        _timeoutSeconds = seconds;
        return this;
    }

    public HttpRequest Build()
    {
        if (_body is not null && _method is "GET" or "HEAD")
        {
            throw new InvalidOperationException($"{_method} requests cannot have a body");
        }
        return new HttpRequest(_method, _url, new Dictionary<string, string>(_headers), _body, _timeoutSeconds);
    }
}

public static class Program
{
    public static void Main()
    {
        HttpRequest request = new HttpRequestBuilder("POST", "https://api.example.com/users")
            .Header("Content-Type", "application/json")
            .Header("Authorization", "Bearer token123")
            .Body("{\"name\": \"Ada\"}")
            .Timeout(5.0)
            .Build();

        Console.WriteLine($"{request.Method} {request.Url} (timeout {request.TimeoutSeconds}s)");
        foreach (var (name, value) in request.Headers)
        {
            Console.WriteLine($"{name}: {value}");
        }
        Console.WriteLine(request.Body);
    }
}
