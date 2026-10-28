/* Factory Method pattern in C.
 *
 * C has no classes or inheritance, so the creator is emulated as a struct
 * holding a `create` function pointer. The shared workflow function
 * (plan_delivery) calls through the pointer, and each concrete creator
 * supplies its own constructor.
 */

#include <stdio.h>

/* Product: a transport with its own deliver behavior. */
typedef struct Transport {
    const char *name;
    void (*deliver)(const struct Transport *self, const char *cargo);
} Transport;

static void truck_deliver(const Transport *self, const char *cargo) {
    printf("%s delivers %s by road in a box\n", self->name, cargo);
}

static void ship_deliver(const Transport *self, const char *cargo) {
    printf("%s delivers %s by sea in a container\n", self->name, cargo);
}

static Transport create_truck(void) {
    Transport t = { "Truck", truck_deliver };
    return t;
}

static Transport create_ship(void) {
    Transport t = { "Ship", ship_deliver };
    return t;
}

/* Creator: the factory method is a function pointer. */
typedef struct {
    const char *name;
    Transport (*create_transport)(void);
} Logistics;

static const Logistics ROAD_LOGISTICS = { "RoadLogistics", create_truck };
static const Logistics SEA_LOGISTICS = { "SeaLogistics", create_ship };

/* Shared workflow: uses whatever transport the creator produces. */
static void plan_delivery(const Logistics *logistics, const char *cargo) {
    Transport transport = logistics->create_transport();
    printf("[%s] ", logistics->name);
    transport.deliver(&transport, cargo);
}

int main(void) {
    plan_delivery(&ROAD_LOGISTICS, "machine parts");
    plan_delivery(&SEA_LOGISTICS, "machine parts");
    return 0;
}
