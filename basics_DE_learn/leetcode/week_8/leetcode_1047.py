"""
1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Problem
  Given a string s of lowercase letters, repeatedly remove **two adjacent
  equal** characters until none remain. Return the final string.
  Removals can cascade (after a pair drops, new neighbors may match).

Examples
  s = "abbaca" → "ca"
    abbaca → a(bb)aca → aaca → (aa)ca → ca
  s = "azxxzy" → "ay"

Pattern (t08 — Stack, adjacent pair)
  Walk left → right. If current char **equals the top**, they form an adjacent
  pair → pop. Else push. Cascades happen automatically: after pop, the new top
  is the left neighbor of whatever comes next.

  Template
    1. stack = []
    2. for c in s:
         if stack and stack[-1] == c:
           stack.pop()
         else:
           stack.append(c)
    3. return "".join(stack)

Your approach (week 8)
  Same idea. You wrote `char in stack[-1]`. For a single-character string that
  is equivalent to `char == stack[-1]`. Prefer `==` — `in` is for "substring /
  membership" and is easier to misread.

Why a stack (not two pointers on the original)?
  After deleting a pair, the string **shrinks** and new pairs form. A stack
  *is* the current result; you never rebuild the whole string each time.

Relation to other problems
  **#844** Backspace Compare — pop on '#' (not on equal letters).
  **#20** Valid Parentheses — pop when closer matches mapped opener.
  **#1209** Remove Adjacent Duplicates II — pop k copies (Medium follow-up).

Common bugs
  - Using `in` on a longer top by mistake (here top is one char)
  - Removing **all** runs of duplicates in one scan without a stack — misses
    cascades unless you loop (slower / messier)
  - Forgetting `"".join(stack)` — LC wants a string
  - Comparing to `stack` (the list) instead of `stack[-1]`

Approach comparison (n = len(s))
  | Approach                         | Time | Space | Notes                     |
  |----------------------------------|------|-------|---------------------------|
  | Repeat scan until no change      | O(n²)| O(n)  | many rebuilds             |
  | Stack adjacent-pair              | O(n) | O(n)  | **Your Solution — submit**|

LeetCode: submit ONE class named Solution.
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
    # Time: O(n) — each char pushed/popped at most once
    # Space: O(n) — output stack
