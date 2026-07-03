<?php
// Composite pattern in PHP.
//
// Files and directories implement one Node interface, so callers can
// total sizes or print trees without distinguishing leaf from branch.
// The classes carry a "Node" suffix because PHP already has a built-in
// Directory class.

interface Node
{
    public function size(): int;
    public function print(int $indent = 0): void;
}

class FileNode implements Node
{
    public function __construct(
        private string $name,
        private int $bytes,
    ) {}

    public function size(): int
    {
        return $this->bytes;
    }

    public function print(int $indent = 0): void
    {
        printf("%s%s (%d B)\n", str_repeat(' ', $indent), $this->name, $this->bytes);
    }
}

class DirectoryNode implements Node
{
    /** @var Node[] */
    private array $children = [];

    public function __construct(private string $name) {}

    public function add(Node $child): static
    {
        $this->children[] = $child;
        return $this;
    }

    public function size(): int
    {
        return array_sum(array_map(fn (Node $child) => $child->size(), $this->children));
    }

    public function print(int $indent = 0): void
    {
        printf("%s%s/ (%d B)\n", str_repeat(' ', $indent), $this->name, $this->size());
        foreach ($this->children as $child) {
            $child->print($indent + 2);
        }
    }
}

$project = (new DirectoryNode('project'))
    ->add((new DirectoryNode('src'))
        ->add(new FileNode('main.py', 1200))
        ->add(new FileNode('util.py', 450)))
    ->add((new DirectoryNode('docs'))->add(new FileNode('readme.md', 800)))
    ->add(new FileNode('.gitignore', 20));

$project->print();
