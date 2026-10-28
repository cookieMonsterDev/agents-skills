// Law of Demeter in C#.
//
// order.GetCustomer().GetWallet().Deduct(due) couples checkout to the
// whole object graph. customer.Pay(due) is tell-don't-ask: the customer
// forwards to its wallet and enforces the never-negative rule.

// --- Before (train wreck, sketched): ---
//
// class Checkout {
//     public void Collect(Order order, decimal due) =>
//         order.GetCustomer().GetWallet().Deduct(due);
// }

// --- After: talk only to immediate collaborators ---

sealed class Wallet
{
    private decimal _balance;

    public Wallet(decimal opening)
    {
        if (opening < 0) throw new ArgumentException("opening balance cannot be negative");
        _balance = opening;
    }

    internal void Deduct(decimal amount)
    {
        if (amount <= 0) throw new ArgumentException("payment must be positive");
        if (amount > _balance) throw new ArgumentException("insufficient funds");
        _balance -= amount;
    }

    internal decimal Balance => _balance;
}

sealed class Customer
{
    public string Name { get; }
    private readonly Wallet _wallet; // no public Wallet property

    public Customer(string name, decimal opening)
    {
        Name = name;
        _wallet = new Wallet(opening);
    }

    public void Pay(decimal amount) => _wallet.Deduct(amount);

    public decimal Balance => _wallet.Balance;
}

sealed class Order
{
    public string Id { get; }
    public Customer Customer { get; }
    public decimal Total { get; }

    public Order(string id, Customer customer, decimal total)
    {
        Id = id;
        Customer = customer;
        Total = total;
    }
}

sealed class Checkout
{
    public void Collect(Order order, decimal due) => order.Customer.Pay(due);
}

class Program
{
    static void Main()
    {
        var ada = new Customer("Ada", 50.00m);
        var order = new Order("ORD-101", ada, 12.50m);
        var checkout = new Checkout();

        Console.WriteLine($"{ada.Name} wallet before: ${ada.Balance:F2}");
        checkout.Collect(order, order.Total);
        Console.WriteLine($"collected ${order.Total:F2} for {order.Id}");
        Console.WriteLine($"{ada.Name} wallet after:  ${ada.Balance:F2}  (invariant intact)");
    }
}
