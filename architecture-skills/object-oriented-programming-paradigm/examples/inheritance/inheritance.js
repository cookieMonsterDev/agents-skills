// Inheritance in JavaScript.
//
// class/extends/super is syntax over the prototype chain: a method
// lookup walks Contractor -> Employee -> Object.prototype, so every
// method is "virtual" by nature. Manager extends the base pay rule via
// super.monthlyPay(); Contractor replaces it.

// Base class: the common payroll contract and default pay rule.
class Employee {
  constructor(name, baseSalary) {
    this.name = name;
    this.baseSalary = baseSalary;
  }

  get role() {
    return "employee";
  }

  monthlyPay() {
    return this.baseSalary;
  }

  payslip() {
    const pay = this.monthlyPay().toFixed(2);
    return `${this.name.padEnd(8)} ${this.role.padEnd(10)} $${pay.padStart(9)}`;
  }
}

// Extends the base rule: standard salary plus a per-report bonus.
class Manager extends Employee {
  constructor(name, baseSalary, directReports) {
    super(name, baseSalary); // required before touching `this`
    this.directReports = directReports;
  }

  get role() {
    return "manager";
  }

  monthlyPay() {
    // Call the base implementation, then extend it.
    return super.monthlyPay() + 400.0 * this.directReports;
  }
}

// Replaces the base rule outright: billed hours, no base salary.
class Contractor extends Employee {
  constructor(name, hourlyRate, hoursBilled) {
    super(name, 0);
    this.hourlyRate = hourlyRate;
    this.hoursBilled = hoursBilled;
  }

  get role() {
    return "contractor";
  }

  monthlyPay() {
    return this.hourlyRate * this.hoursBilled;
  }
}

// Payroll treats everyone as an Employee; the prototype chain dispatches.
const staff = [
  new Employee("Ada", 4200.0),
  new Manager("Grace", 6500.0, 5),
  new Contractor("Linus", 95.0, 140),
];

let total = 0;
for (const person of staff) {
  console.log(person.payslip());
  total += person.monthlyPay();
}
console.log(`${"total".padEnd(19)} $${total.toFixed(2).padStart(9)}`);
