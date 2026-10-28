/* Prototype pattern in C.
 *
 * Plain structs already copy by assignment; the pattern matters when the
 * struct holds pointers. Here the clone function duplicates the
 * heap-allocated tags string so the copy owns its own data.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    double x, y;
    double radius;
    char color[16];
    char *tags; /* heap-owned, must be duplicated on clone */
} Circle;

Circle *circle_new(double x, double y, double radius, const char *color, const char *tags) {
    Circle *c = malloc(sizeof(Circle));
    c->x = x;
    c->y = y;
    c->radius = radius;
    strncpy(c->color, color, sizeof(c->color) - 1);
    c->color[sizeof(c->color) - 1] = '\0';
    c->tags = strdup(tags);
    return c;
}

/* The clone deep-copies pointer fields; a struct assignment alone would
 * leave both circles sharing one tags buffer. */
Circle *circle_clone(const Circle *src) {
    Circle *copy = malloc(sizeof(Circle));
    *copy = *src;
    copy->tags = strdup(src->tags);
    return copy;
}

void circle_free(Circle *c) {
    free(c->tags);
    free(c);
}

void circle_describe(const Circle *c) {
    printf("Circle r=%.0f %s at (%.0f, %.0f) tags=%s\n",
           c->radius, c->color, c->x, c->y, c->tags);
}

int main(void) {
    /* Pre-configured prototype: pay the setup once, clone many times. */
    Circle *warning_marker = circle_new(0, 0, 12, "red", "alert");

    Circle *first = circle_clone(warning_marker);
    Circle *second = circle_clone(warning_marker);
    second->x = 40;
    second->y = 25;
    free(second->tags);
    second->tags = strdup("alert,muted");

    circle_describe(first);
    circle_describe(second);
    printf("independent copies: %s\n", first->tags != second->tags ? "true" : "false");

    circle_free(warning_marker);
    circle_free(first);
    circle_free(second);
    return 0;
}
