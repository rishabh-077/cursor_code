"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Problem
  Write a function to find the longest common prefix string amongst an array of
  strings. If there is no common prefix, return "".

Examples
  ["flower","flow","flight"] → "fl"
  ["dog","racecar","car"] → ""
  ["a"] → "a"

Pattern (t03 — Strings / vertical scan)
  Compare all strings **column by column** (index 0, then 1, …) until a
  mismatch or the shortest string ends.

Your approach (vertical scanning)
  1) Find min string length (prefix cannot be longer than shortest string)
  2) For each index i, check every s[i] == strs[0][i]
  3) On mismatch → return prefix built so far
  4) Else append strs[0][i] to prefix

Pro tip (common prefix)

Whenever you see:
  "common prefix" / "shared start" across many strings
Think:
  - Vertical: same index across all strings (your solution)
  - Horizontal: fold prefix — compare strs[0] vs strs[1], then result vs strs[2]
  - Sort + compare first vs last (longest common prefix ⊆ sorted min/max)

Edge cases
  - One string → return that string
  - Any empty string in array → min_len = 0 → return ""
  - No shared first char → return "" immediately at i = 0

Common bugs
  - Not capping scan at **shortest** string length → index out of range
  - Returning on first string only — must check **all** strings at each i
  - Using `==` on full strings in a loop without early exit (slower, still correct)

Approach comparison (n = len(strs), m = avg string length)
  | Approach           | Time        | Space | Notes                         |
  |--------------------|-------------|-------|-------------------------------|
  | Vertical scan      | O(n × m)    | O(1)  | Preferred — submit Solution   |
  | Horizontal fold    | O(n × m)    | O(m)  | prefix = strs[0]; merge each  |
  | Sort first & last  | O(n log n + m) | O(1) | Trick: LCP ⊆ sort min & max |

LeetCode: submit ONE class named Solution (vertical scan below).
"""

from typing import List


# --- Approach 1: Vertical scanning — compare index i across all strings (submit) ---
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_len = float("inf")
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)

        i = 0
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
            i += 1
        return prefix
    # Time: O(n × m) — n strings, up to m columns checked
    # Space: O(1) — only pointers and result built in place


# --- Approach 2: Horizontal scanning — fold prefix string by string ---
class SolutionHorizontal:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    # Time: O(n × m)   Space: O(m) for prefix slice copies in worst case


# --- Approach 3: Sort — LCP is prefix of first and last after sort ---
class SolutionSort:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
    # Time: O(n log n + m)   Space: O(1) extra if sort in place


if __name__ == "__main__":
    def check(strs, expected):
        got = Solution().longestCommonPrefix(strs)
        ok = got == expected
        print(f"{strs} -> {got!r} (expected {expected!r}) {'OK' if ok else 'FAIL'}")
        assert ok

    check(["flower", "flow", "flight"], "fl")
    check(["dog", "racecar", "car"], "")
    check(["a"], "a")
    check(["ab", "a"], "a")
    check([""], "")

    assert SolutionHorizontal().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert SolutionSort().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    print("leetcode_14: all tests passed")
