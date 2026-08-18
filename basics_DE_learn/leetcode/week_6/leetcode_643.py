"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

Problem
  Given an integer array nums and an integer k, find the maximum average of any
  contiguous subarray of length exactly k.

Examples
  nums = [1, 12, -5, -6, 50, 3], k = 4 → 12.75
    subarray [12, -5, -6, 50] has sum 51 → 51/4 = 12.75
  nums = [5], k = 1 → 5.0

Pattern (t06 — Sliding window, fixed size)
  Window length is **fixed at k**. You are not expanding/shrinking by a condition —
  you **slide** the window one index at a time.

  Template
    1. Build sum of nums[0 : k]          — first window
    2. For i from k to n-1:
         curr_sum += nums[i]              — new element enters (right)
         curr_sum -= nums[i - k]          — old element leaves (left)
         max_sum = max(max_sum, curr_sum)
    3. return max_sum / k

  Why track **sum** not average?
    Dividing by k every step is extra work. Max average ⟺ max sum when k is fixed.

Your approach (week 6 — sliding window, submit Solution)
  curr_sum = sum(nums[:k]); max_sum = curr_sum
  for i in range(k, len(nums)):
      curr_sum += nums[i] - nums[i - k]
      max_sum = max(max_sum, curr_sum)
  return max_sum / k

Pro tip (fixed vs variable window)

Whenever you see:
  "subarray of length k" / "window size k" / "exactly k elements"
Think:
  - **Fixed-size** sliding window — slide with += right, -= left
  - Do **not** use a while-loop to shrink (that's variable window, e.g. #3, #209)

Relation to other problems
  **#1456** Maximum Number of Vowels — same fixed window, count vowels instead of sum.
  **#3** Longest Substring Without Repeating — **variable** window (expand/shrink).
  **#209** Minimum Size Subarray Sum — variable window (shrink while sum >= target).
  **#121** Best Time to Buy/Sell Stock — related idea (running min, not fixed k).

Common bugs
  - Off-by-one: loop `range(k, len(nums))` not `range(k, len(nums)-1)` — last window must be tried
  - Subtracting nums[i-k+1] instead of nums[i-k] — wrong element leaves the window
  - Returning max_sum instead of max_sum / k
  - Recomputing sum(nums[i-k:i]) inside the loop — O(n*k) TLE (brute force)
  - Using float for max_sum when all nums negative — start max_sum from first window sum, not 0

Approach comparison (n = len(nums))
  | Approach                         | Time       | Space | Notes                    |
  |----------------------------------|------------|-------|--------------------------|
  | Brute force — sum each window    | O(n * k)   | O(1)  | SolutionBruteForce below |
  | Fixed sliding window (one pass)  | O(n)       | O(1)  | Your Solution — submit   |

LeetCode: submit ONE class named Solution (sliding window below).
"""

from typing import List


# --- Approach 1: Brute force — re-sum every window of length k ---
class SolutionBruteForce:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float("-inf")
        i = 0
        while i + k <= len(nums):
            curr_sum = 0
            for j in range(i, i + k):
                curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
            i += 1
        return max_sum / k
    # Time: O(n * k)
    # Space: O(1)


# --- Approach 2: Fixed sliding window — add right, drop left (submit as Solution) ---
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k
    # Time: O(n) — each element added once, removed once
    # Space: O(1)
