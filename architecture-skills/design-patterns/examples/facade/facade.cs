// Facade pattern in C#.
//
// A plain class composes the subsystem objects and exposes one method
// per use case. The subsystems stay public for callers that need
// fine-grained control.

using System;

public sealed class Amplifier
{
    public void On() => Console.WriteLine("Amplifier: on");
    public void SetVolume(int level) => Console.WriteLine($"Amplifier: volume {level}");
    public void Off() => Console.WriteLine("Amplifier: off");
}

public sealed class Projector
{
    public void On() => Console.WriteLine("Projector: on");
    public void WideScreenMode() => Console.WriteLine("Projector: 16:9 widescreen mode");
    public void Off() => Console.WriteLine("Projector: off");
}

public sealed class StreamingPlayer
{
    public void On() => Console.WriteLine("StreamingPlayer: on");
    public void Play(string movie) => Console.WriteLine($"StreamingPlayer: playing \"{movie}\"");
    public void Stop() => Console.WriteLine("StreamingPlayer: stopped");
    public void Off() => Console.WriteLine("StreamingPlayer: off");
}

public sealed class HomeTheater
{
    private readonly Amplifier _amp;
    private readonly Projector _projector;
    private readonly StreamingPlayer _player;

    public HomeTheater(Amplifier amp, Projector projector, StreamingPlayer player)
    {
        _amp = amp;
        _projector = projector;
        _player = player;
    }

    public void WatchMovie(string movie)
    {
        Console.WriteLine("= Movie night =");
        _amp.On();
        _amp.SetVolume(5);
        _projector.On();
        _projector.WideScreenMode();
        _player.On();
        _player.Play(movie);
    }

    public void EndMovie()
    {
        Console.WriteLine("= Shutting down =");
        _player.Stop();
        _player.Off();
        _projector.Off();
        _amp.Off();
    }
}

public static class Program
{
    public static void Main()
    {
        var theater = new HomeTheater(new Amplifier(), new Projector(), new StreamingPlayer());
        theater.WatchMovie("Inception");
        theater.EndMovie();
    }
}
