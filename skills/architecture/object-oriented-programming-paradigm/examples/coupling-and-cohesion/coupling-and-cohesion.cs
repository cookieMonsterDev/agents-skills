// Coupling and Cohesion in C#.
//
// A god OrderProcessor that computes tax, validates, and ships couples
// three volatile concerns. Split into cohesive collaborators — a tax
// change touches only OrderCalculator.

// --- Before (tightly coupled, sketched): ---
//
// class OrderProcessor {
//     public decimal Process(Order o) {
//         var total = o.Subtotal * 1.20m;  // tax
//         if (total <= 0) throw ...;       // validation
//         Console.WriteLine("shipped");    // shipping
//         return total;
//     }
// }

record Order(string Id, decimal Subtotal);

/// Finance's class: only tax-rule changes touch this file.
sealed class OrderCalculator(decimal TaxRate)
{
    public decimal Total(Order order) => order.Subtotal * (1 + TaxRate);
}

/// Compliance's class: only validation rules change touch this file.
sealed class OrderValidator
{
    public void Validate(Order order, decimal total)
    {
        if (order.Subtotal <= 0) throw new ArgumentException("subtotal must be positive");
        if (total <= 0) throw new ArgumentException("total must be positive");
    }
}

/// Fulfillment's class: only carrier/API changes touch this file.
sealed class OrderShipper
{
    public string Ship(Order order) => $"shipped {order.Id}";
}

/// Thin orchestrator: wires cohesive pieces, owns no domain rules.
sealed class OrderService(OrderCalculator Calculator, OrderValidator Validator, OrderShipper Shipper)
{
    public decimal Process(Order order)
    {
        var total = Calculator.Total(order);
        Validator.Validate(order, total);
        Console.WriteLine(Shipper.Ship(order));
        return total;
    }
}

class Program
{
    static void Main()
    {
        var order = new Order("ORD-204", 80.00m);

        var service = new OrderService(
            new OrderCalculator(0.20m), new OrderValidator(), new OrderShipper());
        var total = service.Process(order);
        Console.WriteLine($"total with 20% tax: ${total:F2}");

        var newRateService = new OrderService(
            new OrderCalculator(0.08m), new OrderValidator(), new OrderShipper());
        var newTotal = newRateService.Process(order);
        Console.WriteLine($"total with 8% tax:  ${newTotal:F2}  (only OrderCalculator changed)");
    }
}
