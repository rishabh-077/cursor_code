"""
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/

Problem
  You are given strings jewels (types of jewels) and stones (stones you have).
  Each character in stones is a type of stone. Return how many stones are also jewels.

Examples
  jewels = "aA", stones = "aAAbbbb" → 3   ('a' and 'A' count; 'b' is not a jewel)
  jewels = "z",  stones = "ZZ"      → 0

Pattern (t04 — Hash / set membership)
  "Is this item in the allowed set?" → put jewels in a **set**, scan stones once, count hits.

Your approach (week 4 — jewel set + linear scan)
  1) `s = set(jewels)` — O(1) average lookup per stone type
  2) For each stone: if `stone in s`, increment count

Pro tip (membership / counting)

Whenever you see:
  "how many of B are in A?" / "count matches against a type list"
Think:
  - Put the **small lookup set** (jewels) in a hash set — not repeated `in string` scans
  - One pass over stones — no need to count non-jewels unless asked
  - Set for existence; Counter only if you need per-type totals

Relation to other problems
  **#217** Contains Duplicate — set detects membership / repeats.
  **#383** Ransom Note — frequency map when you need **counts**, not just yes/no.
  Here you only need **membership** → set beats dict.

Why set beats brute force
  `if stone in jewels` where jewels is a **string** → O(len(jewels)) per stone → O(S×J).
  `if stone in set(jewels)` → O(1) average per stone → O(S + J).

Why dict count is overkill here
  Counting all stone types then summing jewel keys works, but you can increment
  the answer directly when `stone in jewel_set` — no second loop needed.

Common bugs
  - Using `in jewels` on a string in the hot loop → hidden O(S×J), TLE on large inputs
  - Case sensitivity: 'a' and 'A' are different ('aA' vs 'aa' matters)
  - Confusing "number of jewel **types**" with "number of matching **stones**"

Approach comparison (J = len(jewels), S = len(stones))
  | Approach                    | Time      | Space | Notes                        |
  |-----------------------------|-----------|-------|------------------------------|
  | Brute: `stone in jewels` str| O(S × J)  | O(1)  | Slow — string scan each time |
  | Set + one pass              | O(S + J)  | O(J)  | Preferred — submit Solution  |
  | Count stones dict + sum     | O(S + U)  | O(U)  | U = unique stone types; extra |
  | Counter + sum jewel keys    | O(S + J)  | O(U)  | Same as set when only counting|

  *J and U bounded by 52 (upper + lower case letters on LeetCode).

LeetCode: submit ONE class named Solution (set version below).
"""


# --- Approach 1: Brute force — membership in jewels string (slow) ---
class SolutionBruteForce:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_jewel = 0
        for stone in stones:
            if stone in jewels:
                stone_jewel += 1
        return stone_jewel
    # Time: O(S × J) — each `in jewels` scans the string
    # Space: O(1)


# --- Approach 2: Count all stones in dict, sum counts for jewel types ---
class SolutionDictionary:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_dict = {}
        for c in stones:
            stone_dict[c] = stone_dict.get(c, 0) + 1

        jewel_set = set(jewels)
        stone_jewels = 0
        for st, count in stone_dict.items():
            if st in jewel_set:
                stone_jewels += count
        return stone_jewels
    # Time: O(S + U) — U = unique stone types; jewel lookup O(1) with set
    # Space: O(U)


# --- Approach 3: Set + one pass (submit this as Solution) ---
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        stone_jewel = 0
        for stone in stones:
            if stone in jewel_set:
                stone_jewel += 1
        return stone_jewel
    # Time: O(S + J) — build set + scan stones
    # Space: O(J) — at most 52 chars on LeetCode


# --- Approach 4: Counter — sum counts for jewel types (same result) ---
class SolutionCounter:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter

        stone_counts = Counter(stones)
        jewel_set = set(jewels)
        return sum(stone_counts[j] for j in jewel_set)
    # Time: O(S + J)   Space: O(U)


# --- Approach 5: One-liner (learning) ---
class SolutionSum:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(stone in jewel_set for stone in stones)
    # Time: O(S + J)   Space: O(J)


if __name__ == "__main__":
    tests = [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
        ("Ab", "aaa", 0),  # lowercase 'a' ≠ jewel 'A' — case matters
        ("abc", "abc", 3),
        ("", "abc", 0),
        ("a", "", 0),
    ]
    for jewels, stones, expected in tests:
        for cls in (
            Solution,
            SolutionBruteForce,
            SolutionDictionary,
            SolutionCounter,
            SolutionSum,
        ):
            got = cls().numJewelsInStones(jewels, stones)
            assert got == expected, f"{cls.__name__}: {jewels!r}, {stones!r} -> {got}"
        print(f"jewels={jewels!r}, stones={stones!r} -> {expected} OK")
    print("leetcode_771: all tests passed")
