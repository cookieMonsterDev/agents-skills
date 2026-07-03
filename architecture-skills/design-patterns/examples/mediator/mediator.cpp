// Mediator pattern in C++.
//
// The chat room owns the routing rules; users only hold a pointer to the
// mediator, never to each other. Raw non-owning pointers are fine here
// because the room does not manage user lifetimes.

#include <iostream>
#include <string>
#include <vector>

class User;

class ChatRoom {  // mediator
public:
    void registerUser(User* user);
    void broadcast(const User* sender, const std::string& text) const;
    void direct(const User* sender, const std::string& recipient,
                const std::string& text) const;

private:
    std::vector<User*> users_;
};

class User {  // colleague
public:
    User(std::string name) : name_(std::move(name)) {}

    const std::string& name() const { return name_; }

    void join(ChatRoom& room) {
        room_ = &room;
        room.registerUser(this);
    }

    void say(const std::string& text) const { room_->broadcast(this, text); }

    void dm(const std::string& recipient, const std::string& text) const {
        room_->direct(this, recipient, text);
    }

    void receive(const std::string& sender, const std::string& text) const {
        std::cout << '[' << name_ << "] " << sender << ": " << text << '\n';
    }

private:
    std::string name_;
    ChatRoom* room_ = nullptr;
};

void ChatRoom::registerUser(User* user) { users_.push_back(user); }

void ChatRoom::broadcast(const User* sender, const std::string& text) const {
    for (const User* user : users_) {
        if (user != sender) {
            user->receive(sender->name(), text);
        }
    }
}

void ChatRoom::direct(const User* sender, const std::string& recipient,
                      const std::string& text) const {
    for (const User* user : users_) {
        if (user->name() == recipient) {
            user->receive(sender->name(), "(dm) " + text);
            return;
        }
    }
    sender->receive("room", "no such user: " + recipient);
}

int main() {
    ChatRoom room;
    User ada("Ada");
    User grace("Grace");
    User alan("Alan");
    ada.join(room);
    grace.join(room);
    alan.join(room);

    ada.say("Hello, everyone!");
    grace.dm("Ada", "Hi Ada, got a minute?");
    alan.dm("Linus", "ping");
    return 0;
}
