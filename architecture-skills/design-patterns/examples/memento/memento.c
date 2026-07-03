/* Memento pattern in C.
 *
 * The editor (originator) copies its state into a snapshot struct by
 * value; the history (caretaker) stores snapshots in an array without
 * interpreting them. C has no access control, so the memento's opacity
 * is a convention: only editor_* functions touch snapshot fields.
 */

#include <stdio.h>
#include <string.h>

#define MAX_TEXT 256
#define MAX_HISTORY 16

typedef struct {
    char text[MAX_TEXT];
    size_t cursor;
} Snapshot; /* memento */

typedef struct {
    char text[MAX_TEXT];
    size_t cursor;
} TextEditor; /* originator */

void editor_type(TextEditor *e, const char *insert) {
    size_t len = strlen(insert);
    size_t tail = strlen(e->text) - e->cursor;
    memmove(e->text + e->cursor + len, e->text + e->cursor, tail + 1);
    memcpy(e->text + e->cursor, insert, len);
    e->cursor += len;
}

Snapshot editor_save(const TextEditor *e) {
    Snapshot s;
    strcpy(s.text, e->text);
    s.cursor = e->cursor;
    return s;
}

void editor_restore(TextEditor *e, const Snapshot *s) {
    strcpy(e->text, s->text);
    e->cursor = s->cursor;
}

void editor_print(const TextEditor *e, const char *label) {
    printf("%s '%s' (cursor at %zu)\n", label, e->text, e->cursor);
}

typedef struct {
    Snapshot snapshots[MAX_HISTORY];
    int count;
} History; /* caretaker */

void history_push(History *h, Snapshot s) {
    if (h->count < MAX_HISTORY) {
        h->snapshots[h->count++] = s;
    }
}

int history_pop(History *h, Snapshot *out) {
    if (h->count == 0) {
        return 0;
    }
    *out = h->snapshots[--h->count];
    return 1;
}

int main(void) {
    TextEditor editor = {"", 0};
    History history = {{{{0}, 0}}, 0};

    editor_type(&editor, "Hello");
    history_push(&history, editor_save(&editor));
    editor_type(&editor, ", world");
    history_push(&history, editor_save(&editor));
    editor_type(&editor, "!!!");
    editor_print(&editor, "current:");

    Snapshot s;
    for (int i = 0; i < 2 && history_pop(&history, &s); i++) {
        editor_restore(&editor, &s);
        editor_print(&editor, "undo:   ");
    }
    return 0;
}
