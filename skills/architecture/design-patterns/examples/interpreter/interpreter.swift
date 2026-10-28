// Interpreter pattern in Swift.
//
// A tiny arithmetic grammar: literals, variables, +, -, *. The idiomatic
// Swift form is an indirect enum with one case per grammar rule and a
// single switch in interpret() — no class hierarchy needed.

typealias Context = [String: Int]

indirect enum Expr {
    case literal(Int)
    case variable(String)
    case add(Expr, Expr)
    case sub(Expr, Expr)
    case mul(Expr, Expr)

    func interpret(_ context: Context) -> Int {
        switch self {
        case .literal(let value):
            return value
        case .variable(let name):
            return context[name] ?? 0
        case .add(let left, let right):
            return left.interpret(context) + right.interpret(context)
        case .sub(let left, let right):
            return left.interpret(context) - right.interpret(context)
        case .mul(let left, let right):
            return left.interpret(context) * right.interpret(context)
        }
    }
}

// (x + y) * 2 - z
let expression = Expr.sub(
    .mul(.add(.variable("x"), .variable("y")), .literal(2)),
    .variable("z")
)

let contexts: [Context] = [
    ["x": 6, "y": 2, "z": 3],
    ["x": 1, "y": 1, "z": 10],
]

for context in contexts {
    let bindings = context.sorted { $0.key < $1.key }
        .map { "\($0.key)=\($0.value)" }
        .joined(separator: " ")
    print("(x + y) * 2 - z with \(bindings) = \(expression.interpret(context))")
}
