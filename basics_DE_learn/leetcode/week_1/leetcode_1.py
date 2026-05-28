"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Problem
  Given nums and target, return indices [i, j] (i != j) such that nums[i] + nums[j] == target.
  Exactly one solution exists; you may not use the same element twice.

Pattern
  "What partner do I need?" → for each n, complement = target - n
  Store {value: index} in a hash map; if complement was seen earlier, done.

Approach comparison (n = len(nums))
  | Approach              | Time     | Space | Notes                              |
  |-----------------------|----------|-------|------------------------------------|
  | Brute force (pairs)   | O(n²)    | O(1)  | Every pair (i, j) — too slow       |
  | Hash map (one pass)   | O(n)     | O(n)  | Preferred — one lookup per element |

Key detail (hash map)
  Check `if diff in prevMap` BEFORE `prevMap[n] = i`
  → avoids using the same index twice (e.g. nums = [3, 3], target = 6)

LeetCode: submit ONE class named Solution (hash map version below).
"""

from typing import List


# --- Approach 1: Brute force — try every pair (i, j) where j > i ---
class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    # Time: O(n²)
    # Space: O(1)


# --- Approach 2: Hash map — complement lookup (submit this as Solution) ---
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # prevMap: number -> index where we last saw it
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n  # complement needed to reach target

            if diff in prevMap:
                # diff was seen at an earlier index
                return [prevMap[diff], i]

            # only store after check — so we don't pair n with itself
            prevMap[n] = i

        return []
    # Time: O(n) — one pass; dict in/lookup O(1) average
    # Space: O(n) — map holds up to n entries


if __name__ == "__main__":
    input_seq = [
        ([2, 7, 11, 15], 9),   # [0, 1]  → 2 + 7
        ([3, 2, 4], 6),        # [1, 2]  → 2 + 4
        ([3, 3], 6),           # [0, 1]  → 3 + 3 (different indices)
    ]

    solution = Solution()
    for nums, target in input_seq:
        print(f"nums={nums}, target={target} -> {solution.twoSum(nums, target)}")
        print("--------------------------------")
