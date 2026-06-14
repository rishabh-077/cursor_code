"""
38. Count and Say
https://leetcode.com/problems/count-and-say/

Problem
  The count-and-say sequence is a sequence of digit strings defined recursively:
    - s₁ = "1"
    - sₙ is obtained by reading sₙ₋₁ aloud (run-length encoding in words)

  Given n, return sₙ.

Examples
  n = 1 → "1"
  n = 4 → "1211"
    1 → "1"
    2 → "11"      (one 1)
    3 → "21"      (two 1s)
    4 → "1211"    (one 2, one 1)

Pattern (t03 — Strings / run-length encode)
  Build each term from the previous by scanning **runs** of the same digit.
  For each run: append str(count) + digit.

Your approach (iterate n−1 times, two pointers per term)
  1) Start current_result = "1"
  2) Outer loop n−1 times
  3) Inner: i scans; j counts how many consecutive same digits
  4) next_result += str(count) + current_digit; i = j
  5) current_result = next_result

Pro tip (run-length encoding)

Whenever you see:
  "count consecutive" / "how many in a row" / "compress repeats"
Think:
  - Two pointers: i = start of run, j = end of run (exclusive)
  - Or itertools.groupby in Python
  - Output size can grow fast — LeetCode caps n (usually ≤ 30)

Relation to other problems
  Same "run" scanning as **#485** Max Consecutive Ones (count 1s in a row).
  Inverse idea: decode RLE string back to expanded form (not asked here).

Common bugs
  - Looping n times instead of **n−1** (already start at "1")
  - Not moving i to j after a run → infinite loop
  - Forgetting base case n == 1

Complexity
  Time: O(total output length) — sequence grows quickly; not simple O(n)
  Space: O(output length) — building new strings each iteration

LeetCode: submit ONE class named Solution (run-length scan below).
"""

from itertools import groupby


# --- Approach 1: Two-pointer run scan (submit this as Solution) ---
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        current_result = "1"
        for _ in range(n - 1):
            i = 0
            next_result = ""
            while i < len(current_result):
                count = 1
                current_digit = current_result[i]
                j = i + 1
                while j < len(current_result) and current_result[j] == current_digit:
                    count += 1
                    j += 1

                next_result += str(count) + current_digit
                i = j

            current_result = next_result

        return current_result
    # Time: O(output length)   Space: O(output length)


# --- Approach 2: itertools.groupby (Pythonic; same logic) ---
class SolutionGroupBy:
    def countAndSay(self, n: int) -> str:
        current = "1"
        for _ in range(n - 1):
            parts = []
            for digit, group in groupby(current):
                parts.append(str(len(list(group))) + digit)
            current = "".join(parts)
        return current
    # Time: O(output length)   Space: O(output length)


if __name__ == "__main__":
    sol = Solution()
    assert sol.countAndSay(1) == "1"
    assert sol.countAndSay(2) == "11"
    assert sol.countAndSay(3) == "21"
    assert sol.countAndSay(4) == "1211"
    assert sol.countAndSay(5) == "111221"

    assert SolutionGroupBy().countAndSay(4) == "1211"
    print("leetcode_38: all tests passed")
