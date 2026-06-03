"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Problem
  Given a string s, return true if it is a palindrome after converting all uppercase
  letters to lowercase and removing all non-alphanumeric characters.
  Empty string after filtering counts as palindrome.

Examples
  "A man, a plan, a canal: Panama" → true
  "race a car" → false
  " " → true

Pattern (t03 — Strings / two pointers)
  Compare characters from both ends moving inward.
  Skip anything that is not a letter or digit (or filter once, then compare).

Your approach (filter + two pointers)
  1) lower() + build s_new with only isalnum()
  2) n from start, m from end; while n < m compare s_new[n] vs s_new[m]

Pro tip (two pointers)
  You can also skip non-alnum **in place** on s with left/right — O(1) extra space.
  For interviews, mention both; filter-then-compare is easiest to get right first.

Approach comparison (n = len(s))
  | Approach                         | Time  | Space | Notes                         |
  |----------------------------------|-------|-------|-------------------------------|
  | Filter + two pointers            | O(n)  | O(n)  | Your solution — submit below  |
  | Filter + s == s[::-1]            | O(n)  | O(n)  | Shorter; same complexity      |
  | Two pointers on original (skip)   | O(n)  | O(1)  | Best space — see SolutionO1   |

Common bug (first draft)
  Only incrementing pointers when characters **match** breaks on mismatch detection.
  On mismatch → return False immediately; on match → move both inward.

Complexity (submit version)
  Time:  O(n) — one pass to filter, one pass to compare
  Space: O(n) — s_new string

LeetCode: submit ONE class named Solution (two-pointer on filtered string).
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(s_new) - 1
        while left < right:
            if s_new[left] != s_new[right]:
                return False
            left += 1
            right -= 1
        return True
    # Time: O(n)   Space: O(n)


# --- Same logic, explicit loop to build filtered string (your original style) ---
class SolutionExplicitFilter:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = ""
        for char in s:
            if char.isalnum():
                s_new += char
        n, m = 0, len(s_new) - 1
        while n < m:
            if s_new[n] != s_new[m]:
                return False
            m -= 1
            n += 1
        return True


# --- O(1) extra space: two pointers on s, skip non-alnum ---
class SolutionTwoPointersO1:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    # Time: O(n)   Space: O(1)


# --- One-liner style (learning only) ---
class SolutionReverse:
    def isPalindrome(self, s: str) -> bool:
        s_new = "".join(ch.lower() for ch in s if ch.isalnum())
        return s_new == s_new[::-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama")
    assert not sol.isPalindrome("race a car")
    assert sol.isPalindrome(" ")
    assert not sol.isPalindrome("0P")  # "0p" — not a palindrome
    assert sol.isPalindrome("aba")
    assert SolutionTwoPointersO1().isPalindrome("A man, a plan, a canal: Panama")
    print("leetcode_125: all tests passed")
