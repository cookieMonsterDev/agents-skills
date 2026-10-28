<?php
/**
 * Abstraction in PHP.
 *
 * Callers see the essential model of a note store — save and load —
 * while each implementation hides its operational detail (an array vs
 * a file on disk). An interface names the contract explicitly.
 */

declare(strict_types=1);

interface NoteStore
{
    public function save(string $key, string $text): void;
    public function load(string $key): ?string;
}

final class MemoryStore implements NoteStore
{
  /** @var array<string, string> */
    private array $notes = [];

    public function save(string $key, string $text): void
    {
        $this->notes[$key] = $text;
    }

    public function load(string $key): ?string
    {
        return $this->notes[$key] ?? null;
    }
}

final class FileStore implements NoteStore
{
    public function __construct(private readonly string $path) {}

    public function save(string $key, string $text): void
    {
        file_put_contents($this->path, "$key\t$text\n", FILE_APPEND);
    }

    public function load(string $key): ?string
    {
        if (!is_file($this->path)) {
            return null;
        }
        $found = null;
        foreach (file($this->path, FILE_IGNORE_NEW_LINES) as $line) {
            [$k, $text] = array_pad(explode("\t", $line, 2), 2, '');
            if ($k === $key) {
                $found = $text;
            }
        }
        return $found;
    }
}

function runSession(NoteStore $store): void
{
    $store->save('groceries', 'eggs, flour');
    $store->save('groceries', 'eggs, flour, milk');
    $store->save('idea', 'hide the how, expose the what');
    echo '  groceries: ', $store->load('groceries'), PHP_EOL;
    echo '  idea:      ', $store->load('idea'), PHP_EOL;
    echo '  missing:   ', var_export($store->load('missing'), true), PHP_EOL;
}

echo "memory-backed store:\n";
runSession(new MemoryStore());

$path = 'abstraction_demo.txt';
try {
    echo "file-backed store:\n";
    runSession(new FileStore($path));
} finally {
    if (is_file($path)) {
        unlink($path);
    }
}
