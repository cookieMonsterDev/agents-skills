// Facade pattern in JavaScript.
//
// Note: in JavaScript a module that exports a couple of functions over
// internal classes is the most common facade — the class below is only
// needed because the facade holds the subsystems as state.

class Amplifier {
  on() { console.log("Amplifier: on"); }
  setVolume(level) { console.log(`Amplifier: volume ${level}`); }
  off() { console.log("Amplifier: off"); }
}

class Projector {
  on() { console.log("Projector: on"); }
  wideScreenMode() { console.log("Projector: 16:9 widescreen mode"); }
  off() { console.log("Projector: off"); }
}

class StreamingPlayer {
  on() { console.log("StreamingPlayer: on"); }
  play(movie) { console.log(`StreamingPlayer: playing "${movie}"`); }
  stop() { console.log("StreamingPlayer: stopped"); }
  off() { console.log("StreamingPlayer: off"); }
}

class HomeTheater {
  #amp;
  #projector;
  #player;

  constructor(amp, projector, player) {
    this.#amp = amp;
    this.#projector = projector;
    this.#player = player;
  }

  watchMovie(movie) {
    console.log("= Movie night =");
    this.#amp.on();
    this.#amp.setVolume(5);
    this.#projector.on();
    this.#projector.wideScreenMode();
    this.#player.on();
    this.#player.play(movie);
  }

  endMovie() {
    console.log("= Shutting down =");
    this.#player.stop();
    this.#player.off();
    this.#projector.off();
    this.#amp.off();
  }
}

const theater = new HomeTheater(new Amplifier(), new Projector(), new StreamingPlayer());
theater.watchMovie("Inception");
theater.endMovie();
