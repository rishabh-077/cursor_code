"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Problem
  Given two strings s and t, determine if they are isomorphic.
  Characters in s can be replaced to get t such that:
    - All occurrences of a character map to the same character
    - No two characters map to the same character (one-to-one / bijection)
    - Order is preserved
  A character may map to itself.

Examples
  s = "egg", t = "add"     → True   (e→a, g→d)
  s = "foo", t = "bar"     → False  (o would need to map to both a and r)
  s = "paper", t = "title" → True
  s = "badc", t = "baba"   → False  (c→a but a already maps to b)

Pattern (t04 — Hash / bidirectional mapping)
  Track mapping **s → t** AND **t → s** at the same time.
  If s[i] was seen before, its partner must still be t[i].
  If t[i] was seen before, its partner must still be s[i] — blocks two s-chars → one t-char.

Your approach (week 4 — two hash maps)
  hashST[s[i]] = t[i]   forward map
  hashTS[t[i]] = s[i]   reverse map (enforces bijection)
  Before assigning: conflict if existing mapping points elsewhere → False

Pro tip (isomorphism / bijection)

Whenever you see:
  "isomorphic" / "one-to-one character mapping" / "same pattern"
Think:
  - Two maps (s→t and t→s) OR pattern of first-occurrence indices
  - One map alone is **not enough** — catches s="ab", t="aa" only with reverse check
  - Same length required (different lengths → False immediately)

Relation to other problems
  **#242** Valid Anagram — same multiset of letters, **ignore order** (different question).
  **#205** Isomorphic — **position pattern** must match (e→a everywhere e appears).
  **#383** Ransom Note — frequency counts, not structural mapping.

Why you need **both** hashST and hashTS
  Forward only: s="ab", t="aa" might assign a→a, b→a (two keys → same value).
  Reverse check: when processing b→a, hashTS['a'] is already 'a' ≠ 'b' → False.

Common bugs
  - Single map s→t only → miss two-to-one mapping
  - Updating maps before checking conflict → overwrite hides error (check **then** assign)
  - Forgetting length check
  - Confusing with anagram (counts) vs isomorphism (consistent replacement pattern)

Approach comparison (n = len(s))
  | Approach                    | Time  | Space | Notes                          |
  |-----------------------------|-------|-------|--------------------------------|
  | Two hash maps (bidirectional)| O(n) | O(1)* | Your solution — submit Solution|
  | First-occurrence pattern    | O(n)  | O(1)* | Map each char to pattern index   |
  | zip(s,t) + one dict         | Wrong | —     | Needs reverse check or pattern |

  *At most 26 distinct chars on LeetCode (ASCII letters) → O(1) space.

LeetCode: submit ONE class named Solution (two hash maps below).
"""


# --- Approach 1: Two hash maps — s→t and t→s (submit this as Solution) ---
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashST, hashTS = {}, {}

        for i in range(len(s)):
            # Conflict: char already mapped to a different partner
            if (s[i] in hashST and hashST[s[i]] != t[i]) or (
                t[i] in hashTS and hashTS[t[i]] != s[i]
            ):
                return False
            hashST[s[i]] = t[i]
            hashTS[t[i]] = s[i]

        return True
    # Time: O(n) — one pass
    # Space: O(1) — at most 26 keys per map


# --- Approach 2: Pattern of first-occurrence indices — no reverse map needed ---
class SolutionPattern:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def build_pattern(st: str) -> list[int]:
            seen = {}
            pattern = []
            for c in st:
                if c not in seen:
                    seen[c] = len(seen)
                pattern.append(seen[c])
            return pattern

        return build_pattern(s) == build_pattern(t)
    # Time: O(n)   Space: O(1) for bounded alphabet
    #
    # Trace: s="egg" → [0,1,1]   t="add" → [0,1,1]  → True
    #        s="foo" → [0,1,1]   t="bar" → [0,1,2]  → False


# --- Approach 3: zip iteration — same logic as Solution, cleaner loop ---
class SolutionZip:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t, t_to_s = {}, {}
        for a, b in zip(s, t):
            if a in s_to_t and s_to_t[a] != b:
                return False
            if b in t_to_s and t_to_s[b] != a:
                return False
            s_to_t[a] = b
            t_to_s[b] = a
        return True
    # Time: O(n)   Space: O(1)


if __name__ == "__main__":
    tests = [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),
        ("ab", "aa", False),
        ("a", "a", True),
        ("a", "b", True),
        ("ab", "cd", True),
    ]
    for s, t, expected in tests:
        for cls in (Solution, SolutionPattern, SolutionZip):
            got = cls().isIsomorphic(s, t)
            assert got == expected, f"{cls.__name__}: {s!r}, {t!r} -> {got}"
        print(f"s={s!r}, t={t!r} -> {expected} OK")
    print("leetcode_205: all tests passed")
