# Python & DSA Definitions

Quick glossary for your notes and LeetCode week 1. For Big O details see [big_O_notation.md](../leetcode/week_1/big_O_notation.md).

---

## DSA — Collections & patterns

### Hash Map (`dict`)

A **key → value** lookup structure. In Python, `dict` is implemented as a hash map.

- **Average time:** `O(1)` for get, set, `in` check (by key)
- **Use when:** you need to store or look up *pairs* — e.g. `number → index`, `char → count`
- **LeetCode:** Two Sum (`prevMap[n] = i`), Valid Anagram (letter counts)

```python
prevMap = {}
prevMap[7] = 0          # store: key 7 → value 0
if 7 in prevMap:        # lookup by key
    idx = prevMap[7]
```

---

### Hash Set (`set`)

A collection of **unique** values with no duplicates. Only the value matters (no separate value payload like a map).

- **Average time:** `O(1)` for add, `in` check
- **Use when:** you only care “have I seen this before?” — not *where* or *how many*
- **LeetCode:** Contains Duplicate (return `True` as soon as `n in seen`)

```python
seen = set()
seen.add(3)
if 3 in seen:
    ...
```

**Hash map vs hash set**

| | Hash map (`dict`) | Hash set (`set`) |
|---|-------------------|------------------|
| Stores | key + value | values only |
| Example use | index of a number | duplicate detection |
| LC problems | 1 (Two Sum) | 217 (Contains Duplicate) |

---

### `enumerate`

Built-in that loops over a sequence and gives **(index, item)** pairs.

- Avoids manual `range(len(nums))` and `nums[i]`
- **Time:** `O(n)` — one pass, same as a normal loop

```python
for i, n in enumerate(nums):
    # i = 0, 1, 2, ...
    # n = nums[0], nums[1], ...
```

Used in Two Sum: `for i, n in enumerate(nums):`

---

### Complement

The **partner value** that completes a target. In Two Sum: `diff = target - n`.

- If `diff` was stored earlier in your hash map, `n + diff == target`
- Check the map **before** storing current `n` so you don’t reuse the same index twice

---

### Brute force

Try **every possibility** (e.g. every pair `(i, j)`) until you find an answer.

- Usually **easy to code**, **slow** — often `O(n²)` for array pair problems
- Good for understanding; replace with hash map / two pointers when optimizing

---

### Time complexity / Space complexity

- **Time:** how runtime grows as input size `n` grows
- **Space:** how much *extra* memory the algorithm uses (not counting the input itself)

Say both when you finish a LeetCode problem (e.g. hash set: **O(n)** time, **O(n)** space).

---

## OOP — Core

### Class

A **blueprint** that defines attributes (data) and methods (behavior). Example: `class Employee:`

### Instance

One **real object** created from a class. Example: `emp_1 = Employee('Corey', 'Schafer', 50000)`

### `self`

The **current instance** passed as the first argument to instance methods. Python supplies it: `emp_1.fullname()` → `Employee.fullname(emp_1)`.

### `__init__`

**Constructor** — runs automatically when you create an instance. Sets up `self.first`, `self.pay`, etc.

### Instance variable

Attribute on **one object** — `self.first`, `self.pay`. Each instance has its own copy.

### Class variable

Attribute on the **class**, shared by all instances — `Employee.raise_amount`, `num_of_emps`.

- Reading: `emp_1.raise_amount` looks on instance first, then class
- `emp_1.raise_amount = 1.05` creates an **instance** override; does **not** change the class variable for `emp_2`

---

## OOP — Methods & inheritance

### Instance method

Normal method with `self` — works on one object: `emp_1.apply_raise()`.

### Class method (`@classmethod`)

First argument is **`cls`** (the class). Use for factories (`from_string`) or changing class variables for everyone.

### Static method (`@staticmethod`)

No `self` or `cls` — utility function grouped in the class namespace (e.g. `is_workday(date)`).

### Inheritance

Child class **reuses** parent attributes and methods. `class Developer(Employee):` — Developer **is-a** Employee.

### `super()`

Calls the **parent** class method (often `super().__init__(...)` so you don’t duplicate setup code).

### Override

Child defines the same name as parent (e.g. `raise_amt = 1.10`) — the child’s version wins for that class.

---

## OOP — Advanced

### Dunder (special) method

Method with **double underscores** (`__name__`). Python calls them for built-in behavior.

| Method | Triggered by | Typical use |
|--------|----------------|-------------|
| `__repr__` | `repr(obj)` | Debug string, ideally `Employee(...)` |
| `__str__` | `str(obj)`, `print(obj)` | Human-readable string |
| `__add__` | `a + b` | Custom `+` behavior |
| `__len__` | `len(obj)` | Custom length |

### `@property`

Turns a method into something accessed like an **attribute** — `emp.email` without `()`.

- **Getter:** `@property`
- **Setter:** `@name.setter` — runs on assignment
- **Deleter:** `@name.deleter` — runs on `del`

Use when you want a simple API but need computed or validated values behind the scenes.

---

## Quick links

| Topic | File |
|-------|------|
| Big O | [big_O_notation.md](../leetcode/week_1/big_O_notation.md) |
| Two Sum / hash map | [leetcode_1.py](../leetcode/week_1/leetcode_1.py) |
| Contains Duplicate | [leetcode_217.py](../leetcode/week_1/leetcode_217.py) |
| Classes | [classes_and_instances.py](classes_and_instances.py) |
| Class variables | [class_variables.py](class_variables.py) |
| Inheritance | [inheritance.py](inheritance.py) |
| Class / static methods | [class_and_static_methods.py](class_and_static_methods.py) |
| Dunder methods | [special_methods.py](special_methods.py) |
| Properties | [property_decorators.py](property_decorators.py) |
