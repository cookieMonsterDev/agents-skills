// Facade pattern in Go.
//
// An idiomatic Go package *is* a facade: unexported types do the work
// and a small exported surface fronts them. Everything lives in one
// file here, so the "package boundary" is simulated with an exported
// HomeTheater over lower-case subsystem types.

package main

import "fmt"

type amplifier struct{}

func (amplifier) on()               { fmt.Println("Amplifier: on") }
func (amplifier) setVolume(lvl int) { fmt.Printf("Amplifier: volume %d\n", lvl) }
func (amplifier) off()              { fmt.Println("Amplifier: off") }

type projector struct{}

func (projector) on()             { fmt.Println("Projector: on") }
func (projector) wideScreenMode() { fmt.Println("Projector: 16:9 widescreen mode") }
func (projector) off()            { fmt.Println("Projector: off") }

type streamingPlayer struct{}

func (streamingPlayer) on() { fmt.Println("StreamingPlayer: on") }
func (streamingPlayer) play(movie string) {
	fmt.Printf("StreamingPlayer: playing %q\n", movie)
}
func (streamingPlayer) stop() { fmt.Println("StreamingPlayer: stopped") }
func (streamingPlayer) off()  { fmt.Println("StreamingPlayer: off") }

// HomeTheater is the facade: one method per use case.
type HomeTheater struct {
	amp    amplifier
	proj   projector
	player streamingPlayer
}

func NewHomeTheater() *HomeTheater {
	return &HomeTheater{}
}

func (h *HomeTheater) WatchMovie(movie string) {
	fmt.Println("= Movie night =")
	h.amp.on()
	h.amp.setVolume(5)
	h.proj.on()
	h.proj.wideScreenMode()
	h.player.on()
	h.player.play(movie)
}

func (h *HomeTheater) EndMovie() {
	fmt.Println("= Shutting down =")
	h.player.stop()
	h.player.off()
	h.proj.off()
	h.amp.off()
}

func main() {
	theater := NewHomeTheater()
	theater.WatchMovie("Inception")
	theater.EndMovie()
}
