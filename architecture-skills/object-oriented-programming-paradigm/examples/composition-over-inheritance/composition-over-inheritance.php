<?php
/**
 * Composition over inheritance in PHP.
 *
 * Robot holds MoveBehavior and AttackBehavior collaborators instead of
 * subclassing every movement x weapon combination. Parts swap at runtime.
 */

declare(strict_types=1);

interface MoveBehavior
{
    public function move(): string;
}

interface AttackBehavior
{
    public function attack(): string;
}

final class Treads implements MoveBehavior
{
    public function move(): string { return 'rolls forward on treads'; }
}

final class Rotors implements MoveBehavior
{
    public function move(): string { return 'lifts off on quad rotors'; }
}

final class Turbines implements MoveBehavior
{
    public function move(): string { return 'dives and swims with turbines'; }
}

final class Laser implements AttackBehavior
{
    public function attack(): string { return 'fires a precision laser'; }
}

final class Drill implements AttackBehavior
{
    public function attack(): string { return 'spins up a mining drill'; }
}

final class Robot
{
    public function __construct(
        private readonly string $name,
        private MoveBehavior $mover,
        private readonly AttackBehavior $weapon,
    ) {}

    public function setMover(MoveBehavior $mover): void
    {
        $this->mover = $mover;
    }

    public function perform(): string
    {
        return sprintf(
            '%8s: %s and %s',
            $this->name,
            $this->mover->move(),
            $this->weapon->attack()
        );
    }
}

$squad = [
    new Robot('Scout', new Treads(), new Laser()),
    new Robot('Miner', new Treads(), new Drill()),
    new Robot('Wasp', new Rotors(), new Drill()),
    new Robot('Manta', new Turbines(), new Laser()),
];

foreach ($squad as $robot) {
    echo $robot->perform(), PHP_EOL;
}

echo "-- field upgrade: Miner receives rotors --\n";
$squad[1]->setMover(new Rotors());
echo $squad[1]->perform(), PHP_EOL;
