"""
344. Reverse String
https://leetcode.com/problems/reverse-string/

Problem
  Write a function that reverses a string. The input is given as an array of
  characters s. Modify s in-place with O(1) extra memory.

Examples
  ["h","e","l","l","o"] → ["o","l","l","e","h"]
  ["H","a","n","n","a","h"] → ["h","a","n","n","a","H"]

Pattern (t03 — Strings / two pointers)
  Swap characters from both ends moving inward until pointers meet or cross.

Pro tip (in-place reversal)

Whenever you see:
  "reverse in-place" on an array or char list
Think:
  - Two pointers: left = 0, right = len - 1
  - while left < right: swap(s[left], s[right]); move both inward

Note vs Python str
  LeetCode passes a **mutable list of chars** (`List[str]`), not an immutable `str`.
  In Python interviews, `s[::-1]` on a string is fine for a new string — here you
  must mutate the list in place.

Relation to other problems
  Same inward swap loop as **#125** Valid Palindrome (compare instead of swap)
  and **#27** / **#26** (write/swap toward one side). **#189** triple-reverse is
  the “reverse whole array” building block.

Common bugs
  - Using `left <= right` and swapping the middle twice on odd length (use `<`)
  - Returning a new list instead of mutating `s` (problem says modify in-place)
  - Off-by-one: `right` should start at `len(s) - 1`, not `len(s)`

Approach comparison (n = len(s))
  | Approach              | Time  | Space | Notes                              |
  |-----------------------|-------|-------|------------------------------------|
  | Two pointers + swap   | O(n)  | O(1)  | Preferred — submit as Solution     |
  | Stack pop into s      | O(n)  | O(n)  | Easy to reason about; extra memory |
  | s.reverse()           | O(n)  | O(1)  | Built-in; know two-pointer for interviews |

LeetCode: submit ONE class named Solution (two-pointer version below).
"""

from typing import List


# --- Approach 1: Two pointers — swap from both ends (submit this as Solution) ---
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    # Time: O(n)   Space: O(1)


# --- Approach 2: Stack — pop back into s (learning only) ---
class SolutionStack:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for char in s:
            stack.append(char)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
    # Time: O(n)   Space: O(n)


if __name__ == "__main__":
    def run_test(inp, expected):
        s = inp.copy()
        Solution().reverseString(s)
        ok = s == expected
        print(f"{inp} -> {s} (expected {expected}) {'OK' if ok else 'FAIL'}")
        assert ok

    run_test(["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"])
    run_test(["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
    run_test(["a"], ["a"])
    run_test(["a", "b"], ["b", "a"])

    s = ["x", "y", "z"]
    SolutionStack().reverseString(s)
    assert s == ["z", "y", "x"]
    print("leetcode_344: all tests passed")
