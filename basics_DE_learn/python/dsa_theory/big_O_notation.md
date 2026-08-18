# Big O Notation Cheat Sheet


Big O notation describes the **time complexity** of an algorithm — how runtime grows as input size grows. For a deeper dive, see NeetCode’s “Big O Notation Explained” or a DSA course.

> **Note:** Big O describes **worst-case** growth (upper bound), not exact runtime.

---

## O(1) — Constant

Runtime does **not** grow with input size. Example: array index lookup.

```python
# Array
nums = [1, 2, 3]
nums.append(4)    # push to end — amortized O(1)
nums.pop()        # pop from end
nums[0]           # lookup
nums[1]
nums[2]

# HashMap / Set
hash_map = {}
hash_map["key"] = 10       # insert
print("key" in hash_map)   # lookup
print(hash_map["key"])     # lookup
hash_map.pop("key")        # remove
```

---

## O(n) — Linear

Runtime grows **in proportion** to input size `n`. Example: one pass through an array.

```python
nums = [1, 2, 3]
sum(nums)           # sum of array
for n in nums:      # looping
    print(n)

nums.insert(1, 100) # insert middle — O(n)
nums.remove(100)    # remove middle — O(n)
print(100 in nums)  # search — O(n) for list

import heapq
heapq.heapify(nums) # build heap — O(n)

# Sometimes nested loops are still O(n)
# (e.g. monotonic stack or sliding window)
```

---

## O(n²) — Quadratic

Runtime grows with **n × n**. Common with nested loops over the same input.

Even if the inner loop does not always run `n` times, nested loops over size `n` are often **O(n²)** in worst case.

```python
# Traverse a square grid
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])

# Get every pair of elements in array
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])

# Insertion sort — insert in middle n times → O(n²)
```

---

## O(n × m) — Two different sizes

Outer loop runs `n` times; inner runs `m` times → **n × m** total work.

```python
# Every pair from two different arrays
nums1, nums2 = [1, 2, 3], [4, 5]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        print(nums1[i], nums2[j])

# Traverse a rectangle grid (rows × cols)
nums = [[1, 2, 3], [4, 5, 6]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])
```

---

## O(n³) — Cubic

Three nested loops over size `n` → **n³** in worst case.

```python
# Every triplet in array
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            print(nums[i], nums[j], nums[k])
```

---

## O(log n) — Logarithmic

Each step **cuts the problem in half** (roughly). Think: how many times can you divide `n` by 2 until you reach 1? That count is ~log₂(n).

Binary search on a sorted array is **O(log n)** because you eliminate half the search space per comparison.

```python
# Binary search
nums = [1, 2, 3, 4, 5]
target = 6
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if target < nums[m]:
        r = m - 1
    elif target > nums[m]:
        l = m + 1
    else:
        print(m)
        break

# Binary search on BST (height h → O(h), balanced tree h = log n)
def search(root, target):
    if not root:
        return False
    if target < root.val:
        return search(root.left, target)
    elif target > root.val:
        return search(root.right, target)
    return True

# Heap push and pop — O(log n) each
import heapq
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappop(min_heap)
```

---

## O(n log n) — Linearithmic

Typical for efficient sorts and “do O(log n) work `n` times.”

Example: heap sort — `heapify` is O(n), then `n` pops at O(log n) each → **O(n log n)**.

```python
import heapq

nums = [1, 2, 3, 4, 5]
heapq.heapify(nums)     # O(n)
while nums:
    heapq.heappop(nums) # O(log n) per pop → n pops = O(n log n)

# Merge sort and Python's built-in sorted() are O(n log n)
```

---

## O(2ⁿ) — Exponential (base 2)

Branches double each level — common in recursion with **two choices** per step.

```python
# Recursion: tree height n, two branches per call
def recursion(i, nums):
    if i == len(nums):
        return 0
    branch1 = recursion(i + 1, nums)
    branch2 = recursion(i + 2, nums)
    return branch1 + branch2
```

---

## O(cⁿ) — Exponential (base c)

