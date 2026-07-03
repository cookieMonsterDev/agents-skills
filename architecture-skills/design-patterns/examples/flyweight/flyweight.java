// Flyweight pattern in Java.
//
// The JDK uses this pattern itself: Integer.valueOf caches -128..127
// and String interning shares string storage. Here a HashMap-backed
// factory shares immutable TreeType flyweights among many Tree
// contexts.

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class flyweight {

    /** Flyweight: immutable intrinsic state shared by many trees. */
    record TreeType(String name, String color) {
        void draw(int x, int y) {
            System.out.println(color + " " + name + " at (" + x + ", " + y + ")");
        }
    }

    static final class TreeTypeFactory {
        private final Map<String, TreeType> cache = new HashMap<>();

        TreeType get(String name, String color) {
            return cache.computeIfAbsent(name + "/" + color, k -> new TreeType(name, color));
        }

        int size() {
            return cache.size();
        }
    }

    /** Context: extrinsic state plus a reference to the shared flyweight. */
    record Tree(int x, int y, TreeType kind) {
        void draw() {
            kind.draw(x, y);
        }
    }

    public static void main(String[] args) {
        TreeTypeFactory factory = new TreeTypeFactory();
        List<Tree> forest = new ArrayList<>();
        forest.add(new Tree(1, 1, factory.get("oak", "green")));
        forest.add(new Tree(2, 4, factory.get("pine", "dark green")));
        forest.add(new Tree(5, 2, factory.get("oak", "green")));
        forest.add(new Tree(6, 6, factory.get("birch", "light green")));
        forest.add(new Tree(8, 3, factory.get("pine", "dark green")));
        forest.add(new Tree(9, 9, factory.get("oak", "green")));

        for (Tree tree : forest) {
            tree.draw();
        }

        System.out.println("trees planted: " + forest.size()
                + ", tree types in memory: " + factory.size());
    }
}
