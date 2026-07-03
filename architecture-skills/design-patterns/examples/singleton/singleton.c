/* Singleton pattern in C.
 *
 * A static variable inside the accessor function is the classic emulation:
 * it is created on first call and every caller gets the same address. For
 * multithreaded programs, guard the first initialization with C11
 * call_once or pthread_once. Prefer passing the struct in where feasible;
 * globals make tests order-dependent.
 */

#include <stdio.h>
#include <string.h>

typedef struct {
    char app_name[64];
    char db_url[128];
    char log_level[16];
} AppConfig;

/* Stands in for reading a config file once. */
static void load_config(AppConfig *config) {
    printf("Loading configuration (expensive, happens once)\n");
    strcpy(config->app_name, "InventoryService");
    strcpy(config->db_url, "postgres://localhost/inventory");
    strcpy(config->log_level, "INFO");
}

const AppConfig *app_config_instance(void) {
    static AppConfig instance;
    static int initialized = 0; /* use call_once/pthread_once with threads */

    if (!initialized) {
        load_config(&instance);
        initialized = 1;
    }
    return &instance;
}

int main(void) {
    const AppConfig *a = app_config_instance();
    const AppConfig *b = app_config_instance();

    printf("same instance: %s\n", a == b ? "true" : "false");
    printf("app_name: %s\n", a->app_name);
    printf("db_url: %s\n", b->db_url);
    return 0;
}
