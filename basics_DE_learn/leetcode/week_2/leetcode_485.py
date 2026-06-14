"""
485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/

Problem
  Given a binary array nums (only 0 and 1), return the maximum number of consecutive 1's.

Pattern (t02 — Arrays)
  Single pass: extend a running count when you see 1; reset count to 0 when you see 0.
  Track the best (max) streak seen so far.

Key insight
  You do not need nested loops. Each element either continues the current streak or breaks it.

Approach comparison (n = len(nums))
  | Approach                    | Time  | Space | Notes                          |
  |-----------------------------|-------|-------|--------------------------------|
  | Brute force (all subarrays) | O(n²) | O(1)  | TLE — educational only         |
  | One pass (running count)    | O(n)  | O(1)  | Preferred — submit as Solution |

Examples
  [1,1,0,1,1,1] → 3  (last three 1's)
  [1,0,1,1,0,1] → 2
  [1]           → 1
  [0]           → 0

LeetCode: submit ONE class named Solution (one-pass below).
"""

from typing import List


# --- Approach 1: Brute force — count 1's in every subarray starting at i ---
class SolutionBruteForce:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == 1:
                    count += 1
                    best = max(best, count)
                else:
                    break  # streak broken — longer subarrays from i won't help
        return best
    # Time: O(n²) worst case (all 1's)
    # Space: O(1)


# --- Approach 2: One pass — running streak + global max (submit this as Solution) ---
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        curr_max = 0
        for num in nums:
            if num == 1:
                curr_max += 1
                maxx = max(curr_max, maxx)
            else:
                curr_max = 0
        return maxx
    # Time: O(n) — each index visited once
    # Space: O(1) — only two counters


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
    assert s.findMaxConsecutiveOnes([1]) == 1
    assert s.findMaxConsecutiveOnes([0]) == 0
    assert s.findMaxConsecutiveOnes([]) == 0
    print("leetcode_485: all tests passed")
