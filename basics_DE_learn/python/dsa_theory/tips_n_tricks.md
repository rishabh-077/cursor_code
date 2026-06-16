# Tips & tricks — solved LeetCode (revision sheet)

**Purpose:** Pattern triggers, gotchas, and quick recall for every problem you've solved so far.  
**Source of truth for full solutions:** `leetcode/week_*/leetcode_*.py` · **Tracker:** [trackers/lc_log.md](../../trackers/lc_log.md)  
**Theory depth:** [arrays.md](./arrays.md) · [strings.md](./strings.md) · [hash_maps_n_sets.md](./hash_maps_n_sets.md)

**Count:** 18 problems (13 no-hints) · Topics: t02 arrays · t03 strings · t04 hash

---

## How to use this for revision

1. **Before re-solving:** read the **trigger phrase** for that problem — can you name the pattern in 5 seconds?
2. **After solving:** check **Common bugs** — did you avoid them without looking?
3. **Weekly review:** pick one row from **Pattern families** and re-solve 2 linked problems cold.
4. **Interview prep:** say the **One-liner** out loud, then code the preferred approach from the repo file.

---

## Master trigger table (pattern → problems)

| When you see… | Reach for… | Problems |
|---------------|------------|----------|
| "Have we seen this before?" | Hash **set**, one pass | 217 |
| "What partner makes the target?" | Hash **map** `{value: index}` | 1 |
| "Same letters, same counts?" | Frequency map or `Counter` | 242, 387 |
| "Modify array **in-place**" | Two pointers (often write/swap) | 283, 26, 88, 189 |
| "Sorted input + in-place" | Write pointer; compare to last kept | 26, 88 (merge from **end**) |
| "Track best so far while scanning" | Running min / max / streak | 121, 485 |
| "Move / partition without extra array" | `base` + scan index `i` | 283, 26 |
| "Rotate in-place" | `k = k % n` then triple reverse | 189 |
| "Carry / digit overflow" | Loop from LSD (right) or reverse first | 66 |
| "Build next row from previous" | Pad with 0s, sum neighbors | 118 |
| "Compare from both ends" | Two pointers inward | 125, 344 |
| "Reverse in-place" | `left=0`, `right=n-1`, swap | 344, 189 (building block) |
| "Is whole string a palindrome?" | Filter or skip junk, compare ends | 125 |
| "Longest palindromic **substring**" | Expand around **every** center (odd + even) | 5 |
| "Common prefix across strings" | Vertical scan at index `i` for all | 14 |
| "Symbol value depends on next char" | If `curr < next` → subtract pair, skip 2 | 13 |
| "Count consecutive runs" | `i` start of run, `j` end; output `count+digit` | 485, 38 |

---

## Cross-problem families (revision clusters)

Re-solve these together — they share the same muscle memory.

```
Hash / frequency
  217 Contains Duplicate  →  1 Two Sum  →  242 Anagram  →  387 First Unique

Two-pointer write (in-place partition)
  283 Move Zeroes  →  26 Remove Duplicates  →  88 Merge Sorted Array (from end)

Two-pointer inward
  344 Reverse String  →  125 Valid Palindrome  →  5 Longest Palindromic Substring (expand)

Running count / scan
  485 Max Consecutive Ones  →  38 Count and Say (run-length encode)

Palindrome lane
  125 (whole string?)  vs  5 (best substring?)  — different questions, don't mix templates
```

---

## Global pro tips (from your solved set)

### In-place array edits

> **"Modify in-place"** → two pointers, swapping, or write index — **no extra array**.

- **Merge sorted (88):** merge from the **back** so you don't overwrite unread `nums1` values.
- **Move zeroes (283):** `base` = next slot for a non-zero; swap when `nums[i] != 0`.
- **Remove dups (26):** sorted → dups are **adjacent**; compare `nums[i] != nums[i-1]`, no hash set.
- **Rotate (189):** always `k = k % n`; triple reverse beats shifting one-by-one.

### Hash map ordering traps

