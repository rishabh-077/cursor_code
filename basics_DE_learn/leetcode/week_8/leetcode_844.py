"""
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Problem
  Given two strings s and t that may contain '#' (backspace). After applying
  backspaces, return whether the two strings are equal.
  Typing a '#' deletes the char before it (if any). Extra '#' on empty = no-op.

Examples
  s = "ab#c", t = "ad#c"     → True     (both become "ac")
  s = "ab##", t = "c#d#"     → True     (both become "")
  s = "a#c",  t = "b"        → False    ("c" vs "b")
  s = "xywrrmp", t = "xywrrmu#p" → True

Pattern (t08 — Stack build, then compare)
  Walk left → right. Letter → push. '#' → pop if stack non-empty.
  Final stacks (or joined strings) must be equal.

  Template (stack)
    1. def build(s):
         st = []
         for c in s:
           if c == "#":
             if st: st.pop()
           else:
             st.append(c)
         return st
    2. return build(s) == build(t)

Pattern (O(1) extra space — two pointers from the right)
  '#' deletes to the **left**, so scan **right → left**.
  Skip chars that a later '#' already ate. Compare the next "surviving" char
  of s vs t. Greg/NeetCode helper: count pending backspaces while walking left.

Your two approaches (week 8)
  1) Two stacks — clear, O(n+m) space.  ← easy to write in interview
  2) Reverse two-pointer — O(1) extra.  ← mention if they ask to optimize

Which is better?  **Approach 1** to submit unless they demand O(1) space.
  Approach 2 is the follow-up.

Relation to other problems
  **#1047** Remove All Adjacent Duplicates — pop when **equal** to top (not '#').
  **#20** Valid Parentheses — pop when closer matches top.
  **#682** Baseball Game — same stack simulation.

Common bugs
  - Popping on '#' when stack is empty → crash; guard with `if stack`
  - Comparing original s and t instead of built strings
  - Two-pointer: forgetting to `index -= 1` after comparing a valid pair
  - Two-pointer: treating leftover chars on one side as equal to empty

Approach comparison (n = len(s), m = len(t))
  | Approach                    | Time    | Space | Notes                        |
  |-----------------------------|---------|-------|------------------------------|
  | Build stacks / strings      | O(n+m)  | O(n+m)| **SolutionStack — submit**   |
  | Two pointers from the right | O(n+m)  | O(1)  | SolutionTwoPointer follow-up |

LeetCode: submit ONE class named Solution (stack version below).
"""


# --- Approach 1: Build with stacks (submit) ---
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for char in s:
            if char == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(char)
        for char in t:
            if char == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(char)
        return s_stack == t_stack
    # Time: O(n + m)
    # Space: O(n + m)


# --- Approach 2: Scan from the right — O(1) extra ---
class SolutionTwoPointer:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValidChar(string, index):
            backspace = 0
            while index >= 0:
                if backspace == 0 and string[index] != "#":
                    break
                elif string[index] == "#":
                    backspace += 1
                else:
                    backspace -= 1
                index -= 1
            return index

        index_s, index_t = len(s) - 1, len(t) - 1
        while index_s >= 0 or index_t >= 0:
            index_s = nextValidChar(s, index_s)
            index_t = nextValidChar(t, index_t)

            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""
            if char_s != char_t:
                return False
            index_s -= 1
            index_t -= 1
        return True
    # Time: O(n + m)
    # Space: O(1)
