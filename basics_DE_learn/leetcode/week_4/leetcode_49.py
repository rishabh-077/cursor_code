"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Problem
  Given an array of strings strs, group the anagrams together. You can return the
  answer in any order. An anagram is a word formed by rearranging letters of
  another (e.g. "eat" and "tea").

Examples
  ["eat","tea","tan","ate","nat","bat"]
  → [["bat"],["nat","tan"],["ate","eat","tea"]]  (order of groups may vary)

Pattern (t04 — Hash / frequency signature)
  Anagrams share the **same character counts** → use a canonical **key** per group.
  Bucket strings into hash map: key → list of words with that signature.

Your approach (week 4 — count array + tuple key)
  1) For each string s: build count[26] via ord(c) - ord('a')
  2) Use tuple(count) as dict key (lists are not hashable)
  3) Append s to res[key]; return list(res.values())

Pro tip (group by anagram / same multiset)

Whenever you see:
  "group anagrams" / "same letters same counts"
Think:
  - **Key** = sorted string OR char-frequency tuple OR Counter
  - defaultdict(list) avoids "if key not in dict" boilerplate
  - tuple(count) works because lists can't be dict keys

Relation to other problems
  **#242** Valid Anagram — check two strings share same counts (pair).
  **#49** Group Anagrams — many strings → bucket by shared signature.
  **#383** Ransom Note — one-way count check, not grouping.

Why tuple(count) as key
  Same idea as #242: only counts matter, not order.
  "eat", "tea", "ate" → identical 26-slot count vector → same bucket.

Common bugs
  - Using list as dict key → TypeError (unhashable)
  - Sorting each string works but O(k log k) per word vs O(k) count
  - Forgetting lowercase-only constraint on LC (a-z) — count[26] is fine
  - Returning dict values vs list — LeetCode accepts list(res.values())

Approach comparison (n = len(strs), k = avg word length)
  | Approach              | Time           | Space | Notes                    |
  |-----------------------|----------------|-------|--------------------------|
  | Count array + tuple   | O(n × k)       | O(n)  | Your solution — submit   |
  | Sort each word as key | O(n × k log k) | O(n)  | Simpler to write         |
  | Counter as key        | O(n × k)       | O(n)  | tuple(Counter(s).items())|

LeetCode: submit ONE class named Solution (count tuple below).
"""

from collections import defaultdict
from typing import List


# --- Approach 1: Count array + tuple key (submit this as Solution) ---
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    # Time: O(n × k) — n words, k chars each to count
    # Space: O(n × k) — store all strings in buckets


# --- Approach 2: Sorted string as key — easier to read ---
class SolutionSortKey:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res["".join(sorted(s))].append(s)
        return list(res.values())
    # Time: O(n × k log k)   Space: O(n × k)


# --- Approach 3: Counter — same signature idea ---
class SolutionCounter:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter

        res = defaultdict(list)
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            res[key].append(s)
        return list(res.values())
    # Time: O(n × k)   Space: O(n × k)


if __name__ == "__main__":
    def normalize(groups):
        return sorted(sorted(g) for g in groups)

    tests = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]
    for strs, expected in tests:
        for cls in (Solution, SolutionSortKey, SolutionCounter):
            got = normalize(cls().groupAnagrams(strs))
            exp = normalize(expected)
            assert got == exp, f"{cls.__name__}: {got} != {exp}"
        print(f"{strs} -> OK")
    print("leetcode_49: all tests passed")
