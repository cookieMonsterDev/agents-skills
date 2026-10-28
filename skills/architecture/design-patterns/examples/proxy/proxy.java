// Proxy pattern in Java (virtual proxy: lazy-loading image).
//
// The classic interface + delegating class form. For proxying arbitrary
// interfaces at runtime, java.lang.reflect.Proxy generates the
// delegation dynamically — the mechanism behind most ORM lazy loading
// and mocking frameworks.

public class proxy {

    interface Image {
        void display();
    }

    /** Real subject: expensive to create. */
    static final class RealImage implements Image {
        private final String filename;

        RealImage(String filename) {
            this.filename = filename;
            System.out.println("Loading " + filename + " from disk (expensive)");
        }

        @Override
        public void display() {
            System.out.println("Displaying " + filename);
        }
    }

    /** Virtual proxy: defers creating RealImage until first use. */
    static final class ImageProxy implements Image {
        private final String filename;
        private RealImage real;

        ImageProxy(String filename) {
            this.filename = filename;
        }

        @Override
        public void display() {
            if (real == null) {
                real = new RealImage(filename);
            }
            real.display();
        }
    }

    public static void main(String[] args) {
        Image holiday = new ImageProxy("holiday.png");
        Image unused = new ImageProxy("unused.png");
        System.out.println("Proxies created; nothing loaded yet");

        holiday.display();
        holiday.display(); // loaded once, displayed twice

        System.out.println("unused.png was never loaded");
    }
}
