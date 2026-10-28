/* Visitor pattern in C.
 *
 * Polymorphism is emulated with a tagged union plus a visitor struct of
 * function pointers; the accept function switches on the tag and calls
 * the matching pointer — that switch is the double dispatch. In plain C
 * a direct switch per operation is common; the visitor struct earns its
 * keep when operations are added often and the shape set is stable.
 */

#include <math.h>
#include <stdio.h>

typedef enum { SHAPE_CIRCLE, SHAPE_RECTANGLE, SHAPE_TRIANGLE } ShapeKind;

typedef struct {
    ShapeKind kind;
    union {
        struct { double radius; } circle;
        struct { double width, height; } rectangle;
        struct { double base, height; } triangle;
    } u;
} Shape;

typedef struct {
    void (*visit_circle)(const Shape *shape, void *out);
    void (*visit_rectangle)(const Shape *shape, void *out);
    void (*visit_triangle)(const Shape *shape, void *out);
} ShapeVisitor;

void shape_accept(const Shape *shape, const ShapeVisitor *visitor, void *out) {
    switch (shape->kind) {
    case SHAPE_CIRCLE:    visitor->visit_circle(shape, out); break;
    case SHAPE_RECTANGLE: visitor->visit_rectangle(shape, out); break;
    case SHAPE_TRIANGLE:  visitor->visit_triangle(shape, out); break;
    }
}

/* --- Area visitor: writes the area into out (double*) --- */

void area_circle(const Shape *s, void *out) {
    *(double *)out = M_PI * s->u.circle.radius * s->u.circle.radius;
}

void area_rectangle(const Shape *s, void *out) {
    *(double *)out = s->u.rectangle.width * s->u.rectangle.height;
}

void area_triangle(const Shape *s, void *out) {
    *(double *)out = 0.5 * s->u.triangle.base * s->u.triangle.height;
}

/* --- SVG export visitor: prints markup, ignores out --- */

void svg_circle(const Shape *s, void *out) {
    (void)out;
    printf("<circle r=\"%g\" />\n", s->u.circle.radius);
}

void svg_rectangle(const Shape *s, void *out) {
    (void)out;
    printf("<rect width=\"%g\" height=\"%g\" />\n", s->u.rectangle.width, s->u.rectangle.height);
}

void svg_triangle(const Shape *s, void *out) {
    (void)out;
    printf("<polygon points=\"0,%g %g,%g 0,0\" />\n",
           s->u.triangle.height, s->u.triangle.base, s->u.triangle.height);
}

int main(void) {
    Shape shapes[] = {
        { SHAPE_CIRCLE, { .circle = { 2.0 } } },
        { SHAPE_RECTANGLE, { .rectangle = { 3.0, 4.0 } } },
        { SHAPE_TRIANGLE, { .triangle = { 6.0, 2.0 } } },
    };
    size_t count = sizeof(shapes) / sizeof(shapes[0]);

    ShapeVisitor area = { area_circle, area_rectangle, area_triangle };
    ShapeVisitor svg = { svg_circle, svg_rectangle, svg_triangle };

    double total = 0.0;
    for (size_t i = 0; i < count; i++) {
        double a;
        shape_accept(&shapes[i], &area, &a);
        printf("area=%6.2f  ", a);
        shape_accept(&shapes[i], &svg, NULL);
        total += a;
    }
    printf("total area: %.2f\n", total);
    return 0;
}
