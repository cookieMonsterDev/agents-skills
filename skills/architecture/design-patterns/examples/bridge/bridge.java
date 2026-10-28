// Bridge pattern in Java.
//
// Shapes (the abstraction) hold a Renderer (the implementation) so both
// hierarchies grow independently — the same split JDBC uses between the
// API you call and the driver that implements it.
//
// The public class is lowercase so the filename matches the pattern name.

public class bridge {

    interface Renderer {
        String circle(double radius);
        String rectangle(double width, double height);
    }

    static class VectorRenderer implements Renderer {
        public String circle(double radius) {
            return String.format("<circle r=%.1f/>", radius);
        }
        public String rectangle(double width, double height) {
            return String.format("<rect w=%.1f h=%.1f/>", width, height);
        }
    }

    static class RasterRenderer implements Renderer {
        public String circle(double radius) {
            return String.format("pixels for a circle of radius %.1f", radius);
        }
        public String rectangle(double width, double height) {
            return String.format("pixels for a %.1fx%.1f rectangle", width, height);
        }
    }

    abstract static class Shape {
        protected final Renderer renderer;

        Shape(Renderer renderer) {
            this.renderer = renderer;
        }

        abstract String draw();
    }

    static class Circle extends Shape {
        private final double radius;

        Circle(Renderer renderer, double radius) {
            super(renderer);
            this.radius = radius;
        }

        String draw() {
            return renderer.circle(radius);
        }
    }

    static class Rectangle extends Shape {
        private final double width;
        private final double height;

        Rectangle(Renderer renderer, double width, double height) {
            super(renderer);
            this.width = width;
            this.height = height;
        }

        String draw() {
            return renderer.rectangle(width, height);
        }
    }

    public static void main(String[] args) {
        Renderer[] renderers = {new VectorRenderer(), new RasterRenderer()};
        for (Renderer renderer : renderers) {
            Shape[] shapes = {new Circle(renderer, 5.0), new Rectangle(renderer, 3.0, 4.0)};
            for (Shape shape : shapes) {
                System.out.println(shape.draw());
            }
        }
    }
}
