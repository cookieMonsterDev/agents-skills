// Visitor pattern in Java.
//
// Classic double dispatch: accept() resolves the concrete shape, the
// visit overload resolves the operation. Since Java 17+, sealed
// interfaces with pattern-matching switch offer a lighter alternative
// with exhaustiveness checking; the classic form is shown here.

import java.util.List;

public class visitor {

    interface ShapeVisitor<R> {
        R visit(Circle circle);

        R visit(Rectangle rectangle);

        R visit(Triangle triangle);
    }

    interface Shape {
        <R> R accept(ShapeVisitor<R> visitor);
    }

    record Circle(double radius) implements Shape {
        @Override
        public <R> R accept(ShapeVisitor<R> visitor) {
            return visitor.visit(this);
        }
    }

    record Rectangle(double width, double height) implements Shape {
        @Override
        public <R> R accept(ShapeVisitor<R> visitor) {
            return visitor.visit(this);
        }
    }

    record Triangle(double base, double height) implements Shape {
        @Override
        public <R> R accept(ShapeVisitor<R> visitor) {
            return visitor.visit(this);
        }
    }

    static final class AreaVisitor implements ShapeVisitor<Double> {
        @Override
        public Double visit(Circle c) {
            return Math.PI * c.radius() * c.radius();
        }

        @Override
        public Double visit(Rectangle r) {
            return r.width() * r.height();
        }

        @Override
        public Double visit(Triangle t) {
            return 0.5 * t.base() * t.height();
        }
    }

    static final class SvgExportVisitor implements ShapeVisitor<String> {
        @Override
        public String visit(Circle c) {
            return "<circle r=\"%s\" />".formatted(c.radius());
        }

        @Override
        public String visit(Rectangle r) {
            return "<rect width=\"%s\" height=\"%s\" />".formatted(r.width(), r.height());
        }

        @Override
        public String visit(Triangle t) {
            return "<polygon points=\"0,%s %s,%s 0,0\" />".formatted(t.height(), t.base(), t.height());
        }
    }

    public static void main(String[] args) {
        List<Shape> shapes = List.of(new Circle(2), new Rectangle(3, 4), new Triangle(6, 2));
        var area = new AreaVisitor();
        var svg = new SvgExportVisitor();

        double total = 0;
        for (Shape shape : shapes) {
            double a = shape.accept(area);
            System.out.printf("area=%6.2f  %s%n", a, shape.accept(svg));
            total += a;
        }
        System.out.printf("total area: %.2f%n", total);
    }
}
