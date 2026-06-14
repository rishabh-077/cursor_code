"""
Classes & Instances — important notes

CLASS     → blueprint (defines attributes + methods)
INSTANCE  → one real object built from that blueprint (emp_1, emp_2)

self      → the instance the method is working on (Python passes it for you)
__init__  → constructor; runs automatically when you call Employee(...)
"""

class Employee:
    # __init__ is NOT optional for this pattern — it sets up each new employee

    def __init__(self, first, last, pay):
        # Instance attributes: unique per object (emp_1.first != emp_2.first)
        self.first = first
        self.last = last
        self.pay = pay

        # Derived attribute: computed once at creation (not a separate argument)
        self.email = first + '.' + last + '@company.com'

    # Instance method: first param must be self — gives access to self.first, etc.
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# --- Creating instances (calling the class runs __init__) ---
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# Each instance has its own namespace:
# emp_1.email → 'corey.schafer@company.com'
# emp_2.email → 'test.employee@company.com'

# --- Two equivalent ways to call an instance method ---
# 1) Instance call: Python passes emp_1 as self behind the scenes
print(emp_1.fullname())

# 2) Class call: you pass the instance explicitly as self
print(Employee.fullname(emp_1))

# Both print the same string; prefer emp_1.fullname() in normal code.

# --- Quick mental model ---
# Employee.fullname(emp_1)  ==  emp_1.fullname()
# Class.method(instance)    ==  instance.method()

# yt link: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc