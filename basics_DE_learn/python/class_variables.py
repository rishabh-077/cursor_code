"""
Class variables vs instance variables

INSTANCE VARIABLE  → self.first, self.pay     → unique per object (emp_1, emp_2)
CLASS VARIABLE     → Employee.raise_amount   → shared by all instances (one copy on the class)

Lookup order when you read emp_1.raise_amount:
  1) instance dict  →  2) class dict  →  3) parent classes
Assigning emp_1.raise_amount = 1.05 creates an INSTANCE attribute — it does NOT change the class variable for others.
"""

class Employee:
    # --- Class variables (defined on the class, shared by all employees) ---
    num_of_emps = 0       # counter: every __init__ bumps this
    raise_amount = 1.04   # default 4% raise unless an instance overrides it

    def __init__(self, first, last, pay):
        # --- Instance variables (self.*) — each employee has their own ---
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Use Employee.num_of_emps (or self.num_of_emps) to update the shared counter
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.raise_amount uses lookup: instance first, then class (1.04 or 1.05 if overridden)
        self.pay = int(self.pay * self.raise_amount)


# --- Demo 1: class variable as shared state ---
print('--- num_of_emps (shared counter) ---')
print(Employee.num_of_emps)  # 0 — no employees yet

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.num_of_emps)  # 2 — both instances ran __init__
# print(emp_1.num_of_emps)   # also 2 (same object as Employee.num_of_emps)

# --- Demo 2: class variable vs instance override ---
print('\n--- raise_amount (class vs instance) ---')
print('Before override:')
print('  Employee.raise_amount =', Employee.raise_amount)  # 1.04
print('  emp_1.raise_amount    =', emp_1.raise_amount)     # 1.04 (falls through to class)
print('  emp_2.raise_amount    =', emp_2.raise_amount)     # 1.04

# This does NOT change Employee.raise_amount — it adds emp_1.raise_amount in emp_1's own namespace
emp_1.raise_amount = 1.05

print('After emp_1.raise_amount = 1.05:')
print('  Employee.raise_amount =', Employee.raise_amount)  # still 1.04
print('  emp_1.raise_amount    =', emp_1.raise_amount)     # 1.05 (instance attribute wins)
print('  emp_2.raise_amount    =', emp_2.raise_amount)     # 1.04 (still uses class variable)

# --- Demo 3: apply_raise uses whichever raise_amount lookup finds ---
print('\n--- pay after apply_raise() ---')
print('  emp_1 pay before:', 50000)
emp_1.apply_raise()  # 50000 * 1.05 = 52500
print('  emp_1 pay after: ', emp_1.pay)

print('  emp_2 pay before:', 60000)
emp_2.apply_raise()  # 60000 * 1.04 = 62400
print('  emp_2 pay after: ', emp_2.pay)
emp_2.apply_raise() # 62400 * 1.04 = 64896
print('  emp_2 pay after: ', emp_2.pay)

# --- Quick reference ---
# | Attribute type   | Defined where      | Shared? | Example              |
# |------------------|--------------------|---------|----------------------|
# | Instance         | __init__ as self.x | No      | self.first, self.pay |
# | Class            | body of class      | Yes     | raise_amount, num_of_emps |
