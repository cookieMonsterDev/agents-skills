/** Single Responsibility Principle in JavaScript.
 *
 * An Invoice that computes totals, formats itself, AND persists itself
 * serves three actors. The refactor gives each actor its own collaborator.
 */

class LineItem {
  constructor(description, amount) {
    this.description = description;
    this.amount = amount;
  }
}

class Invoice {
  constructor(invoiceId, customer) {
    this.invoiceId = invoiceId;
    this.customer = customer;
    this.items = [];
  }

  addItem(description, amount) {
    this.items.push(new LineItem(description, amount));
  }
}

class InvoiceCalculator {
  constructor(taxRate) {
    this.taxRate = taxRate;
  }

  total(invoice) {
    const subtotal = invoice.items.reduce((sum, i) => sum + i.amount, 0);
    return subtotal * (1 + this.taxRate);
  }
}

class TextInvoiceFormatter {
  format(invoice, total) {
    const lines = [`Invoice ${invoice.invoiceId} for ${invoice.customer}`];
    for (const item of invoice.items) {
      lines.push(`  ${item.description.padEnd(12)} $${item.amount.toFixed(2).padStart(7)}`);
    }
    lines.push(`  ${'TOTAL'.padEnd(12)} $${total.toFixed(2).padStart(7)}`);
    return lines.join('\n');
  }
}

class InMemoryInvoiceRepository {
  constructor() {
    this.rows = new Map();
  }

  save(invoice) {
    this.rows.set(invoice.invoiceId, invoice);
  }

  count() {
    return this.rows.size;
  }
}

const invoice = new Invoice('INV-042', 'ACME Corp');
invoice.addItem('Consulting', 1200.00);
invoice.addItem('Hosting', 90.00);

const calculator = new InvoiceCalculator(0.20);
const formatter = new TextInvoiceFormatter();
const repository = new InMemoryInvoiceRepository();

const total = calculator.total(invoice);
console.log(formatter.format(invoice, total));

repository.save(invoice);
console.log(`saved ${invoice.invoiceId} (${repository.count()} record(s) stored)`);
