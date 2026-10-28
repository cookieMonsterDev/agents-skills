// Mediator pattern in C#.
//
// The chat room centralizes routing so users never reference each other.
// Note: in modern C# codebases the same decoupling often appears as
// events or the MediatR library's request/notification handlers.

using System;
using System.Collections.Generic;

public sealed class ChatRoom
{
    private readonly Dictionary<string, User> _users = new();

    public void Register(User user)
    {
        _users[user.Name] = user;
        user.Join(this);
    }

    public void Broadcast(User sender, string text)
    {
        foreach (User user in _users.Values)
        {
            if (user != sender)
            {
                user.Receive(sender.Name, text);
            }
        }
    }

    public void Direct(User sender, string recipient, string text)
    {
        if (_users.TryGetValue(recipient, out User? user))
        {
            user.Receive(sender.Name, $"(dm) {text}");
        }
        else
        {
            sender.Receive("room", $"no such user: {recipient}");
        }
    }
}

public sealed class User
{
    private ChatRoom? _room;

    public User(string name) => Name = name;

    public string Name { get; }

    public void Join(ChatRoom room) => _room = room;

    public void Say(string text) => _room!.Broadcast(this, text);

    public void Dm(string recipient, string text) => _room!.Direct(this, recipient, text);

    public void Receive(string sender, string text) =>
        Console.WriteLine($"[{Name}] {sender}: {text}");
}

public static class Program
{
    public static void Main()
    {
        var room = new ChatRoom();
        var ada = new User("Ada");
        var grace = new User("Grace");
        var alan = new User("Alan");
        room.Register(ada);
        room.Register(grace);
        room.Register(alan);

        ada.Say("Hello, everyone!");
        grace.Dm("Ada", "Hi Ada, got a minute?");
        alan.Dm("Linus", "ping");
    }
}
