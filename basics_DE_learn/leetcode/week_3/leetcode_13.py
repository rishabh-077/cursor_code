"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Problem
  Given a roman numeral string s, convert it to an integer.
  Roman numerals: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
  Six subtractive pairs: IV(4), IX(9), XL(40), XC(90), CD(400), CM(900).

Examples
  "III" → 3
  "LVIII" → 58   (50 + 5 + 3)
  "MCMXCIV" → 1994

Pattern (t03 — Strings / left-to-right scan)
  Map symbol → value; walk the string once.
  If a smaller numeral comes **before** a larger one → subtractive pair
  (add big − small, skip both). Otherwise add the current symbol.

Your approach (hash map + subtractive check)
  - rome = char → value
  - If s[a] < s[a+1] → res += rome[s[a+1]] - rome[s[a]]; a += 2
  - Else → res += rome[s[a]]; a += 1

Pro tip (Roman numerals)

Whenever you see:
  "Roman to int" / paired symbols where order matters
Think:
  - Left-to-right: if curr < next → subtract pair, advance 2
  - Right-to-left: if curr < prev → subtract curr else add curr
  - Only **6** legal subtract pairs (don't over-generalize)

Subtractive pairs (memorize or derive)
  I before V,X → 4, 9
  X before L,C → 40, 90
  C before D,M → 400, 900

Common bugs
  - Always adding every symbol (misses IV = 4 not 1+5=6)
  - Not checking `a < n - 1` before peeking s[a+1] → index error
  - Wrong skip: subtract case must advance **2**, not 1

Approach comparison (n = len(s))
  | Approach              | Time  | Space | Notes                        |
  |-----------------------|-------|-------|------------------------------|
  | Left-to-right (yours) | O(n)  | O(1)  | Preferred — submit Solution  |
  | Right-to-left         | O(n)  | O(1)  | Compare curr vs previous     |
  | Hardcoded pairs dict  | O(n)  | O(1)  | Replace 2-char tokens first  |

LeetCode: submit ONE class named Solution (left-to-right below).
"""


# --- Approach 1: Left-to-right — smaller before larger = subtract (submit) ---
class Solution:
    def romanToInt(self, s: str) -> int:
        rome = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        n = len(s)
        a = 0
        while a < n:
            if a < n - 1 and rome[s[a]] < rome[s[a + 1]]:
                res += rome[s[a + 1]] - rome[s[a]]
                a += 2
            else:
                res += rome[s[a]]
                a += 1
        return res
    # Time: O(n)   Space: O(1)


# --- Approach 2: Right-to-left — if curr < prev, subtract ---
class SolutionRightToLeft:
    def romanToInt(self, s: str) -> int:
        rome = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        prev = 0
        for ch in reversed(s):
            curr = rome[ch]
            if curr < prev:
                res -= curr
            else:
                res += curr
            prev = curr
        return res
    # Time: O(n)   Space: O(1)


if __name__ == "__main__":
    sol = Solution()
    assert sol.romanToInt("III") == 3
    assert sol.romanToInt("LVIII") == 58
    assert sol.romanToInt("MCMXCIV") == 1994
    assert sol.romanToInt("IV") == 4
    assert sol.romanToInt("IX") == 9
    assert sol.romanToInt("XL") == 40
    assert sol.romanToInt("XC") == 90
    assert sol.romanToInt("CD") == 400
    assert sol.romanToInt("CM") == 900

    assert SolutionRightToLeft().romanToInt("MCMXCIV") == 1994
    print("leetcode_13: all tests passed")
