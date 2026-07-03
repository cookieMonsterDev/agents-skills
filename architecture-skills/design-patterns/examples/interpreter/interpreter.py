"""Interpreter pattern in Python.

A tiny arithmetic grammar: literals, variables, +, -, *. Each grammar
rule is a node class with interpret(context); a sentence is an object
tree evaluated against a dict of variable bindings.

Note: when trees never need to be inspected or serialized, a plain
lambda (lambda env: env["x"] + 2) is often the simpler Python answer.
"""

from __future__ import annotations

from dataclasses import dataclass

Context = dict[str, int]


@dataclass(frozen=True)
class Literal:
    value: int

    def interpret(self, context: Context) -> int:
        return self.value


@dataclass(frozen=True)
class Variable:
    name: str

    def interpret(self, context: Context) -> int:
        return context[self.name]


@dataclass(frozen=True)
class Add:
    left: Literal | Variable | Add | Sub | Mul
    right: Literal | Variable | Add | Sub | Mul

    def interpret(self, context: Context) -> int:
        return self.left.interpret(context) + self.right.interpret(context)


@dataclass(frozen=True)
class Sub:
    left: Literal | Variable | Add | Sub | Mul
    right: Literal | Variable | Add | Sub | Mul

    def interpret(self, context: Context) -> int:
        return self.left.interpret(context) - self.right.interpret(context)


@dataclass(frozen=True)
class Mul:
    left: Literal | Variable | Add | Sub | Mul
    right: Literal | Variable | Add | Sub | Mul

    def interpret(self, context: Context) -> int:
        return self.left.interpret(context) * self.right.interpret(context)


if __name__ == "__main__":
    # (x + y) * 2 - z
    expression = Sub(Mul(Add(Variable("x"), Variable("y")), Literal(2)), Variable("z"))

    for context in ({"x": 6, "y": 2, "z": 3}, {"x": 1, "y": 1, "z": 10}):
        print(f"(x + y) * 2 - z with {context} = {expression.interpret(context)}")
