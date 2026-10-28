// Facade pattern in Rust.
//
// The facade is a struct owning its subsystems; no traits are needed
// because clients depend on the facade concretely. In library code the
// same idea often appears as a module that `pub use`s a curated slice
// of a larger crate.

struct Amplifier;

impl Amplifier {
    fn on(&self) {
        println!("Amplifier: on");
    }
    fn set_volume(&self, level: u8) {
        println!("Amplifier: volume {level}");
    }
    fn off(&self) {
        println!("Amplifier: off");
    }
}

struct Projector;

impl Projector {
    fn on(&self) {
        println!("Projector: on");
    }
    fn wide_screen_mode(&self) {
        println!("Projector: 16:9 widescreen mode");
    }
    fn off(&self) {
        println!("Projector: off");
    }
}

struct StreamingPlayer;

impl StreamingPlayer {
    fn on(&self) {
        println!("StreamingPlayer: on");
    }
    fn play(&self, movie: &str) {
        println!("StreamingPlayer: playing \"{movie}\"");
    }
    fn stop(&self) {
        println!("StreamingPlayer: stopped");
    }
    fn off(&self) {
        println!("StreamingPlayer: off");
    }
}

struct HomeTheater {
    amp: Amplifier,
    projector: Projector,
    player: StreamingPlayer,
}

impl HomeTheater {
    fn new() -> Self {
        Self { amp: Amplifier, projector: Projector, player: StreamingPlayer }
    }

    fn watch_movie(&self, movie: &str) {
        println!("= Movie night =");
        self.amp.on();
        self.amp.set_volume(5);
        self.projector.on();
        self.projector.wide_screen_mode();
        self.player.on();
        self.player.play(movie);
    }

    fn end_movie(&self) {
        println!("= Shutting down =");
        self.player.stop();
        self.player.off();
        self.projector.off();
        self.amp.off();
    }
}

fn main() {
    let theater = HomeTheater::new();
    theater.watch_movie("Inception");
    theater.end_movie();
}
