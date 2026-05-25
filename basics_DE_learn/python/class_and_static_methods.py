"""
Class methods & static methods

INSTANCE METHOD   → first arg: self   → works on one employee (emp_1.fullname)
CLASS METHOD      → first arg: cls    → works on the class / factory patterns (Employee.from_string)
STATIC METHOD     → no self or cls     → utility in class namespace (Employee.is_workday)

@classmethod receives the CLASS (cls), not an instance — use for:
  - changing class variables for everyone: set_raise_amt
  - alternative constructors: from_string → builds and returns cls(...)

@staticmethod is a regular function grouped inside the class — use when logic
  does not need self or cls (e.g. is this date a weekday?).
"""

import datetime


class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    # --- Instance method: needs a specific employee (self) ---
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # --- Class method: cls is Employee (the class itself) ---
    @classmethod
    def set_raise_amt(cls, amount):
        """Update raise for ALL employees — changes class variable."""
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """Alternative constructor: 'First-Last-Pay' → new Employee instance."""
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))  # cls(...) same as Employee(...)

    # --- Static method: no instance or class data required ---
    @staticmethod
    def is_workday(day):
        """True Mon–Fri. weekday(): Mon=0 … Sun=6."""
        # Bug to avoid: day.weekday (no parens) is the function object, not the day number
        if day.weekday() >= 5:  # Saturday=5, Sunday=6
            return False
        return True


# --- Demo 1: @classmethod changes class variable for everyone ---
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print('--- set_raise_amt (class method) ---')
print('Before:', Employee.raise_amt, emp_1.raise_amt, emp_2.raise_amt)

Employee.set_raise_amt(1.05)  # same as Employee.set_raise_amt(1.05) — cls inside is Employee

print('After Employee.set_raise_amt(1.05):', Employee.raise_amt, emp_1.raise_amt, emp_2.raise_amt)
# All show 1.05 — unlike emp_1.raise_amt = 1.05 which only shadowed one instance

# --- Demo 2: @classmethod as alternative constructor ---
print('\n--- from_string (alternative constructor) ---')
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
# Behind the scenes: cls('John', 'Doe', 70000) → __init__ runs → real Employee object

print(new_emp_1.email)   # john.doe@company.com
print(new_emp_1.pay)     # 70000

# Equivalent manual call (usually you use from_string for clarity):
# new_emp_1 = Employee('John', 'Doe', 70000)

# --- Demo 3: @staticmethod — utility, no self/cls ---
print('\n--- is_workday (static method) ---')
monday = datetime.date(2026, 5, 25)   # weekday() == 0 → True
saturday = datetime.date(2026, 5, 30)  # weekday() == 5 → False
print(monday, 'is workday?', Employee.is_workday(monday))
print(saturday, 'is workday?', Employee.is_workday(saturday))

# Can call on instance too, but convention is ClassName.static_method(...)
# emp_1.is_workday(monday)  # works but misleading

# --- Quick reference ---
# | Type            | First arg | Typical use                          | Call example              |
# |-----------------|-----------|--------------------------------------|---------------------------|
# | Instance method | self      | Use one object's data                | emp_1.apply_raise()       |
# | Class method    | cls       | Class-wide config, alt constructors  | Employee.from_string(s)   |
# | Static method   | (none)    | Helper unrelated to instance/class   | Employee.is_workday(d)  |

# yt: https://www.youtube.com/watch?v=rq8cL2JZ5P4&list=PL-osiE80TeTsqIuOqKhwlXsIBIdSeYtc