- **Two Sum (1):** check `if complement in map` **before** `map[n] = i` — avoids pairing an index with itself (`[3,3], target=6`).
- **First unique (387):** pass 2 must scan **`s` left → right**, not dict keys — order matters.
- **Anagram (242):** different lengths → instant `False`; `.get(c, 0)` for missing keys.

### Two-pointer inward

- Loop condition: **`left < right`**, not `<=` — odd length middle shouldn't swap twice (344).
- **Palindrome (125):** on mismatch → return `False` immediately; move both pointers only on match.
- **Reverse (344):** same swap loop as 125, but swap instead of compare.

### "Best so far" one-pass

- **Stock (121):** track `cur_min` (cheapest buy so far); profit if sell today = `p - cur_min`. Global min/max of whole array is **wrong** when min comes after max.
- **Consecutive ones (485):** `curr` resets to 0 on 0; update global max on every 1.

### Strings — build safely

- Prefer `"".join(...)` over `s += ch` in loops — repeated concat is O(n²) (125 first draft).
- LeetCode **344** uses mutable `List[str]` — must mutate in place; `s[::-1]` on a string returns a new string.

---

## By topic — quick cards

### Hash maps & sets (t04)

#### 217 · Contains Duplicate · [leetcode_217.py](../../leetcode/week_1/leetcode_217.py)

| | |
|---|---|
| **Trigger** | Any duplicate? |
| **Pattern** | Set — `if n in seen: return True` |
| **One-liner** | One pass; early exit beats `len(set) != len(nums)` |
| **Revision Q** | Why is set O(n) time? |
| **Bug** | Using nested loops in interview when n is large |

#### 1 · Two Sum · [leetcode_1.py](../../leetcode/week_1/leetcode_1.py)

| | |
|---|---|
| **Trigger** | Pair that sums to target |
| **Pattern** | Map value → index; complement = `target - n` |
| **One-liner** | Lookup complement **before** storing current index |
| **Revision Q** | Walk through `[3,3], target=6` — why order matters |
| **Bug** | Storing index before checking → same element used twice |

#### 242 · Valid Anagram · [leetcode_242.py](../../leetcode/week_1/leetcode_242.py)

| | |
|---|---|
| **Trigger** | Same character counts? |
| **Pattern** | Two maps, single map (+1/-1), or `Counter(s) == Counter(t)` |
| **One-liner** | Length mismatch → False; then count |
| **Revision Q** | Explain single-map: why `< 0` means not anagram |
| **Bug** | Sorting works but O(n log n) — mention hash first |

#### 387 · First Unique Character · [leetcode_387.py](../../leetcode/week_3/leetcode_387.py)

| | |
|---|---|
| **Trigger** | First char that appears exactly once |
| **Pattern** | Count pass → scan `s` in order for `count == 1` |
| **One-liner** | Two passes; second pass follows **string order** |
| **Revision Q** | Why not iterate dict keys? |
| **Bug** | Returning first dict key vs first char in `s` |

---

### Arrays (t02)

#### 88 · Merge Sorted Array · [leetcode_88.py](../../leetcode/week_1/leetcode_88.py)

| | |
|---|---|
| **Trigger** | Merge two sorted arrays in-place into larger buffer |
| **Pattern** | Three pointers from **right**: `m`, `n`, `last` |
| **One-liner** | Place larger of `nums1[m-1]` vs `nums2[n-1]` at `last` |
| **Revision Q** | Why not merge from the front? |
| **Bug** | Forgetting tail copy when `nums2` still has elements |

#### 121 · Best Time to Buy and Sell Stock · [leetcode_121.py](../../leetcode/week_1/leetcode_121.py)

| | |
|---|---|
| **Trigger** | Max profit, one buy before one sell |
| **Pattern** | One pass: `cur_min = min(cur_min, p)`, `max_prof = max(max_prof, p - cur_min)` |
| **One-liner** | Cheapest buy **so far**, not global min |
| **Revision Q** | Why `[2,4,1]` breaks global min/max? |
| **Bug** | Using `min(prices)` and `max(prices)` without order constraint |

