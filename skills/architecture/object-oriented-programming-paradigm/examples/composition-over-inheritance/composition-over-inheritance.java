// Composition over inheritance in Java (Effective Java, Item 18).
//
// One subclass per movement x weapon combo would multiply forever;
// Robot instead holds two small interfaces and delegates. Java
// identifiers cannot contain hyphens, so unlike single-word examples
// the class cannot be named after this file; a package-private class
// keeps the single-file launcher (`java composition-over-inheritance.java`)
// working.

import java.util.ArrayList;
import java.util.List;

class CompositionOverInheritanceDemo {

    interface MoveBehavior {
        String move();
    }

    interface AttackBehavior {
        String attack();
    }

    // --- Concrete components: one capability each, final so they stay parts ---

    static final class Treads implements MoveBehavior {
        public String move() { return "rolls forward on treads"; }
    }

    static final class Rotors implements MoveBehavior {
        public String move() { return "lifts off on quad rotors"; }
    }

    static final class Turbines implements MoveBehavior {
        public String move() { return "dives and swims with turbines"; }
    }

    static final class Laser implements AttackBehavior {
        public String attack() { return "fires a precision laser"; }
    }

    static final class Drill implements AttackBehavior {
        public String attack() { return "spins up a mining drill"; }
    }

    /** Host: owns its parts and delegates behavior to them. */
    static final class Robot {
        private final String name;
        private MoveBehavior mover;
        private final AttackBehavior weapon;

        Robot(String name, MoveBehavior mover, AttackBehavior weapon) {
            this.name = name;
            this.mover = mover;
            this.weapon = weapon;
        }

        void setMover(MoveBehavior mover) {
            this.mover = mover;
        }

        String perform() {
            return "%8s: %s and %s".formatted(name, mover.move(), weapon.attack());
        }
    }

    public static void main(String[] args) {
        // Any combination is just wiring — no FlyingDrillRobot subclass needed.
        List<Robot> squad = new ArrayList<>(List.of(
                new Robot("Scout", new Treads(), new Laser()),
                new Robot("Miner", new Treads(), new Drill()),
                new Robot("Wasp", new Rotors(), new Drill()),   // flying driller
                new Robot("Manta", new Turbines(), new Laser())
        ));

        for (Robot robot : squad) {
            System.out.println(robot.perform());
        }

        // Inheritance fixes behavior at construction; composition swaps it live.
        System.out.println("-- field upgrade: Miner receives rotors --");
        squad.get(1).setMover(new Rotors());
        System.out.println(squad.get(1).perform());
    }
}
