"""
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Problem
  Given an array of positive integers nums and a positive integer target, return
  the minimal length of a contiguous subarray whose sum is >= target.
  If no such subarray exists, return 0.

Examples
  target = 7,  nums = [2, 3, 1, 2, 4, 3] → 2  ([4, 3]
  target = 4,  nums = [1, 4, 4]          → 1  ([4]
  target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1] → 0  (no subarray sums to >= 11)

Pattern (t06 — Sliding window, variable size)
  Expand right to grow the sum. Once sum >= target, shrink from the left while
  the window is still valid — each shrink may find a shorter valid window.
  Track the minimum length seen.

  Template
    1. l = 0; total = 0; min_len = float("inf")   — sentinel: "no window yet"
    2. for r in range(len(nums)):
         total += nums[r]                         — expand
         while total >= target:                   — valid: try to shrink
             min_len = min(min_len, r - l + 1)
             total -= nums[l]
             l += 1
    3. return 0 if min_len == float("inf") else min_len

  Why shrink with while (not if)?
    After adding nums[r], several left removals may still leave sum >= target.
    Each step can improve (shorten) the answer — keep shrinking until invalid.

  Why float("inf") as the starter for min_len?
    We need a value larger than any real length so the first real window always
    wins in min(...). Using 0 would break min (answer would stay 0 forever).
    At the end: if min_len is still inf, no valid window existed → return 0.

    Note on `float("inf") + 1`:
      In Python, float("inf") + 1 is still float("inf"), so
        min_len == float("inf") + 1
      is the same as
        min_len == float("inf")
      Prefer the plain check — the +1 adds nothing and looks like a bug.

Your approach (week 6 — variable sliding window)
  Grow total with r. While total >= target, record length, drop nums[l], advance l.

Pro tip (fixed vs variable window)

Whenever you see:
  "minimum / shortest subarray with sum >= target" / "at least"
Think:
  - **Variable-size** sliding window — expand with for-r, shrink with while
  - Opposite of #3's validity rule: here shrink while VALID; #3 shrinks while INVALID

Relation to other problems
  **#3** Longest Substring Without Repeating — variable window; shrink while invalid.
  **#643** Maximum Average Subarray I — **fixed** window of length k.
  **#1456** Maximum Number of Vowels — fixed window; count vowels instead of sum.
  Binary search + prefix sums also works in O(n log n) — good follow-up.

Common bugs
  - Returning min_len when it is still inf (should be 0) — miss the "no answer" case
  - Using `if total >= target` instead of `while` — miss shorter windows
  - Updating min_len after shrinking past validity — record length BEFORE subtract
  - Assuming nums can be empty / negatives — this problem guarantees positives
    (negatives break the "shrink while sum >= target" monotonicity)
  - Off-by-one: length is r - l + 1, not r - l

Approach comparison (n = len(nums))
  | Approach                              | Time       | Space | Notes                  |
  |---------------------------------------|------------|-------|------------------------|
  | Brute — all subarray sums             | O(n²)      | O(1)  | nested loops           |
  | Variable sliding window               | O(n)       | O(1)  | Your Solution — submit |
  | Prefix sum + binary search            | O(n log n) | O(n)  | follow-up style        |

LeetCode: submit ONE class named Solution.
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total, min_len = 0, 0, float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_len = min(min_len, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if min_len == float("inf") else min_len
    # Time: O(n) — each index enters/leaves the window at most once
    # Space: O(1)
