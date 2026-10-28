/* State pattern in C.
 *
 * Polymorphism is emulated with structs and function pointers: each
 * state is a table of handlers, and transitions swap which table the
 * machine points at. For simple machines, a switch over an enum is the
 * more common C idiom; the function-pointer form scales better when
 * states carry behavior.
 */

#include <stdio.h>

struct VendingMachine;

typedef struct State {
    const char *name;
    void (*insert_coin)(struct VendingMachine *m);
    void (*select_item)(struct VendingMachine *m);
} State;

typedef struct VendingMachine {
    const State *state;
    int stock;
} VendingMachine;

static const State IDLE, HAS_COIN, SOLD_OUT;

static void idle_insert_coin(VendingMachine *m) {
    printf("coin accepted\n");
    m->state = &HAS_COIN;
}

static void idle_select_item(VendingMachine *m) {
    (void)m;
    printf("insert a coin first\n");
}

static void has_coin_insert_coin(VendingMachine *m) {
    (void)m;
    printf("coin already inserted, returning it\n");
}

static void has_coin_select_item(VendingMachine *m) {
    m->stock--;
    printf("item dispensed (%d left)\n", m->stock);
    m->state = (m->stock == 0) ? &SOLD_OUT : &IDLE;
}

static void sold_out_insert_coin(VendingMachine *m) {
    (void)m;
    printf("sold out, returning coin\n");
}

static void sold_out_select_item(VendingMachine *m) {
    (void)m;
    printf("sold out\n");
}

static const State IDLE = {"idle", idle_insert_coin, idle_select_item};
static const State HAS_COIN = {"has-coin", has_coin_insert_coin, has_coin_select_item};
static const State SOLD_OUT = {"sold-out", sold_out_insert_coin, sold_out_select_item};

void machine_insert_coin(VendingMachine *m) { m->state->insert_coin(m); }
void machine_select_item(VendingMachine *m) { m->state->select_item(m); }

int main(void) {
    VendingMachine machine = {&IDLE, 2};

    machine_select_item(&machine);  /* insert a coin first */
    machine_insert_coin(&machine);
    machine_insert_coin(&machine);  /* coin already inserted */
    machine_select_item(&machine);  /* item dispensed (1 left) */
    machine_insert_coin(&machine);
    machine_select_item(&machine);  /* item dispensed (0 left) */
    machine_insert_coin(&machine);  /* sold out, returning coin */
    return 0;
}
