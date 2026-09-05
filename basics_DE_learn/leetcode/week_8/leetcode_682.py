"""
682. Baseball Game
https://leetcode.com/problems/baseball-game/

Problem
  You are keeping a score record as a stack. Given operations (strings),
  apply them in order and return the **sum** of all scores on the record.

  Ops
    integer  — record that score
    "+"      — record sum of the **previous two** scores
    "D"      — record **double** of the previous score
    "C"      — **invalidate** (remove) the previous score

Examples
  ops = ["5","2","C","D","+"] → 30
    5 → [5]
    2 → [5, 2]
    C → [5]           (drop 2)
    D → [5, 10]       (double 5)
    + → [5, 10, 15]   (5+10)
    sum = 30

  ops = ["5","-2","4","C","D","9","+","+"] → 27

Pattern (t08 — Stack simulation)
  The "record" **is** a stack: last score is always `score[-1]`.
  C / D / + only look at the top (and top-2 for +). Never scan the middle.

  Template
    1. score = []
    2. for op in operations:
         if op == "C": score.pop()
         elif op == "D": score.append(2 * score[-1])
         elif op == "+": score.append(score[-1] + score[-2])
         else: score.append(int(op))
    3. return sum(score)

Your approach (week 8)
  Exactly the template. `res = 0` is unused — `sum(score)` at the end is enough.

Pro tip
  Problem guarantees ops are valid (C/D/+ only when enough previous scores).
  Still think: empty stack + "C" would crash — LC won't send that.

Relation to other problems
  **#20** Valid Parentheses — stack for matching, not numbers.
  **#844** / **#1047** — stack of chars; same push/pop-top idea.
  **#150** Evaluate RPN — stack of numbers + operators (sibling).

Common bugs
  - `int(i)` on "C"/"D"/"+" — check ops **before** converting
  - "+" using only top once — need **two** previous scores
  - Forgetting `C` removes from the record (later D/+ see the new top)
  - Returning last score instead of **sum** of the whole record

Approach comparison (n = len(operations))
  | Approach              | Time | Space | Notes                     |
  |-----------------------|------|-------|---------------------------|
  | Stack simulation      | O(n) | O(n)  | **Your Solution — submit**|

LeetCode: submit ONE class named Solution.
"""

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            if i == "C":
                score.pop()
            elif i == "D":
                score.append(2 * score[-1])
            elif i == "+":
                score.append(score[-1] + score[-2])
            else:
                score.append(int(i))
        return sum(score)
    # Time: O(n) — one pass + O(n) sum
    # Space: O(n) — score stack
