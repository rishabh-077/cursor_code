"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Problem
  Given an integer array nums and an integer k, return the k most frequent elements.
  You may return the answer in any order.

Examples
  nums = [1,1,1,2,2,3], k = 2  →  [1,2]
  nums = [1], k = 1             →  [1]

Pattern (t04 — Hash + bucket sort by frequency)
  1) Count frequency of each number → count map
  2) Bucket index = frequency; bucket[f] holds all nums with frequency f
  3) Scan buckets from highest freq down until you collect k elements

Your approach (week 4 — frequency buckets)
  freq[i] = list of numbers that appear exactly i times
  Max frequency ≤ len(nums) → array size len(nums) + 1
  Walk i from len(freq)-1 down to 1, append nums until res has k items

Pro tip (top K frequent / top K anything)

Whenever you see:
  "top k frequent" / "k most common"
Think:
  - Count first (hash map or Counter)
  - Then pick top k: **bucket sort** (O(n)), **min-heap size k** (O(n log k)), or sort (O(n log n))
  - Bucket sort works when frequencies are bounded by n

Relation to other problems
  **#347** Top K Frequent — bucket by frequency (your solution).
  **#49** Group Anagrams — bucket by anagram signature (different key).
  **#215** Kth Largest — heap or quickselect (value order, not frequency).

Why bucket sort beats sorting all unique elements
  nums length n → frequencies in [1, n] only → O(n) bucket array.
  Heap is O(n log k) — also great when k is small; buckets are simpler here.

Common bugs
  - Bucket size too small — need len(nums) + 1 (max freq = n when all same)
  - Off-by-one on range — scan from high index down, stop when len(res) == k
  - Using index 0 — frequency 0 unused; start from len(freq)-1 down to 1
  - Forgetting numbers can share same frequency (bucket holds a list)

Approach comparison (n = len(nums))
  | Approach                    | Time        | Space | Notes                 |
  |-----------------------------|-------------|-------|-----------------------|
  | Bucket sort by frequency    | O(n)        | O(n)  | Your solution — submit|
  | Min-heap of size k          | O(n log k)  | O(n)  | Classic interview alt |
  | Counter.most_common(k)      | O(n log n)* | O(n)  | Python one-liner      |
  | Sort unique by freq           | O(n log n)  | O(n)  | Simple, slower        |

  *most_common uses heap internally in CPython for large inputs.

LeetCode: submit ONE class named Solution (bucket sort below).
"""

import heapq
from collections import Counter
from typing import List


# --- Approach 1: Bucket sort by frequency (submit this as Solution) ---
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # freq[i] = all numbers that appear exactly i times
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
    # Time: O(n) — count + fill buckets + scan buckets
    # Space: O(n) — count map + buckets store each num once


# --- Approach 2: Min-heap of size k (frequency, number) ---
class SolutionHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Keep k largest by frequency; heap stores (freq, num), pop smallest freq
        heap = []
        for num, f in count.items():
            heapq.heappush(heap, (f, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, num in heap]
    # Time: O(n log k)   Space: O(n)


# --- Approach 3: Counter.most_common — concise (learning) ---
class SolutionCounter:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]
    # Time: O(n log n) typical   Space: O(n)


# --- Approach 4: Sort all unique by frequency descending ---
class SolutionSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_items[:k]]
    # Time: O(n log n)   Space: O(n)


if __name__ == "__main__":
    tests = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 5, 5, 6], 2, {4, 5}),
    ]
    for nums, k, expected in tests:
        for cls in (Solution, SolutionHeap, SolutionCounter, SolutionSort):
            got = set(cls().topKFrequent(nums.copy(), k))
            assert got == expected, f"{cls.__name__}: {got} != {expected}"
        print(f"nums={nums}, k={k} -> {expected} OK")
    print("leetcode_347: all tests passed")
