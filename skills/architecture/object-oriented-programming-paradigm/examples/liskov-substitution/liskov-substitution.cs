// Liskov Substitution Principle in C#.
//
// Square-extends-Rectangle is the classic violation. The fix keeps
// Rectangle and Square as separate immutable types behind a Shape interface.

// --- Violation ---

class Rectangle
{
    protected double Width, Height;

    public Rectangle(double w, double h) { Width = w; Height = h; }
    public virtual void SetWidth(double w) => Width = w;
    public virtual void SetHeight(double h) => Height = h;
    public double Area() => Width * Height;
}

sealed class Square : Rectangle
{
    public Square(double side) : base(side, side) { }
    public override void SetWidth(double w) => Width = Height = w;
    public override void SetHeight(double h) => Width = Height = h;
}

static double StretchTo4x5(Rectangle r)
{
    r.SetWidth(4);
    r.SetHeight(5);
    return r.Area();
}

// --- Fix ---

interface IShape
{
    double Area();
}

readonly record struct Rect(double Width, double Height) : IShape
{
    public double Area() => Width * Height;
}

readonly record struct Sq(double Side) : IShape
{
    public double Area() => Side * Side;
}

static double TotalArea(IEnumerable<IShape> shapes) => shapes.Sum(s => s.Area());

Console.WriteLine("-- Violation: Square substituted for Rectangle --");
foreach (Rectangle rect in new Rectangle[] { new(2, 3), new Square(2) })
{
    double got = StretchTo4x5(rect);
    Console.WriteLine($"{rect.GetType().Name,9}: expected 20, got {got:g}  ({(got == 20 ? "ok" : "CONTRACT BROKEN")})");
}

Console.WriteLine("\n-- Fix: separate types behind Shape --");
IShape[] shapes = [new Rect(4, 5), new Sq(5)];
foreach (var shape in shapes)
    Console.WriteLine($"{shape.GetType().Name,9}: area {shape.Area():g}");
Console.WriteLine($"    total: {TotalArea(shapes):g}");
