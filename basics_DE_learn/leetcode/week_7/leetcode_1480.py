"""
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/

Problem
  Given an array nums, return the running sum: runningSum[i] = sum(nums[0..i]).

Examples
  [1, 2, 3, 4]    → [1, 3, 6, 10]
  [1, 1, 1, 1, 1] → [1, 2, 3, 4, 5]
  [3, 1, 2, 10, 1] → [3, 4, 6, 16, 17]

Pattern (t07 — Prefix sums, build)
  This IS the prefix sum array. Each position stores the total of all elements
  up to and including that index:
    res[0] = nums[0]
    res[i] = res[i-1] + nums[i]

  Building prefix is O(n). Once built, any range sum [l, r] is O(1)
  (see #303 Range Sum Query).

Your approach (week 7 — running accumulation)
  Allocate res[] same length. Seed res[0] = nums[0]. Loop from 1:
  res[i] = nums[i] + res[i-1].

Pro tip (in-place vs new array)
  You could do `nums[i] += nums[i-1]` in-place, but returning a new array
  is safer — keeps the original for later queries if needed.

Relation to other problems
  **#303** Range Sum Query — uses the prefix array you build here.
  **#724** Find Pivot Index — left-sum vs right-sum using prefix or running total.
  **#560** Subarray Sum Equals K — prefix + hashmap.

Common bugs
  - Starting loop at 0 instead of 1 → `res[-1]` index error or wrong seed
  - Returning nums instead of res (if modifying in-place but question wants new list)
  - Using `sum(nums[:i+1])` inside the loop → O(n²) instead of O(n)

Approach comparison (n = len(nums))
  | Approach                     | Time | Space | Notes                  |
  |------------------------------|------|-------|------------------------|
  | Recompute sum each index     | O(n²)| O(n)  | sum(nums[:i+1]) loop   |
  | Running accumulation         | O(n) | O(n)  | Your Solution — submit |
  | In-place nums[i] += nums[i-1]| O(n) | O(1)  | Mutates input          |

LeetCode: submit ONE class named Solution.
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = nums[0]
        for num in range(1, len(nums)):
            res[num] = nums[num] + res[num - 1]
        return res
    # Time: O(n)
    # Space: O(n) — the result array
