// Adapter pattern in Java.
//
// An object adapter: the adapter implements the target interface and
// delegates to the wrapped legacy instance. java.io.InputStreamReader
// (bytes -> chars) is a classic adapter in the standard library.
//
// The public class is lowercase so the filename matches the pattern name.

import java.util.List;

public class adapter {

    interface TemperatureSource {
        String name();
        double celsius();
    }

    static class ModernSensor implements TemperatureSource {
        private final String name;
        private final double celsius;

        ModernSensor(String name, double celsius) {
            this.name = name;
            this.celsius = celsius;
        }

        public String name() { return name; }
        public double celsius() { return celsius; }
    }

    /** Adaptee: third-party class we cannot modify. */
    static class LegacyFahrenheitSensor {
        private final String sensorId;
        private final double fahrenheit;

        LegacyFahrenheitSensor(String sensorId, double fahrenheit) {
            this.sensorId = sensorId;
            this.fahrenheit = fahrenheit;
        }

        String sensorId() { return sensorId; }
        double readFahrenheit() { return fahrenheit; }
    }

    static class FahrenheitAdapter implements TemperatureSource {
        private final LegacyFahrenheitSensor legacy;

        FahrenheitAdapter(LegacyFahrenheitSensor legacy) {
            this.legacy = legacy;
        }

        public String name() { return legacy.sensorId(); }
        public double celsius() {
            return (legacy.readFahrenheit() - 32.0) * 5.0 / 9.0;
        }
    }

    public static void main(String[] args) {
        List<TemperatureSource> sources = List.of(
            new ModernSensor("server-room", 21.5),
            new FahrenheitAdapter(new LegacyFahrenheitSensor("warehouse-legacy", 77.0))
        );
        for (TemperatureSource source : sources) {
            System.out.printf("%s: %.1f°C%n", source.name(), source.celsius());
        }
    }
}
