"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Problem
  Given a string s containing only '()[]{}', return true if it is valid:
    - Open brackets closed by the **same type**.
    - Open brackets closed in the **correct order**.
    - Every close has a matching open.

Examples
  s = "()"       → True
  s = "()[]{}"   → True
  s = "(]"       → False
  s = "([)]"     → False   (wrong order)
  s = "{[]}"     → True

Pattern (t08 — Stack, matching)
  Opens go on a stack. A close must match the **top** (most recent unmatched open).
  LIFO: last open is the first that must close.

  Template
    1. stack = []; close_to_open = {')':'(', ']':'[', '}':'{'}
    2. for c in s:
         if c is a closer:
           if stack and stack[-1] == close_to_open[c]: pop
           else: return False
         else:
           stack.append(c)          ← opener
    3. return stack is empty        ← leftover opens are invalid

Your approach (week 8 — dict of closer → opener + stack)
  Exactly the template. `char_dict` maps closer to the opener it needs.

Why a stack (not a counter)?
  Counters cannot enforce **order**. "([)]" has balanced counts but is invalid.
  Stack remembers which open is still waiting.

Relation to other problems
  **#1047** Remove Adjacent Duplicates — same "pop when matches top."
  **#32** Longest Valid Parentheses — stack of indices (Medium follow-up).
  **#22** Generate Parentheses — backtracking, not this stack match.

Common bugs
  - Closing when stack is empty → False (no matching open)
  - Leftover opens at the end → must return `not stack`, not always True
  - Mapping opener→closer and forgetting to look up the closer
  - Treating "([)]" as valid by counting instead of stack

Approach comparison (n = len(s))
  | Approach                         | Time | Space | Notes                     |
  |----------------------------------|------|-------|---------------------------|
  | Count open/close                 | O(n) | O(1)  | Fails on order            |
  | Stack + closer→opener map        | O(n) | O(n)  | **Your Solution — submit**|

LeetCode: submit ONE class named Solution.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_dict = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in char_dict:
                if stack and stack[-1] == char_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    # Time: O(n) — one pass
    # Space: O(n) — stack of unmatched opens
