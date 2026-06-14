"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Problem
  Given a string s, return the longest palindromic substring in s.

Examples
  "babad" → "bab" or "aba"
  "cbbd" → "bb"
  "a" → "a"

Pattern (t03 — Strings / expand around center)
  Every palindrome has a **center** (one char for odd length, between two
  chars for even). Try each center and expand outward while characters match.

Your approach (expand around center)
  For each index i:
    - Odd:  l = r = i, expand while s[l] == s[r]
    - Even: l = i, r = i + 1, expand while s[l] == s[r]
  Track longest substring seen (res, resLen).

Pro tip (palindrome substring)

Whenever you see:
  "longest palindromic substring"
Think:
  - Expand around center — O(n²) time, O(1) space (interview sweet spot)
  - Not the same as **#125** (is whole string a palindrome?) — here you search all centers
  - Must handle **both** odd and even length palindromes

Relation to other problems
  **#125** Valid Palindrome — two pointers inward on full string.
  **#5** — run that idea from every possible center and keep the max.

Common bugs
  - Only expanding odd centers (miss "bb", "cbbd")
  - Wrong slice: longest is s[l:r+1] after expansion stops (your code updates inside the loop — correct)
  - Using `>=` vs `>` for length — either works; `>` keeps first max of same length

Approach comparison (n = len(s))
  | Approach              | Time   | Space | Notes                       |
  |-----------------------|--------|-------|-----------------------------|
  | Expand around center  | O(n²)  | O(1)  | Preferred — submit Solution |
  | Brute force substrings| O(n³)  | O(1)  | TLE on LeetCode             |
  | DP                    | O(n²)  | O(n²) | dp[i][j] = palindrome?      |
  | Manacher's algorithm  | O(n)   | O(n)  | Mention if asked; rare      |

LeetCode: submit ONE class named Solution (expand around center below).
"""


# --- Approach 1: Expand around center — odd + even (submit this as Solution) ---
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length — center at i
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length — center between i and i+1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
    # Time: O(n²) — n centers, each expands up to n/2
    # Space: O(1) — only pointers and result string


# --- Approach 2: Helper to DRY odd/even expand (same logic, cleaner) ---
class SolutionHelper:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        best = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            best = max(best, odd, even, key=len)
        return best
    # Time: O(n²)   Space: O(1)


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("babad") in ("bab", "aba")
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("ac") in ("a", "c")
    assert sol.longestPalindrome("bb") == "bb"

    assert SolutionHelper().longestPalindrome("cbbd") == "bb"
    print("leetcode_5: all tests passed")
