// Composition over inheritance in Swift.
//
// Robot holds two protocol-typed collaborators instead of subclassing
// every movement x weapon combination. Parts can be swapped at runtime.

import Foundation

protocol MoveBehavior {
    func move() -> String
}

protocol AttackBehavior {
    func attack() -> String
}

struct Treads: MoveBehavior {
    func move() -> String { "rolls forward on treads" }
}

struct Rotors: MoveBehavior {
    func move() -> String { "lifts off on quad rotors" }
}

struct Turbines: MoveBehavior {
    func move() -> String { "dives and swims with turbines" }
}

struct Laser: AttackBehavior {
    func attack() -> String { "fires a precision laser" }
}

struct Drill: AttackBehavior {
    func attack() -> String { "spins up a mining drill" }
}

final class Robot {
    let name: String
    var mover: MoveBehavior
    let weapon: AttackBehavior

    init(name: String, mover: MoveBehavior, weapon: AttackBehavior) {
        self.name = name
        self.mover = mover
        self.weapon = weapon
    }

    func perform() -> String {
        String(format: "%8@: %@ and %@", name, mover.move(), weapon.attack())
    }
}

var squad = [
    Robot(name: "Scout", mover: Treads(), weapon: Laser()),
    Robot(name: "Miner", mover: Treads(), weapon: Drill()),
    Robot(name: "Wasp", mover: Rotors(), weapon: Drill()),
    Robot(name: "Manta", mover: Turbines(), weapon: Laser()),
]

for robot in squad {
    print(robot.perform())
}

print("-- field upgrade: Miner receives rotors --")
squad[1].mover = Rotors()
print(squad[1].perform())
