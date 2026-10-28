// Mediator pattern in Swift.
//
// The chat room mediates between users via a protocol. Users hold a weak
// reference to the room to avoid a retain cycle (the room strongly holds
// its users). NotificationCenter is the stdlib's built-in mediator for
// broadcast-style decoupling.

import Foundation

protocol ChatMediator: AnyObject {
    func broadcast(from sender: User, text: String)
    func direct(from sender: User, to recipient: String, text: String)
}

final class User {
    let name: String
    weak var room: ChatMediator?

    init(name: String) {
        self.name = name
    }

    func say(_ text: String) {
        room?.broadcast(from: self, text: text)
    }

    func dm(_ recipient: String, _ text: String) {
        room?.direct(from: self, to: recipient, text: text)
    }

    func receive(from sender: String, text: String) {
        print("[\(name)] \(sender): \(text)")
    }
}

final class ChatRoom: ChatMediator {
    private var users: [User] = []

    func register(_ user: User) {
        users.append(user)
        user.room = self
    }

    func broadcast(from sender: User, text: String) {
        for user in users where user !== sender {
            user.receive(from: sender.name, text: text)
        }
    }

    func direct(from sender: User, to recipient: String, text: String) {
        guard let user = users.first(where: { $0.name == recipient }) else {
            sender.receive(from: "room", text: "no such user: \(recipient)")
            return
        }
        user.receive(from: sender.name, text: "(dm) \(text)")
    }
}

let room = ChatRoom()
let ada = User(name: "Ada")
let grace = User(name: "Grace")
let alan = User(name: "Alan")
for user in [ada, grace, alan] {
    room.register(user)
}

ada.say("Hello, everyone!")
grace.dm("Ada", "Hi Ada, got a minute?")
alan.dm("Linus", "ping")
