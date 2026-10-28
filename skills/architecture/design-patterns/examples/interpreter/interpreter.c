/* Interpreter pattern in C.
 *
 * A tiny arithmetic grammar: literals, variables, +, -, *. C has no
 * classes, so an expression node is a tagged struct (kind + children)
 * and eval() recursively switches on the kind. The context is a small
 * array of name/value bindings.
 */

#include <stdio.h>
#include <string.h>

typedef struct {
    const char *names[8];
    int values[8];
    int count;
} Context;

static int context_lookup(const Context *ctx, const char *name) {
    for (int i = 0; i < ctx->count; i++) {
        if (strcmp(ctx->names[i], name) == 0) {
            return ctx->values[i];
        }
    }
    return 0;
}

typedef enum { LITERAL, VARIABLE, ADD, SUB, MUL } NodeKind;

typedef struct Expr Expr;
struct Expr {
    NodeKind kind;
    int value;            /* LITERAL */
    const char *name;     /* VARIABLE */
    const Expr *left;     /* ADD / SUB / MUL */
    const Expr *right;
};

static int eval(const Expr *e, const Context *ctx) {
    switch (e->kind) {
    case LITERAL:  return e->value;
    case VARIABLE: return context_lookup(ctx, e->name);
    case ADD:      return eval(e->left, ctx) + eval(e->right, ctx);
    case SUB:      return eval(e->left, ctx) - eval(e->right, ctx);
    case MUL:      return eval(e->left, ctx) * eval(e->right, ctx);
    }
    return 0;
}

int main(void) {
    /* (x + y) * 2 - z */
    Expr x = {VARIABLE, 0, "x", NULL, NULL};
    Expr y = {VARIABLE, 0, "y", NULL, NULL};
    Expr z = {VARIABLE, 0, "z", NULL, NULL};
    Expr two = {LITERAL, 2, NULL, NULL, NULL};
    Expr sum = {ADD, 0, NULL, &x, &y};
    Expr product = {MUL, 0, NULL, &sum, &two};
    Expr expression = {SUB, 0, NULL, &product, &z};

    Context first = {{"x", "y", "z"}, {6, 2, 3}, 3};
    Context second = {{"x", "y", "z"}, {1, 1, 10}, 3};

    printf("(x + y) * 2 - z with x=6 y=2 z=3   = %d\n", eval(&expression, &first));
    printf("(x + y) * 2 - z with x=1 y=1 z=10  = %d\n", eval(&expression, &second));
    return 0;
}
