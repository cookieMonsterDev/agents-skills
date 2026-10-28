/* Bridge pattern in C.
 *
 * Both hierarchies are emulated with structs and function pointers:
 * Renderer is a vtable of drawing functions, and each shape holds a
 * pointer to a Renderer plus its own draw function.
 */

#include <stdio.h>

/* Implementation side: a vtable of primitive drawing operations. */
typedef struct {
    void (*circle)(double radius);
    void (*rectangle)(double width, double height);
} Renderer;

static void vector_circle(double radius) {
    printf("<circle r=%.1f/>\n", radius);
}
static void vector_rectangle(double width, double height) {
    printf("<rect w=%.1f h=%.1f/>\n", width, height);
}
static void raster_circle(double radius) {
    printf("pixels for a circle of radius %.1f\n", radius);
}
static void raster_rectangle(double width, double height) {
    printf("pixels for a %.1fx%.1f rectangle\n", width, height);
}

static const Renderer vector_renderer = {vector_circle, vector_rectangle};
static const Renderer raster_renderer = {raster_circle, raster_rectangle};

/* Abstraction side: a shape refers to a renderer and delegates. */
typedef struct Shape {
    void (*draw)(const struct Shape *self);
    const Renderer *renderer;
    double a, b; /* radius, or width/height */
} Shape;

static void circle_draw(const Shape *self) {
    self->renderer->circle(self->a);
}
static void rectangle_draw(const Shape *self) {
    self->renderer->rectangle(self->a, self->b);
}

static Shape make_circle(const Renderer *renderer, double radius) {
    Shape s = {circle_draw, renderer, radius, 0.0};
    return s;
}
static Shape make_rectangle(const Renderer *renderer, double width, double height) {
    Shape s = {rectangle_draw, renderer, width, height};
    return s;
}

int main(void) {
    const Renderer *renderers[] = {&vector_renderer, &raster_renderer};
    for (int i = 0; i < 2; i++) {
        Shape shapes[] = {
            make_circle(renderers[i], 5.0),
            make_rectangle(renderers[i], 3.0, 4.0),
        };
        for (int j = 0; j < 2; j++) {
            shapes[j].draw(&shapes[j]);
        }
    }
    return 0;
}
