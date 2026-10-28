// Facade pattern in Java.
//
// The textbook home of the pattern: a plain class composing subsystem
// objects and exposing one method per use case. The subsystems remain
// public API for callers that need fine-grained control.

public class facade {

    static final class Amplifier {
        void on() { System.out.println("Amplifier: on"); }
        void setVolume(int level) { System.out.println("Amplifier: volume " + level); }
        void off() { System.out.println("Amplifier: off"); }
    }

    static final class Projector {
        void on() { System.out.println("Projector: on"); }
        void wideScreenMode() { System.out.println("Projector: 16:9 widescreen mode"); }
        void off() { System.out.println("Projector: off"); }
    }

    static final class StreamingPlayer {
        void on() { System.out.println("StreamingPlayer: on"); }
        void play(String movie) { System.out.println("StreamingPlayer: playing \"" + movie + "\""); }
        void stop() { System.out.println("StreamingPlayer: stopped"); }
        void off() { System.out.println("StreamingPlayer: off"); }
    }

    static final class HomeTheater {
        private final Amplifier amp;
        private final Projector projector;
        private final StreamingPlayer player;

        HomeTheater(Amplifier amp, Projector projector, StreamingPlayer player) {
            this.amp = amp;
            this.projector = projector;
            this.player = player;
        }

        void watchMovie(String movie) {
            System.out.println("= Movie night =");
            amp.on();
            amp.setVolume(5);
            projector.on();
            projector.wideScreenMode();
            player.on();
            player.play(movie);
        }

        void endMovie() {
            System.out.println("= Shutting down =");
            player.stop();
            player.off();
            projector.off();
            amp.off();
        }
    }

    public static void main(String[] args) {
        HomeTheater theater = new HomeTheater(new Amplifier(), new Projector(), new StreamingPlayer());
        theater.watchMovie("Inception");
        theater.endMovie();
    }
}
