// Composition over inheritance in C#.
//
// Robot holds two small interfaces and delegates instead of extending a
// base class per movement x weapon combo. Sealed component classes keep
// the parts honest, and a settable property swaps a part at runtime —
// something no subclass can do after construction.

using System;
using System.Collections.Generic;

interface IMoveBehavior
{
    string Move();
}

interface IAttackBehavior
{
    string Attack();
}

// --- Concrete components: one capability each ---

sealed class Treads : IMoveBehavior
{
    public string Move() => "rolls forward on treads";
}

sealed class Rotors : IMoveBehavior
{
    public string Move() => "lifts off on quad rotors";
}

sealed class Turbines : IMoveBehavior
{
    public string Move() => "dives and swims with turbines";
}

sealed class Laser : IAttackBehavior
{
    public string Attack() => "fires a precision laser";
}

sealed class Drill : IAttackBehavior
{
    public string Attack() => "spins up a mining drill";
}

/// <summary>Host: owns its parts and delegates behavior to them.</summary>
sealed class Robot
{
    private readonly string _name;
    private readonly IAttackBehavior _weapon;

    public IMoveBehavior Mover { get; set; }

    public Robot(string name, IMoveBehavior mover, IAttackBehavior weapon)
    {
        _name = name;
        Mover = mover;
        _weapon = weapon;
    }

    public string Perform() => $"{_name,8}: {Mover.Move()} and {_weapon.Attack()}";
}

static class Program
{
    static void Main()
    {
        // Any combination is just wiring — no FlyingDrillRobot subclass needed.
        var squad = new List<Robot>
        {
            new("Scout", new Treads(), new Laser()),
            new("Miner", new Treads(), new Drill()),
            new("Wasp", new Rotors(), new Drill()),   // flying driller
            new("Manta", new Turbines(), new Laser()),
        };

        foreach (var robot in squad)
        {
            Console.WriteLine(robot.Perform());
        }

        // Inheritance fixes behavior at construction; composition swaps it live.
        Console.WriteLine("-- field upgrade: Miner receives rotors --");
        squad[1].Mover = new Rotors();
        Console.WriteLine(squad[1].Perform());
    }
}
