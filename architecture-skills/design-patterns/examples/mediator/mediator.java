// Mediator pattern in Java.
//
// The chat room centralizes routing so users never reference each other.
// The mediator interface lets colleagues be tested against a fake room.

import java.util.LinkedHashMap;
import java.util.Map;

public class mediator {

    interface ChatMediator {
        void broadcast(User sender, String text);
        void direct(User sender, String recipient, String text);
    }

    static final class ChatRoom implements ChatMediator {
        private final Map<String, User> users = new LinkedHashMap<>();

        void register(User user) {
            users.put(user.name(), user);
            user.join(this);
        }

        @Override
        public void broadcast(User sender, String text) {
            for (User user : users.values()) {
                if (user != sender) {
                    user.receive(sender.name(), text);
                }
            }
        }

        @Override
        public void direct(User sender, String recipient, String text) {
            User user = users.get(recipient);
            if (user == null) {
                sender.receive("room", "no such user: " + recipient);
            } else {
                user.receive(sender.name(), "(dm) " + text);
            }
        }
    }

    static final class User {
        private final String name;
        private ChatMediator room;

        User(String name) {
            this.name = name;
        }

        String name() {
            return name;
        }

        void join(ChatMediator room) {
            this.room = room;
        }

        void say(String text) {
            room.broadcast(this, text);
        }

        void dm(String recipient, String text) {
            room.direct(this, recipient, text);
        }

        void receive(String sender, String text) {
            System.out.printf("[%s] %s: %s%n", name, sender, text);
        }
    }

    public static void main(String[] args) {
        ChatRoom room = new ChatRoom();
        User ada = new User("Ada");
        User grace = new User("Grace");
        User alan = new User("Alan");
        room.register(ada);
        room.register(grace);
        room.register(alan);

        ada.say("Hello, everyone!");
        grace.dm("Ada", "Hi Ada, got a minute?");
        alan.dm("Linus", "ping");
    }
}
