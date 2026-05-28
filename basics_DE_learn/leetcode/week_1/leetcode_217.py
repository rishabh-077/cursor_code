"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Problem
  Given integer array nums, return True if any value appears at least twice,
  else False if every element is distinct.

Pattern
  "Have we seen this before?" → hash set (or dict) while scanning once.

Approach comparison (n = len(nums))
  | Approach              | Time     | Space | Notes                          |
  |-----------------------|----------|-------|--------------------------------|
  | Brute force (pairs)   | O(n²)    | O(1)  | Compare every pair — too slow  |
  | Hash set (one pass)   | O(n)     | O(n)  | Preferred — early exit on dup  |
  | len vs set(nums)      | O(n)     | O(n)  | One-liner; always builds full set|

LeetCode: submit ONE class named Solution (use hash set version below).
"""

from typing import List

# --- Approach 1: Brute force — compare every pair (i, j) where j > i ---
class SolutionBruteForce:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    # Time: O(n²) — nested loops over n
    # Space: O(1) — no extra structure, only indices i, j


# --- Approach 2: Hash set — track seen values (submit this as Solution) ---
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            # O(1) average lookup in set
            if n in seen:
                return True  # duplicate found — stop early
            seen.add(n)

        return False
    # Time: O(n) — one pass; each in/add is O(1) average
    # Space: O(n) — set holds up to n distinct values


# --- Approach 3: One-liner (same complexity as hash set, no early exit) ---
# def containsDuplicate(self, nums: List[int]) -> bool:
#     return len(nums) != len(set(nums))
# If duplicate exists, set is smaller than list length.


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]
    for nums, expected in tests:
        got = Solution().containsDuplicate(nums)
        print(f"{nums} -> {got} (expected {expected})")
