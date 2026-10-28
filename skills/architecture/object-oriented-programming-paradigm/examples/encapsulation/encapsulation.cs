// Encapsulation in C#.
//
// Properties are the idiom: `public decimal Balance { get; private set; }`
// gives public read and class-only write in one line, and leaves room to
// add validation later without breaking callers. The constructor
// establishes the invariant (balance >= 0); Deposit/Withdraw maintain it.

using System;

class BankAccount
{
    public decimal Balance { get; private set; } // public read, private write

    public BankAccount(decimal openingBalance)
    {
        if (openingBalance < 0)
        {
            throw new ArgumentException("opening balance cannot be negative");
        }
        Balance = openingBalance;
    }

    public void Deposit(decimal amount)
    {
        if (amount <= 0)
        {
            throw new ArgumentException("deposit must be positive");
        }
        Balance += amount;
    }

    public void Withdraw(decimal amount)
    {
        if (amount <= 0)
        {
            throw new ArgumentException("withdrawal must be positive");
        }
        if (amount > Balance)
        {
            throw new InvalidOperationException("insufficient funds");
        }
        Balance -= amount;
    }
}

class Program
{
    static void Main()
    {
        var account = new BankAccount(100.00m);

        account.Deposit(50.00m);
        Console.WriteLine($"after deposit:  ${account.Balance:F2}");

        try
        {
            account.Withdraw(250.00m);
        }
        catch (InvalidOperationException err)
        {
            Console.WriteLine($"withdraw $250 rejected: {err.Message}");
        }

        account.Withdraw(30.00m);
        Console.WriteLine($"after withdraw: ${account.Balance:F2}  (invariant intact)");

        // account.Balance = -500m;  // compile error: setter is private
    }
}
