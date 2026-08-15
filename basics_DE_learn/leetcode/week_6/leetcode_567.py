"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Problem
  Given two strings s1 and s2, return true if s2 contains a permutation of s1
  (any rearrangement of s1 as a contiguous substring of s2). Otherwise false.
  Lowercase English letters only.

Examples
  s1 = "ab",  s2 = "eidbaooo" → True   ("ba" is a permutation of "ab")
  s1 = "ab",  s2 = "eidboaoo" → False
  s1 = "adc", s2 = "dcda"     → True   ("cda" / "adc")

Pattern (t06 — Sliding window, fixed size)
  A permutation of s1 is any substring of s2 with the **same character counts**
  and length **exactly n1 = len(s1)**. That is a **fixed window of size n1**.

  Template
    1. Build count of s1 and of s2[0 : n1]     — first window
    2. if counts equal → True
    3. for i from n1 to n2-1:
         s2_counts[s2[i]]     += 1             — new char enters (right)
         s2_counts[s2[i-n1]]  -= 1             — old char leaves (left)
         if counts equal → True
    4. return False

  Same slide as #643 / #1456: enter at i, leave at **i - k** with k = n1.

Your approach (week 6 — fixed window + freq arrays, submit Solution)
  Two arrays of 26 (a–z). Fill first n1 chars of both. Then slide: +s2[i],
  -s2[i-n1]. Compare arrays after each slide.

Why freq arrays, not a set?
  Permutation cares about **counts**, not uniqueness. "aab" vs "aba" match;
  a set would lose the extra 'a'.

Pro tip (fixed vs variable window)

Whenever you see:
  "permutation of s1 inside s2" / "anagram substring" / "window size = len(s1)"
Think:
  - **Fixed-size** sliding window of length n1
  - Compare **frequency maps**, not sorted copies of every window
  - Do **not** shrink with while (that's variable, e.g. #3, #209)

Relation to other problems
  **#438** Find All Anagrams in a String — same window; collect start indices.
  **#242** Valid Anagram — one full-string count compare (no slide).
  **#643** Maximum Average — same i / i-k slide; sum instead of counts.
  **#1456** Max Vowels — same fixed k; vowel count instead of 26-letter map.
  **#3** Longest Substring Without Repeating — **variable** window.

Common bugs
  - Forgetting early `if n1 > n2: return False`
  - Leaving at `i - n1 + 1` instead of `i - n1` — wrong char exits
  - Using a set (loses duplicate letters in s1)
  - Sorting every window of s2 — O(n2 * n1 log n1) TLE
  - Comparing counts **before** updating the slide — stale window
  - Not checking the **first** window (loop starts at n1, so check once before)

Approach comparison (n2 = len(s2), n1 = len(s1))
  | Approach                              | Time              | Space | Notes                  |
  |---------------------------------------|-------------------|-------|------------------------|
  | Brute — sort each window of s2        | O(n2 · n1 log n1) | O(n1) | TLE-prone              |
  | Fixed window + 26-count arrays        | O(n1 + n2)        | O(1)  | Your Solution — submit |
  | Window + "matches" counter (26)       | O(n1 + n2)        | O(1)  | skip full array ==     |

LeetCode: submit ONE class named Solution.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            s2_counts[ord(s2[i]) - ord("a")] += 1
        if s1_counts == s2_counts:
            return True

        for i in range(n1, n2):
            s2_counts[ord(s2[i]) - ord("a")] += 1
            s2_counts[ord(s2[i - n1]) - ord("a")] -= 1
            if s1_counts == s2_counts:
                return True
        return False
    # Time: O(n1 + n2) — each char of s2 enters/leaves once; array == is O(26)
    # Space: O(1) — two arrays of 26
