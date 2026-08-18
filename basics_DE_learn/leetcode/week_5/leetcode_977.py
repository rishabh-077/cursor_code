"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Problem
  Given an integer array nums sorted in non-decreasing order, return an array of
  the squares of each number sorted in non-decreasing order.

Examples
  [-4, -1, 0, 3, 10] → [0, 1, 9, 16, 100]
  [-7, -3, -2, -1, 0, 1, 2, 3, 4] → [0, 1, 1, 4, 4, 9, 9, 16, 49]

Pattern (t05 — Two pointers / opposite ends)
  Input is **already sorted**. Squaring makes large values at **both ends**
  (negative left, positive right). Compare |nums[l]| vs |nums[r]| — place the
  larger square first, then reverse (or fill result from the right).

Your approach (week 5 — inward pointers + reverse)
  l = 0, r = len-1
  While l <= r: append max(nums[l]², nums[r]²) to res; move pointer from larger end
  return res[::-1]  — built largest→smallest, reverse for ascending

Pro tip (sorted array + squares)

Whenever you see:
  "sorted array" + "squares" / "merge from ends" / "largest at both ends"
Think:
  - Two pointers from **left and right** (not one pass left→right)
  - Compare absolute values or squares at ends
  - Fill answer **from the back** (like #88 merge) to skip final reverse

Why not square every element then sort?
  Works: [x*x for x in nums] then sort → O(n log n).
  Two pointers → O(n) because original order already tells you where big squares live.

Relation to other problems
  **#88** Merge Sorted Array — fill from the **right** with two pointers.
  **#125** / **#344** — inward pointers on opposite ends.
  **#167** Two Sum II — same sorted + two-pointer family (wk 5).

Common bugs
  - Single pass left→right squaring — wrong order when negatives exist
  - Forgetting to reverse (if you append largest first)
  - Using `l < r` only — need `l <= r` when one element left (middle square)
  - `nums[l] * nums[l]` vs `nums[l] ** 2` — same; watch overflow on other problems

Approach comparison (n = len(nums))
  | Approach                    | Time       | Space | Notes                    |
  |-----------------------------|------------|-------|--------------------------|
  | Two pointers + reverse      | O(n)       | O(n)  | Your solution — submit   |
  | Two pointers, write from end| O(n)       | O(n)  | No reverse step          |
  | Square all + sort           | O(n log n) | O(n)  | Simple but slower        |

LeetCode: submit ONE class named Solution (two pointers below).
"""

from typing import List


# --- Approach 1: Two pointers inward — append max square, then reverse (submit) ---
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1
        return res[::-1]
    # Time: O(n) — each index visited once
    # Space: O(n) — output list


# --- Approach 2: Fill result from the right — no reverse (same logic, cleaner) ---
class SolutionWriteFromEnd:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        i = n - 1
        while l <= r:
            left_sq = nums[l] * nums[l]
            right_sq = nums[r] * nums[r]
            if left_sq > right_sq:
                res[i] = left_sq
                l += 1
            else:
                res[i] = right_sq
                r -= 1
            i -= 1
        return res
    # Time: O(n)   Space: O(n)


# --- Approach 3: Square + sort — learning only ---
class SolutionSort:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x * x for x in nums)
    # Time: O(n log n)   Space: O(n)


if __name__ == "__main__":
    tests = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, -2, -1, 0, 1, 2, 3, 4], [0, 1, 1, 4, 4, 9, 9, 16, 49]),
        ([-5, -3, -2, -1], [1, 4, 9, 25]),
        ([1, 2, 3], [1, 4, 9]),
    ]
    for nums, expected in tests:
        for cls in (Solution, SolutionWriteFromEnd, SolutionSort):
            got = cls().sortedSquares(nums)
            assert got == expected, f"{cls.__name__}: {got} != {expected}"
        print(f"{nums} -> {expected} OK")
    print("leetcode_977: all tests passed")
