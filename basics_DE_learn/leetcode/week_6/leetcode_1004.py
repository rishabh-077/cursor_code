"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Problem
  Given a binary array nums and an integer k, return the maximum number of
  consecutive 1s you can get if you can flip **at most k** 0s to 1s.

Examples
  nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 → 6
    flip the two 0s before the last streak → [1,1,1,0,0,1,1,1,1,1,1]
  nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3 → 10

Pattern (t06 — Sliding window, variable size)
  Valid window = contains **at most k zeros**. Expand r. When zeros exceed k,
  shrink from the left until the window is valid again. Track max length.

  This is #485 (max consecutive 1s) with a budget of k flips.

  Template (preferred)
    1. l = 0; zeros = 0; max_len = 0
    2. for r in range(len(nums)):
         if nums[r] == 0: zeros += 1          — expand
         while zeros > k:                     — invalid: too many flips
             if nums[l] == 0: zeros -= 1
             l += 1
         max_len = max(max_len, r - l + 1)    — window now valid
    3. return max_len

  Length is **r - l + 1** (both ends inclusive) — do not maintain a separate
  cur_len unless you want extra bugs.

Your two approaches (week 6)
  1) Manual cur_len + while/else to skip 1s then drop one 0
  2) Standard expand/shrink; length = r - l + 1  ← submit this

Which is better, and why?  →  **Approach 2 (submit as Solution)**

  Approach 2: after the while, [l, r] is always a valid "at most k zeros"
  window. Length falls out of the two pointers. One code path.

  Approach 1: you increment/decrement cur_len yourself, then a `while nums[l]
  == 1` / `else` to find the 0 to drop. Python `while…else` runs the else
  when the loop condition becomes false (no `break`) — easy to misread.
  Dropping the 0 does not decrement cur_len, so length and l can drift.
  Same O(n), more moving parts.

  Same family as #3 (shrink while invalid). Opposite of #209 (shrink while valid).

Pro tip (fixed vs variable window)

Whenever you see:
  "longest ones if you may flip at most k zeros" / "at most k replacements"
Think:
  - **Variable** window — shrink **while** zeros > k
  - Not fixed k length (that's #643 / #1456)
  - k = 0 reduces to #485 (no flips)

Relation to other problems
  **#485** Max Consecutive Ones — this problem with k = 0.
  **#3** Longest Substring Without Repeating — same "shrink while invalid".
  **#209** Min Size Subarray Sum — shrink while **valid** (minimize length).
  **#424** Longest Repeating Character Replacement — same "at most k changes".
  **#1456 / #643** — **fixed** window of length k; different question.

Common bugs
  - Using `if zeros > k` instead of `while` — one shrink may not be enough
  - Updating max_len **before** shrinking — counts a window with > k zeros
  - Length as `r - l` instead of `r - l + 1`
  - Forgetting to decrement zeros when nums[l] == 0 (only moving l)
  - Approach 1: `while/else` drop of a 0 without fixing cur_len
  - Two classes named Solution — LeetCode submits the last one only

Approach comparison (n = len(nums))
  | Approach                              | Time | Space | Notes                        |
  |---------------------------------------|------|-------|------------------------------|
  | Brute — try every subarray            | O(n²)| O(1)  | count zeros per range        |
  | Variable window (r - l + 1)           | O(n) | O(1)  | **Submit** — Solution below  |
  | Variable window + manual cur_len      | O(n) | O(1)  | SolutionManualLen — avoid    |

LeetCode: submit ONE class named Solution (clean window below).
"""

from typing import List


# --- Approach 1: manual cur_len + while/else (works, harder to reason) ---
class SolutionManualLen:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, count_0, cur_len, max_len = 0, 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 1:
                cur_len += 1
                max_len = max(max_len, cur_len)
            if nums[r] == 0:
                count_0 += 1
                if count_0 <= k:
                    cur_len += 1
                    max_len = max(max_len, cur_len)
                else:
                    while nums[l] == 1:
                        cur_len -= 1
                        l += 1
                    else:
                        count_0 -= 1
                        l += 1
        return max_len
    # Time: O(n)
    # Space: O(1)


# --- Approach 2: variable window — shrink while zeros > k (submit) ---
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, count_0, max_len = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count_0 += 1

            while count_0 > k:
                if nums[l] == 0:
                    count_0 -= 1
                l += 1

            w = r - l + 1
            max_len = max(max_len, w)
        return max_len
    # Time: O(n) — each index enters/leaves at most once
    # Space: O(1)
