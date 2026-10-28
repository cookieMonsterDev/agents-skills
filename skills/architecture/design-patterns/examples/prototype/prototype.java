// Prototype pattern in Java.
//
// java.lang.Cloneable is widely considered broken (shallow default, checked
// exception, no clone() in the interface), so the idiomatic form is a copy
// constructor exposed through a copy() method, as shown here.

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class prototype {

    static final class Circle {
        double x;
        double y;
        final double radius;
        final String color;
        final List<String> tags;

        Circle(double x, double y, double radius, String color, List<String> tags) {
            this.x = x;
            this.y = y;
            this.radius = radius;
            this.color = color;
            this.tags = new ArrayList<>(tags);
        }

        /** Copy constructor: deep-copies mutable fields. */
        Circle(Circle other) {
            this(other.x, other.y, other.radius, other.color, other.tags);
        }

        Circle copy() {
            return new Circle(this);
        }

        String describe() {
            return "Circle r=" + (int) radius + " " + color
                    + " at (" + (int) x + ", " + (int) y + ") tags=" + tags;
        }
    }

    /** Catalog of pre-configured prototypes, cloned instead of constructed. */
    static final class ShapeRegistry {
        private final Map<String, Circle> prototypes = new LinkedHashMap<>();

        void register(String name, Circle prototypeShape) {
            prototypes.put(name, prototypeShape);
        }

        Circle create(String name) {
            return prototypes.get(name).copy();
        }
    }

    public static void main(String[] args) {
        ShapeRegistry registry = new ShapeRegistry();
        registry.register("warning-marker", new Circle(0, 0, 12, "red", List.of("alert")));

        Circle first = registry.create("warning-marker");
        Circle second = registry.create("warning-marker");
        second.x = 40;
        second.y = 25;
        second.tags.add("muted");

        System.out.println(first.describe());
        System.out.println(second.describe());
        System.out.println("independent copies: " + (first.tags != second.tags));
    }
}
