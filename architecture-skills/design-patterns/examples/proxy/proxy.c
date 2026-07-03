/* Proxy pattern in C (virtual proxy: lazy-loading image).
 *
 * Polymorphism is emulated with a struct of function pointers — a
 * hand-rolled vtable. Both the real image and the proxy start with the
 * same Image "base", so callers hold an Image* and cannot tell which
 * one they are talking to.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Image {
    void (*display)(struct Image *self);
} Image; /* subject interface */

/* --- real subject: expensive to create --- */

typedef struct {
    Image base;
    char filename[64];
} RealImage;

static void real_image_display(Image *self) {
    RealImage *img = (RealImage *)self;
    printf("Displaying %s\n", img->filename);
}

Image *real_image_new(const char *filename) {
    printf("Loading %s from disk (expensive)\n", filename);
    RealImage *img = malloc(sizeof(RealImage));
    img->base.display = real_image_display;
    strncpy(img->filename, filename, sizeof(img->filename) - 1);
    img->filename[sizeof(img->filename) - 1] = '\0';
    return &img->base;
}

/* --- virtual proxy: defers creating the real image until first use --- */

typedef struct {
    Image base;
    char filename[64];
    Image *real;
} ImageProxy;

static void image_proxy_display(Image *self) {
    ImageProxy *proxy = (ImageProxy *)self;
    if (proxy->real == NULL) {
        proxy->real = real_image_new(proxy->filename);
    }
    proxy->real->display(proxy->real);
}

Image *image_proxy_new(const char *filename) {
    ImageProxy *proxy = malloc(sizeof(ImageProxy));
    proxy->base.display = image_proxy_display;
    strncpy(proxy->filename, filename, sizeof(proxy->filename) - 1);
    proxy->filename[sizeof(proxy->filename) - 1] = '\0';
    proxy->real = NULL;
    return &proxy->base;
}

void image_proxy_free(Image *self) {
    ImageProxy *proxy = (ImageProxy *)self;
    free(proxy->real); /* NULL-safe */
    free(proxy);
}

int main(void) {
    Image *holiday = image_proxy_new("holiday.png");
    Image *unused = image_proxy_new("unused.png");
    printf("Proxies created; nothing loaded yet\n");

    holiday->display(holiday);
    holiday->display(holiday); /* loaded once, displayed twice */

    printf("unused.png was never loaded\n");
    image_proxy_free(holiday);
    image_proxy_free(unused);
    return 0;
}
