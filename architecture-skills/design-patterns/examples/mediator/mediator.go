// Mediator pattern in Go.
//
// The chat room implements a small mediator interface, so users depend
// on behavior rather than a concrete type. For concurrent designs, Go
// often replaces this with a goroutine owning a channel of messages
// (the goroutine itself becomes the mediator).

package main

import "fmt"

type Mediator interface {
	Broadcast(sender *User, text string)
	Direct(sender *User, recipient, text string)
}

type User struct {
	Name string
	room Mediator
}

func (u *User) Say(text string)              { u.room.Broadcast(u, text) }
func (u *User) Dm(recipient, text string)    { u.room.Direct(u, recipient, text) }
func (u *User) Receive(sender, text string)  { fmt.Printf("[%s] %s: %s\n", u.Name, sender, text) }

type ChatRoom struct {
	users map[string]*User
	order []string
}

func NewChatRoom() *ChatRoom {
	return &ChatRoom{users: map[string]*User{}}
}

func (r *ChatRoom) Register(user *User) {
	r.users[user.Name] = user
	r.order = append(r.order, user.Name)
	user.room = r
}

func (r *ChatRoom) Broadcast(sender *User, text string) {
	for _, name := range r.order {
		if user := r.users[name]; user != sender {
			user.Receive(sender.Name, text)
		}
	}
}

func (r *ChatRoom) Direct(sender *User, recipient, text string) {
	user, ok := r.users[recipient]
	if !ok {
		sender.Receive("room", "no such user: "+recipient)
		return
	}
	user.Receive(sender.Name, "(dm) "+text)
}

func main() {
	room := NewChatRoom()
	ada := &User{Name: "Ada"}
	grace := &User{Name: "Grace"}
	alan := &User{Name: "Alan"}
	room.Register(ada)
	room.Register(grace)
	room.Register(alan)

	ada.Say("Hello, everyone!")
	grace.Dm("Ada", "Hi Ada, got a minute?")
	alan.Dm("Linus", "ping")
}
