/* Iterator pattern in C.
 *
 * A binary search tree traversed in sorted order. C has no iteration
 * protocol, so the pattern is a struct holding the traversal state (an
 * explicit stack replacing the recursive call stack) plus a next()
 * function that reports whether it produced a value. Polymorphism, if
 * several collection types must share one interface, would add a
 * function pointer to the struct; a single collection does not need it.
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *left, *right;
} Node;

static Node *tree_add(Node *root, int value) {
    if (root == NULL) {
        Node *n = calloc(1, sizeof(Node));
        n->value = value;
        return n;
    }
    if (value < root->value) {
        root->left = tree_add(root->left, value);
    } else {
        root->right = tree_add(root->right, value);
    }
    return root;
}

static void tree_free(Node *root) {
    if (root != NULL) {
        tree_free(root->left);
        tree_free(root->right);
        free(root);
    }
}

/* Iterator: an explicit stack of nodes whose left subtrees are done. */
typedef struct {
    Node *stack[64];
    int top;
} TreeIter;

static void iter_push_left_spine(TreeIter *it, Node *node) {
    for (; node != NULL; node = node->left) {
        it->stack[it->top++] = node;
    }
}

static void iter_init(TreeIter *it, Node *root) {
    it->top = 0;
    iter_push_left_spine(it, root);
}

/* Returns 1 and writes to *out if a value was produced, 0 when done. */
static int iter_next(TreeIter *it, int *out) {
    if (it->top == 0) {
        return 0;
    }
    Node *node = it->stack[--it->top];
    *out = node->value;
    iter_push_left_spine(it, node->right);
    return 1;
}

int main(void) {
    const int values[] = {5, 3, 8, 1, 4, 9, 7};
    Node *tree = NULL;
    for (size_t i = 0; i < sizeof(values) / sizeof(values[0]); i++) {
        tree = tree_add(tree, values[i]);
    }

    TreeIter it;
    iter_init(&it, tree);

    int value, sum = 0;
    printf("in order:");
    while (iter_next(&it, &value)) {
        printf(" %d", value);
        sum += value;
    }
    printf("\nsum: %d\n", sum);

    tree_free(tree);
    return 0;
}
