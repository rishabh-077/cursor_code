"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Problem
  Given an integer array nums, return an array answer where
  answer[i] = product of all elements of nums except nums[i].
  Solve in O(n) time **without** using division.

Examples
  nums = [1, 2, 3, 4] → [24, 12, 8, 6]
    (i=0: 2*3*4, i=1: 1*3*4, i=2: 1*2*4, i=3: 1*2*3)
  nums = [-1, 1, 0, -3, 3] → [0, 0, 9, 0, 0]

Pattern (t07 — Prefix / postfix products)
  answer[i] = (product of everything left of i) * (product of everything right of i)

  Two passes, no division:
    1. Left → right: write prefix product into res[i], then multiply prefix by nums[i]
    2. Right → left: multiply res[i] by postfix, then multiply postfix by nums[i]

  Template
    res = [1] * n
    prefix = 1
    for i in 0..n-1:
      res[i] = prefix
      prefix *= nums[i]
    postfix = 1
    for i in n-1..0:
      res[i] *= postfix
      postfix *= nums[i]
    return res

Your approach (week 7 — prefix then postfix into one array)
  Exactly the template. First pass seeds left products; second multiplies
  right products in place. Output uses O(1) extra space (res doesn't count).

Why not division?
  Zeros break `total // nums[i]` (divide-by-zero / wrong zero placement).
  Even without zeros, the problem forbids division — prefix/postfix is the
  intended interview answer.

Relation to other problems
  **#1480** Running Sum — same "left accumulation" idea, but sum not product.
  **#238** is the product analogue of a two-sided prefix.
  **#42** Trapping Rain Water — left-max / right-max two-pass (same shape).

Common bugs
  - Starting prefix at nums[0] instead of 1 → wrong first cell
  - Updating prefix **before** writing res[i] → includes nums[i] in left product
  - Using division and special-casing zeros → fragile + violates constraint
  - Building separate left[] and right[] then forgetting O(1)-extra variant
  - Off-by-one on the reverse loop: range(n-1, -1, -1)

Approach comparison (n = len(nums))
  | Approach                         | Time | Space   | Notes                     |
  |----------------------------------|------|---------|---------------------------|
  | Division (total / nums[i])       | O(n) | O(1)    | Forbidden / fails on 0    |
  | left[] + right[] arrays          | O(n) | O(n)    | Clear but extra arrays    |
  | Prefix then postfix into res     | O(n) | O(1)*   | **Your Solution — submit**|

  * Output array does not count as extra space per LC.

LeetCode: submit ONE class named Solution.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    # Time: O(n) — two linear passes
    # Space: O(1) extra — only prefix/postfix scalars (res is output)
