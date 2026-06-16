# Hash Tables — Interview Notes

## Table of Contents
1. [Core Concept](#core-concept)
2. [Hash Function](#hash-function)
3. [Collision Handling](#collision-handling)
4. [Dynamic Resizing](#dynamic-resizing)
5. [Python Internals — dict & set](#python-internals--dict--set)
6. [Time & Space Complexity](#time--space-complexity)
7. [dict vs set vs map](#dict-vs-set-vs-map)
8. [Common Interview Patterns](#common-interview-patterns)
9. [Tricky Edge Cases](#tricky-edge-cases)
10. [Quick Cheatsheet](#quick-cheatsheet)

---

## Core Concept

A **hash table** maps keys to values using a hash function to compute an index into an array of buckets.

```
key  →  hash(key)  →  index  →  bucket  →  value
```

**Why it's powerful:** Average O(1) lookup, insert, and delete — regardless of table size.

**Internal structure:**
```
Index:  [ 0 ][ 1 ][ 2 ][ 3 ][ 4 ][ 5 ][ 6 ][ 7 ]
Value:  [ - ][ - ][k1][ - ][k2][ - ][k3][ - ]
```

---

## Hash Function

A hash function converts a key into an integer index.

**Properties of a good hash function:**
- **Deterministic** — same key always gives same hash
- **Uniform distribution** — spreads keys evenly across buckets
- **Fast to compute** — O(1) ideally
- **Avalanche effect** — small change in key → large change in hash

**Mapping hash to index:**
```
index = hash(key) % table_size
```

### Python's hash() by type

| Type | Hash Strategy |
|------|--------------|
| `int` | The integer itself (with bit mixing) |
| `str` | SipHash-1-3 (randomized per process) |
| `float` | Based on integer representation |
| `tuple` | Combined hash of all elements |
| `frozenset` | XOR of element hashes |
| Custom class | `__hash__()` method (defaults to `id()`) |

**Hash randomization (Python 3.3+):**
```python
# Strings are randomized per process — changes on every run
hash("hello")   # → 123456 (run 1)
hash("hello")   # → 789012 (run 2, different process)

# Integers are always stable
hash(42)        # → always 42
hash(-1)        # → -2  (special case: -1 is reserved internally)

# Control seed for reproducibility (testing only)
# PYTHONHASHSEED=42 python script.py
```

**Hashable vs Unhashable:**
```python
# Hashable (immutable) — can be dict keys / set elements
hash(42)          # ✅ int
hash("hello")     # ✅ str
hash((1, 2, 3))   # ✅ tuple (if all elements are hashable)
hash(frozenset()) # ✅ frozenset

# Unhashable (mutable) — CANNOT be dict keys / set elements
hash([1, 2, 3])   # ❌ TypeError: unhashable type: 'list'
hash({1: 2})      # ❌ TypeError: unhashable type: 'dict'
hash({1, 2})      # ❌ TypeError: unhashable type: 'set'
```

> **Interview tip:** Rule of thumb — mutable objects are unhashable. If an object can change, its hash would change too, breaking the hash table contract.

---

## Collision Handling

A **collision** occurs when two different keys hash to the same index.

### Strategy 1 — Separate Chaining
Each bucket holds a **linked list** of entries. On collision, append to the list.

```
Index 3 → [ (key1, val1) → (key2, val2) → None ]
```

- Simple to implement
- Performance degrades to O(n) in worst case (all keys in one bucket)
- Used in: Java's `HashMap` (before Java 8), most textbook implementations

### Strategy 2 — Open Addressing (used by Python)
On collision, **probe** for the next available slot in the same array.

```
Slot taken? → probe next slot → probe next → ...
```

**Probing methods:**
| Method | Formula | Issue |
|--------|---------|-------|
| Linear | `(i + 1) % size` | Clustering |
| Quadratic | `(i + k²) % size` | Secondary clustering |
| Double hashing | `(i + k * h2(key)) % size` | Best distribution |

**Python's perturbation-based probing:**
```python
# Simplified version of CPython's probe sequence
index = hash(key) % size
perturb = hash(key)
while slot[index] is not empty:
    index = (5 * index + 1 + perturb) % size
    perturb >>= 5
```
This ensures all slots are eventually visited, avoiding infinite loops.

> **Interview tip:** Open addressing has better **cache performance** than chaining (data stays in contiguous memory). Chaining uses more memory (pointers) but handles high load factors better.

---

## Dynamic Resizing

### Load Factor
```
Load Factor (α) = Number of entries / Number of buckets
```

| Load Factor | State |
|-------------|-------|
| α < 0.5 | Lots of empty space, fast but memory wasteful |
| α ≈ 0.75 | Sweet spot (Java HashMap's default threshold) |
| α > 1.0 | Only possible with chaining; performance degrades |

### Python's resize behavior

| Event | Trigger | New size |
|-------|---------|----------|
| Grow | Table is 2/3 full | ~2–4× current size |
| Shrink | Table is too sparse (after many deletes) | Shrinks to fit |

**What happens during resize:**
1. Allocate a new array (larger)
2. **Rehash every key** into the new array
3. Discard the old array

> **Cost:** Resize is O(n) — but since it happens infrequently (exponential backoff), amortized cost is still O(1) per insert.

**Python initial sizes:**
```python
d = {}      # starts with 8 slots
# Grows to: 8 → 32 → 128 → 512 → ...
```

---

## Python Internals — dict & set

### dict (CPython implementation)
- Implemented in `Objects/dictobject.c`
- Uses **open addressing** with perturbation
- Since Python 3.7: **insertion order is guaranteed**
- Since Python 3.6: dict is more compact (stores keys/values separately from hash array)

```python
# Dict internals (conceptual)
# Each slot stores: [hash | key | value]
d = {"a": 1, "b": 2}
#     ↓
# slot 0: [hash("a"), "a", 1]
# slot 5: [hash("b"), "b", 2]
# slot 1,2,3,4,6,7: empty
```

**dict operations:**
```python
d = {}

# Insert / Update — O(1) avg
d["key"] = "value"

# Lookup — O(1) avg
val = d["key"]           # raises KeyError if missing
val = d.get("key", -1)  # safe, returns default

# Delete — O(1) avg
del d["key"]
d.pop("key", None)       # safe delete

# Membership — O(1) avg
"key" in d               # ✅ fast
"key" in d.values()      # ❌ O(n) — values() is a list scan

# Iteration
for k in d:              # keys
for k, v in d.items():   # key-value pairs
for v in d.values():     # values

# Merge (Python 3.9+)
d3 = d1 | d2             # new merged dict
d1 |= d2                 # update d1 in place

# Useful methods
d.setdefault("key", []).append(1)   # init if missing
collections.defaultdict(list)       # auto-init on missing key
collections.Counter(iterable)       # frequency count dict
```

### set
- Implemented in `Objects/setobject.c`
- Essentially a `dict` with **only keys, no values**
- Also uses open addressing

```python
s = set()

# Add — O(1) avg
s.add(1)

# Remove — O(1) avg
s.remove(1)     # raises KeyError if missing
s.discard(1)    # safe, no error if missing

# Membership — O(1) avg  ← key advantage over list
1 in s

# Set operations
a | b           # union
a & b           # intersection
a - b           # difference
a ^ b           # symmetric difference (in one but not both)
a <= b          # is a subset of b?
a >= b          # is a superset of b?

# frozenset — immutable set (can be used as dict key)
fs = frozenset([1, 2, 3])
```

---

## Time & Space Complexity

### dict / set / hash map

| Operation | Average | Worst Case | When worst happens |
|-----------|---------|------------|-------------------|
| Insert | O(1) | O(n) | All keys collide (same hash) |
| Lookup | O(1) | O(n) | All keys collide |
| Delete | O(1) | O(n) | All keys collide |
| Resize | O(n) | O(n) | Amortized O(1) per insert |
| Iteration | O(n) | O(n) | Always |

> **Worst case is rare in practice** because Python's hash function distributes well. Adversarial inputs could force it, which is why hash randomization was introduced.

### Comparison with other structures

| Structure | Lookup | Insert | Delete | Ordered? |
|-----------|--------|--------|--------|----------|
| Hash Table | O(1) avg | O(1) avg | O(1) avg | No (dict preserves insertion order) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | Yes |
| Array | O(n) | O(1) append | O(n) | Yes |
| Sorted Array | O(log n) binary search | O(n) | O(n) | Yes |

---

## dict vs set vs map

| | Python `dict` | Python `set` | Java `HashMap` | Java `HashSet` |
|--|--------------|-------------|---------------|---------------|
| Stores | key → value | keys only | key → value | keys only |
| Ordered | Yes (insertion, 3.7+) | No | No | No |
| Null keys | 1 `None` key allowed | `None` allowed | 1 null key | null allowed |
| Thread safe | No | No | No | No |
| Collision strategy | Open addressing | Open addressing | Separate chaining (tree after 8) | Same as HashMap |
| Load factor threshold | 2/3 (~0.67) | 2/3 (~0.67) | 0.75 | 0.75 |

**Python `dict` vs `collections.OrderedDict`:**
- Since Python 3.7, plain `dict` preserves insertion order
- `OrderedDict` still useful for `move_to_end()` and order-sensitive equality

---

## Common Interview Patterns

### 1. Frequency Count
```python
from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
freq = Counter(nums)         # {3: 3, 2: 2, 1: 1}
freq.most_common(2)          # [(3, 3), (2, 2)]

# Manual version
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
```

### 2. Two Sum (classic)
```python
def two_sum(nums, target):
    seen = {}               # value → index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
```

### 3. Grouping / Anagram detection
```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))   # anagrams share same sorted key
        groups[key].append(w)
    return list(groups.values())
```

### 4. Sliding window with frequency map
```python
def length_of_longest_substring(s):
    seen = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

### 5. Caching / Memoization
```python
from functools import lru_cache

@lru_cache(maxsize=None)    # uses dict internally
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

# Manual memo
memo = {}
def fib(n):
    if n in memo: return memo[n]
    if n < 2: return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

### 6. Set for O(1) membership / deduplication
```python
# Deduplication (preserving order)
seen = set()
result = [x for x in nums if not (x in seen or seen.add(x))]

# Longest consecutive sequence
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n - 1 not in num_set:          # start of a sequence
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)
    return best
```

### 7. Custom object as dict key
```python
# Tuples work as keys (immutable)
grid_visits = {}
grid_visits[(0, 0)] = True
grid_visits[(1, 2)] = True

# Custom class — must implement __hash__ and __eq__
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

---

## Tricky Edge Cases

### 1. Modifying a dict while iterating
```python
d = {"a": 1, "b": 2}
# ❌ RuntimeError: dictionary changed size during iteration
for k in d:
    del d[k]

# ✅ Iterate over a copy
for k in list(d.keys()):
    del d[k]
```

### 2. Mutable default argument trap
```python
# ❌ Bug — all calls share the same dict
def add(key, val, d={}):
    d[key] = val
    return d

# ✅ Fix
def add(key, val, d=None):
    if d is None:
        d = {}
    d[key] = val
    return d
```

### 3. hash(-1) == hash(-2) in Python
```python
hash(-1)   # returns -2 (CPython special case: -1 is reserved as error code in C)
hash(-2)   # returns -2
# Both map to the same bucket — valid collision, handled automatically
```

### 4. Equal objects must have equal hashes
```python
# If __eq__ is overridden, __hash__ MUST be overridden too
class Bad:
    def __eq__(self, other): return True
    # Missing __hash__ → Python sets __hash__ = None → unhashable!

class Good:
    def __eq__(self, other): return True
    def __hash__(self): return 0   # all objects same bucket, but valid
```

### 5. `in` operator on dict checks keys, not values
```python
d = {"a": 1, "b": 2}
"a" in d            # ✅ True  — O(1)
1 in d              # ❌ False — checks keys, not values
1 in d.values()     # ✅ True  — but O(n)
```

---

## Quick Cheatsheet

```
HASH TABLE
├── hash(key) % size  →  bucket index
├── Collision: Open Addressing (Python) / Chaining (Java)
├── Load factor threshold: 0.67 (Python) / 0.75 (Java)
├── Resize: doubles size, rehashes everything — O(n), amortized O(1)
└── Worst case O(n) only when all keys collide

PYTHON DICT
├── Ordered (insertion order, Python 3.7+)
├── Keys must be hashable (immutable types)
├── d.get(k, default)  →  safe lookup
├── d.setdefault(k, [])  →  init if missing
├── defaultdict / Counter  →  frequency problems
└── dict | dict  →  merge (Python 3.9+)

PYTHON SET
├── O(1) membership test  ←  best use case vs list
├── add / discard (safe) / remove (raises error)
├── Union |, Intersection &, Difference -, Symmetric ^
└── frozenset  →  immutable, hashable set (usable as dict key)

INTERVIEW RED FLAGS TO AVOID
├── Using list for membership checks — use set instead
├── Iterating and modifying dict simultaneously
├── Making mutable objects dict keys
├── Forgetting __hash__ when overriding __eq__
└── Using d.values() for membership — always O(n)

WHEN TO USE HASH TABLE IN INTERVIEWS
├── "Find if X exists" → set
├── "Count frequency" → Counter / dict
├── "Group by property" → defaultdict(list)
├── "Avoid recomputation" → memo dict
└── "Two elements that satisfy condition" → dict lookup
```

---

*Sources: CPython source (dictobject.c, setobject.c), Python docs, CLRS Chapter 11*
