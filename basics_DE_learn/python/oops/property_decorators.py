"""
Property decorators (@property, .setter, .deleter)

@property     → method behaves like an attribute: emp.email (no parentheses)
                Use for computed/read-only values derived from other state

.setter       → run code when someone assigns: emp.fullname = "Corey Schafer"
                Same method name as the @property (fullname) — Python links them

.deleter      → run code when someone deletes: del emp.fullname
                Same method name again — optional cleanup / validation

Why use properties instead of plain attributes?
  - Keep a simple public API (emp.email) while logic lives in methods
  - email always stays in sync with first/last — no stale copy in __init__
  - setter can parse, validate, or split input before updating real attributes

Without @property you'd use get_email() / set_fullname() — properties look cleaner.
"""

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # --- Read-only computed attribute (no .setter → cannot assign to emp.email) ---
    @property
    def email(self):
        # Rebuilt every access from current first/last
        return f'{self.first}.{self.last}@email.com'

    # --- Getter: access like emp.fullname (not emp.fullname()) ---
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    # --- Setter: emp.fullname = "Corey Schafer" splits and updates first/last ---
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # --- Deleter: del emp.fullname runs this instead of removing an attribute ---
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

# Setter in action — looks like attribute assignment, runs fullname() setter logic
emp_1.fullname = "Corey Schafer"

print(emp_1.first)      # Corey  (updated by setter, not stored as fullname field)
print(emp_1.email)      # Corey.Schafer@email.com  (recomputed from first/last)
print(emp_1.fullname)   # Corey Schafer

# Deleter in action
del emp_1.fullname      # prints "Delete Name!", sets first/last to None

# After delete:
# print(emp_1.fullname)   # "None None"
# print(emp_1.email)      # "None.None@email.com"