#### 485 · Max Consecutive Ones · [leetcode_485.py](../../leetcode/week_2/leetcode_485.py)

| | |
|---|---|
| **Trigger** | Longest streak of 1s in binary array |
| **Pattern** | Running count; reset on 0 |
| **One-liner** | `curr += 1` on 1, `curr = 0` on 0, track max |
| **Revision Q** | Why no nested loops needed? |
| **Bug** | Not resetting counter after seeing 0 |

#### 283 · Move Zeroes · [leetcode_283.py](../../leetcode/week_2/leetcode_283.py)

| | |
|---|---|
| **Trigger** | Move all 0s to end, keep relative order, in-place |
| **Pattern** | `base` write pointer + scan `i`; swap non-zeros forward |
| **One-liner** | Partition: everything before `base` is finalized non-zeros |
| **Revision Q** | Swap vs write-index — which minimizes writes? |
| **Bug** | Using extra array (violates constraint) |

#### 26 · Remove Duplicates from Sorted Array · [leetcode_26.py](../../leetcode/week_2/leetcode_26.py)

| | |
|---|---|
| **Trigger** | Unique elements in-place, return `k` |
| **Pattern** | Same family as 283: `base` write, scan `i` from 1 |
| **One-liner** | `if nums[i] != nums[i-1]: nums[base]=nums[i]; base++` |
| **Revision Q** | Why no hash set on sorted input? |
| **Bug** | Starting `base` at 0 instead of 1 (`nums[0]` always kept) |

#### 66 · Plus One · [leetcode_66.py](../../leetcode/week_2/leetcode_66.py)

| | |
|---|---|
| **Trigger** | Add 1 to digit array (MSD first) |
| **Pattern** | Carry from LSD; 9 → 0 and continue |
| **One-liner** | Reverse → carry loop → reverse; or loop `i` from `len-1` down |
| **Revision Q** | What happens for `[9,9,9]`? |
| **Bug** | Not handling new leading digit when all 9s |

#### 118 · Pascal's Triangle · [leetcode_118.py](../../leetcode/week_2/leetcode_118.py)

| | |
|---|---|
| **Trigger** | Build triangle row by row |
| **Pattern** | Pad prev row `[0] + row + [0]`; new cell = `temp[j] + temp[j+1]` |
| **One-liner** | Each interior = sum of two above; edges are 1 |
| **Revision Q** | Why padding with zeros works |
| **Bug** | Off-by-one on new row length (`len(prev) + 1`) |

#### 189 · Rotate Array · [leetcode_189.py](../../leetcode/week_2/leetcode_189.py)

| | |
|---|---|
| **Trigger** | Rotate right by `k`, in-place |
| **Pattern** | `k %= n`; reverse all → reverse `[0:k]` → reverse `[k:n]` |
| **One-liner** | Triple reverse = O(1) space |
| **Revision Q** | Where does index `i` land? `(i + k) % n` |
| **Bug** | Forgetting `k = k % n` when `k > len(nums)` |

---

### Strings (t03)

#### 125 · Valid Palindrome · [leetcode_125.py](../../leetcode/week_2/leetcode_125.py)

| | |
|---|---|
| **Trigger** | Is filtered string a palindrome? |
| **Pattern** | Filter alnum + lower → two pointers inward |
| **One-liner** | O(1) space variant: skip junk on original string |
| **Revision Q** | Difference vs #5? (whole string vs substring search) |
| **Bug** | Only moving pointers on match → misses early False |

#### 344 · Reverse String · [leetcode_344.py](../../leetcode/week_3/leetcode_344.py)

| | |
|---|---|
| **Trigger** | Reverse char array in-place, O(1) space |
| **Pattern** | Same inward loop as 125 — swap instead of compare |
| **One-liner** | `while left < right: swap; left++; right--` |
| **Revision Q** | Why `List[str]` not Python `str`? |
| **Bug** | `left <= right` double-swaps middle on odd length |

