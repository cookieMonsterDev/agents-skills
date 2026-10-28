/* Facade pattern in C.
 *
 * No polymorphism is required for a facade, so no function pointers are
 * needed here: the subsystems are plain structs with functions, and the
 * facade is a struct holding them plus two functions that call the
 * subsystem operations in the right order.
 */

#include <stdio.h>

/* --- subsystems --- */

typedef struct { int volume; } Amplifier;

void amp_on(Amplifier *a)                 { (void)a; printf("Amplifier: on\n"); }
void amp_set_volume(Amplifier *a, int v)  { a->volume = v; printf("Amplifier: volume %d\n", v); }
void amp_off(Amplifier *a)                { (void)a; printf("Amplifier: off\n"); }

typedef struct { int widescreen; } Projector;

void projector_on(Projector *p)   { (void)p; printf("Projector: on\n"); }
void projector_wide(Projector *p) { p->widescreen = 1; printf("Projector: 16:9 widescreen mode\n"); }
void projector_off(Projector *p)  { (void)p; printf("Projector: off\n"); }

typedef struct { const char *movie; } StreamingPlayer;

void player_on(StreamingPlayer *s)   { (void)s; printf("StreamingPlayer: on\n"); }
void player_play(StreamingPlayer *s, const char *movie) {
    s->movie = movie;
    printf("StreamingPlayer: playing \"%s\"\n", movie);
}
void player_stop(StreamingPlayer *s) { s->movie = NULL; printf("StreamingPlayer: stopped\n"); }
void player_off(StreamingPlayer *s)  { (void)s; printf("StreamingPlayer: off\n"); }

/* --- facade --- */

typedef struct {
    Amplifier amp;
    Projector projector;
    StreamingPlayer player;
} HomeTheater;

void home_theater_watch_movie(HomeTheater *ht, const char *movie) {
    printf("= Movie night =\n");
    amp_on(&ht->amp);
    amp_set_volume(&ht->amp, 5);
    projector_on(&ht->projector);
    projector_wide(&ht->projector);
    player_on(&ht->player);
    player_play(&ht->player, movie);
}

void home_theater_end_movie(HomeTheater *ht) {
    printf("= Shutting down =\n");
    player_stop(&ht->player);
    player_off(&ht->player);
    projector_off(&ht->projector);
    amp_off(&ht->amp);
}

int main(void) {
    HomeTheater theater = {0};
    home_theater_watch_movie(&theater, "Inception");
    home_theater_end_movie(&theater);
    return 0;
}
