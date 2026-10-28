"""Inheritance in Python.

Manager and Contractor are genuinely *is-a* Employee: payroll can pay
any of them through the base interface. Manager *extends* the base pay
rule by calling super().monthly_pay(); Contractor *replaces* it.
Python allows multiple inheritance; super() follows the MRO, which is
why cooperative __init__ chains always call super().__init__().
"""

from __future__ import annotations


class Employee:
    """Base class: the common payroll contract and default pay rule."""

    def __init__(self, name: str, base_salary: float) -> None:
        self.name = name
        self.base_salary = base_salary

    @property
    def role(self) -> str:
        return "employee"

    def monthly_pay(self) -> float:
        return self.base_salary

    def payslip(self) -> str:
        return f"{self.name:<8} {self.role:<10} ${self.monthly_pay():>9,.2f}"


class Manager(Employee):
    """Extends the base rule: standard salary plus a per-report bonus."""

    def __init__(self, name: str, base_salary: float, direct_reports: int) -> None:
        super().__init__(name, base_salary)
        self.direct_reports = direct_reports

    @property
    def role(self) -> str:
        return "manager"

    def monthly_pay(self) -> float:
        # Call the base implementation, then extend it.
        return super().monthly_pay() + 400.00 * self.direct_reports


class Contractor(Employee):
    """Replaces the base rule outright: billed hours, no base salary."""

    def __init__(self, name: str, hourly_rate: float, hours_billed: float) -> None:
        super().__init__(name, base_salary=0.0)
        self.hourly_rate = hourly_rate
        self.hours_billed = hours_billed

    @property
    def role(self) -> str:
        return "contractor"

    def monthly_pay(self) -> float:
        return self.hourly_rate * self.hours_billed


if __name__ == "__main__":
    # Payroll treats everyone as an Employee; dispatch picks the override.
    staff: list[Employee] = [
        Employee("Ada", 4_200.00),
        Manager("Grace", 6_500.00, direct_reports=5),
        Contractor("Linus", 95.00, hours_billed=140),
    ]
    for person in staff:
        print(person.payslip())
    print(f"{'total':<19} ${sum(p.monthly_pay() for p in staff):>9,.2f}")
