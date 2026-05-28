"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Problem
  Given strings s and t, return True if t is an anagram of s.
  Anagram = same characters, same counts, any order (e.g. "anagram" / "nagaram").

Pattern
  "How many of each letter?" → hash map (char → count) or Counter.

Approach comparison (n = len(s), assume s and t same length after early check)
  | Approach           | Time       | Space | Notes                              |
  |--------------------|------------|-------|------------------------------------|
  | Hash map (2 dicts) | O(n)       | O(1)* | Build countS and countT, then compare |
  | Single hash map    | O(n)       | O(1)* | +1 for s, -1 for t; early exit < 0   |
  | collections.Counter| O(n)       | O(1)* | Same complexity; less boilerplate  |
  | Sorting            | O(n log n) | O(n)  | Simple one-liner; slower time      |

  *English lowercase only → map size bounded by alphabet (26), not n.

Key ideas
  - Different lengths → cannot be anagram → return False immediately
  - countS[c] = 1 + countS.get(c, 0)  → default 0 if char not seen yet
  - Compare counts in countS to countT (or use countS == countT after both built)

LeetCode: submit ONE class named Solution (hash map version below).
"""

from collections import Counter


# --- Approach 1: Two hash maps — count each string (submit this as Solution) ---
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            # .get(c, 0) → treat missing char as count 0 before adding 1
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Every char in s must appear same number of times in t
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    # Time: O(n)
    # Space: O(1) for fixed alphabet (26 lowercase letters)


# --- Approach 2: Counter — same idea, cleaner ---
class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


# --- Approach 3: Sorting — compare sorted character lists ---
class SolutionSorting:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    # Time: O(n log n) — sorting dominates
    # Space: O(n) — sorted() builds new lists


# --- Approach 4: Single hash map — +1 for s, -1 for t (same as Solution, one dict) ---
#
# Mental model: one bucket per letter — add tiles from s, remove tiles from t.
#   Any bucket below 0 → t used a letter more than s had → not an anagram.
#   If same length and no bucket went negative, all buckets are 0 → anagram.
#
# Trace: s="rat", t="tar"
#   After s loop:  {r:1, a:1, t:1}
#   t 't': t→0     t 'a': a→0     t 'r': r→0  → True
#
# Trace: s="rat", t="car"
#   After s loop:  {r:1, a:1, t:1}
#   t 'c': c→-1   → False (extra letter in t)
#
class SolutionSingleMap:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # char → net count (how many more of that letter in s than we've cancelled with t)
        count = {}

        # Pass 1: count every letter in s (order irrelevant — only totals matter)
        for c in s:
            count[c] = count.get(c, 0) + 1

        # Pass 2: cancel with t; fail fast if t has too many of any letter
        for c in t:
            count[c] = count.get(c, 0) - 1
            if count[c] < 0:
                return False

        # Same length + no negative counts → all values are 0 (sums to 0, each entry ≥ 0)
        return True
    # Time: O(n)
    # Space: O(1) for lowercase English (at most 26 keys in count)


if __name__ == "__main__":
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("anagrama", "nagaramn", False),
        ("aaaa", "aaab", False)
    ]
    for s, t, expected in tests:
        got = SolutionSingleMap().isAnagram(s, t)
        print(f"s={s!r}, t={t!r} -> {got} (expected {expected})")
