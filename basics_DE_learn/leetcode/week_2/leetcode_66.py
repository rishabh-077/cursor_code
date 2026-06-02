"""
66. Plus One
https://leetcode.com/problems/plus-one/

Problem
  digits represents a non-negative integer (most significant digit first).
  Add 1 to the integer and return the digits of the result.

Pattern (t02 — Arrays)
  Grade-school **carry**: start at the least significant digit (right end).
  If digit is 9 → becomes 0 and carry continues; else add 1 and stop.
  If carry runs past the left end (all 9's) → new leading 1 (e.g. 999 + 1 = 1000).

Your approach
  Reverse array → LSD is at index 0 → carry loop with `start` as carry flag → reverse back.
  When i walks past the end while carry is still 1 → append 1 (handles [9,9,9] → [1,0,0,0]).

Alternative (no reverse)
  Loop i from len(digits)-1 down to 0 with carry; if carry remains, return [1] + digits.

Approach comparison (n = len(digits))
  | Approach              | Time  | Space | Notes                          |
  |-----------------------|-------|-------|--------------------------------|
  | Convert to int/str    | O(n)  | O(n)  | Easy; may overflow huge inputs |
  | Carry from right      | O(n)  | O(1)* | Preferred — *O(n) if new array |
  | Reverse + carry + rev | O(n)  | O(1)  | Same logic — submit as Solution|

Examples
  [1,2,3]   → [1,2,4]
  [4,3,2,1] → [4,3,2,2]
  [9]       → [1,0]
  [9,9,9]   → [1,0,0,0]

LeetCode: submit ONE class named Solution (reverse + carry below).
"""

from typing import List


# --- Approach 1: int() — only for learning; huge inputs can fail in some languages ---
class SolutionInt:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(map(str, digits))) + 1
        return [int(c) for c in str(n)]
    # Time: O(n)  Space: O(n)


# --- Approach 2: Carry from the right (no reverse) ---
class SolutionRightToLeft:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                break
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
        if carry:
            return [1] + digits
        return digits
    # Time: O(n)  Space: O(n) worst case when new digit array [1]+digits


# --- Approach 3: Reverse → carry → reverse (submit this as Solution) ---
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        start = 1  # carry
        i = 0
        while start:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    start = 0
            else:
                digits.append(1)
                start = 0
            i += 1
        return digits[::-1]
    # Time: O(n)
    # Space: O(1) extra if you treat in-place reverse as O(1); append may resize


if __name__ == "__main__":
    def check(inp, expected):
        out = Solution().plusOne(inp.copy())
        ok = out == expected
        print(f"{inp} -> {out} (expected {expected}) {'OK' if ok else 'FAIL'}")
        assert ok

    check([1, 2, 3], [1, 2, 4])
    check([4, 3, 2, 1], [4, 3, 2, 2])
    check([9], [1, 0])
    check([9, 9, 9], [1, 0, 0, 0])
    check([0], [1])
    print("leetcode_66: all tests passed")
