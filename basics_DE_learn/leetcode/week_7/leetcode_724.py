"""
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/

Problem
  Given an integer array nums, return the **leftmost** pivot index where
  the sum of elements strictly to its left equals the sum strictly to its right.
  If no pivot exists, return -1. (Elements at the pivot itself are excluded.)

Examples
  nums = [1, 7, 3, 6, 5, 6] → 3   (left = 1+7+3 = 11, right = 5+6 = 11)
  nums = [1, 2, 3]          → -1
  nums = [2, 1, -1]         → 0   (left = 0, right = 1+(-1) = 0)

Pattern (t07 — Prefix sums, pivot / balance point)
  Two ways to think about it:

  **Approach 1 — prefix array (size n+1)**
    Build p_sum[0..n] where p_sum[0] = 0, p_sum[i] = p_sum[i-1] + nums[i-1].
    Pivot at index j (0-based in nums) when:
      leftSum  = p_sum[j]
      rightSum = p_sum[n] - p_sum[j+1]
    i.e. p_sum[j] == p_sum[n] - p_sum[j+1]

    In your code j is `index - 1` because you loop index over 1..n:
      p_sum[index - 1] == p_sum[n] - p_sum[index]

  **Approach 2 — running left_sum (no extra array)**
    total = sum(nums)
    Scan left to right. At each i:
      rightSum = total - nums[i] - leftSum
      if rightSum == leftSum → return i
      leftSum += nums[i]

Your two approaches (week 7)
  1) Prefix array of size n+1 — clear O(1) lookups, uses O(n) space.
  2) Running left_sum — same O(n) time, O(1) space.  ← submit this

Which is better?  **Approach 2** — O(1) space, one pass after initial sum.
  Approach 1 is fine for learning prefix mechanics; Approach 2 is cleaner
  in interviews (no off-by-one on the extra slot).

Pro tip
  "Left sum == right sum" means `2 * leftSum + nums[i] == total`.
  You can skip computing rightSum explicitly:
    if leftSum == (total - nums[i]) / 2  — but watch integer division.
  Safer to compare `rightSum == leftSum` directly.

Relation to other problems
  **#1480** Running Sum — builds the prefix array you use in Approach 1.
  **#303** Range Sum Query — same prefix but answers [l, r] queries.
  **#560** Subarray Sum Equals K — prefix + hashmap.

Common bugs
  - Including nums[i] in left or right sum → pivot element must be excluded
  - Off-by-one in prefix array: p_sum has n+1 elements, index shift by 1
  - Returning the first match from the right instead of leftmost
  - Forgetting left_sum starts at 0 (nothing to the left of index 0)
  - Edge: pivot at index 0 → leftSum = 0 (valid)

Approach comparison (n = len(nums))
  | Approach                     | Time | Space | Notes                        |
  |------------------------------|------|-------|------------------------------|
  | Prefix array (n+1)           | O(n) | O(n)  | SolutionPrefixArray          |
  | Running left_sum             | O(n) | O(1)  | **Solution — submit**        |

LeetCode: submit ONE class named Solution (running left_sum below).
"""

from typing import List


# --- Approach 1: Prefix array of size n+1 ---
class SolutionPrefixArray:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        p_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            p_sum[i] = p_sum[i - 1] + nums[i - 1]

        for index in range(1, len(p_sum)):
            if p_sum[index - 1] == p_sum[len(nums)] - p_sum[index]:
                return index - 1
        return -1
    # Time: O(n)
    # Space: O(n)


# --- Approach 2: Running left_sum — O(1) space (submit) ---
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = t_sum - nums[i] - left_sum
            if right_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1
    # Time: O(n) — one sum() + one pass
    # Space: O(1)
