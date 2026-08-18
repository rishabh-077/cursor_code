"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Problem
  Given strings s and p, return the start indices of all anagrams of p in s.
  An anagram of p is a contiguous substring of s with the same letter counts.
  Order of indices does not matter. Lowercase English letters only.

Examples
  s = "cbaebabacd", p = "abc" → [0, 6]
    "cba" at 0, "bac" at 6
  s = "abab", p = "ab" → [0, 1, 2]
    "ab", "ba", "ab"

Pattern (t06 — Sliding window, fixed size)
  Same as **#567 Permutation in String**, but collect **every** start index
  instead of returning True on the first match.

  Window length is **exactly n2 = len(p)**. Enter at i, leave at **i - n2**.

  Template
    1. Count p and s[0 : n2]               — first window
    2. if counts equal → append start 0
    3. for i from n2 to n1-1:
         count_s[s[i]]     += 1            — new char enters
         count_s[s[i-n2]]  -= 1            — old char leaves
         if counts equal → append i - n2 + 1
    4. return res

  Start index of the current window: **i - n2 + 1**  (same as r - l + 1 with
  l = i - n2 + 1, r = i). After the first loop, i is n2-1 so i - n2 + 1 == 0.

Your two approaches (week 6)
  1) Two arrays of 26  — count[ord(c)-ord('a')]
  2) Two dicts         — count[c] = count.get(c, 0) + 1; pop keys that hit 0

Which is better, and why?  →  **26-count arrays (submit this)**

  LeetCode #438/#567 guarantee **only a–z**. Then:

  | | 26-array | dict |
  |-|----------|------|
  | Compare `==` | always O(26), 0-slots already lined up | must **pop** keys at 0 or leftover 0s make dicts unequal |
  | Indexing | `arr[ord(c)-'a']` — no hash | hash + `.get` / `.pop` every step |
  | Extra charset | would break (need bigger table) | works for any characters |
  | Space | O(1) true (52 ints) | O(min(n2, Σ)) — more overhead in CPython |

  Arrays win here: fewer moving parts, no pop-zero bug, slightly faster.
  Use **dicts** when the alphabet is large / unknown (Unicode, not interview #438).

  Optional interview upgrade: track `matches` (how many of 26 letters agree)
  so you don't compare full arrays each slide — still O(n), same idea.

Pro tip (anagram window)

Whenever you see:
  "all start indices of anagrams" / "permutations of p in s"
Think:
  - **Fixed window** of len(p) + frequency compare
  - #567 = exists? (bool) · #438 = where? (list of starts)
  - Do **not** sort every window

Relation to other problems
  **#567** Permutation in String — same slide; return bool not indices.
  **#242** Valid Anagram — one pair, no window.
  **#49** Group Anagrams — bucket by count-tuple (hash key), not a slide.
  **#643 / #1456** — same i / i-k slide; metric is sum / vowels, not 26 counts.

Common bugs
  - Forgetting first-window check (loop starts at n2)
  - Using `i - n2` as the start index — off by one; start is `i - n2 + 1`
  - Leave index `i - n2 + 1` instead of `i - n2`
  - Dict path: decrement without **pop** when count hits 0 → `==` fails
  - `if n2 > n1: return []` missing
  - Two classes named `Solution` in one file — LeetCode only submits the last one

Approach comparison (n = len(s), k = len(p))
  | Approach                         | Time     | Space | Notes                         |
  |----------------------------------|----------|-------|-------------------------------|
  | Brute — sort each window         | O(n k log k) | O(k) | TLE                           |
  | Fixed window + **26 arrays**     | O(n)     | O(1)  | **Better for this problem**   |
  | Fixed window + **dicts**         | O(n)     | O(Σ)  | More general; pop zeros       |

LeetCode: submit ONE class named Solution (arrays below).
"""

from typing import List


# --- Approach 1: Fixed window + 26-count arrays (submit as Solution) ---
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s)
        n2 = len(p)
        res = []
        if n2 > n1:
            return res
        count_s = [0] * 26
        count_p = [0] * 26

        for i in range(n2):
            count_p[ord(p[i]) - ord("a")] += 1
            count_s[ord(s[i]) - ord("a")] += 1
        if count_s == count_p:
            res.append(0)

        for i in range(n2, n1):
            count_s[ord(s[i]) - ord("a")] += 1
            count_s[ord(s[i - n2]) - ord("a")] -= 1
            if count_s == count_p:
                res.append(i - n2 + 1)
        return res
    # Time: O(n) — each char of s enters/leaves once; == is O(26)
    # Space: O(1) — two arrays of 26


# --- Approach 2: Fixed window + dicts (same idea; more general alphabet) ---
class SolutionDict:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1, n2 = len(s), len(p)
        res = []
        if n2 > n1:
            return res
        count_s, count_p = {}, {}

        for i in range(n2):
            count_p[p[i]] = 1 + count_p.get(p[i], 0)
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
        if count_s == count_p:
            res.append(i - n2 + 1)

        for i in range(n2, n1):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_s[s[i - n2]] -= 1
            if count_s[s[i - n2]] == 0:
                count_s.pop(s[i - n2])
            if count_s == count_p:
                res.append(i - n2 + 1)
        return res
    # Time: O(n) — hash ops per slide
    # Space: O(min(k, alphabet))
    # Must pop keys at 0 or dict == the pattern map fails
