/* Builder pattern in C.
 *
 * C has no methods or chaining, so the builder is a plain struct that
 * accumulates configuration, plus a build function that validates and
 * produces the finished product.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char method[8];
    char url[256];
    char content_type[64];
    char body[1024];
    double timeout_seconds;
} HttpRequest; /* product */

typedef struct {
    char method[8];
    char url[256];
    char content_type[64];
    char body[1024];
    double timeout_seconds;
    int has_body;
} HttpRequestBuilder;

void builder_init(HttpRequestBuilder *b, const char *method, const char *url) {
    memset(b, 0, sizeof(*b));
    strncpy(b->method, method, sizeof(b->method) - 1);
    strncpy(b->url, url, sizeof(b->url) - 1);
    b->timeout_seconds = 30.0;
}

void builder_set_content_type(HttpRequestBuilder *b, const char *value) {
    strncpy(b->content_type, value, sizeof(b->content_type) - 1);
}

void builder_set_body(HttpRequestBuilder *b, const char *body) {
    strncpy(b->body, body, sizeof(b->body) - 1);
    b->has_body = 1;
}

void builder_set_timeout(HttpRequestBuilder *b, double seconds) {
    b->timeout_seconds = seconds;
}

/* Returns 0 on success, -1 on validation failure. */
int builder_build(const HttpRequestBuilder *b, HttpRequest *out) {
    if (b->has_body && (strcmp(b->method, "GET") == 0 || strcmp(b->method, "HEAD") == 0)) {
        fprintf(stderr, "%s requests cannot have a body\n", b->method);
        return -1;
    }
    strcpy(out->method, b->method);
    strcpy(out->url, b->url);
    strcpy(out->content_type, b->content_type);
    strcpy(out->body, b->body);
    out->timeout_seconds = b->timeout_seconds;
    return 0;
}

int main(void) {
    HttpRequestBuilder builder;
    builder_init(&builder, "POST", "https://api.example.com/users");
    builder_set_content_type(&builder, "application/json");
    builder_set_body(&builder, "{\"name\": \"Ada\"}");
    builder_set_timeout(&builder, 5.0);

    HttpRequest request;
    if (builder_build(&builder, &request) != 0) {
        return EXIT_FAILURE;
    }

    printf("%s %s (timeout %.1fs)\n", request.method, request.url, request.timeout_seconds);
    printf("Content-Type: %s\n", request.content_type);
    printf("%s\n", request.body);
    return EXIT_SUCCESS;
}
