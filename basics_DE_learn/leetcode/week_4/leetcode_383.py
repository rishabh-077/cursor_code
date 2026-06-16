"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/

Problem
  Given two strings ransomNote and magazine, return True if ransomNote can be
  constructed from letters in magazine. Each letter in magazine may only be used
  once in your construction.

Examples
  ransomNote = "a", magazine = "b"       → False
  ransomNote = "aa", magazine = "ab"     → False
  ransomNote = "aa", magazine = "aab"    → True

Pattern (t04 — Hash / frequency map)
  "Can I build A using letters from B?" → count available letters in magazine,
  then subtract as you "spend" each letter for ransomNote.

Your approach (week 4 — single map, decrement)
  1) Count every char in magazine → magdict
  2) For each char in ransomNote: decrement count; if missing or count < 0 → False
  3) If all chars satisfied → True

Pro tip (one-way frequency check)

Whenever you see:
  "can construct / can form / enough letters in pool"
Think:
  - Not the same as **#242** anagram (must match exactly both ways)
  - Here: magazine is the **pool** — need count_mag[c] >= count_ransom[c] for every c
  - One map: count pool once, spend while scanning ransomNote (early exit on deficit)

Relation to other problems
  **#242** Valid Anagram — equal counts both ways (two strings same multiset).
  **#383** Ransom Note — one-way subset: magazine must cover ransomNote (can have extras).
  **#387** First Unique — same counting machinery, different question.

Why single map beats two maps
  Building ransomdict + magdict then comparing works, but you only need to know
  "do I still have this letter?" — decrement magazine counts as you consume.

Common bugs
  - Treating like anagram → requiring exact equality of full strings
  - Checking `magdict[c] == 0` before decrement instead of `< 0` after (off-by-one)
  - Forgetting char not in magazine at all → use `.get(c, 0)` or `if c not in magdict`
  - Deleting keys at count 1 (Solution 3) — works but extra logic; decrement + < 0 is simpler

Approach comparison (m = len(magazine), n = len(ransomNote))
  | Approach              | Time    | Space | Notes                         |
  |-----------------------|---------|-------|-------------------------------|
  | Two hash maps         | O(m+n)  | O(1)* | Count both, compare ransom keys |
  | Single map (decrement)| O(m+n)  | O(1)* | Preferred — submit Solution   |
  | Counter subtraction   | O(m+n)  | O(1)* | Counter(magazine) then spend  |
  | Delete key at 0       | O(m+n)  | O(1)* | Same logic, more bookkeeping  |

  *Lowercase English → at most 26 keys.

LeetCode: submit ONE class named Solution (single map decrement below).
"""

from collections import Counter


# --- Approach 1: Two hash maps — count ransom + magazine, compare (your first draft) ---
class SolutionTwoMaps:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomdict = {}
        magdict = {}
        for i in range(len(ransomNote)):
            ransomdict[ransomNote[i]] = 1 + ransomdict.get(ransomNote[i], 0)
        for j in range(len(magazine)):
            magdict[magazine[j]] = 1 + magdict.get(magazine[j], 0)
        for k in ransomdict:
            if k not in magdict or ransomdict[k] > magdict[k]:
                return False
        return True
# Time: O(m + n) because we are iterating through the ransomNote and magazine list once
# Space: O(1) because the dictionary will only exist for the fixed 26 characters


# --- Approach 2: Single map — count magazine, spend on ransomNote (submit as Solution) ---
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magdict = {}
        for i in magazine:
            if i in magdict:
                magdict[i] += 1
            else:
                magdict[i] = 1
        for j in ransomNote:
            if j in magdict:
                magdict[j] -= 1
                if magdict[j] == -1:
                    return False
            else:
                return False
        return True
# Time: O(M + N) because we are iterating through the list once
# Space: O(1) because fixed 26 characters will only exist in the dictionary


# --- Approach 3: Same logic — .get(c, 0) avoids separate "not in" check ---
class SolutionGet:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magdict = {}
        for c in magazine:
            magdict[c] = magdict.get(c, 0) + 1

        for c in ransomNote:
            magdict[c] = magdict.get(c, 0) - 1
            if magdict[c] < 0:
                return False
        return True
    # Time: O(m + n)   Space: O(1) for bounded alphabet


# --- Approach 4: Delete key when count hits 0 ---
class SolutionDeleteKeys:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magdict = {}
        for c in magazine:
            magdict[c] = magdict.get(c, 0) + 1

        for c in ransomNote:
            if c not in magdict:
                return False
            if magdict[c] == 1:
                del magdict[c]
            else:
                magdict[c] -= 1
        return True
    # Time: O(m + n)   Space: O(1)


# --- Approach 5: Counter — count magazine, subtract for ransomNote ---
class SolutionCounter:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)
        for c in ransomNote:
            counts[c] -= 1
            if counts[c] < 0:
                return False
        return True
    # Time: O(m + n)   Space: O(1) for bounded alphabet


if __name__ == "__main__":
    tests = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("", "abc", True),
        ("f", "ff", True),
    ]
    for ransom, mag, expected in tests:
        for cls in (
            Solution,
            SolutionTwoMaps,
            SolutionGet,
            SolutionDeleteKeys,
            SolutionCounter,
        ):
            got = cls().canConstruct(ransom, mag)
            assert got == expected, f"{cls.__name__}: {ransom!r}, {mag!r} -> {got}"
        print(f"ransom={ransom!r}, mag={mag!r} -> {expected} OK")
    print("leetcode_383: all tests passed")
