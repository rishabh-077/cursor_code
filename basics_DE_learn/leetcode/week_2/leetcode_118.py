"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Problem
  Given numRows, return the first numRows of Pascal's triangle.
  Row 0 is [1]. Each row has one more element than the row above.
  Each interior value is the sum of the two values directly above it.

Example (numRows = 5)
  [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
  ]

Pattern (t02 — Arrays / simulation)
  Build row by row from the previous row — classic **DP on a triangle**.
  Pad the previous row with 0 on both ends, then each new cell = left neighbor + right neighbor
  in the padded array (your `temp[j] + temp[j+1]`).

Why padding works
  For previous row [1, 3, 3, 1], padded temp = [0, 1, 3, 3, 1, 0].
  New row length = len(prev) + 1. Index j in new row uses temp[j] and temp[j+1]:
    → "above-left" + "above-right" (0 at edges gives the 1's on the sides).

Approach comparison (R = numRows)
  | Approach                    | Time        | Space     | Notes                    |
  |-----------------------------|-------------|-----------|--------------------------|
  | Row-by-row with padding     | O(R²)       | O(R²) out | Preferred — submit below |
  | Combinatorics per cell C(n,k)| O(R²)       | O(R²)     | math; watch integer div  |
  | Recursion on triangle       | O(R²)       | O(R) stack| Same idea, less iterative|

Complexity (your solution)
  Time:  O(numRows²) — row i has i+1 cells; 1+2+…+n ≈ n²/2
  Space: O(numRows²) — output; extra O(numRows) for `temp` per iteration

Edge cases
  numRows = 1 → return [[1]]
  numRows = 0 → not in constraints (1 ≤ numRows ≤ 30)

LeetCode: submit ONE class named Solution.
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
    # Time: O(numRows²)   Space: O(numRows²) output




# --- Alternative: math (n choose k) per cell — interview optional ---
class SolutionCombinatorics:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(numRows):
            row = [1]
            for k in range(1, n):
                row.append(row[-1] * (n - k) // k)
            if n > 0:
                row.append(1)
            res.append(row)
        return res


if __name__ == "__main__":
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    out = Solution().generate(5)
    assert out == expected, out
    assert Solution().generate(1) == [[1]]
    print("leetcode_118: all tests passed")
