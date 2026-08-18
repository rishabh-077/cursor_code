"""
66. Plus One
https://leetcode.com/problems/plus-one/

Problem
  digits represents a non-negative integer (most significant digit first).
  Add 1 to the integer and return the digits of the result.

Pattern (t02 — Arrays)
  Grade-school **carry**: start at the least significant digit (right end).
  If digit is 9 → becomes 0 and carry continues left; else add 1 and stop.
  If carry runs past the left end (all 9's) → new leading 1 (e.g. 999 + 1 = 1000).

Your approach (week 3 — carry from the right, no reverse)
  Loop i from len(digits)-1 down to 0:
    - 9 → set to 0, keep going (carry)
    - else → add 1, return immediately (no more carry)
  If every digit was 9 (i ends at -1) → prepend 1: [1] + digits or digits.insert(0, 1)

Pro tip (digit array + carry)

Whenever you see:
  "add to number stored as digit array" / "plus one" / "carry propagation"
Think:
  - Process from **right** (LSD) — that's where +1 starts
  - 9 is the only digit that triggers carry to the next position
  - All 9's → new array one digit longer ([9,9,9] → [1,0,0,0])

Relation to other problems
  Same right-to-left scan as **#189** Rotate Array (index math from the end).
  Week 2 version used reverse → carry → reverse — same logic, more steps.

Common bugs
  - Looping left-to-right (MSD first) — carry goes the wrong direction
  - Forgetting all-9s case → [9,9,9] becomes [0,0,0] without leading 1
  - Returning before handling carry overflow when i reaches -1
  - Using int("".join(...)) — fine for learning; huge inputs can overflow in some langs

Approach comparison (n = len(digits))
  | Approach              | Time  | Space | Notes                          |
  |-----------------------|-------|-------|--------------------------------|
  | int() / str()         | O(n)  | O(n)  | Easy; overflow risk on huge n  |
  | Carry from right      | O(n)  | O(1)* | Preferred — submit Solution    |
  | Reverse + carry + rev | O(n)  | O(1)  | Week 2 style — see week_2 file |

  *O(n) worst-case space when returning [1] + digits (new list for leading 1).

Examples
  [1,2,3]   → [1,2,4]
  [4,3,2,1] → [4,3,2,2]
  [9]       → [1,0]
  [9,9,9]   → [1,0,0,0]
  [0]       → [1]

LeetCode: submit ONE class named Solution (carry from right below).
"""

from typing import List


# --- Approach 1: int() — learning only; may fail on very large inputs ---
class SolutionInt:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(map(str, digits))) + 1
        return [int(c) for c in str(n)]
    # Time: O(n)   Space: O(n)


# --- Approach 2: Carry from right — early return (submit this as Solution) ---
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits

        # All 9's: carry created a new most significant digit
        return [1] + digits
    # Time: O(n) — worst case scan all digits (all 9's)
    # Space: O(n) worst case when [1] + digits allocates new list


# --- Approach 3: Same loop — insert leading 1 in-place instead of [1] + digits ---
class SolutionInsert:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits

        digits.insert(0, 1)
        return digits
    # Time: O(n)   Space: O(n) — insert(0, 1) may shift entire list


# --- Approach 4: Explicit carry flag (same logic, different style) ---
class SolutionCarryFlag:
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
    # Time: O(n)   Space: O(n) worst case


# --- Approach 5: Reverse → carry → reverse (week 2 version) ---
# Full code: leetcode/week_2/leetcode_66.py


if __name__ == "__main__":
    def check(inp, expected):
        for cls in (Solution, SolutionInsert, SolutionCarryFlag):
            out = cls().plusOne(inp.copy())
            assert out == expected, f"{cls.__name__}: {inp} -> {out}, expected {expected}"
        print(f"{inp} -> {expected} OK")

    check([1, 2, 3], [1, 2, 4])
    check([4, 3, 2, 1], [4, 3, 2, 2])
    check([9], [1, 0])
    check([9, 9, 9], [1, 0, 0, 0])
    check([0], [1])
    assert SolutionInt().plusOne([1, 2, 3]) == [1, 2, 4]
    print("leetcode_66: all tests passed")
