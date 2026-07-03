// Mediator pattern in JavaScript.
//
// A chat room routes messages between users. In Node or the browser the
// same decoupling is often built on an EventEmitter or EventTarget acting
// as the mediator; the explicit class makes the routing rules visible.

class ChatRoom {
  #users = new Map();

  register(user) {
    this.#users.set(user.name, user);
    user.room = this;
  }

  broadcast(sender, text) {
    for (const user of this.#users.values()) {
      if (user !== sender) {
        user.receive(sender.name, text);
      }
    }
  }

  direct(sender, recipient, text) {
    const user = this.#users.get(recipient);
    if (!user) {
      sender.receive("room", `no such user: ${recipient}`);
    } else {
      user.receive(sender.name, `(dm) ${text}`);
    }
  }
}

class User {
  constructor(name) {
    this.name = name;
    this.room = null;
  }

  say(text) {
    this.room.broadcast(this, text);
  }

  dm(recipient, text) {
    this.room.direct(this, recipient, text);
  }

  receive(sender, text) {
    console.log(`[${this.name}] ${sender}: ${text}`);
  }
}

const room = new ChatRoom();
const ada = new User("Ada");
const grace = new User("Grace");
const alan = new User("Alan");
for (const user of [ada, grace, alan]) {
  room.register(user);
}

ada.say("Hello, everyone!");
grace.dm("Ada", "Hi Ada, got a minute?");
alan.dm("Linus", "ping");
