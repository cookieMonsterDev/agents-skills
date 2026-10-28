// Facade pattern in C++.
//
// The facade owns the subsystem objects by value and exposes one method
// per use case. No virtual functions are needed: clients depend on the
// facade concretely (the same idea underlies the pImpl idiom, which is
// a facade over a single translation unit).

#include <iostream>
#include <string>

class Amplifier {
public:
    void on() { std::cout << "Amplifier: on\n"; }
    void setVolume(int level) { std::cout << "Amplifier: volume " << level << '\n'; }
    void off() { std::cout << "Amplifier: off\n"; }
};

class Projector {
public:
    void on() { std::cout << "Projector: on\n"; }
    void wideScreenMode() { std::cout << "Projector: 16:9 widescreen mode\n"; }
    void off() { std::cout << "Projector: off\n"; }
};

class StreamingPlayer {
public:
    void on() { std::cout << "StreamingPlayer: on\n"; }
    void play(const std::string& movie) {
        std::cout << "StreamingPlayer: playing \"" << movie << "\"\n";
    }
    void stop() { std::cout << "StreamingPlayer: stopped\n"; }
    void off() { std::cout << "StreamingPlayer: off\n"; }
};

class HomeTheater {
public:
    void watchMovie(const std::string& movie) {
        std::cout << "= Movie night =\n";
        amp_.on();
        amp_.setVolume(5);
        projector_.on();
        projector_.wideScreenMode();
        player_.on();
        player_.play(movie);
    }

    void endMovie() {
        std::cout << "= Shutting down =\n";
        player_.stop();
        player_.off();
        projector_.off();
        amp_.off();
    }

private:
    Amplifier amp_;
    Projector projector_;
    StreamingPlayer player_;
};

int main() {
    HomeTheater theater;
    theater.watchMovie("Inception");
    theater.endMovie();
    return 0;
}
