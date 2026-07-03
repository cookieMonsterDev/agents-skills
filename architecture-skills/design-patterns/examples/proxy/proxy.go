// Proxy pattern in Go (virtual proxy: lazy-loading image).
//
// An interface satisfied by both the real struct and the proxy; the
// proxy holds a nil pointer until first use. Go's implicit interface
// satisfaction means neither type declares that it implements Image —
// composition does all the work.

package main

import "fmt"

type Image interface {
	Display()
}

// RealImage is the real subject: expensive to create.
type RealImage struct {
	filename string
}

func NewRealImage(filename string) *RealImage {
	fmt.Printf("Loading %s from disk (expensive)\n", filename)
	return &RealImage{filename: filename}
}

func (r *RealImage) Display() {
	fmt.Printf("Displaying %s\n", r.filename)
}

// ImageProxy defers creating the RealImage until first use.
type ImageProxy struct {
	filename string
	real     *RealImage
}

func NewImageProxy(filename string) *ImageProxy {
	return &ImageProxy{filename: filename}
}

func (p *ImageProxy) Display() {
	if p.real == nil {
		p.real = NewRealImage(p.filename)
	}
	p.real.Display()
}

func main() {
	gallery := []Image{
		NewImageProxy("holiday.png"),
		NewImageProxy("unused.png"),
	}
	fmt.Println("Proxies created; nothing loaded yet")

	gallery[0].Display()
	gallery[0].Display() // loaded once, displayed twice

	fmt.Println("unused.png was never loaded")
}
