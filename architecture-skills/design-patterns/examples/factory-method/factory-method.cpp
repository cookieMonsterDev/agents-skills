// Factory Method pattern in C++.
//
// The abstract creator owns the shared workflow (planDelivery) and defers
// one creation step to subclasses, which return products via unique_ptr.

#include <iostream>
#include <memory>
#include <string>

class Transport {  // product interface
public:
    virtual ~Transport() = default;
    virtual std::string deliver(const std::string& cargo) const = 0;
};

class Truck : public Transport {
public:
    std::string deliver(const std::string& cargo) const override {
        return "Truck delivers " + cargo + " by road in a box";
    }
};

class Ship : public Transport {
public:
    std::string deliver(const std::string& cargo) const override {
        return "Ship delivers " + cargo + " by sea in a container";
    }
};

class Logistics {  // creator: shared workflow + one overridable step
public:
    virtual ~Logistics() = default;

    std::string planDelivery(const std::string& cargo) const {
        auto transport = createTransport();
        return "[" + name() + "] " + transport->deliver(cargo);
    }

protected:
    virtual std::unique_ptr<Transport> createTransport() const = 0;
    virtual std::string name() const = 0;
};

class RoadLogistics : public Logistics {
protected:
    std::unique_ptr<Transport> createTransport() const override {
        return std::make_unique<Truck>();
    }
    std::string name() const override { return "RoadLogistics"; }
};

class SeaLogistics : public Logistics {
protected:
    std::unique_ptr<Transport> createTransport() const override {
        return std::make_unique<Ship>();
    }
    std::string name() const override { return "SeaLogistics"; }
};

int main() {
    RoadLogistics road;
    SeaLogistics sea;

    std::cout << road.planDelivery("machine parts") << '\n';
    std::cout << sea.planDelivery("machine parts") << '\n';
    return 0;
}
