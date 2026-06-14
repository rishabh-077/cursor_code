/** Study schedule — mirrors learn_plan_v2 + plan_weekN.md (weeks Mon → Sun) */
export const WEEK_PLAN = {
  1: {
    title: "Week 1",
    range: "Mon 25 May – Sun 31 May 2026",
    dsaTopics: [
      { id: "t01", title: "Big-O Notation" },
      { id: "t02", title: "Arrays (start)" },
    ],
    blockAHint: "t01 finish · start t02 — see DSA_PACING.md",
    sqlRange: "SQL 50 #1–4",
  },
  2: {
    title: "Week 2",
    range: "Mon 1 Jun – Sun 7 Jun 2026",
    dsaTopics: [
      { id: "t02", title: "Arrays (finish)" },
      { id: "t03", title: "Strings (start)" },
    ],
    blockAHint: "t02 finish · t03 start",
    sqlRange: "SQL 50 #5–8",
    schedule: [
      { date: "2026-06-01", day: "Mon", a: "t02 review + Move Zeroes", b: "SQL #5", c: "Chip Ch 3" },
      { date: "2026-06-02", day: "Tue", a: "t02 Remove Dup", b: "Zoomcamp", c: "Chip" },
      { date: "2026-06-03", day: "Wed", a: "t03 + 242 review", b: "SQL #6–7", c: "Embeddings" },
      { date: "2026-06-04", day: "Thu", a: "t03 Valid Palindrome", b: "SQL #8", c: "Chip Ch 4" },
      { date: "2026-06-05", day: "Fri", a: "t03 catch-up", b: "Zoomcamp", c: "RAG note" },
      { date: "2026-06-06", day: "Sat", a: "re-solve hardest", b: "Spark lazy", c: "review" },
      { date: "2026-06-07", day: "Sun", a: "tick t02 in /dsa", b: "SQL review", c: "reflection" },
    ],
  },
};
