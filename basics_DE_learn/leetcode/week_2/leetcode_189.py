"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/

Problem
  Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
  Modify nums in-place — do not return anything.

Examples
  [1, 2, 3, 4, 5, 6, 7], k=3 → [5, 6, 7, 1, 2, 3, 4]
  [-1, -100, 3, 99], k=2 → [3, 99, -1, -100]

Pattern (t02 — Arrays / in-place)
  "Rotate right by k" → normalize k with k % n, then either:
  - map each index to (i + k) % n (extra buffer), or
  - triple reverse (no extra array).

Pro tip (very important)

Whenever you see:
  "rotate array in-place"
Think:
  - k = k % n first (k >= n means full cycles — no change)
  - Triple reverse: reverse all → reverse first k → reverse rest
  - Or index formula: new_index = (i + k) % n

Why triple reverse works
  Rotating right by k moves the last k elements to the front.
  Reversing the whole array puts those k elements at the front (but reversed).
  Reversing the first k and the remaining n-k segments restores correct order.

Index formula (extra-array approach)
  Element at index i ends up at (i + k) % n after a right rotation.

Common bugs
  - Forgetting k = k % n → wrong index when k > n
  - k == 0 or n == 1 → should return early (optional; triple reverse still works)
  - Off-by-one on reverse ranges (first segment is indices 0..k-1, second is k..n-1)

Approach comparison (n = len(nums))
  | Approach           | Time  | Space | Notes                              |
  |--------------------|-------|-------|------------------------------------|
  | Extra array        | O(n)  | O(n)  | Easiest to reason about            |
  | Triple reverse     | O(n)  | O(1)  | Preferred for interviews — submit  |
  | Cyclic replacement | O(n)  | O(1)  | GCD-based; trickier to implement   |

LeetCode: submit ONE class named Solution (triple reverse below).
"""

from typing import List

class SolutionWithoutHint:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        temp = nums[n-k:]
        for i in range(n-k-1, -1, -1) :
            nums[n-1] = nums[i]
            n -= 1
        for i in range(k):
            nums[i] = temp[i]
    # Time: O(n)   Space: O(n)


# --- Approach 1: Extra array — index mapping (i + k) % n ---
class SolutionExtraArray:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        new_arr = [0] * n
        for i in range(n):
            new_index = (i + k) % n
            new_arr[new_index] = nums[i]
        nums[:] = new_arr
    # Time: O(n)   Space: O(n)


# --- Approach 2: Triple reverse — O(1) extra space (submit this as Solution) ---

class SolutionTripleReverse:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        m, n = 0, l - 1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
        m, n = 0, k - 1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
        m, n = k, l - 1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
        

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)       # whole array reversed
        reverse(0, k - 1)       # first k elements back in order
        reverse(k, n - 1)       # remaining n-k elements back in order
    # Time: O(n)   Space: O(1)


if __name__ == "__main__":
    def run_test(nums, k, expected):
        nums_copy = nums.copy()
        Solution().rotate(nums_copy, k)
        ok = nums_copy == expected
        print(f"nums={nums}, k={k} -> {nums_copy} (expected {expected}) {'OK' if ok else 'FAIL'}")

    run_test([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
    run_test([-1, -100, 3, 99], 2, [3, 99, -1, -100])
    run_test([1, 2, 3], 4, [3, 1, 2])   # k % n == 1
    run_test([1, 2, 3], 3, [1, 2, 3])   # k % n == 0 — no change
    run_test([1], 0, [1])
    nums = [1, 2, 3, 4, 5]
    SolutionExtraArray().rotate(nums, 2)
    assert nums == [4, 5, 1, 2, 3]
    print("leetcode_189: all tests passed")
