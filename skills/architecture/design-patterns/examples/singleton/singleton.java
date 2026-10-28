// Singleton pattern in Java.
//
// The initialization-on-demand holder idiom: the JVM guarantees the nested
// class (and thus the instance) is initialized lazily and thread-safely,
// with no locks. A single-element enum is the other standard form. Prefer
// injecting the instance (Spring/Guice singleton scope) where feasible;
// static singletons hide dependencies and leak state between tests.

import java.util.Map;

public class singleton {

    static final class AppConfig {
        private final Map<String, String> settings;

        private AppConfig() {
            // Stands in for reading a config file once.
            System.out.println("Loading configuration (expensive, happens once)");
            settings = Map.of(
                    "app_name", "InventoryService",
                    "db_url", "postgres://localhost/inventory",
                    "log_level", "INFO");
        }

        // Holder is not initialized until getInstance() first runs.
        private static final class Holder {
            static final AppConfig INSTANCE = new AppConfig();
        }

        static AppConfig getInstance() {
            return Holder.INSTANCE;
        }

        String get(String key) {
            return settings.get(key);
        }
    }

    public static void main(String[] args) {
        AppConfig a = AppConfig.getInstance();
        AppConfig b = AppConfig.getInstance();

        System.out.println("same instance: " + (a == b));
        System.out.println("app_name: " + a.get("app_name"));
        System.out.println("db_url: " + b.get("db_url"));
    }
}
