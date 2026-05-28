"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Problem
  nums1 has length m + n; first m values are sorted, last n slots are empty (0).
  nums2 has length n, all sorted.
  Merge nums2 into nums1 in-place so nums1 is one sorted array (length m + n).
  Do not return anything — modify nums1 only.

Pro tip (very important)

Whenever you see:
  "modify in-place"
Think:
  - Two pointers
  - Swapping
  - No extra array

This problem is the classic example: merge from the end with two pointers, O(1) extra space.

Pattern (in-place + sorted inputs)
  → Two pointers, often from the END (avoids overwriting nums1 you haven't merged yet)

Why merge from the back?
  If you merge from the front, placing a small nums2 value can overwrite a nums1
  value you still need. Writing from index m+n-1 downward uses empty buffer slots first.

Pointer meaning (two-pointer solution)
  m → count of unmerged elements left in nums1 (index m-1 is the rightmost)
  n → count of unmerged elements left in nums2 (index n-1 is the rightmost)
  last → next position to fill from the right

Approach comparison (m = valid in nums1, n = len(nums2))
  | Approach        | Time           | Space | Notes                        |
  |-----------------|----------------|-------|------------------------------|
  | Sort combined   | O((m+n) log(m+n)) | O(m+n) | Easy; extra list from slice |
  | Two pointers end| O(m + n)       | O(1)  | Preferred for interviews     |

LeetCode: submit ONE class named Solution (two-pointer version below).
"""

from typing import List


# --- Approach 1: Concatenate + sort — simple, not optimal ---
class SolutionSort:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1[:m] = real data; tail m..m+n-1 is padding
        # Creates a new list (extra space), then copies back into nums1
        nums1[:] = sorted(nums1[:m] + nums2)
    # Time: O((m + n) log(m + n))
    # Space: O(m + n) for the temporary combined list


# --- Approach 2: Two pointers from the end (submit this as Solution) ---
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1  # rightmost index of merged result

        # While both arrays have unmerged elements, place the larger at `last`
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                # nums2[n-1] is larger OR equal — take from nums2 (stable tie-break)
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # If nums2 still has values (nums1 exhausted first), copy them
        # If nums1 still has values, they are already in the correct positions — no copy needed
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
    # Time: O(m + n) — each element moved at most once
    # Space: O(1) — only pointers m, n, last


if __name__ == "__main__":
    def run_test(nums1, m, nums2, n, expected):
        nums1_copy = nums1.copy()
        Solution().merge(nums1_copy, m, nums2, n)
        ok = nums1_copy == expected
        print(f"nums1={nums1}, m={m}, nums2={nums2} -> {nums1_copy} (expected {expected}) {'OK' if ok else 'FAIL'}")

    run_test([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    run_test([1], 1, [], 0, [1])
    run_test([0], 0, [1], 1, [1])
    run_test([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6])
