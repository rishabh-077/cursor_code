"""
27. Remove Element
https://leetcode.com/problems/remove-element/

Problem
  Given an integer array nums and an integer val, remove all occurrences of val in-place.
  Return k = number of elements not equal to val.
  The first k slots of nums may hold the result in any order; values beyond k do not matter.

Examples
  nums = [3, 2, 2, 3], val = 3  →  k = 2,  nums starts with [2, 2, ...]
  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2  →  k = 5,  first five ≠ 2 (order flexible)

Pattern (t02 — Arrays / in-place)
  "Remove X in-place" → two pointers; pack elements you want to keep toward one side.

Pro tip (very important)

Whenever you see:
  "remove in-place" + "return count k"
Think:
  - Write pointer: copy non-val items to the front, return write index
  - OR swap-with-last: when you hit val, overwrite with tail and shrink length

Key difference vs 283 (Move Zeroes)
  This problem does NOT require preserving order of kept elements.
  That unlocks swap-with-last and scan-from-end — fewer moves when many vals.

Pointer meaning (write-pointer solution — submit version)
  m → next index to write a kept element; everything before m is finalized

Approach comparison (n = len(nums))
  | Approach              | Time  | Space | Keeps order? | Notes                        |
  |-----------------------|-------|-------|--------------|------------------------------|
  | New array + copy back | O(n)  | O(n)  | Yes          | Violates in-place constraint |
  | Write pointer         | O(n)  | O(1)  | Yes          | Clearest — submit as Solution|
  | Swap with last        | O(n)  | O(1)  | No           | Fewer ops when vals are common|
  | Scan from end + swap  | O(n)  | O(1)  | No           | Same idea, right-to-left     |

Common bugs
  - Returning wrong count (write index vs shrunk length vs m + 1)
  - Swap-with-last: forgetting NOT to advance m after replacing nums[m] with tail
    (the new nums[m] might still equal val and needs another check)
  - Empty array → return 0

LeetCode: submit ONE class named Solution (write-pointer version below).
"""

from typing import List


# --- Approach 1: Scan from end — swap val toward the tail region ---
class SolutionSwapFromEnd:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        m, n = last, last
        while n >= 0:
            if nums[n] == val:
                nums[m], nums[n] = nums[n], nums[m]
                m -= 1
            n -= 1
        return m + 1
    # Time: O(n)   Space: O(1)
    # Order of kept elements not preserved


# --- Approach 2: Swap with last — shrink valid length when val found at front ---
class SolutionSwapWithLast:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        m = 0
        while m < length:
            if nums[m] == val:
                nums[m] = nums[length - 1]
                length -= 1
            else:
                m += 1
        return length
    # Time: O(n)   Space: O(1)
    # Order of kept elements not preserved; re-check nums[m] after overwrite


# --- Approach 3: Write pointer — pack non-val elements left (submit this as Solution) ---
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write] = nums[i]
                write += 1
        return write
    # Time: O(n)   Space: O(1)
    # Preserves relative order of kept elements


if __name__ == "__main__":
    def run_test(nums, val, expected_k, check_prefix=None):
        nums_copy = nums.copy()
        k = Solution().removeElement(nums_copy, val)
        ok_k = k == expected_k
        ok_prefix = True
        if check_prefix is not None:
            ok_prefix = sorted(nums_copy[:k]) == sorted(check_prefix)
        ok = ok_k and ok_prefix
        print(
            f"nums={nums}, val={val} -> k={k}, prefix={nums_copy[:k]} "
            f"(expected k={expected_k}) {'OK' if ok else 'FAIL'}"
        )
        assert ok

    run_test([3, 2, 2, 3], 3, 2, [2, 2])
    run_test([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4])
    run_test([], 1, 0)
    run_test([1], 1, 0)
    run_test([1, 2, 3], 4, 3, [1, 2, 3])

    nums = [3, 2, 2, 3]
    assert SolutionSwapWithLast().removeElement(nums, 3) == 2
    assert sorted(nums[:2]) == [2, 2]

    nums = [3, 2, 2, 3]
    assert SolutionSwapFromEnd().removeElement(nums, 3) == 2
    assert sorted(nums[:2]) == [2, 2]

    print("leetcode_27: all tests passed")
