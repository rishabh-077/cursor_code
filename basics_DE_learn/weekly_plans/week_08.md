# Week 8 — Mon 31 Aug – Sun 6 Sep 2026

**Phase:** 1 · **DSA topic:** t08 Stacks (primary)  
**Mastery goal:** t08 — **theory** + **3–4 Easy no hints** (#20, #682, #844) + **1 Medium attempted** (#155 Min Stack or #739 Daily Temperatures)  
**Master plan:** [MASTER_PLAN.md](../MASTER_PLAN.md) · **Portal:** http://127.0.0.1:5050/portal?w=8  
**DE menu:** [DE_CURRICULUM.md](../DE_CURRICULUM.md) week 8 row · **SQL log:** [sql/week8_sql50_log.md](../sql/week8_sql50_log.md)

> **Calendar slip (2026-08-31):** Original Week 8 was **24–30 Aug**. Plan remapped to **31 Aug – 6 Sep** (1-week gap). Partial work during gap: **#442**, **#128**, some SQL #29–32 — counts as catch-up, not t08 primary.

---

## Hybrid inputs (from Week 7 reflection + repo auto-read)

| Input | Value |
|-------|--------|
| **Finished (wk 7)** | t07 LC + notes: **#1480, #724, #303, #560, #238, #525**. SQL through **#28**. Portal **t07 mastery ticked**. |
| **Gap week (24–30 Aug)** | Off-plan LC: **#442**, **#128**. SQL #29–32 partially started — carry Tue/Thu checkboxes into this week. |
| **Blocked** | Nothing on t08. Chip Ch 1 / Zoomcamp still backlog — Sat optional only. |
| **Next week** | Keep moving; light practice of past patterns (prefix / window) only after primary. |
| **Energy** | 3 |
| **t07 mastered?** | **Yes** (portal) — do not reopen as primary |
| **SQL count** | ~**28/50** (#1–28) · keep **Tue/Thu 30 min** · target **32/50** after wk 8 |
| **Parallel backlog** | Chip Ch 1 · Zoomcamp mod 1 · StrataScratch · LangChain chunking · DDIA — **Sat optional ONE** |

### LC hint / backlog queue (optional, after primary)

| # | Problem | Topic | When |
|---|---------|-------|------|
| 560 / 238 | Subarray Sum / Product Except Self | prefix | spare 15 min |
| 3 / 209 | Longest substring / Min subarray | window | Fri if t08 gated |
| 496 | Next Greater Element I | monotonic stack | Fri after #739 attempt |

**t08 focus:** LIFO — `append` = push, `pop` = pop top. Matching (#20), simulation (#682, #844), then **monotonic stack** (#739). Save files in `leetcode/week_8/`. **Do not start t09** until stack push/pop and valid-parens are automatic ([DSA_PACING.md](../learn_plans/DSA_PACING.md)).

**SQL note:** DE_CURRICULUM week 8 emphasizes **StrataScratch** on Sat — SQL still **#29–32** Tue/Thu only (30 min each).

---

## Mon 31 Aug

**PRIMARY (2 hrs):** **t08 theory** — stack LIFO; draw push/pop on paper. Watch Abdul Bari stack intro (15 min) or NeetCode stack overview. **#20** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — no hints; `leetcode/week_8/leetcode_20.py`. Say aloud: “open → push, close → match top or fail.”

**SECONDARY:** none

---

## Tue 1 Sep

**PRIMARY (2 hrs):** **#682** [Baseball Game](https://leetcode.com/problems/baseball-game/) — stack simulation (Google Easy). Notes in `week_8/`.

**SECONDARY (30 min):** SQL 50 **#29** [Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/) · **#30** [The Number of Employees Which Report to Each Employee](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/)

---

## Wed 2 Sep

**PRIMARY (2 hrs):** **#844** [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) — stack (or two-pointer variant after stack pass). Optional 15 min: **#1047** Remove All Adjacent Duplicates In String. Re-solve **#20** no hints if rusty.

**SECONDARY:** none

---

## Thu 3 Sep

**PRIMARY (2 hrs):** t08 **Medium attempt** (25 min timer): **#155** [Min Stack](https://leetcode.com/problems/min-stack/) — design class with O(1) min. Notes either way. If clean early, skim **#739** Daily Temperatures (monotonic stack — do not brute O(n²)).

**SECONDARY (30 min):** SQL 50 **#31** [Primary Department for Each Employee](https://leetcode.com/problems/primary-department-for-each-employee/) · **#32** [Triangle Judgement](https://leetcode.com/problems/triangle-judgement/)

---

## Fri 4 Sep

**PRIMARY (2 hrs):** Second pass **#155** if stuck **OR** **#739** [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) — monotonic decreasing stack. Tick t08 theory + easyNoHints if Easy set is clean. Optional: **#496** Next Greater Element I if #739 done.

**SECONDARY:** none

---

## Sat 5 Sep

**PRIMARY (2 hrs):** t08 review — paper: valid parens trace, min stack invariant, one monotonic-stack walk-through on `[73,74,75,71,69,72,76,73]`. Confirm mastery gate (3 Easy no hints + Medium attempted).

**SECONDARY (optional, pick ONE — ~30 min):** **StrataScratch** signup + 1 easy **OR** **Chip Ch 1** ([ai_engineering_notes.md](../theory/ai_engineering_notes.md)) **OR** LangChain chunking video (DE_CURRICULUM wk 8) — skip if t08 behind.

---

## Sun 6 Sep (15 min)

- Fill **reflection** in portal for Week 9 generation (**t09 Queues**, starts Mon 7 Sep)
- t08 mastery met? **Y/N** (theory + 3 Easy no hints + #155 or #739 attempted)
- SQL on track? Target **~32/50**
- Theory: Chip Ch 1 still open, or did Sat optional land?
