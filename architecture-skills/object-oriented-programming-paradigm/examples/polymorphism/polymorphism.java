// Polymorphism in Java.
//
// All instance methods are virtual by default, so one loop over a
// List<Shape> dispatches to each record's own implementation. The
// generic method totalArea shows the parametric kind, and the two
// overloaded label methods show ad-hoc polymorphism resolved
// statically by the declared argument type.

import java.util.List;

public class polymorphism {

    /** The abstraction: the only type the client mentions. */
    interface Shape {
        double area();
        String describe();
    }

    record Circle(double radius) implements Shape {
        public double area() { return Math.PI * radius * radius; }
        public String describe() { return "circle r=" + radius; }
    }

    record Rectangle(double width, double height) implements Shape {
        public double area() { return width * height; }
        public String describe() { return "rectangle " + width + "x" + height; }
    }

    record Triangle(double base, double height) implements Shape {
        public double area() { return 0.5 * base * height; }
        public String describe() { return "triangle b=" + base + " h=" + height; }
    }

    /** Parametric polymorphism: one method, any list of shapes. */
    static <T extends Shape> double totalArea(List<T> shapes) {
        return shapes.stream().mapToDouble(Shape::area).sum();
    }

    /** Ad-hoc polymorphism: overloads chosen at compile time by the
     *  static argument type — not by the runtime type. */
    static String label(Circle c) { return "round: " + c.describe(); }
    static String label(Shape s)  { return "shape: " + s.describe(); }

    public static void main(String[] args) {
        List<Shape> shapes = List.of(
            new Circle(1.0),
            new Rectangle(3.0, 4.0),
            new Triangle(6.0, 2.0)
        );

        // One call site, three implementations (dynamic dispatch).
        for (Shape shape : shapes) {
            System.out.printf("%22s: area %.2f%n", shape.describe(), shape.area());
        }
        System.out.printf("%22s: area %.2f%n", "total", totalArea(shapes));

        // Overload resolution is static: both variables hold a Circle,
        // but the declared type picks the overload.
        Circle asCircle = new Circle(2.0);
        Shape asShape = asCircle;
        System.out.println(label(asCircle)); // round: ...
        System.out.println(label(asShape));  // shape: ... (same object!)
    }
}
