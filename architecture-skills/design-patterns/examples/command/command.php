<?php
// Command pattern in PHP.
//
// Text editor with undo: a Command interface with execute/undo, concrete
// commands capturing their own undo state, and a history stack as the
// invoker. For one-shot commands without undo, a closure is the lighter
// idiom (framework job queues are commands in production form).

declare(strict_types=1);

final class Editor // receiver
{
    public string $text = '';
}

interface Command
{
    public function execute(): void;

    public function undo(): void;
}

final class InsertText implements Command
{
    public function __construct(
        private readonly Editor $editor,
        private readonly string $text,
    ) {
    }

    public function execute(): void
    {
        $this->editor->text .= $this->text;
    }

    public function undo(): void
    {
        $this->editor->text = substr($this->editor->text, 0, -strlen($this->text));
    }
}

final class DeleteLast implements Command
{
    private string $deleted = ''; // captured on execute so undo can restore it

    public function __construct(
        private readonly Editor $editor,
        private readonly int $count,
    ) {
    }

    public function execute(): void
    {
        $this->deleted = substr($this->editor->text, -$this->count);
        $this->editor->text = substr($this->editor->text, 0, -$this->count);
    }

    public function undo(): void
    {
        $this->editor->text .= $this->deleted;
    }
}

final class History // invoker
{
    /** @var Command[] */
    private array $undoStack = [];

    public function execute(Command $command): void
    {
        $command->execute();
        $this->undoStack[] = $command;
    }

    public function undo(): void
    {
        $command = array_pop($this->undoStack);
        $command?->undo();
    }
}

$editor = new Editor();
$history = new History();

$history->execute(new InsertText($editor, 'Hello'));
$history->execute(new InsertText($editor, ', world!'));
$history->execute(new DeleteLast($editor, 1));
printf("after edits: \"%s\"\n", $editor->text);

$history->undo();
$history->undo();
printf("after 2 undos: \"%s\"\n", $editor->text);
