# Arrays — static, dynamic (Python `list`), and strings contrast

**Topic:** t02 Arrays (and foundation for t03) · **Source:** Greg — static vs dynamic arrays (transcript)  
**Related:** [strings.md](./strings.md) · **Practice:** [leetcode/week_2/](../../leetcode/week_2/) (283, 26, 66, 118, …)

---

## 1. Static array

**Definition:** A **contiguous block of memory** with a **fixed size** (capacity does not grow).

```
Index:     0    1    2    3    4
         ┌────┬────┬────┬────┬────┐
Value:   │ 1  │ 2  │ 3  │ 4  │ 5  │   length = 5
         └────┴────┴────┴────┴────┘
Last index = length − 1  →  4
```

- Positions are called **indices** (0-based).
- **Mutable** in the sense you can **change values** at an index — but **not** the fixed length (in pure static-array thinking).

### Operations (static array)

| Operation | Time | Why |
|-----------|------|-----|
| **Access** `a[i]` | **O(1)** | Direct index into contiguous memory |
| **Update** `a[i] = x` | **O(1)** | Same |
| **Search** `x in a` | **O(n)** | May scan entire array (worst case) |
| **Insert at middle** (shift right) | **O(n)** | Shift elements; fixed size → **lose last element** if no room |
| **Delete at middle** (shift left) | **O(n)** | Must stay contiguous — fill gap by shifting |

**Insert/delete intuition:** Memory must stay **contiguous**. Inserting at index 2 pushes 2→3, 3→4, …; the last value falls off if capacity is full. Deleting leaves a “hole” unless you shift everything left.

**Why static arrays matter:** They mirror how memory works under the hood. They are **limiting** for real programs (fixed size, painful middle insert).

---

## 2. Dynamic array (Python: `list`)

Python does **not** expose static arrays to you for daily use — you use a **`list`**, which is a **dynamic array**.

**Definition:** Like an array, but **size can grow** (append, pop, etc.).

### How it works under the hood

1. Backed by a **static array** with **extra capacity** (empty slots at the end).
2. **Append at end** when space exists → **O(1)** — write into next slot.
3. When **full** → allocate a **new, larger** static array, **copy** all elements → **O(n)** for that resize.
4. Python often **doubles** capacity (2 → 4 → 8 → 16 …) so resizes are rare.

```
Before full:  [1, 2, 3, 7, 8, _]   ← room at end → append is O(1)

When full:    copy all n items → new bigger block → then append
```

**Amortized O(1) append:** Most appends are O(1); occasionally O(n) resize. **Average** cost per append is still O(1) — you may see this called **amortized** time.

### Operations (dynamic array / `list`)

| Operation | Time | Notes |
|-----------|------|--------|
| Access `a[i]` | **O(1)** | |
| Update `a[i] = x` | **O(1)** | |
| `len(a)` | **O(1)** | Python stores length — does not count elements each time |
| Search `x in a` | **O(n)** | Worst case scan all |
| **Append** `a.append(x)` | **O(1)** amortized | End only; occasional O(n) copy when resizing |
| **Pop** `a.pop()` (end) | **O(1)** | |
| **Insert** `a.insert(i, x)` (not end) | **O(n)** | Shift elements right |
| **Delete** middle / front | **O(n)** | Shift to stay contiguous |

**Middle/front insert:** Even if there is free space at the end, inserting **not at the end** requires shifting the tail → **O(n)**.

---

## 3. LeetCode-style cheat sheet (dynamic array = `list`)

| Operation | Dynamic array (`list`) |
|-----------|-------------------------|
| Access `a[i]` | O(1) |
| Update `a[i]` | O(1) |
| Append end | O(1) *amortized* |
| Pop end | O(1) |
| Insert (not end) | O(n) |
| Delete (not end) | O(n) |
| Search / `x in a` | O(n) |

*From LeetCode “list” = dynamic array diagram in the video.*

---

## 4. Strings vs arrays (Python)

| | **Dynamic array (`list`)** | **String (`str`)** |
|---|---------------------------|---------------------|
| Memory | Contiguous | Contiguous (chars) |
| Mutable? | **Yes** — change items, append, pop | **No** in Python — **immutable** |
| `s[i]` read | O(1) | O(1) |
| `s[i] = 'x'` | O(1) on list | **Not allowed** on str |
| Append / concat | `append` amortized O(1) | `s + 'z'` → **new string**, **O(n)** |
| Insert / delete middle | O(n) on list | Effectively “new string” → **O(n)** |
| Search `x in s` | O(n) | O(n) |
| `len()` | O(1) | O(1) |

**Takeaway:** In Python, “changing” a string always means **building a new string** (copy n chars). That’s why string loops with `+=` can hurt; see [strings.md](./strings.md).

---

## 5. Python examples (from transcript)

### List = dynamic array

```python
a = [1, 2, 3]

a.append(5)      # O(1) amortized — insert at end
a.pop()          # O(1) — delete at end

a.insert(2, 5)   # O(n) — insert NOT at end (shifts)
a[0] = 7         # O(1) — modify at index
print(a[2])      # O(1) — access

if 7 in a:       # O(n) — search
    print(True)

print(len(a))    # O(1) — length stored
```

### String — immutable

```python
s = "hello"

# "Append" = new string (O(n))
b = s + "z"

print(s[2])      # O(1) — access 'l'
# s[1] = 'd'     # TypeError — cannot mutate

if 'e' in s:     # O(n) — search
    print(True)

print(len(s))    # O(1)
```

---

## 6. Big O mindset (from video)

- Big O describes **worst case** (upper bound), not every run.
- `5 in a` might find it on the first try, but we still say **O(n)** because you *could* scan everything.
- **Prefer end operations** on lists: `append` / `pop` vs `insert(0, x)` (O(n)).

---

## 7. Interview patterns (t02 — arrays)

| Pattern | Idea | Example LC |
|---------|------|------------|
| Two pointers | `i` scan + `base` write index | 283 Move Zeroes, 26 Remove Duplicates |
| In-place write | Fill from left, don’t allocate new array | 88 Merge Sorted Array |
| Simulation / row build | Build from previous state | 118 Pascal's Triangle |
| Carry / digit | Right-to-left with overflow | 66 Plus One |

Your notes: [leetcode_283.py](../../leetcode/week_2/leetcode_283.py), [leetcode_26.py](../../leetcode/week_2/leetcode_26.py), [leetcode_66.py](../../leetcode/week_2/leetcode_66.py), [leetcode_118.py](../../leetcode/week_2/leetcode_118.py).

---

## 8. Quick reference

```python
# Dynamic array
a = []
a.append(x)           # end — amortized O(1)
a.pop()               # end — O(1)
a.insert(i, x)        # middle — O(n)
a[i]; a[i] = v        # O(1)
len(a)                # O(1)
x in a                # O(n)

# String — treat as read-mostly; build with join
s[i]                  # O(1)
s + t; s[::-1]        # O(n) new string
"".join(parts)        # better than += in loops
```

---

## 9. What to study next

| File | Content |
|------|---------|
| [strings.md](./strings.md) | Methods, slicing, LC 125 |
| [DSA_PACING.md](../../learn_plans/DSA_PACING.md) | t02 one week, t03 next |
| [big_O_notation.md](../../leetcode/week_1/big_O_notation.md) | Week 1 Big-O drills |

**Mastery (portal):** t02 = theory done + Easy **without hints** + ≥1 Medium attempted.
