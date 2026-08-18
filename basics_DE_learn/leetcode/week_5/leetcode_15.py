"""
15. 3Sum
https://leetcode.com/problems/3sum/

Problem
  Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]]
  such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
  The solution set must not contain duplicate triplets.

Examples
  nums = [-1, 0, 1, 2, -1, -4]
  → [[-1, -1, 2], [-1, 0, 1]]

  nums = [0, 1, 1]  →  []
  nums = [0, 0, 0]  →  [[0, 0, 0]]

Pattern (t05 — Sort + fix one + two pointers)
  1) Sort the array
  2) Fix index i (first number a)
  3) Two pointers l, r on the subarray after i — find pairs where a + nums[l] + nums[r] == 0
  4) Skip duplicates at i, and after each hit at l (and optionally r)

Your approach (week 5 — sort + outer loop + two pointers)
  nums.sort()
  For each i with value a:
    Skip if i > 0 and a == nums[i-1]
    l = i+1, r = len-1
    While l < r: compare sum to 0 like #167 (target = 0)
    On hit: append triplet, l += 1, skip duplicate l values

Pro tip (k-sum / 3Sum)

Whenever you see:
  "3Sum" / "triplets that sum to zero" / "no duplicate triplets"
Think:
  - **Sort first** — enables two pointers + duplicate skipping
  - Outer loop fixes smallest (or leftmost) value
  - Inner loop is **Two Sum II** with target = -a
  - Skip duplicates at each level or answer repeats

Relation to other problems
  **#167** Two Sum II — inner loop of 3Sum is the same pointer logic (target 0).
  **#1** Two Sum — pair version; hash map if unsorted.
  **#18** 4Sum — same template + one more outer loop.

Why sort + two pointers
  Brute force all triplets → O(n³).
  Sort O(n log n) + for each i, two-pointer scan → O(n²) total.

Common bugs
  - Not sorting first → two pointers don't work
  - Not skipping duplicate **i** → same triplet from repeated `a`
  - Not skipping duplicate **l** (and **r**) after a hit → duplicate triplets in output
  - Using same element twice (l and r must stay with l < r, i < l)
  - Naming inner sum `threeSum` shadows the function — use `total` for clarity
  - Forgetting sum compares to **0** (not a generic target)

Approach comparison (n = len(nums))
  | Approach                    | Time        | Space | Notes                 |
  |-----------------------------|-------------|-------|-----------------------|
  | Sort + fix i + two pointers | O(n²)       | O(1)* | Your solution — submit|
  | Hash map per i              | O(n²)       | O(n)  | Harder duplicate handling |
  | Brute force triplets        | O(n³)       | O(1)  | TLE                   |

  *O(n²) output worst case; sort may use O(log n) stack.

LeetCode: submit ONE class named Solution (sort + two pointers below).
"""

from typing import List


# --- Approach 1: Sort + fix i + two pointers (submit this as Solution) ---
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
    # Time: O(n²) — O(n log n) sort + O(n²) two-pointer scans
    # Space: O(1) extra excluding output (sort in-place)


# --- Approach 2: Also skip duplicate r after a hit (full duplicate guard) ---
class SolutionSkipBoth:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
    # Time: O(n²)   Space: O(1) extra


if __name__ == "__main__":
    def normalize(triplets):
        return sorted(sorted(t) for t in triplets)

    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([1, 2, -2, -1], []),
    ]
    for nums, expected in tests:
        for cls in (Solution, SolutionSkipBoth):
            got = normalize(cls().threeSum(nums.copy()))
            exp = normalize(expected)
            assert got == exp, f"{cls.__name__}: {got} != {exp}"
        print(f"{nums} -> {expected} OK")
    print("leetcode_15: all tests passed")
