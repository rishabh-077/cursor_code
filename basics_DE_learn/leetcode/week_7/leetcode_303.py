"""
303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/

Problem
  Design a class NumArray that:
    - Takes an integer array nums in the constructor.
    - sumRange(left, right) returns the sum of nums[left..right] (inclusive).
  sumRange is called many times — must be efficient.

Examples
  nums = [-2, 0, 3, -5, 2, -1]
  sumRange(0, 2) → 1    (-2 + 0 + 3)
  sumRange(2, 5) → -1   (3 + -5 + 2 + -1)
  sumRange(0, 5) → -3

Pattern (t07 — Prefix sums, range query)
  Build prefix array once in the constructor (O(n)).
  Answer each query in O(1):
    sumRange(l, r) = prefix[r] - prefix[l-1]
  Edge: when l == 0 there is no prefix[l-1], so treat it as 0.

  This is **the** canonical prefix sum use-case: precompute once,
  query many times.

  Your prefix stores:
    prefix[i] = nums[0] + nums[1] + ... + nums[i]

  So:
    sumRange(l, r) = prefix[r]                     if l == 0
                   = prefix[r] - prefix[l - 1]     otherwise

Your approach (week 7 — class with prefix build + O(1) query)
  Constructor: running cur → append to self.prefix.
  sumRange: rightSum = prefix[r], leftSum = prefix[l-1] if l > 0 else 0.

Why store prefix in the constructor?
  Calling `sum(nums[l:r+1])` each time is O(r-l+1) per query. With many
  queries that is O(q * n). Prefix makes each query O(1) → total O(n + q).

Relation to other problems
  **#1480** Running Sum — literally builds this prefix array.
  **#724** Find Pivot Index — left/right sums from prefix.
  **#560** Subarray Sum Equals K — prefix + hashmap to count subarrays.
  **#304** Range Sum Query 2D — same idea on a matrix (follow-up).

Common bugs
  - Off-by-one: `prefix[l-1]` when l == 0 → index -1 wraps to last element
  - Building prefix of size n+1 with prefix[0]=0 avoids the l==0 edge
    (your approach handles it with an `if` — both are fine)
  - Confusing inclusive [l, r] with exclusive [l, r) — LC uses inclusive
  - Using sum() in sumRange — defeats the purpose of precomputation

Approach comparison
  | Approach                     | Constructor | sumRange | Space |
  |------------------------------|-------------|----------|-------|
  | Brute force (sum each call)  | O(1)        | O(n)     | O(1)  |
  | Prefix array (precompute)    | O(n)        | **O(1)** | O(n)  |

LeetCode: submit the NumArray class.
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)
        # O(n) build

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum
        # O(1) per query