Same idea as O(2ⁿ), but **c branches** per step (c may be a constant or related to n).

```python
def recursion(i, nums, c):
    if i == len(nums):
        return 0
    total = 0
    for j in range(i, i + c):
        total += recursion(j + 1, nums, c)
    return total
```

---

## O(n!) — Factorial

All permutations of `n` items — grows extremely fast.

```python
def permute(nums):
    res = []

    def backtrack(path, remaining):
        if not remaining:
            res.append(path)
            return
        for i in range(len(remaining)):
            backtrack(
                path + [remaining[i]],
                remaining[:i] + remaining[i + 1:],
            )

    backtrack([], nums)
    return res
```

---

## O(√n) — Square root

Often appears when you only iterate up to √n (e.g. finding factors).

```python
import math

n = 12
factors = set()
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        factors.add(i)
        factors.add(n // i)
```

---

## How to analyze your own code

Use this checklist on every LeetCode solution (start with **217 — Contains Duplicate**).

### Step 1 — Define `n`

`n` = size of the main input (here, `len(nums)`). All complexity is expressed in terms of `n`.

### Step 2 — Count operations that scale with `n`

Ask:

1. **How many loops?** One pass → often O(n). Two nested passes over the same array → often O(n²).
2. **What does each loop do?** A hash lookup inside one loop is still O(1) per iteration → whole loop stays O(n).
3. **Hidden costs** — `nums.sort()`, `in` on a list, `insert`/`remove` in the middle of a list are not O(1); check the cheat sheet above.

### Step 3 — Space (auxiliary memory)

Separate from time:

- **O(1)** — only a few variables (indices, counters).
- **O(n)** — you store up to `n` items (set, dict, extra array).

Input storage does not count toward auxiliary space on LeetCode.

### Step 4 — State time and space together

Example format for your notes:

> **Approach:** …  
> **Time:** O(…) because …  
> **Space:** O(…) because …

---

### Worked example: LeetCode 217 (Contains Duplicate)

**Problem (one line):** Return `true` if any value in `nums` appears more than once.

Do not memorize one answer — compare **approaches** and their tradeoffs:

| Approach (idea only) | Time | Space | Why |
|----------------------|------|-------|-----|
| Compare every pair of indices | O(n²) | O(1) | Two nested loops over `n` elements |
| Sort, then scan neighbors | O(n log n) | O(1)* | Sort dominates; one linear scan after |
| Track seen values in a set | O(n) | O(n) | One loop; each add / lookup is O(1) on average |

\*Python’s `sort()` may use O(n) extra memory internally; for interviews, O(1) auxiliary is often accepted if you only count your own variables.

**Practice prompt for Day 2:** Pick one approach, implement it, then write three sentences: what is `n`, what repeats `n` times, and what extra storage you use.

```python
# Analysis template — fill in after you solve (no solution here)
def containsDuplicate(self, nums: list[int]) -> bool:
  # Time: O(?) because ...
  # Space: O(?) because ...
  ...
```

### Common mistakes when labeling Big O

| Mistake | Fix |
|---------|-----|
| Saying O(n²) for two loops on **different**-sized inputs | Use O(n × m) if sizes differ |
| Ignoring `sort()` | Sorting is usually O(n log n), not O(n) |
| Forgetting set/dict space | Storing up to `n` keys → O(n) space |
| Using worst case for hash tables | Average O(1) lookup is standard in interviews; mention worst case only if asked |

---

## Quick reference

| Notation   | Name          | Typical pattern                          |
|-----------|---------------|------------------------------------------|
| O(1)      | Constant      | Index lookup, hash map get/set           |
| O(log n)  | Logarithmic   | Binary search, heap push/pop             |
| O(n)      | Linear        | Single loop, scan array                  |
| O(n log n)| Linearithmic  | Efficient sort, heap sort                |
| O(n²)     | Quadratic     | Nested loops on same array               |
| O(n × m)  | Rectangular   | Grid or two arrays of different sizes    |
| O(2ⁿ)     | Exponential   | Two-branch recursion                     |
| O(n!)     | Factorial     | Permutations                             |
