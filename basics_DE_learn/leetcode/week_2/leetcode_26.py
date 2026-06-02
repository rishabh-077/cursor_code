"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Problem
  nums is sorted in non-decreasing order. Remove duplicates in-place so each unique
  element appears once. Return k = number of unique elements.
  First k slots of nums must hold those unique values (order preserved). Rest ignored.

Pro tip (sorted + in-place)
  Duplicates are adjacent. Compare nums[i] with the last kept value — no hash set needed.

Pattern (t02 — Arrays, same family as Move Zeroes #283)
  Write pointer `base` = length of the unique prefix built so far.
  Scan with `i`; when nums[i] is a new value, copy to nums[base] and grow base.

Pointer meaning (your solution)
  base → index where the next NEW unique value should be written (starts at 1)
  i    → scans from index 1 onward
  Check nums[i] != nums[i - 1]  (new value vs previous element in original order)

  nums[0] is always kept. After loop, return base (= k).

Equivalent check
  nums[i] != nums[base - 1]  — compare to last unique in the prefix (same logic).

Approach comparison (n = len(nums))
  | Approach           | Time  | Space | Notes                              |
  |--------------------|-------|-------|------------------------------------|
  | New unique array   | O(n)  | O(n)  | Extra space — not what LC wants    |
  | Hash set (unsorted)| O(n)  | O(n)  | Loses sort order                   |
  | Two pointers write | O(n)  | O(1)  | Preferred — submit as Solution     |

Examples
  [1,1,2]       → k=2, nums prefix [1,2]
  [0,0,1,1,2]   → k=3, prefix [0,1,2]
  [1]           → k=1

LeetCode: submit ONE class named Solution (two-pointer write below).
"""

from typing import List


# --- Approach 1: Build new list — extra space ---
class SolutionExtraArray:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != unique[-1]:
                unique.append(nums[i])
        for i, v in enumerate(unique):
            nums[i] = v
        return len(unique)
    # Time: O(n)  Space: O(n)


# --- Approach 2: Two pointers — write index (submit this as Solution) ---
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        base = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[base] = nums[i]
                base += 1
        return base
    # Time: O(n) — single scan
    # Space: O(1) — only base and i


if __name__ == "__main__":
    def check(nums, expected_k, expected_prefix):
        arr = nums.copy()
        k = Solution().removeDuplicates(arr)
        prefix = arr[:k]
        ok = k == expected_k and prefix == expected_prefix
        print(f"{nums} -> k={k}, prefix={prefix} (expected k={expected_k}, {expected_prefix}) {'OK' if ok else 'FAIL'}")
        assert ok

    check([1, 1, 2], 2, [1, 2])
    check([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
    check([1], 1, [1])
    check([], 0, [])
    print("leetcode_26: all tests passed")
