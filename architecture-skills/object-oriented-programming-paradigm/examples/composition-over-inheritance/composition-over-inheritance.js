/** Composition over inheritance in JavaScript.
 *
 * One subclass per movement x weapon combo would multiply forever;
 * Robot instead holds two small interfaces and delegates. Parts can be
 * swapped at runtime without a new subclass.
 */

class Treads {
  move() { return 'rolls forward on treads'; }
}

class Rotors {
  move() { return 'lifts off on quad rotors'; }
}

class Turbines {
  move() { return 'dives and swims with turbines'; }
}

class Laser {
  attack() { return 'fires a precision laser'; }
}

class Drill {
  attack() { return 'spins up a mining drill'; }
}

class Robot {
  constructor(name, mover, weapon) {
    this.name = name;
    this.mover = mover;
    this.weapon = weapon;
  }

  perform() {
    return `${this.name.padStart(8)}: ${this.mover.move()} and ${this.weapon.attack()}`;
  }
}

const squad = [
  new Robot('Scout', new Treads(), new Laser()),
  new Robot('Miner', new Treads(), new Drill()),
  new Robot('Wasp', new Rotors(), new Drill()),
  new Robot('Manta', new Turbines(), new Laser()),
];

for (const robot of squad) {
  console.log(robot.perform());
}

console.log('-- field upgrade: Miner receives rotors --');
squad[1].mover = new Rotors();
console.log(squad[1].perform());
