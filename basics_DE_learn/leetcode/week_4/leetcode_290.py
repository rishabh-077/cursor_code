"""
290. Word Pattern
https://leetcode.com/problems/word-pattern/

Problem
  Given a pattern string and a string s, return True if s follows the same pattern.
  A full match means there is a bijection between each letter in pattern and a
  **non-empty word** in s. Words in s are separated by single spaces.

Examples
  pattern = "abba", s = "dog cat cat dog"     → True
  pattern = "abba", s = "dog cat cat fish"    → False
  pattern = "aaaa", s = "dog cat cat dog"     → False
  pattern = "abba", s = "dog dog dog dog"     → False

Pattern (t04 — Hash / bidirectional mapping)
  Same idea as **#205** Isomorphic Strings — but tokens are **words**, not chars.
  1) Split s into words: s.split(" ")
  2) len(pattern) must equal len(words)
  3) Two maps: pattern char → word AND word → pattern char (bijection)

Your approach (week 4 — two hash maps)
  hashPS[pattern[i]] = s_list[i]   forward: letter → word
  hashSP[s_list[i]] = pattern[i]   reverse: word → letter
  Conflict if either map disagrees with current pair → False

Pro tip (word pattern / bijection)

Whenever you see:
  "word pattern" / "map letters to words" / "one-to-one pattern match"
Think:
  - Tokenize first (split on space)
  - Length check: one letter per word
  - Two maps (pattern→word, word→pattern) — same as #205
  - One map alone fails when two letters map to same word

Relation to other problems
  **#205** Isomorphic Strings — character-level bijection (nearly identical code).
  **#290** Word Pattern — split s, then same two-map loop on pattern[i] vs word[i].
  Change: `s.split(" ")` + compare len to pattern; inner logic is the same.

Why you need **both** hashPS and hashSP
  Forward only: pattern="ab", s="dog dog" → a→dog, b→dog (two keys → same word).
  Reverse check: word "dog" already maps to 'a', but pattern[1]='b' → False.

Common bugs
  - Forgetting to split s → comparing whole string to one letter
  - Not checking len(pattern) == len(words) before the loop
  - Single map pattern→word only → miss two letters → one word
  - Using split() with no arg vs split(" ") — LeetCode uses single spaces; split(" ") is fine
  - Updating maps before conflict check → overwrites hide errors

Approach comparison (p = len(pattern), w = number of words)
  | Approach                    | Time      | Space | Notes                        |
  |-----------------------------|-----------|-------|------------------------------|
  | Two hash maps (bidirectional)| O(p + w) | O(p)  | Your solution — submit Solution|
  | zip(pattern, words) + maps  | O(p + w)  | O(p)  | Same logic, cleaner loop     |
  | First-occurrence pattern    | O(p + w)  | O(p)  | Map char/word to index id    |

  *At most p distinct letters and p words → O(p) extra space.

LeetCode: submit ONE class named Solution (two hash maps below).
"""


# --- Approach 1: Two hash maps — pattern→word and word→pattern (submit as Solution) ---
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(pattern) != len(s_list):
            return False

        hashPS, hashSP = {}, {}

        for i in range(len(pattern)):
            if (pattern[i] in hashPS and hashPS[pattern[i]] != s_list[i]) or (
                s_list[i] in hashSP and hashSP[s_list[i]] != pattern[i]
            ):
                return False
            hashPS[pattern[i]] = s_list[i]
            hashSP[s_list[i]] = pattern[i]
        return True
    # Time: O(p + w) — split is O(w); one pass over pattern
    # Space: O(p) — at most p entries in each map


# --- Approach 2: zip iteration — same logic, cleaner loop ---
class SolutionZip:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        p_to_w, w_to_p = {}, {}
        for ch, word in zip(pattern, words):
            if ch in p_to_w and p_to_w[ch] != word:
                return False
            if word in w_to_p and w_to_p[word] != ch:
                return False
            p_to_w[ch] = word
            w_to_p[word] = ch
        return True
    # Time: O(p + w)   Space: O(p)


# --- Approach 3: First-occurrence pattern — map char and word to same index id ---
class SolutionPattern:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        def build_ids(items):
            seen = {}
            ids = []
            for item in items:
                if item not in seen:
                    seen[item] = len(seen)
                ids.append(seen[item])
            return ids

        return build_ids(pattern) == build_ids(words)
    # Time: O(p + w)   Space: O(p)
    #
    # Trace: pattern="abba", words=["dog","cat","cat","dog"]
    #   pattern ids → [0,1,1,0]
    #   word ids    → [0,1,1,0]  → True


if __name__ == "__main__":
    tests = [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
        ("a", "dog", True),
        ("a", "dog cat", False),
        ("ab", "dog dog", False),
    ]
    for pattern, s, expected in tests:
        for cls in (Solution, SolutionZip, SolutionPattern):
            got = cls().wordPattern(pattern, s)
            assert got == expected, f"{cls.__name__}: {pattern!r}, {s!r} -> {got}"
        print(f"pattern={pattern!r}, s={s!r} -> {expected} OK")
    print("leetcode_290: all tests passed")
