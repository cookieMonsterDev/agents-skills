// Adapter pattern in C++.
//
// An object adapter: the adapter holds a reference to the legacy class
// and implements the target interface. C++ also allows a class adapter
// via (private) multiple inheritance, but composition is preferred.

#include <cstdio>
#include <string>
#include <vector>

class TemperatureSource {
public:
    virtual ~TemperatureSource() = default;
    virtual std::string name() const = 0;
    virtual double celsius() const = 0;
};

class ModernSensor : public TemperatureSource {
public:
    ModernSensor(std::string name, double celsius)
        : name_(std::move(name)), celsius_(celsius) {}

    std::string name() const override { return name_; }
    double celsius() const override { return celsius_; }

private:
    std::string name_;
    double celsius_;
};

// Adaptee: third-party class we cannot modify.
class LegacyFahrenheitSensor {
public:
    LegacyFahrenheitSensor(std::string id, double fahrenheit)
        : sensor_id_(std::move(id)), fahrenheit_(fahrenheit) {}

    const std::string& sensorId() const { return sensor_id_; }
    double readFahrenheit() const { return fahrenheit_; }

private:
    std::string sensor_id_;
    double fahrenheit_;
};

class FahrenheitAdapter : public TemperatureSource {
public:
    explicit FahrenheitAdapter(const LegacyFahrenheitSensor& legacy)
        : legacy_(legacy) {}

    std::string name() const override { return legacy_.sensorId(); }
    double celsius() const override {
        return (legacy_.readFahrenheit() - 32.0) * 5.0 / 9.0;
    }

private:
    const LegacyFahrenheitSensor& legacy_;
};

void report(const std::vector<const TemperatureSource*>& sources) {
    for (const auto* source : sources) {
        std::printf("%s: %.1f°C\n", source->name().c_str(), source->celsius());
    }
}

int main() {
    ModernSensor modern("server-room", 21.5);
    LegacyFahrenheitSensor legacy("warehouse-legacy", 77.0);
    FahrenheitAdapter adapter(legacy);

    report({&modern, &adapter});
    return 0;
}
