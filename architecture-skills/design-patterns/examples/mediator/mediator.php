<?php
// Mediator pattern in PHP.
//
// The chat room centralizes routing so users never reference each other.
// Frameworks often provide this shape as an event dispatcher
// (e.g. Symfony EventDispatcher) acting as the mediator.

declare(strict_types=1);

final class ChatRoom
{
    /** @var array<string, User> */
    private array $users = [];

    public function register(User $user): void
    {
        $this->users[$user->name] = $user;
        $user->join($this);
    }

    public function broadcast(User $sender, string $text): void
    {
        foreach ($this->users as $user) {
            if ($user !== $sender) {
                $user->receive($sender->name, $text);
            }
        }
    }

    public function direct(User $sender, string $recipient, string $text): void
    {
        $user = $this->users[$recipient] ?? null;
        if ($user === null) {
            $sender->receive('room', "no such user: $recipient");
        } else {
            $user->receive($sender->name, "(dm) $text");
        }
    }
}

final class User
{
    private ?ChatRoom $room = null;

    public function __construct(public readonly string $name)
    {
    }

    public function join(ChatRoom $room): void
    {
        $this->room = $room;
    }

    public function say(string $text): void
    {
        $this->room->broadcast($this, $text);
    }

    public function dm(string $recipient, string $text): void
    {
        $this->room->direct($this, $recipient, $text);
    }

    public function receive(string $sender, string $text): void
    {
        echo "[{$this->name}] $sender: $text\n";
    }
}

$room = new ChatRoom();
$ada = new User('Ada');
$grace = new User('Grace');
$alan = new User('Alan');
foreach ([$ada, $grace, $alan] as $user) {
    $room->register($user);
}

$ada->say('Hello, everyone!');
$grace->dm('Ada', 'Hi Ada, got a minute?');
$alan->dm('Linus', 'ping');
