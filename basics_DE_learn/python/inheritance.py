"""
Inheritance

INHERITANCE  → child class reuses parent attributes & methods (Developer IS-A Employee)
super()      → call parent __init__ / methods so you don't duplicate setup code
OVERRIDE     → child defines same method/attribute name → child's version wins for that class

Developer(Employee) gets: fullname(), apply_raise(), email logic from Employee
          plus: prog_lang, and raise_amt = 1.10 (overrides parent's 1.04)
"""

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    # Class variable override — apply_raise uses 1.10 for Developer, not 1.04
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # Run Employee.__init__ first → sets first, last, pay, email
        super().__init__(first, last, pay)
        # Then add Developer-only attribute
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # Never use employees=[] as default — same list shared by all managers (mutable default trap)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# --- Demo 1: inherited methods & attributes ---
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print('--- Developer inherits from Employee ---')
print(dev_1.email)        # from Employee.__init__ via super()
print(dev_1.fullname())     # inherited method
print(dev_1.prog_lang)      # Developer-only
print('raise_amt:', dev_1.raise_amt, 'vs Employee:', Employee.raise_amt)

dev_1.apply_raise()
print('pay after raise (×1.10):', dev_1.pay)  # 55000

# --- Demo 2: Manager composes a team (has-a list of employees) ---
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print('\n--- Manager ---')
print(mgr_1.email)          # inherited
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)
print('Team after add/remove dev_2:')
mgr_1.print_emps()

# --- Demo 3: isinstance — check type in code / interviews ---
print('\n--- isinstance ---')
print(isinstance(mgr_1, Manager))    # True
print(isinstance(mgr_1, Employee))   # True — Manager is a subclass of Employee
print(isinstance(mgr_1, Developer))  # False
print(issubclass(Developer, Employee))  # True

# --- Mental model ---
# Employee     → base: pay, email, apply_raise (4%)
# Developer    → + prog_lang, 10% raise (override raise_amt)
# Manager      → + employees list, add/remove/print team
#
# super().__init__(...)  = "set up the parent part first, then add my extras"

# yt: https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqIuOqKhwlXsIBIdSeYtc
