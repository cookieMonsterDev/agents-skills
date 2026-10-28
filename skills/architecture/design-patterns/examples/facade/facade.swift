// Facade pattern in Swift.
//
// A plain struct wraps the subsystems; no protocol is needed because
// clients depend on the facade concretely. The subsystems remain
// directly usable for callers that need fine-grained control.

struct Amplifier {
    func on() { print("Amplifier: on") }
    func setVolume(_ level: Int) { print("Amplifier: volume \(level)") }
    func off() { print("Amplifier: off") }
}

struct Projector {
    func on() { print("Projector: on") }
    func wideScreenMode() { print("Projector: 16:9 widescreen mode") }
    func off() { print("Projector: off") }
}

struct StreamingPlayer {
    func on() { print("StreamingPlayer: on") }
    func play(_ movie: String) { print("StreamingPlayer: playing \"\(movie)\"") }
    func stop() { print("StreamingPlayer: stopped") }
    func off() { print("StreamingPlayer: off") }
}

struct HomeTheater {
    private let amp = Amplifier()
    private let projector = Projector()
    private let player = StreamingPlayer()

    func watchMovie(_ movie: String) {
        print("= Movie night =")
        amp.on()
        amp.setVolume(5)
        projector.on()
        projector.wideScreenMode()
        player.on()
        player.play(movie)
    }

    func endMovie() {
        print("= Shutting down =")
        player.stop()
        player.off()
        projector.off()
        amp.off()
    }
}

let theater = HomeTheater()
theater.watchMovie("Inception")
theater.endMovie()
