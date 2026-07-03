// Template Method pattern in JavaScript.
//
// The class form relies on subclasses overriding methods the base class
// calls. In practice JS often prefers a higher-order function that takes
// the varying steps as an object of functions — both forms are shown.

class SalesReport {
  // The template method: iteration and totalling never vary.
  generate(items) {
    const lines = [this.header()];
    let total = 0;
    for (const item of items) {
      const subtotal = item.units * item.price;
      lines.push(this.row(item, subtotal));
      total += subtotal;
    }
    lines.push(this.footer(total));
    return lines.join("\n");
  }

  header() {
    throw new Error("subclass must implement header()");
  }

  row(item, subtotal) {
    throw new Error("subclass must implement row()");
  }

  footer(total) {
    throw new Error("subclass must implement footer()");
  }
}

class CsvReport extends SalesReport {
  header() {
    return "product,units,price,subtotal";
  }

  row(item, subtotal) {
    return `${item.product},${item.units},${item.price.toFixed(2)},${subtotal.toFixed(2)}`;
  }

  footer(total) {
    return `total,,,${total.toFixed(2)}`;
  }
}

// --- Alternative: composition with a steps object (often preferred) ---

function generateReport(steps, items) {
  const lines = [steps.header()];
  let total = 0;
  for (const item of items) {
    const subtotal = item.units * item.price;
    lines.push(steps.row(item, subtotal));
    total += subtotal;
  }
  lines.push(steps.footer(total));
  return lines.join("\n");
}

const markdownSteps = {
  header: () => "| Product | Units | Subtotal |\n| --- | --- | --- |",
  row: (item, subtotal) => `| ${item.product} | ${item.units} | $${subtotal.toFixed(2)} |`,
  footer: (total) => `\n**Total: $${total.toFixed(2)}**`,
};

const items = [
  { product: "Keyboard", units: 2, price: 80.0 },
  { product: "Mouse", units: 1, price: 25.5 },
  { product: "Monitor", units: 3, price: 210.0 },
];

console.log("--- CsvReport (inheritance) ---");
console.log(new CsvReport().generate(items));
console.log();
console.log("--- MarkdownReport (composition) ---");
console.log(generateReport(markdownSteps, items));
