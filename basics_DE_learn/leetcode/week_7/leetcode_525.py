"""
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/

Problem
  Given a binary array nums (only 0 and 1), return the maximum length of a
  contiguous subarray with an equal number of 0 and 1.

Examples
  nums = [0, 1]       → 2
  nums = [0, 1, 0]    → 2   ([0,1] or [1,0])
  nums = [0, 0, 1, 1] → 4
  nums = [0, 1, 0, 1] → 4

Pattern (t07 — Prefix balance + hashmap)
  Equal 0s and 1s ⟺ (count[1] - count[0]) is unchanged across a subarray,
  or equivalently: treat 0 as -1, then look for subarray sum == 0.

  Your code tracks zero/one counts and maps:
    diff = one - zero  →  earliest index where that diff appeared

  If the same diff appears again at i, the subarray (idx+1 .. i) has equal
  0s and 1s. Length = i - idx.

  Special case: one == zero at any point → subarray from the start has
  equal counts → length = one + zero (whole prefix).

  Template (0→-1 rewrite, same idea as #560 with k = 0)
    1. cur = 0; first = {0: -1}; res = 0
    2. for i, n in enumerate(nums):
         cur += 1 if n == 1 else -1
         if cur in first:
           res = max(res, i - first[cur])
         else:
           first[cur] = i
    3. return res

Your approach (week 7 — zero/one counts + diff→index map)
  Same math as the -1 rewrite. Store first occurrence of each (one - zero).
  When balance returns, update max length. When one == zero, take full prefix.

Why store the *first* index only?
  Longest subarray → earliest start for a given balance. Overwriting with a
  later index would only shorten later matches.

Relation to other problems
  **#560** Subarray Sum Equals K — same prefix + map; here k = 0 after 0→-1.
  **#523** Continuous Subarray Sum — prefix mod + map (related family).
  **#325** Maximum Size Subarray Sum Equals k — longest, not count (like this).

Common bugs
  - Storing *every* update of diff (last index) instead of first → shorter answers
  - Forgetting the one == zero full-prefix case (or not seeding {0: -1})
  - Looking up diff *after* inserting current i → length 0 self-match
  - Using count of subarrays (#560 style) instead of max length
  - Off-by-one: length is i - idx, not i - idx + 1, when idx is last index
    *before* the good subarray starts

Approach comparison (n = len(nums))
  | Approach                            | Time  | Space | Notes                     |
  |-------------------------------------|-------|-------|---------------------------|
  | Brute — check every subarray        | O(n²) | O(1)  | count 0/1 each range      |
  | Prefix balance + first-index map    | O(n)  | O(n)  | **Your Solution — submit**|

LeetCode: submit ONE class named Solution.
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one, res = 0, 0, 0
        dif_index = {}  # count[1] - count[0] -> earliest index

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            if one - zero not in dif_index:
                dif_index[one - zero] = i

            if one == zero:
                res = one + zero
            else:
                idx = dif_index[one - zero]
                res = max(res, i - idx)

        return res
    # Time: O(n) — one pass, O(1) map ops per step
    # Space: O(n) — hashmap of balance → first index
