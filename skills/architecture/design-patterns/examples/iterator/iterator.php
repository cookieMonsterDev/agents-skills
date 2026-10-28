<?php
// Iterator pattern in PHP.
//
// A binary search tree traversed in sorted order. PHP builds the
// pattern in: implementing IteratorAggregate with a generator (yield)
// plugs a custom collection into foreach and iterator_to_array — no
// hand-rolled current/next/valid Iterator class needed.

declare(strict_types=1);

final class Node
{
    public ?Node $left = null;
    public ?Node $right = null;

    public function __construct(public readonly int $value)
    {
    }
}

/** @implements IteratorAggregate<int, int> */
final class SortedTree implements IteratorAggregate
{
    private ?Node $root = null;

    public function add(int $value): void
    {
        if ($this->root === null) {
            $this->root = new Node($value);
            return;
        }
        $node = $this->root;
        while (true) {
            if ($value < $node->value) {
                if ($node->left === null) {
                    $node->left = new Node($value);
                    return;
                }
                $node = $node->left;
            } else {
                if ($node->right === null) {
                    $node->right = new Node($value);
                    return;
                }
                $node = $node->right;
            }
        }
    }

    public function getIterator(): Generator
    {
        yield from $this->walk($this->root);
    }

    private function walk(?Node $node): Generator
    {
        if ($node !== null) {
            yield from $this->walk($node->left);
            yield $node->value;
            yield from $this->walk($node->right);
        }
    }
}

$tree = new SortedTree();
foreach ([5, 3, 8, 1, 4, 9, 7] as $value) {
    $tree->add($value);
}

$inOrder = iterator_to_array($tree, false);
echo 'in order: ' . implode(' ', $inOrder) . "\n";
echo 'sum: ' . array_sum($inOrder) . "\n";

foreach ($tree as $value) {
    if ($value > 4) {
        echo "first value above 4: $value\n";
        break; // generators support early exit cleanly
    }
}
