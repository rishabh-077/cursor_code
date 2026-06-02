"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Problem
  Given an integer array nums, move all 0's to the end while keeping the relative
  order of non-zero elements. Must do this in-place without making a copy of the array.

Pro tip (in-place array)
  Think: two pointers — one scans (i), one marks where the next non-zero should land (base).

Pattern (t02 — Arrays)
  "Partition" style: everything non-zero packs to the left; zeros end up on the right.
  Relative order preserved because you process left → right and only advance base on non-zeros.

Pointer meaning (your swap solution)
  i    → scans every index
  base → next slot that should hold a non-zero (everything before base is finalized)

  When nums[i] != 0: swap nums[i] with nums[base], then base += 1.
  When nums[i] == 0: only i moves — zero stays until a later non-zero swaps past it.

Approach comparison (n = len(nums))
  | Approach              | Time  | Space | Notes                                    |
  |-----------------------|-------|-------|------------------------------------------|
  | New array + copy back | O(n)  | O(n)  | Violates in-place requirement            |
  | Two passes (copy+fill)| O(n)  | O(1)  | Write non-zeros, then zero the tail      |
  | Swap (base + scan)    | O(n)  | O(1)  | Preferred — submit as Solution           |

Follow-up (LeetCode)
  Minimize the total number of operations? Use write-index (assign, not swap) to cut swaps.

LeetCode: submit ONE class named Solution (swap version below).
"""

from typing import List


# --- Approach 1: Extra array — not acceptable for this problem ---
class SolutionExtraArray:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = [x for x in nums if x != 0]
        for i, v in enumerate(non_zero):
            nums[i] = v
        for i in range(len(non_zero), len(nums)):
            nums[i] = 0
    # Time: O(n)  Space: O(n)


# --- Approach 2: Two passes — write non-zeros, then fill zeros (fewer writes than swap) ---
class SolutionWriteIndex:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for x in nums:
            if x != 0:
                nums[write] = x
                write += 1
        while write < len(nums):
            nums[write] = 0
            write += 1
    # Time: O(n)  Space: O(1)


# --- Approach 3: Swap non-zero forward (submit this as Solution) ---
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        base = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[base] = nums[base], nums[i]
                base += 1
    # Time: O(n) — i visits each index once
    # Space: O(1) — only base and i


if __name__ == "__main__":
    def check(inp, expected):
        nums = inp.copy()
        Solution().moveZeroes(nums)
        ok = nums == expected
        print(f"{inp} -> {nums} (expected {expected}) {'OK' if ok else 'FAIL'}")
        assert ok

    check([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
    check([0], [0])
    check([1], [1])
    check([1, 2, 0, 0, 3], [1, 2, 3, 0, 0])
    check([0, 0, 1], [1, 0, 0])
    print("leetcode_283: all tests passed")
