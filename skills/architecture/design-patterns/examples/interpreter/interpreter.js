// Interpreter pattern in JavaScript.
//
// A tiny arithmetic grammar: literals, variables, +, -, *. In JS the
// idiomatic form skips classes entirely: each grammar rule is a factory
// returning an evaluator function (env) => number, and composing
// factories builds the expression tree.

const literal = (value) => () => value;
const variable = (name) => (env) => env[name];
const add = (left, right) => (env) => left(env) + right(env);
const sub = (left, right) => (env) => left(env) - right(env);
const mul = (left, right) => (env) => left(env) * right(env);

// (x + y) * 2 - z
const expression = sub(mul(add(variable("x"), variable("y")), literal(2)), variable("z"));

const contexts = [
  { x: 6, y: 2, z: 3 },
  { x: 1, y: 1, z: 10 },
];

for (const context of contexts) {
  console.log(`(x + y) * 2 - z with ${JSON.stringify(context)} = ${expression(context)}`);
}

// Class-based nodes (the literal GoF form) are only worth it when the
// tree must be inspected, transformed, or serialized — closures are
// opaque. A minimal node form for that case:
const node = {
  interpret: (env) => env.x + 2,
  toString: () => "x + 2",
};
console.log(`${node} with x=40 = ${node.interpret({ x: 40 })}`);
