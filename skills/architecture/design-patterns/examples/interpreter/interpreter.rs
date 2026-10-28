// Interpreter pattern in Rust.
//
// A tiny arithmetic grammar: literals, variables, +, -, *. The idiomatic
// Rust form is an enum with one variant per grammar rule and a single
// match in eval() — no trait objects or class hierarchy needed. Boxed
// children make the type recursive.

use std::collections::HashMap;

type Context = HashMap<&'static str, i64>;

enum Expr {
    Literal(i64),
    Variable(&'static str),
    Add(Box<Expr>, Box<Expr>),
    Sub(Box<Expr>, Box<Expr>),
    Mul(Box<Expr>, Box<Expr>),
}

impl Expr {
    fn interpret(&self, context: &Context) -> i64 {
        match self {
            Expr::Literal(value) => *value,
            Expr::Variable(name) => context[name],
            Expr::Add(left, right) => left.interpret(context) + right.interpret(context),
            Expr::Sub(left, right) => left.interpret(context) - right.interpret(context),
            Expr::Mul(left, right) => left.interpret(context) * right.interpret(context),
        }
    }
}

fn main() {
    // (x + y) * 2 - z
    let expression = Expr::Sub(
        Box::new(Expr::Mul(
            Box::new(Expr::Add(
                Box::new(Expr::Variable("x")),
                Box::new(Expr::Variable("y")),
            )),
            Box::new(Expr::Literal(2)),
        )),
        Box::new(Expr::Variable("z")),
    );

    let first = Context::from([("x", 6), ("y", 2), ("z", 3)]);
    let second = Context::from([("x", 1), ("y", 1), ("z", 10)]);

    println!(
        "(x + y) * 2 - z with x=6 y=2 z=3   = {}",
        expression.interpret(&first)
    );
    println!(
        "(x + y) * 2 - z with x=1 y=1 z=10  = {}",
        expression.interpret(&second)
    );
}
