"""
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Problem
  Given a string s and an integer k, return the maximum number of vowel letters
  in any substring of s with length exactly k.
  Vowels are 'a', 'e', 'i', 'o', 'u' (lowercase only for this problem).

Examples
  s = "abciiidef", k = 3 → 3  ("iii")
  s = "aeiou",     k = 2 → 2  ("ae", "ei", …)
  s = "leetcode",  k = 3 → 2  ("eet", "ode", …)

Pattern (t06 — Sliding window, fixed size)
  Window length is **fixed at k**. Slide one index at a time: add the new right
  char's vowel contribution, drop the old left char's contribution.

  Template
    1. Count vowels in s[0 : k]           — first window (or grow to size k)
    2. For each new r:
         cnt += 1 if s[r] is vowel
         if window length > k:
             cnt -= 1 if s[l] is vowel; l += 1
         res = max(res, cnt)
    3. return res

  Same idea as #643 (max average): track a running metric over a fixed window,
  not average/sum of ints — here it's vowel count.

Your approach (week 6 — fixed sliding window, submit Solution)
  Expand r; when window exceeds k, drop s[l] and advance l. Keep max vowel count.

Pro tip (fixed vs variable window)

Whenever you see:
  "substring of length k" / "window size k" / "exactly k characters"
Think:
  - **Fixed-size** sliding window — += right, -= left when len > k
  - Do **not** use a while-loop to shrink by a condition (that's variable, e.g. #3, #209)

Relation to other problems
  **#643** Maximum Average Subarray I — same fixed window; sum instead of vowel count.
  **#3** Longest Substring Without Repeating — **variable** window (expand/shrink).
  **#209** Minimum Size Subarray Sum — variable window (shrink while sum >= target).

Common bugs
  - Using a tuple/list for vowels and `in` is fine, but a **set** is O(1) lookup
  - Updating res before the window has reached size k (if you build differently)
  - Forgetting to subtract when leaving char is a vowel — count drifts high
  - Subtracting before checking `r - l + 1 > k` — shrinks too early
  - Brute recounting every window of k chars — O(n * k) (BruteForceSolution below)

Approach comparison (n = len(s))
  | Approach                              | Time     | Space | Notes                         |
  |---------------------------------------|----------|-------|-------------------------------|
  | Brute — recount vowels each window    | O(n * k) | O(1)  | BruteForceSolution below      |
  | Fixed sliding window (one pass)       | O(n)     | O(1)  | Your Solution — submit        |

LeetCode: submit ONE class named Solution (sliding window below).
"""


# --- Approach 1: Brute force — recount vowels in every window of length k ---
class BruteForceSolution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ("a", "e", "i", "o", "u")
        max_vowel = 0
        j = 0
        while j + k <= len(s):
            vowel_count = 0
            for i in range(j, j + k):
                if s[i] in vowel:
                    vowel_count += 1
            max_vowel = max(max_vowel, vowel_count)
            j += 1
        return max_vowel
    # Time: O(n * k)
    # Space: O(1)


# --- Approach 2: Fixed sliding window — add right, drop left (submit as Solution) ---
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {"a", "e", "i", "o", "u"}
        res, cnt, l = 0, 0, 0
        for r in range(len(s)):
            cnt += 1 if s[r] in vowel else 0
            if r - l + 1 > k:
                cnt -= 1 if s[l] in vowel else 0
                l += 1
            res = max(res, cnt)
        return res
    # Time: O(n) — each char enters/leaves the window once
    # Space: O(1)
