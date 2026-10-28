// Composition over inheritance in C++.
//
// Instead of a virtual Robot hierarchy with one subclass per movement x
// weapon combo, Robot owns std::unique_ptr<Interface> members and
// delegates to them. Small interfaces are still used — but for the
// parts, not for the robot's identity. Parts swap at runtime via a
// setter, which no subclass could do.

#include <iostream>
#include <memory>
#include <string>
#include <vector>

struct MoveBehavior {
    virtual ~MoveBehavior() = default;
    virtual std::string move() const = 0;
};

struct AttackBehavior {
    virtual ~AttackBehavior() = default;
    virtual std::string attack() const = 0;
};

// --- Concrete components: one capability each ---

struct Treads : MoveBehavior {
    std::string move() const override { return "rolls forward on treads"; }
};
struct Rotors : MoveBehavior {
    std::string move() const override { return "lifts off on quad rotors"; }
};
struct Turbines : MoveBehavior {
    std::string move() const override { return "dives and swims with turbines"; }
};

struct Laser : AttackBehavior {
    std::string attack() const override { return "fires a precision laser"; }
};
struct Drill : AttackBehavior {
    std::string attack() const override { return "spins up a mining drill"; }
};

// Host: owns its parts and delegates behavior to them.
class Robot {
public:
    Robot(std::string name, std::unique_ptr<MoveBehavior> mover,
          std::unique_ptr<AttackBehavior> weapon)
        : name_(std::move(name)), mover_(std::move(mover)), weapon_(std::move(weapon)) {}

    void setMover(std::unique_ptr<MoveBehavior> mover) { mover_ = std::move(mover); }

    void perform() const {
        std::cout << name_ << ": " << mover_->move() << " and "
                  << weapon_->attack() << "\n";
    }

private:
    std::string name_;
    std::unique_ptr<MoveBehavior> mover_;
    std::unique_ptr<AttackBehavior> weapon_;
};

int main() {
    // Any combination is just wiring — no FlyingDrillRobot subclass needed.
    std::vector<Robot> squad;
    squad.emplace_back("Scout", std::make_unique<Treads>(), std::make_unique<Laser>());
    squad.emplace_back("Miner", std::make_unique<Treads>(), std::make_unique<Drill>());
    squad.emplace_back("Wasp", std::make_unique<Rotors>(), std::make_unique<Drill>());
    squad.emplace_back("Manta", std::make_unique<Turbines>(), std::make_unique<Laser>());

    for (const Robot &robot : squad) {
        robot.perform();
    }

    // Inheritance fixes behavior at construction; composition swaps it live.
    std::cout << "-- field upgrade: Miner receives rotors --\n";
    squad[1].setMover(std::make_unique<Rotors>());
    squad[1].perform();
}
