<?php
// Memento pattern in PHP.
//
// Readonly properties make the snapshot immutable once created; the
// history stacks snapshots without interpreting them. For crude
// whole-object snapshots, clone (with __clone for deep copies) is a
// lighter alternative.

declare(strict_types=1);

/** Memento: immutable snapshot of editor state. */
final class Snapshot
{
    public function __construct(
        public readonly string $text,
        public readonly int $cursor,
    ) {
    }
}

/** Originator. */
final class TextEditor
{
    private string $text = '';
    private int $cursor = 0;

    public function type(string $insert): void
    {
        $this->text = substr($this->text, 0, $this->cursor)
            . $insert
            . substr($this->text, $this->cursor);
        $this->cursor += strlen($insert);
    }

    public function save(): Snapshot
    {
        return new Snapshot($this->text, $this->cursor);
    }

    public function restore(Snapshot $snapshot): void
    {
        $this->text = $snapshot->text;
        $this->cursor = $snapshot->cursor;
    }

    public function __toString(): string
    {
        return "'{$this->text}' (cursor at {$this->cursor})";
    }
}

/** Caretaker: stores snapshots but never inspects them. */
final class History
{
    /** @var list<Snapshot> */
    private array $snapshots = [];

    public function push(Snapshot $snapshot): void
    {
        $this->snapshots[] = $snapshot;
    }

    public function pop(): ?Snapshot
    {
        return array_pop($this->snapshots);
    }
}

$editor = new TextEditor();
$history = new History();

$editor->type('Hello');
$history->push($editor->save());
$editor->type(', world');
$history->push($editor->save());
$editor->type('!!!');
echo "current: $editor\n";

for ($i = 0; $i < 2; $i++) {
    $snapshot = $history->pop();
    if ($snapshot !== null) {
        $editor->restore($snapshot);
        echo "undo:    $editor\n";
    }
}
