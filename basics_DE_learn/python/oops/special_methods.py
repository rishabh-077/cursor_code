"""
Special (dunder) methods

DUNDER  → "double underscore" (__name__) — hooks Python calls for built-in behavior

__repr__  → developer-facing string; goal: unambiguous, ideally valid Python to recreate object
            Called by: repr(obj), and as fallback when __str__ is missing (e.g. in containers)

__str__   → user-facing string; goal: readable
            Called by: str(obj), print(obj)

__add__   → defines what + means for your class (emp_1 + emp_2)
            Without it, + raises TypeError. You choose the semantics (here: sum pay).

__len__   → defines what len(obj) returns
            Without it, len() raises TypeError. Here: length of full name string.

Rule of thumb:
  - Implement __repr__ for every class you care about in logs/debuggers
  - Add __str__ when print() should look nice for end users
  - Add other dunders only when you want that operator/function to work on your type
"""

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # --- __repr__: "official" object representation (debugging, REPL) ---
    def __repr__(self):
        # Should look like a constructor call — copy/paste into Python to recreate
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # --- __str__: human-readable string (print, str()) ---
    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    # --- __add__: custom + behavior (not limited to numbers!) ---
    def __add__(self, other):
        # Example: treat emp_1 + emp_2 as combined salary (could return a new Employee instead)
        return self.pay + other.pay

    # --- __len__: custom len() behavior ---
    def __len__(self):
        # len(emp_1) → number of characters in full name (including space)
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# repr vs str
print(repr(emp_1))   # Employee('Corey', 'Schafer', 50000)
print(str(emp_1))    # Corey Schafer - Corey.Schafer@email.com
print(emp_1)         # uses __str__ (falls back to __repr__ if __str__ missing)

print(emp_1 + emp_2)  # 110000  (__add__ returns combined pay, not a new Employee)

print(len(emp_1))  # 13  → len("Corey Schafer")
