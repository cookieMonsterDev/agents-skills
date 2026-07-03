/* Strategy pattern in C.
 *
 * A strategy in C is literally a function pointer: the context stores
 * the pointer and swapping algorithms means swapping pointers. A void*
 * context argument lets a strategy carry state (see carrier_rate).
 */

#include <stdio.h>

typedef struct {
    double weight_kg;
    double distance_km;
} Order;

typedef double (*ShippingStrategy)(const Order *order, void *ctx);

double flat_rate(const Order *order, void *ctx) {
    (void)order;
    (void)ctx;
    return 5.00;
}

double weight_based(const Order *order, void *ctx) {
    (void)ctx;
    return 4.00 + 1.50 * order->weight_kg;
}

double distance_based(const Order *order, void *ctx) {
    (void)ctx;
    return 2.00 + 0.05 * order->distance_km;
}

/* A stateful strategy: its configuration travels through the ctx pointer. */
typedef struct {
    double base;
    double per_kg;
} CarrierRate;

double carrier_rate(const Order *order, void *ctx) {
    const CarrierRate *rate = ctx;
    return rate->base + rate->per_kg * order->weight_kg;
}

/* Context: holds the current strategy and delegates to it. */
typedef struct {
    ShippingStrategy strategy;
    void *strategy_ctx;
} Checkout;

double checkout_shipping(const Checkout *c, const Order *order) {
    return c->strategy(order, c->strategy_ctx);
}

int main(void) {
    Order order = { 2.4, 120.0 };
    Checkout checkout = { flat_rate, NULL };

    printf("    flat: $%.2f\n", checkout_shipping(&checkout, &order));

    checkout.strategy = weight_based;
    printf("  weight: $%.2f\n", checkout_shipping(&checkout, &order));

    checkout.strategy = distance_based;
    printf("distance: $%.2f\n", checkout_shipping(&checkout, &order));

    CarrierRate negotiated = { 3.00, 2.00 };
    checkout.strategy = carrier_rate;
    checkout.strategy_ctx = &negotiated;
    printf(" carrier: $%.2f\n", checkout_shipping(&checkout, &order));

    return 0;
}
