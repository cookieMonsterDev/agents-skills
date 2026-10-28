/* Flyweight pattern in C.
 *
 * No polymorphism is needed for a flyweight, so no function pointers:
 * the flyweight is a const struct in a small static pool, and each tree
 * context holds a plain pointer into that pool plus its own extrinsic
 * coordinates.
 */

#include <stdio.h>
#include <string.h>

typedef struct {
    char name[32];
    char color[32];
} TreeType; /* flyweight: immutable intrinsic state */

void tree_type_draw(const TreeType *t, int x, int y) {
    printf("%s %s at (%d, %d)\n", t->color, t->name, x, y);
}

/* --- flyweight factory: a linear-scan pool --- */

#define MAX_TYPES 16

static TreeType type_pool[MAX_TYPES];
static int type_count = 0;

const TreeType *get_tree_type(const char *name, const char *color) {
    for (int i = 0; i < type_count; i++) {
        if (strcmp(type_pool[i].name, name) == 0 && strcmp(type_pool[i].color, color) == 0) {
            return &type_pool[i];
        }
    }
    TreeType *t = &type_pool[type_count++];
    strncpy(t->name, name, sizeof(t->name) - 1);
    strncpy(t->color, color, sizeof(t->color) - 1);
    return t;
}

/* --- context: extrinsic state + pointer to shared flyweight --- */

typedef struct {
    int x;
    int y;
    const TreeType *kind;
} Tree;

int main(void) {
    Tree forest[] = {
        {1, 1, get_tree_type("oak", "green")},
        {2, 4, get_tree_type("pine", "dark green")},
        {5, 2, get_tree_type("oak", "green")},
        {6, 6, get_tree_type("birch", "light green")},
        {8, 3, get_tree_type("pine", "dark green")},
        {9, 9, get_tree_type("oak", "green")},
    };
    int trees = (int)(sizeof(forest) / sizeof(forest[0]));

    for (int i = 0; i < trees; i++) {
        tree_type_draw(forest[i].kind, forest[i].x, forest[i].y);
    }

    printf("trees planted: %d, tree types in memory: %d\n", trees, type_count);
    return 0;
}
