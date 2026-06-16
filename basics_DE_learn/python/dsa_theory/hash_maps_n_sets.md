# Hash maps, hash sets & hash tables

**Topic:** t04 Hash maps · **Source:** Greg (CS Dojo) — [Hash Tables](https://www.youtube.com/watch?v=sfWyugl4JWA)  
**Related:** [arrays.md](./arrays.md) · [strings.md](./strings.md) · [tips_n_tricks.md](./tips_n_tricks.md)  
**Practice:** [leetcode/week_1/](../../leetcode/week_1/) (217, 1, 242) · [leetcode/week_4/](../../leetcode/week_4/) (383, 290, 49)

---

## 1. Mental model — what is a hash table?

A hash table **looks** like an array but works differently. Instead of storing values at fixed indices you choose, a **hash function** computes **where** each item belongs.

```
Bucket index:   0       1       2       3       4
              ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
              │     │ │     │ │Greg │ │     │ │     │
              │     │ │     │ │  ↓  │ │     │ │     │
              │     │ │     │ │gr   │ │     │ │     │   ← separate chaining
              │     │ │     │ │Joe  │ │     │ │     │     (linked list in bucket 2)
              └─────┘ └─────┘ └─────┘ └─────┘ └─────┘
```

- Each slot is a **bucket** (position 0 … capacity−1).
- **Hashing** = run input through a hash function → get a bucket index.
- Hash tables are the **engine** behind hash **sets** and hash **maps**.

**Why they exist:** **fast lookup** — “is X here?” or “what value goes with key X?” in **average O(1)** instead of scanning O(n).

---

## 2. Hash function (worked example)

**Input:** string `"Greg"`  
**Buckets:** 5 (indices 0–4)

Simple teaching hash (sum letter positions, then mod):

| Char | Position in alphabet |
|------|----------------------|
| G | 7 |
| r | 18 |
| e | 5 |
| g | 7 |

```
sum = 7 + 18 + 5 + 7 = 37
index = 37 % 5 = 2   →  "Greg" goes in bucket 2
```

| String | Sum | % 5 | Bucket |
|--------|-----|-----|--------|
| Greg | 37 | 2 | 2 |
| gr | 30 | 0 | 0 |
| grg | 32 | 2 | 2 ← **collision** with Greg |

- Real languages use **much better** hash functions (not alphabet sums).
- Hash functions are **many** — some distribute keys more evenly than others.
- **Mod by bucket count** forces the index into range `[0, capacity−1]`.

---

## 3. Collisions — two ways to handle them

A **collision** = two different keys hash to the **same bucket**. Unavoidable when possible keys ≫ buckets.

### A. Separate chaining (Greg’s preference)

Each bucket holds a **linked list** (chain) of all items that hashed there.

```
bucket 2:  Greg → grg → Joe → ...
```

- **Insert:** hash → go to bucket → append to list (often as new head) → **O(1)** average.
- **Lookup:** hash → walk that bucket’s list until match or end.
- **Delete:** hash → find node in list → remove.

### B. Linear probing

No lists inside buckets. On collision, **probe forward** one slot at a time until an empty bucket.

```
"Greg"  → bucket 2  (occupied)
"grg"   → bucket 2 full → try 3 → empty → store at 3
```

- **Lookup:** start at hashed index; if wrong key, keep probing (+1) until match or **empty slot** (not found).
- **Delete is tricky:** clearing a slot breaks probing for keys stored **after** the deleted one.
- **Fix:** mark deleted slots with a **tombstone** (e.g. sentinel like −1) — “something was here; keep probing.”

| Technique | Pros | Cons |
|-----------|------|------|
| Separate chaining | Simple; handles many collisions per bucket | Extra pointer memory per item |
| Linear probing | Cache-friendly; no linked lists | Clustering; delete needs tombstones |

**Interview note:** you rarely implement either by hand in Python — but **know collisions exist** and why average case is O(1) with a good hash + load factor.

---

## 4. Hash set vs hash map

| | **Hash set** | **Hash map** (dict) |
|---|-------------|---------------------|
| Stores | **Unique keys only** | **Key → value** pairs |
| Question | “Is key in the set?” | “Is key present?” **or** “What is `map[key]`?” |
| Python | `set` | `dict` |
| Values | N/A (presence only) | **Any type** — lists, nested dicts, etc. |

**Hash map terminology:** **key** (must be hashable) maps to **value** (anything).

```
Greg  →  7        # key → value
gr    →  5
```

**Hash set operations (all average O(1) w.r.t. n = number of items):**

| Op | What it does |
|----|--------------|
| Lookup | `key in set` — exists? |
| Add | insert unique key |
| Remove | delete key |

**Hash map operations (average O(1) w.r.t. n):**

| Op | What it does |
|----|--------------|
| Key lookup | `key in d` — exists? |
| Value lookup | `d[key]` — get value |
| Add / update | `d[key] = value` |
| Remove | `del d[key]` |

---

## 5. Big O — the asterisk matters

### Average vs worst case

| Operation | Average (good hash) | Worst case |
|-----------|---------------------|------------|
| Lookup / add / remove (set or map) | **O(1)** *amortized average* | **O(n)** — all keys in one bucket / long probe chain |

**Why average is O(1):** hash jumps directly to one bucket; other buckets don’t matter for that lookup.

**Why worst is O(n):** absurd but possible — every key lands in the same chain; you scan the whole chain.

### Two different “sizes”

| Symbol | Meaning |
|--------|---------|
| **n** | Number of items **in** the hash table |
| **s** | Length of the **key** (e.g. string chars to hash) |

- Hashing a string of length **s** costs **O(s)** — must read every character.
- Lookup is **O(1) in n** (table size), not O(1) in key length — but don’t forget the O(s) hash step for long keys.

**Contrast with list/string scan:**

```python
# O(n) per lookup — scan the whole string each time
if 'x' in million_char_string: ...

# O(s) once to build set, then O(1) per lookup
chars = set(million_char_string)
if 'x' in chars: ...   # fast repeated checks
```

**Looping the whole set/dict is O(n)** — `for x in s` or `for k, v in d.items()` visits every entry. That’s fine for iteration; it’s not the same as a single membership test.

---

## 6. What is hashable? (keys only)

Only **hashable** objects can be **keys** in a set or dict.

| Hashable (immutable) | Not hashable (mutable) |
|----------------------|-------------------------|
| `str` | `list` |
| `int`, `float` | `dict` |
| `tuple` (if all elements hashable) | `set` |
| `frozenset` | most custom mutable objects |

**Rule of thumb:** **immutable → hashable**, **mutable → not hashable**.

**Why:** a hash table stores keys at indices computed from the key’s hash. If a key could **change in place**, its hash/index could change → you’d lose it in the table.

```python
# If strings were mutable (they aren't in Python):
# "Greg" hashes to bucket 2
# mutate to "Freg" → different hash → wrong bucket → broken lookup
```

**Values** in a dict can be **anything** — lists, dicts, nested structures. Only **keys** must be hashable.

```python
d = {}
d["Greg"] = [1, 2, 3]          # OK — value is a list
# d[[1, 2]] = "bad"            # TypeError — list is not hashable as key
d[(1, 2)] = "ok"               # OK — tuple is hashable
```

---

## 7. Python — `set`

```python
s = set()           # empty set — use set(), not {} (that's a dict)

s.add(1)
s.add(2)
s.add(3)            # duplicates ignored — set = unique items

1 in s              # True  — O(1) average
4 not in s          # True

s.remove(3)         # O(1) average; KeyError if missing
# s.remove(4)       # KeyError — not in set

# Build from iterable — O(len(iterable)) to hash each item
unique = set("aabbccdde")   # {'a', 'b', 'c', 'd', 'e'}

for x in s:         # O(n) — full iteration, not a single lookup
    print(x)
```

**Pattern:** need repeated “is char/item in collection?” on a long sequence → **pay O(n) once** to build a set, then **O(1)** per check.

---

## 8. Python — `dict` (hash map)

```python
d = {"Greg": 1, "Steve": 2, "Rob": 3}

d["Art"] = 4                    # add / update — O(1) average
"Greg" in d                     # True — key exists
d["Greg"]                       # 1 — value lookup

# d["Ghost"]                    # KeyError — key not in dict
# Always check first, or use .get()
if "Greg" in d:
    val = d["Greg"]

d.get("Ghost", 0)               # safe default — no KeyError

del d["Rob"]                    # remove key-value pair

for key, value in d.items():    # O(n) — all pairs
    print(f"{key} → {value}")
```

### `defaultdict` — auto-create missing keys

```python
from collections import defaultdict

dd = defaultdict(int)       # missing key → 0
dd[2] += 1                  # no KeyError; starts at 0 then increments

dd_list = defaultdict(list)
dd_list["a"].append(1)      # missing key → [] then append
```

**Use when:** counting or grouping — avoids `if key not in d: d[key] = 0` boilerplate.

### `Counter` — frequency map in one line

```python
from collections import Counter

s = "aabbbccce"
freq = Counter(s)           # Counter({'b': 3, 'a': 2, 'c': 3, 'e': 1})
freq['a']                   # 2
```

**Interview etiquette (from Greg):**

| Tool | Interview safety |
|------|------------------|
| Plain `dict` | Safest — shows you understand the hash map |
| `defaultdict` | Usually fine — small convenience |
| `Counter` | Slightly “Python cheat” — know how to build freq map manually |

**Manual frequency map (interview-safe):**

```python
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
```

---

## 9. When to use set vs map (pattern triggers)

| You need… | Reach for… | Example LC |
|-----------|------------|------------|
| “Have we seen this before?” | **set**, one pass | 217 Contains Duplicate |
| “What partner makes the target?” | **map** `{value: index}` | 1 Two Sum |
| “Same letters, same counts?” | **freq map** or Counter | 242 Valid Anagram, 387 First Unique |
| “Count occurrences” | **freq map** `key → count` | 383 Ransom Note |
| “Group by normalized key” | **map** `key → list` | 49 Group Anagrams |
| “Two strings same pattern?” | **two maps** (bijection) | 290 Word Pattern |

**Core trade:** **trade space for speed** — O(n) extra memory for O(1) average lookups instead of O(n) scans.

---

## 10. Common bugs & pro tips

### Two Sum — store **after** lookup

```python
# WRONG order — can pair index with itself
map[nums[i]] = i
if target - nums[i] in map: ...

# RIGHT — check complement first, then store
if target - nums[i] in map:
    return [map[complement], i]
map[nums[i]] = i
```

### Anagram / frequency — length shortcut

```python
if len(s) != len(t):
    return False   # instant reject
```

### `d[key]` vs `d.get(key)`

- `d[key]` → **KeyError** if missing (fine when you’ve already checked `key in d`).
- `d.get(key, default)` → safe when key might be absent.

### Set remove vs discard

- `s.remove(x)` → **KeyError** if x not in set.
- `s.discard(x)` → no error if missing.

### Empty set syntax

```python
s = set()      # correct empty set
# s = {}       # WRONG — this is an empty dict
```

### Don’t confuse “O(1) lookup” with “O(1) everything”

- Building a set/dict from n items: **O(n)**.
- One membership test: **O(1) average** in n.
- Looping all items: **O(n)**.

---

## 11. LeetCode cheat sheet

| Operation | `set` | `dict` |
|-----------|-------|--------|
| Create empty | `set()` | `{}` or `dict()` |
| Add | `s.add(x)` | `d[k] = v` |
| Contains key | `x in s` | `k in d` |
| Get value | N/A | `d[k]` or `d.get(k, default)` |
| Remove | `s.remove(x)` / `s.discard(x)` | `del d[k]` |
| Size | `len(s)` | `len(d)` |
| Iterate | `for x in s` | `for k, v in d.items()` |

| Pattern | Time | Space |
|---------|------|-------|
| One-pass set membership | O(n) | O(n) |
| Two-pass freq map (count then scan) | O(n) | O(1)* or O(k)** |
| Two Sum complement map | O(n) | O(n) |
| Group by sorted string / freq tuple | O(n · k log k) or O(n · k) | O(n) |

\* O(1) extra when alphabet size is bounded (e.g. 26 letters).  
\** k = distinct keys / alphabet size.

---

## 12. Quick reference

```python
# --- Set ---
seen = set()
seen.add(x)
x in seen                    # O(1) avg
seen.remove(x)               # KeyError if missing
seen.discard(x)              # safe remove

# --- Dict ---
freq = {}
freq[c] = freq.get(c, 0) + 1

complement_map = {}
if complement in complement_map:
    return [complement_map[complement], i]
complement_map[nums[i]] = i

# --- Collections (optional) ---
from collections import defaultdict, Counter
groups = defaultdict(list)
groups[key].append(item)
counts = Counter(iterable)
```

---

## 13. Revision checklist (t04 mastery)

Before ticking t04 in the portal:

- [ ] Explain hash function → bucket index → collision in your own words
- [ ] Name separate chaining vs linear probing
- [ ] State why keys must be immutable / hashable
- [ ] Say “average O(1), worst O(n)” and mean it
- [ ] Solve **217**, **1**, **242** cold without hints
- [ ] Add **383** (and attempt **49** Medium) from week 4

**Cross-links:** pattern triggers in [tips_n_tricks.md](./tips_n_tricks.md) · week plan [week_04.md](../../weekly_plans/week_04.md)
