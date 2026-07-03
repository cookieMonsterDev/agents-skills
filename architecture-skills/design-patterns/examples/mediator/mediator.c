/* Mediator pattern in C.
 *
 * Polymorphism is emulated with structs and function pointers: each
 * user carries a `receive` callback that the chat room (mediator)
 * invokes when routing messages, so users never call each other.
 */

#include <stdio.h>
#include <string.h>

#define MAX_USERS 8

struct ChatRoom;

typedef struct User {
    const char *name;
    struct ChatRoom *room;
    void (*receive)(struct User *self, const char *sender, const char *text);
} User;

typedef struct ChatRoom {
    User *users[MAX_USERS];
    int count;
} ChatRoom;

void room_register(ChatRoom *room, User *user) {
    room->users[room->count++] = user;
    user->room = room;
}

void room_broadcast(ChatRoom *room, User *sender, const char *text) {
    for (int i = 0; i < room->count; i++) {
        User *user = room->users[i];
        if (user != sender) {
            user->receive(user, sender->name, text);
        }
    }
}

void room_direct(ChatRoom *room, User *sender, const char *recipient, const char *text) {
    for (int i = 0; i < room->count; i++) {
        User *user = room->users[i];
        if (strcmp(user->name, recipient) == 0) {
            char message[256];
            snprintf(message, sizeof(message), "(dm) %s", text);
            user->receive(user, sender->name, message);
            return;
        }
    }
    char message[256];
    snprintf(message, sizeof(message), "no such user: %s", recipient);
    sender->receive(sender, "room", message);
}

void user_say(User *user, const char *text) {
    room_broadcast(user->room, user, text);
}

void user_dm(User *user, const char *recipient, const char *text) {
    room_direct(user->room, user, recipient, text);
}

void user_receive(User *self, const char *sender, const char *text) {
    printf("[%s] %s: %s\n", self->name, sender, text);
}

int main(void) {
    ChatRoom room = {0};
    User ada = {"Ada", NULL, user_receive};
    User grace = {"Grace", NULL, user_receive};
    User alan = {"Alan", NULL, user_receive};

    room_register(&room, &ada);
    room_register(&room, &grace);
    room_register(&room, &alan);

    user_say(&ada, "Hello, everyone!");
    user_dm(&grace, "Ada", "Hi Ada, got a minute?");
    user_dm(&alan, "Linus", "ping");
    return 0;
}
