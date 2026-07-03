<?php
// Interpreter pattern in PHP.
//
// A tiny arithmetic grammar: literals, variables, +, -, *. The classic
// form: an Expr interface with one class per grammar rule; a sentence
// is an object tree evaluated against an array of variable bindings.

declare(strict_types=1);

interface Expr
{
    /** @param array<string, int> $context */
    public function interpret(array $context): int;
}

final class Literal implements Expr
{
    public function __construct(private readonly int $value)
    {
    }

    public function interpret(array $context): int
    {
        return $this->value;
    }
}

final class Variable implements Expr
{
    public function __construct(private readonly string $name)
    {
    }

    public function interpret(array $context): int
    {
        return $context[$this->name];
    }
}

final class Add implements Expr
{
    public function __construct(private readonly Expr $left, private readonly Expr $right)
    {
    }

    public function interpret(array $context): int
    {
        return $this->left->interpret($context) + $this->right->interpret($context);
    }
}

final class Sub implements Expr
{
    public function __construct(private readonly Expr $left, private readonly Expr $right)
    {
    }

    public function interpret(array $context): int
    {
        return $this->left->interpret($context) - $this->right->interpret($context);
    }
}

final class Mul implements Expr
{
    public function __construct(private readonly Expr $left, private readonly Expr $right)
    {
    }

    public function interpret(array $context): int
    {
        return $this->left->interpret($context) * $this->right->interpret($context);
    }
}

// (x + y) * 2 - z
$expression = new Sub(
    new Mul(new Add(new Variable('x'), new Variable('y')), new Literal(2)),
    new Variable('z'),
);

foreach ([['x' => 6, 'y' => 2, 'z' => 3], ['x' => 1, 'y' => 1, 'z' => 10]] as $context) {
    printf(
        "(x + y) * 2 - z with %s = %d\n",
        json_encode($context),
        $expression->interpret($context),
    );
}
