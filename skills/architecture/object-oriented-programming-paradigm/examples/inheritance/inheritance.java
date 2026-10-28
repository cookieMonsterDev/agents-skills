// Inheritance in Java.
//
// Java allows a single superclass; every non-final method is virtual by
// default. Manager extends the base pay rule via super.monthlyPay();
// Contractor is `final`, closing it to further subclassing. (Java 17+
// `sealed` can instead whitelist the permitted subclasses up front.)

import java.util.List;

public class inheritance {

    /** Base class: the common payroll contract and default pay rule. */
    static class Employee {
        protected final String name;
        protected final double baseSalary;

        Employee(String name, double baseSalary) {
            this.name = name;
            this.baseSalary = baseSalary;
        }

        String role() {
            return "employee";
        }

        double monthlyPay() {
            return baseSalary;
        }

        void printPayslip() {
            System.out.printf("%-8s %-10s $%,9.2f%n", name, role(), monthlyPay());
        }
    }

    /** Extends the base rule: standard salary plus a per-report bonus. */
    static class Manager extends Employee {
        private final int directReports;

        Manager(String name, double baseSalary, int directReports) {
            super(name, baseSalary);
            this.directReports = directReports;
        }

        @Override
        String role() {
            return "manager";
        }

        @Override
        double monthlyPay() {
            // Call the base implementation, then extend it.
            return super.monthlyPay() + 400.00 * directReports;
        }
    }

    /** Replaces the base rule outright: billed hours, no base salary. */
    static final class Contractor extends Employee {
        private final double hourlyRate;
        private final double hoursBilled;

        Contractor(String name, double hourlyRate, double hoursBilled) {
            super(name, 0.0);
            this.hourlyRate = hourlyRate;
            this.hoursBilled = hoursBilled;
        }

        @Override
        String role() {
            return "contractor";
        }

        @Override
        double monthlyPay() {
            return hourlyRate * hoursBilled; // full replacement
        }
    }

    public static void main(String[] args) {
        // Payroll treats everyone as an Employee; dispatch picks the override.
        List<Employee> staff = List.of(
            new Employee("Ada", 4200.00),
            new Manager("Grace", 6500.00, 5),
            new Contractor("Linus", 95.00, 140.0));

        double total = 0.0;
        for (Employee person : staff) {
            person.printPayslip();
            total += person.monthlyPay();
        }
        System.out.printf("%-19s $%,9.2f%n", "total", total);
    }
}
