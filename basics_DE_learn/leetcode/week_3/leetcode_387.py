"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Problem
  Given a string s, find the first non-repeating character in it and return its
  index. If it does not exist, return -1.

Examples
  "leetcode" → 0   ('l')
  "loveleetcode" → 2   ('v')
  "aabb" → -1

Pattern (t03 — Strings / frequency map)
  Count each character, then scan the string left → right for the first char
  with count == 1.

Pro tip (frequency counting)

Whenever you see:
  "first unique" / "only appears once" / "character frequency"
Think:
  - Pass 1: build char → count map
  - Pass 2: walk s in order; return index of first char where count == 1

Two-pass is clearer than trying to find the answer in one pass.

Relation to other problems
  Same counting idea as **#242** Valid Anagram (compare two frequency maps).
  **#217** Contains Duplicate is the simpler "any repeat?" version.

Why scan s in order (not dict keys)
  Your first draft iterated `for c in dictS` then nested `enumerate(s)` to find
  the index. In Python 3.7+ dict keys follow insertion order, so it can work —
  but the inner loop is redundant (use `s.index(c)` or just scan s once).
  **Always scan s left → right in pass 2** — correct in any language.

Common bugs
  - Returning the first key in the dict instead of first char in **string order**
  - Forgetting to return -1 when no unique char exists
  - Off-by-one: return **index** (0-based), not count

Approach comparison (n = len(s), k = alphabet size)
  | Approach                    | Time  | Space   | Notes                        |
  |-----------------------------|-------|---------|------------------------------|
  | Count + scan s in order     | O(n)  | O(1)*   | Preferred — submit Solution  |
  | Count + iterate dict keys   | O(n)  | O(1)*   | Works in Py 3.7+; less clear  |
  | Counter + scan              | O(n)  | O(1)*   | Same logic, shorter syntax   |

  *O(1) space if alphabet is bounded (26 lowercase letters); else O(k) unique chars.

LeetCode: submit ONE class named Solution (two-pass count + scan below).
"""

from collections import defaultdict


# --- Approach 1: Count with dict.get — then dict keys + nested scan (first draft) ---
class SolutionCountThenDictKeys:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
        for c in counts:
            if counts[c] == 1:
                for i, val in enumerate(s):
                    if val == c:
                        return i
        return -1
    # Time: O(n) — nested loop bounded by small alphabet
    # Space: O(1) — at most 26 keys for lowercase a-z


# --- Approach 2: defaultdict — same dict-key walk (learning only) ---
class SolutionDefaultDictKeys:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        for ch in s:
            counts[ch] += 1
        for c in counts:
            if counts[c] == 1:
                for i, val in enumerate(s):
                    if val == c:
                        return i
        return -1
    # Time: O(n)   Space: O(1) for bounded alphabet


# --- Approach 3: Count then scan s in order (submit this as Solution) ---
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        for ch in s:
            counts[ch] += 1
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1
    # Time: O(n) — two linear passes
    # Space: O(1) — bounded alphabet (26 lowercase)


if __name__ == "__main__":
    sol = Solution()
    assert sol.firstUniqChar("leetcode") == 0
    assert sol.firstUniqChar("loveleetcode") == 2
    assert sol.firstUniqChar("aabb") == -1
    assert sol.firstUniqChar("z") == 0
    assert sol.firstUniqChar("aabc") == 2

    assert SolutionCountThenDictKeys().firstUniqChar("loveleetcode") == 2
    assert SolutionDefaultDictKeys().firstUniqChar("leetcode") == 0
    print("leetcode_387: all tests passed")
