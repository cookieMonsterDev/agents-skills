// Singleton pattern in C++.
//
// The Meyers singleton: a function-local static is initialized exactly once,
// thread-safely (since C++11), and sidesteps the static-initialization-order
// fiasco. Deleted copy/move operations enforce uniqueness. Prefer passing
// the object in (dependency injection) where feasible; singletons hide
// dependencies and couple tests.

#include <iostream>
#include <map>
#include <string>

class AppConfig {
public:
    // Thread-safe lazy construction on first call.
    static AppConfig& instance() {
        static AppConfig config;
        return config;
    }

    AppConfig(const AppConfig&) = delete;
    AppConfig& operator=(const AppConfig&) = delete;

    const std::string& get(const std::string& key) const { return settings_.at(key); }

private:
    AppConfig() {
        // Stands in for reading a config file once.
        std::cout << "Loading configuration (expensive, happens once)\n";
        settings_ = {
            {"app_name", "InventoryService"},
            {"db_url", "postgres://localhost/inventory"},
            {"log_level", "INFO"},
        };
    }

    std::map<std::string, std::string> settings_;
};

int main() {
    AppConfig& a = AppConfig::instance();
    AppConfig& b = AppConfig::instance();

    std::cout << "same instance: " << (&a == &b ? "true" : "false") << '\n';
    std::cout << "app_name: " << a.get("app_name") << '\n';
    std::cout << "db_url: " << b.get("db_url") << '\n';
    return 0;
}
