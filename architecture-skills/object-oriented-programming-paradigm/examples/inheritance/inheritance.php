<?php
/**
 * Inheritance in PHP.
 *
 * Manager and Contractor are genuinely is-a Employee: payroll can pay
 * any of them through the base class. Manager extends the base pay
 * rule via parent::monthlyPay(); Contractor replaces it.
 */

declare(strict_types=1);

class Employee
{
    public function __construct(
        protected string $name,
        protected float $baseSalary,
    ) {}

    public function role(): string
    {
        return 'employee';
    }

    public function monthlyPay(): float
    {
        return $this->baseSalary;
    }

    public function payslip(): string
    {
        return sprintf('%-8s %-10s $%9.2f', $this->name, $this->role(), $this->monthlyPay());
    }
}

final class Manager extends Employee
{
    public function __construct(
        string $name,
        float $baseSalary,
        private readonly int $directReports,
    ) {
        parent::__construct($name, $baseSalary);
    }

    public function role(): string
    {
        return 'manager';
    }

    public function monthlyPay(): float
    {
        return parent::monthlyPay() + 400.00 * $this->directReports;
    }
}

final class Contractor extends Employee
{
    public function __construct(
        string $name,
        private readonly float $hourlyRate,
        private readonly float $hoursBilled,
    ) {
        parent::__construct($name, 0.0);
    }

    public function role(): string
    {
        return 'contractor';
    }

    public function monthlyPay(): float
    {
        return $this->hourlyRate * $this->hoursBilled;
    }
}

/** @var Employee[] */
$staff = [
    new Employee('Ada', 4200.00),
    new Manager('Grace', 6500.00, 5),
    new Contractor('Linus', 95.00, 140.0),
];

$total = 0.0;
foreach ($staff as $person) {
    echo $person->payslip(), PHP_EOL;
    $total += $person->monthlyPay();
}
printf("%-19s $%9.2f\n", 'total', $total);
