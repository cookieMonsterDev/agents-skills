// Liskov Substitution Principle in Java.
//
// Square-extends-Rectangle is the classic violation. The fix keeps
// Rectangle and Square as separate immutable types behind a Shape interface.

class LiskovSubstitution {

    // --- Violation ---

    static class Rectangle {
        protected double width, height;

        Rectangle(double w, double h) {
            width = w;
            height = h;
        }

        void setWidth(double w) { width = w; }
        void setHeight(double h) { height = h; }
        double area() { return width * height; }
    }

    static final class Square extends Rectangle {
        Square(double side) { super(side, side); }

        @Override void setWidth(double w) { width = height = w; }
        @Override void setHeight(double h) { width = height = h; }
    }

    static double stretchTo4x5(Rectangle r) {
        r.setWidth(4);
        r.setHeight(5);
        return r.area();
    }

    // --- Fix ---

    interface Shape {
        double area();
    }

    record Rect(double width, double height) implements Shape {
        public double area() { return width * height; }
    }

    record Sq(double side) implements Shape {
        public double area() { return side * side; }
    }

    static double totalArea(Shape[] shapes) {
        double sum = 0;
        for (Shape s : shapes) sum += s.area();
        return sum;
    }

    public static void main(String[] args) {
        System.out.println("-- Violation: Square substituted for Rectangle --");
        for (Rectangle rect : new Rectangle[] { new Rectangle(2, 3), new Square(2) }) {
            double got = stretchTo4x5(rect);
            String verdict = got == 20 ? "ok" : "CONTRACT BROKEN";
            System.out.printf("%9s: expected 20, got %g  (%s)%n",
                    rect.getClass().getSimpleName(), got, verdict);
        }

        System.out.println("\n-- Fix: separate types behind Shape --");
        Shape[] shapes = { new Rect(4, 5), new Sq(5) };
        for (Shape shape : shapes) {
            System.out.printf("%9s: area %g%n", shape.getClass().getSimpleName(), shape.area());
        }
        System.out.printf("    total: %g%n", totalArea(shapes));
    }
}
