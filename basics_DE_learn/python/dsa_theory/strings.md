# Strings — Python (coding interviews)

**Topic:** t03 Strings · **Source:** NeetCode-style strings overview (transcript)  
**Practice:** [leetcode_125.py](../../leetcode/week_2/leetcode_125.py) (Valid Palindrome)

---

## What is a string? (mental model)

A string is effectively an **array of characters** (single letters).  
**Arrays vs strings (memory, mutability, Big O):** [arrays.md](./arrays.md).

```python
s = "banana"
# s[0] → 'b'   same idea as arr[0]
```

Interview angle: many string problems are **array problems** + built-in helpers. Use Python’s string methods so you don’t rebuild logic by hand (e.g. manual uppercase via a hashmap letter-by-letter vs one call to `.upper()`).

---

## Time / space (common operations)

| Operation | Time | Notes |
|-----------|------|--------|
| Index `s[i]` | O(1) | |
| Slice `s[a:b]` | O(b − a) | **new string** (copy of that range) |
| `s + t` (concat) | O(len(s) + len(t)) | |
| `s.lower()`, `.upper()`, etc. | O(n) | new string |
| `s[::-1]` (reverse) | O(n) | new string |
| Build with `+=` in a loop | O(n²) worst case | strings are immutable; repeated `+=` reallocates — prefer `"".join(parts)` or list + join |
| `.join(list)` | O(total chars) | preferred builder |

**Space:** any method that returns a **new** string uses O(n) extra for that result.

---

## 1. Casing methods

| Method | What it does |
|--------|----------------|
| `s.upper()` | Every letter → uppercase |
| `s.lower()` | Every letter → lowercase |
| `s.capitalize()` | First char upper, **rest lower** |
| `s.isupper()` | `True` if every cased letter is upper |
| `s.islower()` | `True` if every cased letter is lower |

```python
"Hello".upper()        # "HELLO"
"Hello".lower()        # "hello"
"hello world".capitalize()  # "Hello world"
```

---

## 2. Character checks

| Method | `True` when |
|--------|-------------|
| `c.isalpha()` | Every char is a **letter** (no digits/spaces) |
| `c.isnumeric()` | Every char is a **number** |
| `c.isalnum()` | Every char is **letter or digit** (excludes space, `-`, `:`, etc.) |

**Typo trap (from video):** it’s **`isalnum()`**, not `islnnum` / `isLnnum`. Syntax slips are fine if the approach is right.

```python
"A".isalpha()      # True
"9".isnumeric()    # True
"A1".isalnum()     # True
"A man".isalnum()  # False  (space)
```

Use `isalnum()` when filtering input like LeetCode 125 (letters + digits only).

---

## 3. Search / count

| Method | Returns |
|--------|---------|
| `s.count(ch)` | How many times `ch` appears |
| `s.find(ch)` | **First** index of `ch`, or `-1` if missing |
| `s.rfind(ch)` | **Last** index of `ch`, or `-1` if missing |

---

## 4. Slicing (same idea as subarrays)

Format: `s[start : stop : step]` — `stop` is **exclusive**.

```python
s = "banana"
s[2:5]      # "nan"     indices 2,3,4
s[1:6:2]    # "aaa"     start 1, stop before 6, step 2 → indices 1,3,5
```

**Reverse entire string** (used in palindrome check):

```python
s[::-1]     # step −1 → walk backwards
```

| Slice | Meaning |
|-------|---------|
| `s[:]` | whole string |
| `s[2:]` | from index 2 to end |
| `s[:4]` | start to index 3 |
| `s[::2]` | every 2nd char |
| `s[::-1]` | reversed |

---

## 5. Formatting / manipulation

| Method | What it does |
|--------|----------------|
| `s.strip()` | Remove **leading & trailing** whitespace |
| `s.replace(old, new)` | Replace all `old` with `new` |
| `s.split(sep)` | Split into **list** of substrings on `sep` |
| `sep.join(iterable)` | Opposite of split — join list with `sep` between items |
| f-strings | `f"value={x}"` embed expressions in literals |

```python
"  hi  ".strip()           # "hi"
"a-b-c".split("-")        # ['a', 'b', 'c']
"-".join(["a", "b", "c"]) # "a-b-c"
name = "Ada"
f"Hello, {name}"          # "Hello, Ada"
```

**`join` is on the separator string**, not on the list: `",".join(words)`.

---

## Pattern: Valid Palindrome (LC 125)

**Goal:** After `lower()` + remove non-alphanumeric, reads same forward and backward.

### Approach A — everything from this video

1. `s = s.lower()`
2. Build filtered string — loop each char, keep only if `char.isalnum()`:

```python
s_new = ""
for char in s:
    if char.isalnum():
        s_new += char
```

3. Compare forward vs backward with slicing:

```python
return s_new == s_new[::-1]
```

### Approach B — idiomatic filter (same logic)

```python
s_new = "".join(ch.lower() for ch in s if ch.isalnum())
return s_new == s_new[::-1]
```

### Approach C — two pointers (O(1) extra space)

Skip non-alnum on original `s` with `left` / `right` — see [leetcode_125.py](../../leetcode/week_2/leetcode_125.py).

| Approach | Time | Extra space |
|----------|------|-------------|
| Filter + `==` reverse | O(n) | O(n) |
| Two pointers on `s` | O(n) | O(1) |

---

## Interview checklist (strings)

1. Can I use a **built-in** instead of a manual loop? (casing, strip, split, join)
2. Am I creating many **copies** (`+=` in loop, repeated slices)?
3. Do I need **two pointers** (palindrome, reverse words) or **sliding window** (substring)?
4. For “only letters/digits” → **`isalnum()`** per character
5. To reverse → **`s[::-1]`** or two pointers from both ends

---

## Quick reference (copy before practice)

```python
# casing
s.lower(); s.upper(); s.capitalize()

# checks (per char c)
c.isalpha(); c.isnumeric(); c.isalnum()

# search
s.count(x); s.find(x); s.rfind(x)

# slice & reverse
sub = s[i:j]; rev = s[::-1]

# edit
s.strip(); s.replace(a, b); parts = s.split(","); s2 = "|".join(parts)
```

---

## Your repo

| File | Notes |
|------|--------|
| [leetcode_125.py](../../leetcode/week_2/leetcode_125.py) | Filter + two pointers + complexity table |
| [dsa-study-plan.html](../../learn_plans/dsa-study-plan.html) | t03 Strings — full LC list |

**Next:** re-solve #125 **without hints**, then mark **No hints** in portal when clean.
