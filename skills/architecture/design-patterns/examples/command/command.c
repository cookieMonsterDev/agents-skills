/* Command pattern in C.
 *
 * Text editor with undo. C has no classes, so a command is a struct of
 * function pointers (execute, undo) plus the state each command needs;
 * a fixed-size stack of executed commands provides undo.
 */

#include <stdio.h>
#include <string.h>

typedef struct {
    char text[256];
} Editor; /* receiver */

typedef struct Command Command;
struct Command {
    void (*execute)(Command *self);
    void (*undo)(Command *self);
    Editor *editor;
    char arg[64];     /* text to insert, or text captured by delete */
    int count;        /* chars to delete */
};

static void insert_execute(Command *self) {
    strcat(self->editor->text, self->arg);
}

static void insert_undo(Command *self) {
    size_t len = strlen(self->editor->text);
    self->editor->text[len - strlen(self->arg)] = '\0';
}

static void delete_execute(Command *self) {
    size_t len = strlen(self->editor->text);
    /* Capture the deleted tail so undo can restore it. */
    strcpy(self->arg, self->editor->text + len - self->count);
    self->editor->text[len - self->count] = '\0';
}

static void delete_undo(Command *self) {
    strcat(self->editor->text, self->arg);
}

static Command make_insert(Editor *editor, const char *text) {
    Command c = {insert_execute, insert_undo, editor, {0}, 0};
    strncpy(c.arg, text, sizeof(c.arg) - 1);
    return c;
}

static Command make_delete_last(Editor *editor, int count) {
    Command c = {delete_execute, delete_undo, editor, {0}, count};
    return c;
}

/* Invoker: executes commands and tracks them for undo. */
typedef struct {
    Command stack[16];
    int top;
} History;

static void history_execute(History *h, Command command) {
    command.execute(&command);
    h->stack[h->top++] = command;
}

static void history_undo(History *h) {
    if (h->top > 0) {
        Command *c = &h->stack[--h->top];
        c->undo(c);
    }
}

int main(void) {
    Editor editor = {""};
    History history = {{{0}}, 0};

    history_execute(&history, make_insert(&editor, "Hello"));
    history_execute(&history, make_insert(&editor, ", world!"));
    history_execute(&history, make_delete_last(&editor, 1));
    printf("after edits: \"%s\"\n", editor.text);

    history_undo(&history);
    history_undo(&history);
    printf("after 2 undos: \"%s\"\n", editor.text);
    return 0;
}
