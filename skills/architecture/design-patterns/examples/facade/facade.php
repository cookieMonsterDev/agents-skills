<?php
// Facade pattern in PHP.
//
// Note: Laravel "facades" are static proxies to container services, not
// GoF facades. The GoF form is shown here: a plain class composing the
// subsystems and exposing one method per use case.

declare(strict_types=1);

final class Amplifier
{
    public function on(): void { echo "Amplifier: on\n"; }
    public function setVolume(int $level): void { echo "Amplifier: volume $level\n"; }
    public function off(): void { echo "Amplifier: off\n"; }
}

final class Projector
{
    public function on(): void { echo "Projector: on\n"; }
    public function wideScreenMode(): void { echo "Projector: 16:9 widescreen mode\n"; }
    public function off(): void { echo "Projector: off\n"; }
}

final class StreamingPlayer
{
    public function on(): void { echo "StreamingPlayer: on\n"; }
    public function play(string $movie): void { echo "StreamingPlayer: playing \"$movie\"\n"; }
    public function stop(): void { echo "StreamingPlayer: stopped\n"; }
    public function off(): void { echo "StreamingPlayer: off\n"; }
}

final class HomeTheater
{
    public function __construct(
        private readonly Amplifier $amp,
        private readonly Projector $projector,
        private readonly StreamingPlayer $player,
    ) {
    }

    public function watchMovie(string $movie): void
    {
        echo "= Movie night =\n";
        $this->amp->on();
        $this->amp->setVolume(5);
        $this->projector->on();
        $this->projector->wideScreenMode();
        $this->player->on();
        $this->player->play($movie);
    }

    public function endMovie(): void
    {
        echo "= Shutting down =\n";
        $this->player->stop();
        $this->player->off();
        $this->projector->off();
        $this->amp->off();
    }
}

$theater = new HomeTheater(new Amplifier(), new Projector(), new StreamingPlayer());
$theater->watchMovie('Inception');
$theater->endMovie();
