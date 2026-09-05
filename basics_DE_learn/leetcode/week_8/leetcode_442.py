"""
442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Problem
  Given an array nums of length n where each nums[i] is in **1..n**, and each
  integer appears **once or twice**, return all integers that appear **twice**.
  Follow-up: O(n) time and **O(1) extra space** (output does not count).

Examples
  nums = [4, 3, 2, 7, 8, 2, 3, 1] → [2, 3]
  nums = [1, 1, 2]                → [1]
  nums = [1]                      → []

Pattern (t04 / gap-week — hashmap count)
  Count frequencies; keep keys with count == 2. Simple, O(n) extra space.
  Does **not** meet the follow-up.

Pattern (t02 — index as hash, negate in place)
  Values are in 1..n → value `v` "belongs" at index `v - 1`.
  First visit of `v`: flip `nums[v-1]` to **negative** (mark seen).
  Second visit: that slot is **already negative** → `v` is a duplicate.

  Template (in-place)
    1. res = []
    2. for x in nums:
         i = abs(x) - 1          ← index for this value (abs: may already be negated)
         if nums[i] < 0:
           res.append(abs(x))    ← seen before
         else:
           nums[i] = -nums[i]    ← mark seen
    3. return res

  Why abs?
    Later values may already have negated the cell you are reading as `x`.
    The **value** is still abs(x); the **sign** is a mark on that slot.

Your two approaches (week 8 folder — catch-up, not t08 stack)
  1) Hashmap counts — clear, extra O(n) space.
  2) Negate-by-index — O(1) extra.  ← submit this for the follow-up

Which is better?  **Approach 2** if they mention constant extra space.
  Approach 1 is fine for a first pass.

Relation to other problems
  **#287** Find the Duplicate Number — one duplicate, Floyd or negate.
  **#448** Find All Numbers Disappeared — same 1..n marking; collect positives.
  **#41** First Missing Positive — cycle / sign marking family.

Common bugs
  - Using `nums[i]` without `abs` after some slots are negative
  - Index `nums[i]` instead of `nums[i]-1` (values are 1-based)
  - Flipping sign **before** checking "already negative" → every value looks duplicate
  - Hashmap: `value == 2` vs `>= 2` — here at most twice, so == 2 is OK

Approach comparison (n = len(nums))
  | Approach              | Time | Space | Notes                          |
  |-----------------------|------|-------|--------------------------------|
  | Hashmap counts        | O(n) | O(n)  | SolutionCount                  |
  | Negate index v-1      | O(n) | O(1)* | **SolutionInPlace — submit**   |

  * Output list does not count as extra space per LC.

LeetCode: submit ONE class named Solution (in-place below).
"""

from typing import List


# --- Approach 1: Count with hashmap ---
class SolutionCount:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = 1 + nums_dict.get(num, 0)
        return [num for num, value in nums_dict.items() if value == 2]
    # Time: O(n)
    # Space: O(n)


# --- Approach 2: Mark seen by negating nums[v-1] (submit) ---
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(abs(nums[i]))
            else:
                nums[idx] = -nums[idx]
        return res
    # Time: O(n)
    # Space: O(1) extra excluding output
