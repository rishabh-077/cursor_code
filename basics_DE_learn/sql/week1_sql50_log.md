# SQL 50 — Week 1 log (problems 1–4)

**Study plan:** https://leetcode.com/studyplan/top-sql-50/  
**Tracker:** [portal_week_01.md](../trackers/portal_week_01.md)

| # | LC # | Problem | Section | Done | Pattern / notes |
|---|------|---------|---------|:----:|-----------------|
| 1 | 1757 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | Select | [x] | `WHERE` + `OR` / flags |
| 2 | 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | Select | [x] | `NULL` handling — `IS NULL`, `COALESCE`, or `IFNULL` |
| 3 | 595 | [Big Countries](https://leetcode.com/problems/big-countries/) | Select | [x] | Filter on multiple columns |
| 4 | 1148 | [Article Views I](https://leetcode.com/problems/article-views-i/) | Select | [x] | `GROUP BY` + `HAVING` (self-views) |

**Week 2 starts at #5:** [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/) (1683) — still Select, then Basic Joins from #6.

---

## Interview tip (DE switch)

For SQL rounds: say **what** you’re filtering, **why** `NULL` behaves differently, and **readability** (`COALESCE` vs nested `CASE`) — aligns with production SQL in BQ/Snowflake.
