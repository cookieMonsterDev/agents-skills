// Interfaces & abstract classes in C++.
//
// An interface is a class with only pure virtual functions and a
// virtual destructor; an abstract class mixes implemented and pure
// virtual members. A non-virtual method written in terms of the pure
// virtuals (fileName) plays the default-method role. `export` is a
// C++ keyword, hence exportAll.

#include <iostream>
#include <sstream>
#include <string>
#include <vector>

struct Metric {
    std::string name;
    double value;
};

// The interface: a pure contract.
class Exporter {
public:
    virtual ~Exporter() = default;
    virtual std::string contentType() const = 0;
    virtual std::string exportAll(const std::vector<Metric>& metrics) const = 0;

    // "Default method": derived purely from the contract itself.
    std::string fileName() const {
        const std::string ct = contentType();
        return "report." + ct.substr(ct.find('/') + 1);
    }
};

// Abstract class: implements exportAll() once, defers the varying parts.
class TabularExporter : public Exporter {
public:
    std::string exportAll(const std::vector<Metric>& metrics) const override {
        std::ostringstream out;
        out << header() << '\n';
        for (const auto& m : metrics) {
            out << row(m) << '\n';
        }
        out << "# " << metrics.size() << " records";
        return out.str();
    }

protected:
    virtual std::string header() const = 0;
    virtual std::string row(const Metric& metric) const = 0;
};

class CsvExporter : public TabularExporter {
public:
    std::string contentType() const override { return "text/csv"; }

protected:
    std::string header() const override { return "name,value"; }
    std::string row(const Metric& m) const override {
        std::ostringstream out;
        out << m.name << ',' << m.value;
        return out.str();
    }
};

// Implements the contract directly — no base-class logic needed.
class JsonExporter : public Exporter {
public:
    std::string contentType() const override { return "application/json"; }
    std::string exportAll(const std::vector<Metric>& metrics) const override {
        std::ostringstream out;
        out << '[';
        for (size_t i = 0; i < metrics.size(); i++) {
            if (i) out << ", ";
            out << "{\"name\": \"" << metrics[i].name
                << "\", \"value\": " << metrics[i].value << '}';
        }
        out << ']';
        return out.str();
    }
};

// The client programs to the contract, never to a concrete class.
void deliver(const Exporter& exporter, const std::vector<Metric>& metrics) {
    std::cout << "--- " << exporter.contentType() << " -> "
              << exporter.fileName() << " ---\n"
              << exporter.exportAll(metrics) << "\n\n";
}

int main() {
    const std::vector<Metric> metrics = {
        {"cpu", 0.93}, {"memory", 0.67}, {"disk", 0.41}
    };
    deliver(CsvExporter{}, metrics);
    deliver(JsonExporter{}, metrics);
    return 0;
}
