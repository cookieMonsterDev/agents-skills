// Interpreter pattern in Java.
//
// A tiny arithmetic grammar: literals, variables, +, -, *. A sealed
// interface with one record per grammar rule keeps the class-per-rule
// structure compact; a sentence is a record tree evaluated against a
// map of variable bindings.

import java.util.Map;

public class interpreter {

    sealed interface Expr permits Literal, Variable, Add, Sub, Mul {
        int interpret(Map<String, Integer> context);
    }

    record Literal(int value) implements Expr {
        public int interpret(Map<String, Integer> context) {
            return value;
        }
    }

    record Variable(String name) implements Expr {
        public int interpret(Map<String, Integer> context) {
            return context.get(name);
        }
    }

    record Add(Expr left, Expr right) implements Expr {
        public int interpret(Map<String, Integer> context) {
            return left.interpret(context) + right.interpret(context);
        }
    }

    record Sub(Expr left, Expr right) implements Expr {
        public int interpret(Map<String, Integer> context) {
            return left.interpret(context) - right.interpret(context);
        }
    }

    record Mul(Expr left, Expr right) implements Expr {
        public int interpret(Map<String, Integer> context) {
            return left.interpret(context) * right.interpret(context);
        }
    }

    public static void main(String[] args) {
        // (x + y) * 2 - z
        Expr expression = new Sub(
                new Mul(new Add(new Variable("x"), new Variable("y")), new Literal(2)),
                new Variable("z"));

        Map<String, Integer> first = Map.of("x", 6, "y", 2, "z", 3);
        Map<String, Integer> second = Map.of("x", 1, "y", 1, "z", 10);

        System.out.println("(x + y) * 2 - z with x=6 y=2 z=3   = " + expression.interpret(first));
        System.out.println("(x + y) * 2 - z with x=1 y=1 z=10  = " + expression.interpret(second));
    }
}