#### 14 · Longest Common Prefix · [leetcode_14.py](../../leetcode/week_3/leetcode_14.py)

| | |
|---|---|
| **Trigger** | Shared start across many strings |
| **Pattern** | Vertical scan: for each index `i`, all `s[i] == strs[0][i]` |
| **One-liner** | Cap at **shortest** string length |
| **Revision Q** | Sort + compare first/last trick |
| **Bug** | Index past shortest string → out of range |

#### 13 · Roman to Integer · [leetcode_13.py](../../leetcode/week_3/leetcode_13.py)

| | |
|---|---|
| **Trigger** | Parse Roman numerals |
| **Pattern** | Left-to-right: if `val[s[i]] < val[s[i+1]]` → add difference, `i += 2` |
| **One-liner** | Only 6 subtract pairs (IV, IX, XL, XC, CD, CM) |
| **Revision Q** | Right-to-left alternative? |
| **Bug** | Always adding (IV becomes 6 not 4); peek without `i < n-1` |

#### 38 · Count and Say · [leetcode_38.py](../../leetcode/week_3/leetcode_38.py)

| | |
|---|---|
| **Trigger** | Generate nth term from run-length of previous |
| **Pattern** | Outer `n-1` times; inner scan runs → `str(count)+digit` |
| **One-liner** | Same "run" idea as 485, but output encoded string |
| **Revision Q** | Why loop `n-1` not `n`? (start at `"1"`) |
| **Bug** | Not setting `i = j` after each run → infinite loop |

#### 5 · Longest Palindromic Substring · [leetcode_5.py](../../leetcode/week_3/leetcode_5.py)

| | |
|---|---|
| **Trigger** | Longest substring that reads same forward/back |
| **Pattern** | Expand around center — **odd** (`i,i`) and **even** (`i,i+1`) |
| **One-liner** | O(n²) expand is the interview sweet spot |
| **Revision Q** | Why brute force all substrings is O(n³)? |
| **Bug** | Only odd centers → misses `"bb"`, `"cbbd"` |

---

## Complexity cheat sheet (what to say in interviews)

| Problem | Time | Space | Key reason |
|---------|------|-------|------------|
| 217, 1, 242, 387 | O(n) | O(n) or O(1)* | Single/double pass; *bounded alphabet |
| 88, 283, 26, 189 | O(n) | O(1) | Each element touched constant times |
| 121, 485, 13, 344, 125 | O(n) | O(1) or O(n) | One pass; filter adds O(n) space |
| 118 | O(R²) | O(R²) | Row `i` has `i+1` cells |
| 14 | O(n·m) | O(1) | n strings, m columns |
| 38 | O(output) | O(output) | Sequence grows quickly |
| 5 | O(n²) | O(1) | n centers × expand |

---

## Pre-interview 60-second drills

Say pattern → complexity → one bug to avoid:

1. **Two Sum** → hash map complement → O(n) → store after lookup  
2. **Merge Sorted Array** → merge from end → O(m+n) → don't overwrite unread nums1  
3. **Move Zeroes / Remove Dups** → write pointer `base` → O(n) → sorted means adjacent dups  
4. **Rotate Array** → triple reverse → O(n) → `k %= n`  
5. **Valid Palindrome vs Longest Palindromic** → whole string check vs expand all centers  
6. **First Unique** → count then scan string order → O(n) → not dict key order  
7. **Roman to Int** → smaller before larger subtract → O(n) → advance 2 on pairs  

---

## Spaced repetition order (suggested)

| Week | Re-solve cold (no hints) |
|------|--------------------------|
| +3 days | 1, 217, 283, 26 |
| +1 week | 121, 88, 125, 242 |
| +2 weeks | 189, 66, 387, 344 |
| +3 weeks | 14, 13, 485, 118 |
| +4 weeks | 38, 5 |

Mark **No hints** in [lc_log.md](../../trackers/lc_log.md) only when you solve without opening repo files or this sheet.

---

*Last updated from lc_log: 18 problems · aligns with `leetcode/week_1`, `week_2`, `week_3`.*
