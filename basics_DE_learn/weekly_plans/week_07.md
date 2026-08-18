# Week 7 — Mon 17 Aug – Sun 23 Aug 2026

**Phase:** 1 · **DSA topic:** t07 Prefix sums (primary)  
**Mastery goal:** t07 — **theory** + **2–3 Easy no hints** (#1480, #724, optional #303) + **1 Medium attempted** (#560 Subarray Sum Equals K)  
**Master plan:** [MASTER_PLAN.md](../MASTER_PLAN.md) · **Portal:** http://127.0.0.1:5050/portal?w=7  
**DE menu:** [DE_CURRICULUM.md](../DE_CURRICULUM.md) week 7 row · **SQL log:** [sql/week7_sql50_log.md](../sql/week7_sql50_log.md)

---

## Hybrid inputs (from Week 6 reflection + repo auto-read)

| Input | Value |
|-------|--------|
| **Finished (wk 6)** | t06 LC + notes: **#643, #1456, #3, #209, #567, #438, #1004**. SQL through **#24**. Portal **t06 mastery ticked**. |
| **Blocked** | Nothing on t07. Theory (Chip / Zoomcamp) still backlog — Sat optional only. |
| **Next week** | Proceed to t07. SQL Tue/Thu. Light t06 / array backlog only after primary. |
| **Energy** | 3 |
| **t06 mastered?** | **Yes** (portal) — do not reopen as primary |
| **SQL count** | ~**24/50** (#1–24) · keep **Tue/Thu 30 min** · target **28/50** after wk 7 |
| **Parallel backlog** | Chip Ch 1 · Zoomcamp mod 1 · PySpark lazy · StrataScratch · DDIA — **Sat optional ONE** |

### LC hint / backlog queue (optional, after primary)

| # | Problem | Topic | When |
|---|---------|-------|------|
| 88 / 118 | Merge Sorted / Pascal | arrays | spare 15 min |
| 167 / 15 | Two Sum II / 3Sum | 2ptr | Fri if t07 gated |
| 49 / 347 | Group Anagrams / Top K | hash | skip unless energy |

**t07 focus:** `prefix[i] = prefix[i-1] + nums[i]`; range sum `prefix[r] - prefix[l-1]`. Hashmap on prefix makes **#560**. Save files in `leetcode/week_7/`. **Do not start t08** until prefix + range formula is automatic ([DSA_PACING.md](../learn_plans/DSA_PACING.md)).

**SQL note:** DE_CURRICULUM menu says “finish SQL 50” this week — that is the **Phase 1 bucket**, not two 30-min sessions. Continue **#25–28** only.

---

## Mon 17 Aug

**PRIMARY (2 hrs):** **t07 theory** — build prefix array; range `[l, r]` in O(1). Draw `prefix[r+1] - prefix[l]` vs inclusive indexing on paper. **#1480** [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) — no hints; `leetcode/week_7/leetcode_1480.py`.

**SECONDARY:** none

---

## Tue 18 Aug

**PRIMARY (2 hrs):** **#724** [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) — left sum vs total; Google Easy. Notes in `week_7/`.

**SECONDARY (30 min):** SQL 50 **#25** [Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/) · **#26** [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/)

---

## Wed 19 Aug

**PRIMARY (2 hrs):** **#303** [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) — `NumArray` constructor + `sumRange`. Say the O(1) formula aloud. Optional 15 min: re-solve **#1480** or **#724** no hints.

**SECONDARY:** none

---

## Thu 20 Aug

**PRIMARY (2 hrs):** t07 **Medium attempt** (25 min timer): **#560** [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — prefix + hashmap (`count[prefix - k]`). Notes either way. Do **not** brute O(n²) as the submitted story.

**SECONDARY (30 min):** SQL 50 **#27** [Find Followers Count](https://leetcode.com/problems/find-followers-count/) · **#28** [Biggest Single Number](https://leetcode.com/problems/biggest-single-number/)

---

## Fri 21 Aug

**PRIMARY (2 hrs):** Second pass **#560** if stuck **OR** **#238** [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) — prefix/suffix products (related, no hashmap). Tick t07 theory + easyNoHints if Easy set is clean. Optional: **#525** Contiguous Array if #560 done.

**SECONDARY:** none

---

## Sat 22 Aug

**PRIMARY (2 hrs):** t07 review — paper: running sum, pivot, range query, then **#560** hashmap walk-through. Confirm mastery gate (Easy no hints + Medium attempted).

**SECONDARY (optional, pick ONE — ~30 min):** **Chip Ch 1** (still first unchecked — [ai_engineering_notes.md](../theory/ai_engineering_notes.md)) **OR** Zoomcamp mod 1 **OR** skip if t07 behind.

---

## Sun 23 Aug (15 min)

- Fill **reflection** in portal for Week 8 generation (**t08 Stacks**, starts Mon 24 Aug)
- t07 mastery met? **Y/N** (theory + 2–3 Easy no hints + #560 attempted)
- SQL on track? Target **~28/50** (not all 50)
- Theory: one Sat optional, or still Chip Ch 1 backlog?
