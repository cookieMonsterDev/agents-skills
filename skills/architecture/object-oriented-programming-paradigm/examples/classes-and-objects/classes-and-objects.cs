// Classes & objects in C#.
//
// C# is class-mandatory like Java, so transfer() lives as a static
// method. Properties (Balance { get; private set; }) replace public
// fields, and a static member holds the per-class account counter.
// Top-level statements form the demo entry point.

using System;

BankAccount alice = new("Alice", 100.00);
BankAccount bob = new("Bob");

alice.Deposit(50.00);
bob.Deposit(20.00);
alice.Withdraw(30.00);

Console.WriteLine(alice); // Bob's balance is untouched
Console.WriteLine(bob);

Bank.Transfer(alice, bob, 40.00);
Console.WriteLine("after transfer:");
Console.WriteLine(alice);
Console.WriteLine(bob);

Console.WriteLine($"accounts opened: {BankAccount.TotalOpened}");

public sealed class BankAccount
{
    // Static member: one counter shared by all instances.
    private static int accountsOpened;

    // Instance state: one copy per object, never shared.
    public string Number { get; }
    public string Owner { get; }
    public double Balance { get; private set; }

    // Constructor: the only way in; if it returns, state is valid.
    public BankAccount(string owner, double openingBalance = 0.0)
    {
        if (openingBalance < 0)
            throw new ArgumentOutOfRangeException(nameof(openingBalance));
        Number = $"ACC-{++accountsOpened:D4}";
        Owner = owner;
        Balance = openingBalance;
    }

    // Instance methods: implicit `this` binds them to one object.
    public void Deposit(double amount)
    {
        if (amount <= 0)
            throw new ArgumentOutOfRangeException(nameof(amount));
        Balance += amount;
    }

    public void Withdraw(double amount)
    {
        if (amount > Balance)
            throw new InvalidOperationException($"{Number}: insufficient funds");
        Balance -= amount;
    }

    // Static property: bound to the class, readable with no instance.
    public static int TotalOpened => accountsOpened;

    public override string ToString() => $"{Number} ({Owner}): ${Balance:F2}";
}

// No free functions in C#: a static method on a utility class is the
// closest fit for behavior coordinating two objects that owns neither.
public static class Bank
{
    public static void Transfer(BankAccount from, BankAccount to, double amount)
    {
        from.Withdraw(amount);
        to.Deposit(amount);
    }
}
