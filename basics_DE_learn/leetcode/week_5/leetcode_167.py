"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem
  Given a 1-indexed array of integers numbers that is sorted in non-decreasing
  order, find two numbers such that they add up to target.
  Return the indices **1-indexed** [index1, index2] with index1 < index2.
  Exactly one solution exists; you may not use the same element twice.

Examples
  numbers = [2, 7, 11, 15], target = 9  →  [1, 2]   (2 + 7)
  numbers = [2, 3, 4], target = 6         →  [1, 3]
  numbers = [-1, 0], target = -1          →  [1, 2]

Pattern (t05 — Two pointers / opposite ends on sorted array)
  Sorted → if sum too big, drop the **right** (larger) pointer; if too small,
  advance the **left** (smaller) pointer. O(n) time, O(1) space.

Your approach (week 5 — two pointers)
  l = 0, r = len - 1
  sum > target → r -= 1
  sum < target → l += 1
  sum == target → return [l + 1, r + 1]  (1-indexed)

Your first draft (hash map — works but ignores sorted input)
  Same as **#1** Two Sum — O(n) space; correct logic, not optimal for this problem.

Pro tip (sorted + pair sum)

Whenever you see:
  "sorted array" + "two sum" / "pair that adds to target"
Think:
  - **Two pointers** from both ends (use the sort order)
  - Return **1-indexed** on this problem (LeetCode quirk vs #1)
  - Hash map from #1 still works — but wastes O(n) extra space here

Why two pointers work (proof sketch)
  If numbers[l] + numbers[r] > target, any pair including numbers[r] with a
  larger left index is also too big → safe to decrement r.
  Symmetric argument for l += 1 when sum is too small.

Relation to other problems
  **#1** Two Sum — unsorted → hash map {value: index}.
  **#167** Two Sum II — **sorted** → two pointers O(1) space.
  **#977** Squares of Sorted Array — same inward pointer family.
  **#15** 3Sum — sort + fix one + two pointers on rest (wk 5).

Common bugs
  - Returning 0-indexed `[l, r]` instead of `[l+1, r+1]`
  - Using hash map when interview expects O(1) space on sorted input
  - `l <= r` with same element — use `l < r` (need two distinct indices)
  - Off-by-one on which pointer to move when sum != target

Approach comparison (n = len(numbers))
  | Approach              | Time  | Space | Notes                          |
  |-----------------------|-------|-------|--------------------------------|
  | Two pointers          | O(n)  | O(1)  | Preferred — submit Solution    |
  | Hash map (#1 style)   | O(n)  | O(n)  | Your first draft — still AC    |
  | Binary search per l   | O(n log n) | O(1) | Overkill                       |

LeetCode: submit ONE class named Solution (two pointers below).
"""

from typing import List


# --- Approach 1: Hash map — same as #1 (your first draft; learning only) ---
class SolutionHashMap:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff] + 1, i + 1]
            prevMap[n] = i
        return []
    # Time: O(n)   Space: O(n)
    # Correct, but does not use sorted order — extra space vs two pointers


# --- Approach 2: Two pointers — use sorted order (submit this as Solution) ---
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
    # Time: O(n) — each pointer moves at most n times
    # Space: O(1) — only l and r


if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
    ]
    for numbers, target, expected in tests:
        for cls in (Solution, SolutionHashMap):
            got = cls().twoSum(numbers, target)
            assert got == expected, f"{cls.__name__}: {got} != {expected}"
        print(f"numbers={numbers}, target={target} -> {expected} OK")
    print("leetcode_167: all tests passed")
