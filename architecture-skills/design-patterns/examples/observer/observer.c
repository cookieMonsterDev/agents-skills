/* Observer pattern in C.
 *
 * Polymorphism is emulated with function pointers: each observer is a
 * callback plus a context pointer (the C idiom for closures). The
 * ticker walks its observer array on every price change.
 */

#include <stdio.h>
#include <string.h>

#define MAX_OBSERVERS 8

typedef void (*PriceObserver)(void *context, const char *symbol, double price);

typedef struct {
    PriceObserver notify;
    void *context;
} Subscription;

typedef struct {
    Subscription observers[MAX_OBSERVERS];
    int count;
} StockTicker; /* subject */

void ticker_subscribe(StockTicker *t, PriceObserver notify, void *context) {
    t->observers[t->count].notify = notify;
    t->observers[t->count].context = context;
    t->count++;
}

void ticker_update_price(StockTicker *t, const char *symbol, double price) {
    for (int i = 0; i < t->count; i++) {
        t->observers[i].notify(t->observers[i].context, symbol, price);
    }
}

/* Observer 1: a named display board. */
void display_on_price(void *context, const char *symbol, double price) {
    const char *name = context;
    printf("%s: %s is now $%.2f\n", name, symbol, price);
}

/* Observer 2: a threshold alert; context carries its configuration. */
typedef struct {
    char symbol[16];
    double threshold;
} Alert;

void alert_on_price(void *context, const char *symbol, double price) {
    const Alert *alert = context;
    if (strcmp(symbol, alert->symbol) == 0 && price > alert->threshold) {
        printf("ALERT: %s crossed $%.2f (now $%.2f)\n",
               alert->symbol, alert->threshold, price);
    }
}

int main(void) {
    StockTicker ticker = {0};
    Alert acme_alert = {"ACME", 100.0};

    ticker_subscribe(&ticker, display_on_price, "Lobby display");
    ticker_subscribe(&ticker, alert_on_price, &acme_alert);

    ticker_update_price(&ticker, "ACME", 98.5);
    ticker_update_price(&ticker, "ACME", 101.25);
    ticker_update_price(&ticker, "GLOBEX", 45.0);
    return 0;
}
