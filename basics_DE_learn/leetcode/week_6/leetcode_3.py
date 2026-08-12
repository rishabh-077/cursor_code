"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem
  Given a string s, find the length of the longest substring without repeating
  characters.

Examples
  s = "abcabcbb" → 3  ("abc")
  s = "bbbbb"    → 1  ("b")
  s = "pwwkew"   → 3  ("wke")

Pattern (t06 — Sliding window, variable size)
  Window grows with r. When a duplicate appears, shrink from the left until the
  window is valid again (no repeats). Track max length of any valid window.

  Template
    1. charSet = set(); l = 0; max_len = 0
    2. for r in range(len(s)):
         while s[r] in charSet:          — invalid: duplicate entered
             charSet.remove(s[l])        — shrink from left
             l += 1
         charSet.add(s[r])               — expand: include s[r]
         max_len = max(max_len, r - l + 1)
    3. return max_len

  Why a set?
    O(1) membership check for "is s[r] already in the current window?"
    The set mirrors the characters currently in s[l : r+1].

Your approach (week 6 — variable sliding window)
  Expand r one char at a time. While s[r] is already in the set, remove s[l]
  and advance l. Then add s[r] and update max_len.

Pro tip (fixed vs variable window)

Whenever you see:
  "longest / shortest substring with property X" / "at most / without"
Think:
  - **Variable-size** sliding window — expand with for-r, shrink with while
  - Do **not** use fixed k add/drop (that's fixed window, e.g. #643, #1456)

Relation to other problems
  **#209** Minimum Size Subarray Sum — same variable template; shrink while sum >= target.
  **#643** Maximum Average Subarray I — **fixed** window of length k.
  **#1456** Maximum Number of Vowels — fixed window; count vowels instead of sum.
  Hashmap variant: store last index of each char and jump l — same idea, O(n).

Common bugs
  - Updating max_len before shrinking — may count a window that still has a duplicate
  - Using `if` instead of `while` to shrink — one remove may not clear the duplicate
  - Forgetting to add s[r] after the while — window set goes out of sync
  - Returning r - l instead of r - l + 1 — off-by-one on length
  - Empty string: loop never runs → max_len stays 0 (correct)

Approach comparison (n = len(s))
  | Approach                              | Time  | Space | Notes                  |
  |---------------------------------------|-------|-------|------------------------|
  | Brute — check all substrings          | O(n²) | O(n)  | nested loops + set     |
  | Variable sliding window (set)         | O(n)  | O(min(n, Σ)) | Your Solution — submit |

LeetCode: submit ONE class named Solution.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        max_len = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len
    # Time: O(n) — each char added/removed from set at most once
    # Space: O(min(n, charset size))
