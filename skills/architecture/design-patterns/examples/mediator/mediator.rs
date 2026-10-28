// Mediator pattern in Rust.
//
// Cross-references between colleagues fight the borrow checker, so the
// idiomatic shape is to let the mediator OWN the colleagues and address
// them by name/id. Callers talk to the room, never to another user.
// (The GoF form with shared colleagues needs Rc<RefCell<User>>.)

use std::collections::BTreeMap;

struct User {
    name: String,
}

impl User {
    fn receive(&self, sender: &str, text: &str) {
        println!("[{}] {}: {}", self.name, sender, text);
    }
}

struct ChatRoom {
    users: BTreeMap<String, User>,
}

impl ChatRoom {
    fn new() -> Self {
        Self {
            users: BTreeMap::new(),
        }
    }

    fn register(&mut self, name: &str) {
        self.users.insert(
            name.to_string(),
            User {
                name: name.to_string(),
            },
        );
    }

    fn broadcast(&self, sender: &str, text: &str) {
        for user in self.users.values() {
            if user.name != sender {
                user.receive(sender, text);
            }
        }
    }

    fn direct(&self, sender: &str, recipient: &str, text: &str) {
        match self.users.get(recipient) {
            Some(user) => user.receive(sender, &format!("(dm) {text}")),
            None => {
                if let Some(user) = self.users.get(sender) {
                    user.receive("room", &format!("no such user: {recipient}"));
                }
            }
        }
    }
}

fn main() {
    let mut room = ChatRoom::new();
    room.register("Ada");
    room.register("Grace");
    room.register("Alan");

    room.broadcast("Ada", "Hello, everyone!");
    room.direct("Grace", "Ada", "Hi Ada, got a minute?");
    room.direct("Alan", "Linus", "ping");
}
