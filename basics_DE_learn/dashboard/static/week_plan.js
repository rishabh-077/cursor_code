/** Study schedule — mirrors learn_plan_v2 + plan_weekN.md */
export const WEEK_PLAN = {
  1: {
    title: "Week 1",
    range: "25 May – 31 May 2026",
    dsaTopics: [
      { id: "t01", title: "Big-O Notation" },
      { id: "t02", title: "Arrays" },
      { id: "t03", title: "Strings" },
      { id: "t04", title: "Hash Maps & Sets" },
    ],
    blockAHint: "Open DSA plan → complete t01, t02, t03, t04 (theory + Easy LC each).",
    sqlRange: "SQL 50 #1–4",
    leetcodeTab: "Week 1 LC (from topics)",
  },
  2: {
    title: "Week 2",
    range: "1 Jun – 7 Jun 2026",
    dsaTopics: [
      { id: "t05", title: "Two Pointers" },
      { id: "t06", title: "Sliding Window" },
      { id: "t07", title: "Prefix Sums (optional)" },
    ],
    blockAHint: "Open DSA plan → t05 then t06 (theory → pattern → Easy LC first).",
    sqlRange: "SQL 50 #5–8",
    leetcodeTab: "Week 2 LC",
    schedule: [
      { date: "2026-06-01", day: "Sun", a: "t05 + LC 125", b: "SQL #5", c: "Chip Ch 3" },
      { date: "2026-06-02", day: "Mon", a: "t05 + LC 167", b: "Zoomcamp", c: "Chip" },
      { date: "2026-06-03", day: "Tue", a: "t06 + LC 3", b: "SQL #6–7", c: "Embeddings" },
      { date: "2026-06-04", day: "Wed", a: "t06 finish", b: "SQL #8", c: "Chip Ch 4" },
      { date: "2026-06-05", day: "Thu", a: "t07 or review", b: "Zoomcamp", c: "RAG note" },
      { date: "2026-06-06", day: "Fri", a: "catch-up", b: "Spark lazy", c: "review" },
      { date: "2026-06-07", day: "Sat", a: "tick t05–t06 in /dsa", b: "SQL review", c: "reflection" },
    ],
  },
};
