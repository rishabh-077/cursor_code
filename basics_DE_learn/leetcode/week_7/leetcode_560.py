"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Problem
  Given an integer array nums and an integer k, return the total number of
  contiguous subarrays whose sum equals k.

Examples
  nums = [1, 1, 1], k = 2 → 2      ([1,1] starting at 0 and at 1)
  nums = [1, 2, 3], k = 3 → 2      ([1,2] and [3])
  nums = [1, -1, 0], k = 0 → 3     ([1,-1], [-1,0], [1,-1,0])

Pattern (t07 — Prefix sums + hashmap)
  Running prefix: cur_sum after processing index i = sum(nums[0..i]).
  A subarray nums[j+1..i] sums to k when:
    cur_sum - prefix_at_j == k   →   prefix_at_j == cur_sum - k

  So at each step, look up how many times `cur_sum - k` has appeared as a
  previous prefix sum. Store counts in a hashmap: `{prefix_value: count}`.

  Template
    1. res = 0; cur_sum = 0; prefix_sum = {0: 1}   ← seed: empty subarray
    2. for each num:
         cur_sum += num
         diff = cur_sum - k
         res += prefix_sum.get(diff, 0)             ← count of matching j's
         prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
    3. return res

  Why seed {0: 1}?
    If cur_sum itself equals k at some point, the subarray nums[0..i] is valid.
    diff = cur_sum - k = 0 must find one hit → the seed provides it.

Your approach (week 7 — prefix + hashmap, one pass)
  Exactly the template above. cur_sum grows; diff = cur_sum - k; look up
  how many earlier prefix sums equal diff; then record cur_sum.

Why not sliding window?
  nums can have **negative numbers**. Sliding window (expand/shrink) relies
  on the sum growing when you add elements — negatives break that monotonicity.
  Prefix + hashmap handles any integers in O(n).

Relation to other problems
  **#1** Two Sum — same "complement lookup" idea: target - current → map.
  **#1480** Running Sum — builds the prefix array (here implicit in cur_sum).
  **#303** Range Sum Query — prefix for O(1) range sums (no hashmap needed).
  **#724** Find Pivot Index — prefix balance, not counting subarrays.
  **#525** Contiguous Array — same prefix + hashmap; replace 0 with -1, k = 0.
  **#974** Subarrays Divisible by K — prefix mod + hashmap.

Common bugs
  - Forgetting to seed {0: 1} → misses subarrays starting at index 0
  - Recording cur_sum in the map **before** checking diff → counts the
    current element as its own "previous prefix" (self-pairing)
  - Using sliding window on arrays with negatives → wrong answer
  - Confusing "number of subarrays" with "longest subarray" (different question)
  - Not handling duplicate prefix sums → must count, not just store existence

Approach comparison (n = len(nums))
  | Approach                       | Time  | Space | Notes                        |
  |--------------------------------|-------|-------|------------------------------|
  | Brute — all subarray sums      | O(n²) | O(1)  | nested loops                 |
  | Prefix + hashmap               | O(n)  | O(n)  | Your Solution — submit       |

LeetCode: submit ONE class named Solution.
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, cur_sum = 0, 0
        prefix_sum = {0: 1}
        for i in nums:
            cur_sum += i
            diff = cur_sum - k

            res += prefix_sum.get(diff, 0)
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
        return res
    # Time: O(n) — one pass, O(1) map ops per step
    # Space: O(n) — hashmap of prefix sums
