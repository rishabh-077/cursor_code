"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Problem
  Given an unsorted integer array nums, return the length of the longest
  sequence of **consecutive** integers (order in the array does not matter).
  Must run in **O(n)** time.

Examples
  nums = [100, 4, 200, 1, 3, 2] → 4     (1, 2, 3, 4)
  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] → 9
  nums = [] → 0

Pattern (t04 — Hash set, only start a run at the left edge)
  Put all numbers in a set (O(1) lookup, drops duplicates).
  A number `n` can **start** a consecutive run only if `n - 1` is **not** in
  the set (nothing immediately before it).
  From each start, walk `n, n+1, n+2, …` while present; track max length.

  Why only starts?
  If you walked from every n, each run would be counted many times → O(n²)
  in disguise (e.g. 1..n all present). Starting only at left edges visits
  each number **once** across all walks → O(n).

  Template
    1. s = set(nums); longest = 0
    2. for n in s:
         if n - 1 not in s:          ← n is a start
           length = 0
           while n + length in s:
             length += 1
           longest = max(longest, length)
    3. return longest

Your approach (week 8 folder — catch-up, not t08 stack)
  Exactly the template. Iterate `set_nums` not `nums` so duplicates do not
  restart the same walk.

Why not sort?
  Sorting is O(n log n) — violates the O(n) constraint (still a valid
  fallback if they allow it).

Relation to other problems
  **#217** Contains Duplicate — set membership only.
  **#298** Binary Tree Longest Consecutive Sequence — tree version.
  Union-find can also merge consecutives — overkill here.

Common bugs
  - Walking from every n without the `n-1 not in set` guard → TLE
  - Using `nums` in the for-loop with duplicates → extra work (usually still OK)
  - `length` starting at 1 vs 0: with `while n + length in s` start at **0**
    (first hit is n itself)
  - Empty input: set empty → longest stays 0

Approach comparison (n = len(nums))
  | Approach                         | Time       | Space | Notes                     |
  |----------------------------------|------------|-------|---------------------------|
  | Sort + scan runs                 | O(n log n) | O(1)* | *if sort in place         |
  | Set + start only at n-1 missing  | O(n)       | O(n)  | **Your Solution — submit**|

LeetCode: submit ONE class named Solution.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for n in set_nums:
            if (n - 1) not in set_nums:
                length = 0
                while (n + length) in set_nums:
                    length += 1
                longest = max(longest, length)
        return longest
    # Time: O(n) — each value enters the while at most once
    # Space: O(n) — hash set
