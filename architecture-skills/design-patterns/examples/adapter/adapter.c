/* Adapter pattern in C.
 *
 * C has no interfaces; polymorphism is emulated with a struct of
 * function pointers (a hand-rolled vtable). The adapter fills that
 * struct with functions that translate the expected interface into
 * calls on the legacy API, converting units along the way.
 */

#include <stdio.h>

/* Target interface the monitoring code expects. */
typedef struct TemperatureSource {
    const char *(*name)(const struct TemperatureSource *self);
    double (*celsius)(const struct TemperatureSource *self);
} TemperatureSource;

/* A modern sensor that natively implements the interface. */
typedef struct {
    TemperatureSource base;
    const char *label;
    double reading_celsius;
} ModernSensor;

static const char *modern_name(const TemperatureSource *self) {
    return ((const ModernSensor *)self)->label;
}

static double modern_celsius(const TemperatureSource *self) {
    return ((const ModernSensor *)self)->reading_celsius;
}

static ModernSensor modern_sensor(const char *label, double celsius) {
    ModernSensor s = {{modern_name, modern_celsius}, label, celsius};
    return s;
}

/* Adaptee: legacy API we cannot change, reports Fahrenheit. */
typedef struct {
    const char *sensor_id;
    double fahrenheit;
} LegacyFahrenheitSensor;

static double legacy_read_fahrenheit(const LegacyFahrenheitSensor *sensor) {
    return sensor->fahrenheit;
}

/* Adapter: implements the interface on top of the legacy sensor. */
typedef struct {
    TemperatureSource base;
    const LegacyFahrenheitSensor *legacy;
} FahrenheitAdapter;

static const char *adapter_name(const TemperatureSource *self) {
    return ((const FahrenheitAdapter *)self)->legacy->sensor_id;
}

static double adapter_celsius(const TemperatureSource *self) {
    const FahrenheitAdapter *a = (const FahrenheitAdapter *)self;
    return (legacy_read_fahrenheit(a->legacy) - 32.0) * 5.0 / 9.0;
}

static FahrenheitAdapter adapt(const LegacyFahrenheitSensor *legacy) {
    FahrenheitAdapter a = {{adapter_name, adapter_celsius}, legacy};
    return a;
}

static void report(const TemperatureSource *sources[], int count) {
    for (int i = 0; i < count; i++) {
        printf("%s: %.1f°C\n", sources[i]->name(sources[i]),
               sources[i]->celsius(sources[i]));
    }
}

int main(void) {
    ModernSensor modern = modern_sensor("server-room", 21.5);
    LegacyFahrenheitSensor legacy = {"warehouse-legacy", 77.0};
    FahrenheitAdapter adapter = adapt(&legacy);

    const TemperatureSource *sources[] = {&modern.base, &adapter.base};
    report(sources, 2);
    return 0;
}
