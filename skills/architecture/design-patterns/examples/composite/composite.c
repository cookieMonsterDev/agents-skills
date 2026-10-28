/* Composite pattern in C.
 *
 * Polymorphism is emulated with structs and function pointers: every
 * node carries its own size/print implementations, so callers treat
 * files and directories uniformly. Children live in a fixed-size array
 * to keep the example dependency-free.
 */

#include <stdio.h>

#define MAX_CHILDREN 8

typedef struct Node {
    const char *name;
    long (*size)(const struct Node *self);
    void (*print)(const struct Node *self, int indent);
    long file_size;                            /* leaf only */
    const struct Node *children[MAX_CHILDREN]; /* composite only */
    int child_count;
} Node;

static long file_size_fn(const Node *self) {
    return self->file_size;
}

static void file_print(const Node *self, int indent) {
    printf("%*s%s (%ld B)\n", indent, "", self->name, self->file_size);
}

static long dir_size(const Node *self) {
    long total = 0;
    for (int i = 0; i < self->child_count; i++) {
        total += self->children[i]->size(self->children[i]);
    }
    return total;
}

static void dir_print(const Node *self, int indent) {
    printf("%*s%s/ (%ld B)\n", indent, "", self->name, dir_size(self));
    for (int i = 0; i < self->child_count; i++) {
        self->children[i]->print(self->children[i], indent + 2);
    }
}

static Node make_file(const char *name, long size) {
    Node n = {0};
    n.name = name;
    n.size = file_size_fn;
    n.print = file_print;
    n.file_size = size;
    return n;
}

static Node make_dir(const char *name) {
    Node n = {0};
    n.name = name;
    n.size = dir_size;
    n.print = dir_print;
    return n;
}

static void dir_add(Node *dir, const Node *child) {
    dir->children[dir->child_count++] = child;
}

int main(void) {
    Node main_py = make_file("main.py", 1200);
    Node util_py = make_file("util.py", 450);
    Node readme = make_file("readme.md", 800);
    Node gitignore = make_file(".gitignore", 20);

    Node src = make_dir("src");
    dir_add(&src, &main_py);
    dir_add(&src, &util_py);

    Node docs = make_dir("docs");
    dir_add(&docs, &readme);

    Node project = make_dir("project");
    dir_add(&project, &src);
    dir_add(&project, &docs);
    dir_add(&project, &gitignore);

    project.print(&project, 0);
    return 0;
}
