/* Study schedule — mirrors learn_plan_v2 + plan_weekN.md */
const WEEK_PLAN = {
  1: {
    title: "Week 1",
    range: "25 May – 31 May 2026",
    dsaTopics: ["t01", "t02", "t03", "t04"],
    dsaLabels: {
      t01: "Big-O Notation",
      t02: "Arrays",
      t03: "Strings",
      t04: "Hash Maps & Sets",
    },
    blockAHint: "DSA plan → topics t01–t04 (theory + Easy LC each)",
    sqlRange: "SQL 50 #1–4",
  },
  2: {
    title: "Week 2",
    range: "1 Jun – 7 Jun 2026",
    dsaTopics: ["t05", "t06", "t07"],
    dsaLabels: {
      t05: "Two Pointers",
      t06: "Sliding Window",
      t07: "Prefix Sums (optional)",
    },
    blockAHint: "DSA plan → t05 then t06 (theory → pattern → Easy LC)",
    sqlRange: "SQL 50 #5–8",
    schedule: {
      "2026-06-01": { a: "t05 + LC 125", b: "SQL #5", c: "Chip Ch 3" },
      "2026-06-02": { a: "t05 + LC 167", b: "Zoomcamp", c: "Chip" },
      "2026-06-03": { a: "t06 + LC 3", b: "SQL #6–7", c: "Embeddings video" },
      "2026-06-04": { a: "t06 finish", b: "SQL #8", c: "Chip Ch 4" },
      "2026-06-05": { a: "t07 or review", b: "Zoomcamp", c: "RAG paragraph" },
      "2026-06-06": { a: "catch-up LC", b: "Spark lazy vs action", c: "review" },
      "2026-06-07": { a: "tick t05–t06 in /dsa", b: "SQL review", c: "reflection" },
    },
  },
};

let state = null;
let dsaState = { topics: {} };
let todayInfo = null;
let saveTimer = null;
const weekNum = new URLSearchParams(location.search).get("w") || "2";
const weekKey = () => `week${weekNum}`;
const week = () => state[weekKey()] || {};
const plan = () => WEEK_PLAN[weekNum] || WEEK_PLAN[2];

const $ = (sel) => document.querySelector(sel);
const statusEl = $("#saveStatus");

async function load() {
  const [progRes, dsaRes, todayRes] = await Promise.all([
    fetch("/api/progress"),
    fetch("/api/dsa-progress"),
    fetch("/api/today"),
  ]);
  state = await progRes.json();
  dsaState = await dsaRes.json();
  todayInfo = await todayRes.json();

  if (!state[weekKey()]) {
    alert(`No data for week ${weekNum} in progress.json`);
  }

  renderHeader();
  renderTodayStatus();
  renderToday();
  render();
  renderStats();
}

function renderTodayStatus() {
  const el = $("#todayStatus");
  if (!el || !todayInfo) return;
  const { storedToday, actualToday, inSync, timezone, suggestedWeek } = todayInfo;
  el.textContent = inSync
    ? `Today: ${storedToday}`
    : `Stored ${storedToday} · IST ${actualToday}`;
  el.classList.toggle("out-of-sync", !inSync);
  el.title = inSync
    ? `${timezone}`
    : `Click "Set today" to use ${actualToday} (suggested week ${suggestedWeek})`;
}

async function setTodayFromServer() {
  const res = await fetch("/api/set-today", { method: "POST" });
  const data = await res.json();
  if (!data.ok) {
    showToast("Could not set today");
    return;
  }
  state.meta.today = data.today;
  state.meta.currentWeek = data.currentWeek;
  todayInfo = {
    ...todayInfo,
    storedToday: data.today,
    actualToday: data.today,
    inSync: true,
    currentWeek: data.currentWeek,
    suggestedWeek: data.currentWeek,
  };
  renderTodayStatus();
  renderHeader();
  renderToday();
  renderDays(week().days);
  showToast(`Today → ${data.today} · Week ${data.currentWeek}`);
  if (String(data.currentWeek) !== String(weekNum)) {
    setTimeout(() => {
      location.href = `/week?w=${data.currentWeek}`;
    }, 900);
  }
}

function renderHeader() {
  const p = plan();
  const cw = state.meta?.currentWeek || 2;
  $("#pageTitle").textContent = `${p.title} · Tracker`;
  const today = state.meta?.today || "";
  $("#pageSubtitle").innerHTML =
    `${p.range}${today ? ` · Today <strong>${today}</strong> IST` : ""} · ` +
    `<a href="/">Hub</a> · <a href="/dsa">DSA plan (Block A)</a>`;

  $("#weekNav").innerHTML = [1, 2]
    .map(
      (w) =>
        `<a href="/week?w=${w}" class="${w == weekNum ? "active" : ""}">${WEEK_PLAN[w].title}${w == cw ? " ← current" : ""}</a>`
    )
    .join("");

  $("#dsaTopicList").textContent = p.dsaTopics.join(", ");
  $("#planWeekLink").innerHTML = `<a href="/week?w=${weekNum}">plan_week${weekNum}.md</a> (Daily tab)`;
  $("#sqlPanelTitle").textContent = `SQL 50 · ${p.sqlRange}`;
  $("#lcPanelTitle").textContent = `LeetCode · ${p.title}`;
  document.title = `DE Learn · ${p.title}`;
}

function renderToday() {
  const today = state.meta?.today;
  const p = plan();
  const sched = p.schedule?.[today];

  if (!today) {
    $("#todayBox").innerHTML = "";
    return;
  }

  const banner =
    todayInfo && !todayInfo.inSync
      ? `<div class="today-banner">
          <span>Dashboard date is <strong>${todayInfo.storedToday}</strong> but IST is <strong>${todayInfo.actualToday}</strong>.</span>
          <button type="button" class="btn btn-secondary" id="setTodayBannerBtn">Set today (IST)</button>
        </div>`
      : "";

  if (sched) {
    $("#todayBox").innerHTML = `${banner}
      <h2>Today · ${today} (${getDayName(today)})</h2>
      <div class="today-grid">
        <div><strong>Block A · 90 min</strong>${sched.a}<br/><a href="/dsa">Open DSA plan</a></div>
        <div><strong>Block B · 90 min</strong>${sched.b}</div>
        <div><strong>Block C · 30 min</strong>${sched.c}</div>
      </div>
      <p class="hint" style="margin-top:0.75rem;margin-bottom:0">After each block, tick the <strong>Daily</strong> tab for ${today}.</p>`;
  } else {
    $("#todayBox").innerHTML = `${banner}
      <h2>Today · ${today}</h2>
      <p style="margin:0;font-size:0.9rem;color:var(--muted)">
        Block A: <a href="/dsa">DSA plan</a> → ${p.dsaTopics.join(", ")}.
        Open <strong>Daily</strong> tab for this week's day list.
      </p>`;
  }

  $("#setTodayBannerBtn")?.addEventListener("click", setTodayFromServer);
}

function getDayName(iso) {
  try {
    return new Date(iso + "T12:00:00").toLocaleDateString("en-IN", { weekday: "long" });
  } catch {
    return "";
  }
}

async function save() {
  statusEl.textContent = "Saving…";
  statusEl.className = "save-status saving";
  try {
    const res = await fetch("/api/progress", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(state),
    });
    const data = await res.json();
    statusEl.textContent = `Saved ${formatTime(data.lastUpdated)}`;
    statusEl.className = "save-status";
    renderStats();
  } catch {
    statusEl.textContent = "Save failed";
    statusEl.className = "save-status error";
  }
}

async function saveDsaTopics() {
  try {
    await fetch("/api/dsa-progress", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dsaState),
    });
  } catch {
    /* ignore */
  }
}

function scheduleSave() {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(save, 400);
}

function formatTime(iso) {
  if (!iso) return "";
  try {
    return new Date(iso).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  } catch {
    return "";
  }
}

function showToast(msg) {
  let t = document.querySelector(".toast");
  if (!t) {
    t = document.createElement("div");
    t.className = "toast";
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.classList.add("show");
  setTimeout(() => t.classList.remove("show"), 2800);
}

async function renderStats() {
  const res = await fetch(`/api/stats?week=${weekNum}`);
  const s = await res.json();
  const pct = (d, t) => (t ? Math.round((d / t) * 100) : 0);
  const p = plan();
  const dsaDone = p.dsaTopics.filter((id) => dsaState.topics[id]).length;

  $("#statsGrid").innerHTML = `
    <div class="stat-card">
      <div class="label">DSA topics</div>
      <div class="value">${dsaDone}/${p.dsaTopics.length}</div>
      <div class="bar"><div class="bar-fill" style="width:${pct(dsaDone, p.dsaTopics.length)}%"></div></div>
    </div>
    <div class="stat-card">
      <div class="label">LeetCode</div>
      <div class="value">${s.leetcode.done}/${s.leetcode.total}</div>
      <div class="bar"><div class="bar-fill" style="width:${pct(s.leetcode.done, s.leetcode.total)}%"></div></div>
    </div>
    <div class="stat-card">
      <div class="label">SQL 50</div>
      <div class="value">${s.sql50.done}/${s.sql50.total}</div>
      <div class="bar"><div class="bar-fill" style="width:${pct(s.sql50.done, s.sql50.total)}%"></div></div>
    </div>
    <div class="stat-card">
      <div class="label">Daily blocks</div>
      <div class="value">${s.blocks.done}/${s.blocks.total}</div>
      <div class="bar"><div class="bar-fill" style="width:${pct(s.blocks.done, s.blocks.total)}%"></div></div>
    </div>
  `;
}

function render() {
  const w = week();
  renderDsaTopics();
  renderDays(w.days);
  renderLeetcode(w.leetcode);
  renderSql(w.sql50);
  renderDe(w.deTopics);
  renderExit(w.exitChecklist);
  renderOverviewExit(w.exitChecklist);
  renderReflection(w.reflection);
}

function renderDsaTopics() {
  const p = plan();
  $("#dsaTopicsList").innerHTML = p.dsaTopics
    .map((id) => {
      const done = dsaState.topics[id];
      const label = p.dsaLabels[id] || id;
      return `
      <div class="card ${done ? "done" : ""}" data-dsa-id="${id}">
        <input type="checkbox" ${done ? "checked" : ""} />
        <div class="card-body">
          <div class="card-title"><a href="/dsa">${id} · ${label}</a></div>
          <div class="card-meta">Complete theory + pattern + Easy problems in DSA plan</div>
        </div>
      </div>`;
    })
    .join("");

  $("#dsaTopicsList").querySelectorAll("[data-dsa-id]").forEach((el) => {
    const id = el.dataset.dsaId;
    el.querySelector("input").addEventListener("change", (e) => {
      dsaState.topics[id] = e.target.checked;
      saveDsaTopics();
      renderDsaTopics();
      renderStats();
      syncDsaExitChecklist();
      scheduleSave();
    });
  });
}

function syncDsaExitChecklist() {
  const w = week();
  const p = plan();
  const allDone = p.dsaTopics.every((id) => dsaState.topics[id]);
  const item = w.exitChecklist?.find((e) => e.id === "dsa-t05" || e.id === "dsa-week");
  if (item && weekNum === "2") item.done = dsaState.topics.t05 && dsaState.topics.t06;
}

function renderDays(days) {
  const today = state.meta?.today;
  const sched = plan().schedule || {};

  $("#daysList").innerHTML = days
    .map((d, i) => {
      const s = sched[d.date];
      const isToday = d.date === today;
      const taskLines = s
        ? `<div class="day-task-line">A: ${s.a} · B: ${s.b} · C: ${s.c}</div>`
        : `<div class="day-task-line">${escapeHtml(d.notes || "")}</div>`;
      return `
    <div class="card ${d.blockA && d.blockB && d.blockC ? "done" : ""} ${isToday ? "today-highlight" : ""}" data-day="${i}">
      <div class="card-body">
        <div class="card-title">${d.date} · ${d.day}${isToday ? " · TODAY" : ""}</div>
        ${taskLines}
        <div class="day-blocks">
          <label><input type="checkbox" data-field="blockA" ${d.blockA ? "checked" : ""} /> A · DSA</label>
          <label><input type="checkbox" data-field="blockB" ${d.blockB ? "checked" : ""} /> B · DE</label>
          <label><input type="checkbox" data-field="blockC" ${d.blockC ? "checked" : ""} /> C · Theory</label>
        </div>
      </div>
    </div>`;
    })
    .join("");

  $("#daysList").querySelectorAll("[data-day]").forEach((el) => {
    const i = +el.dataset.day;
    el.querySelectorAll("input").forEach((inp) => {
      inp.addEventListener("change", () => {
        const field = inp.dataset.field;
        week().days[i][field] = inp.checked;
        scheduleSave();
        renderStats();
        renderDays(week().days);
      });
    });
  });
}

function renderLeetcode(items) {
  $("#leetcodeList").innerHTML = (items || [])
    .map(
      (p, i) => `
    <div class="card ${p.done ? "done" : ""}" data-lc="${i}">
      <div class="card-body">
        <div class="card-title">
          <a href="https://leetcode.com/problems/${p.slug}/" target="_blank" rel="noopener">${p.id}. ${p.title}</a>
        </div>
        <div class="card-meta">${p.pattern}</div>
        <div class="card-subchecks">
          <label><input type="checkbox" data-field="done" ${p.done ? "checked" : ""} /> Solved</label>
          <label><input type="checkbox" data-field="noHints" ${p.noHints ? "checked" : ""} /> No hints</label>
          <label><input type="checkbox" data-field="complexityInRepo" ${p.complexityInRepo ? "checked" : ""} /> Notes in repo</label>
        </div>
      </div>
    </div>`
    )
    .join("");

  bindSubchecks("#leetcodeList", "leetcode");
}

function renderSql(items) {
  $("#sqlList").innerHTML = (items || [])
    .map(
      (s, i) => `
    <div class="card ${s.done ? "done" : ""}" data-sql="${i}">
      <input type="checkbox" data-field="done" ${s.done ? "checked" : ""} />
      <div class="card-body">
        <div class="card-title">
          <a href="https://leetcode.com/problems/${s.slug}/" target="_blank" rel="noopener">#${s.num} · ${s.title}</a>
        </div>
        <div class="card-meta">LC ${s.lc} · ${s.section}</div>
      </div>
    </div>`
    )
    .join("");

  $("#sqlList").querySelectorAll("[data-sql]").forEach((el) => {
    const i = +el.dataset.sql;
    el.querySelector("input").addEventListener("change", (e) => {
      week().sql50[i].done = e.target.checked;
      scheduleSave();
      render();
    });
  });
}

function renderDe(items) {
  $("#deList").innerHTML = (items || [])
    .map(
      (t, i) => `
    <div class="card ${t.done ? "done" : ""}" data-de="${i}">
      <input type="checkbox" data-field="done" ${t.done ? "checked" : ""} />
      <div class="card-body">
        <div class="card-title">${t.title}</div>
        ${t.path ? `<div class="card-meta">${t.path}</div>` : ""}
      </div>
    </div>`
    )
    .join("");

  $("#deList").querySelectorAll("[data-de]").forEach((el) => {
    const i = +el.dataset.de;
    el.querySelector("input").addEventListener("change", (e) => {
      week().deTopics[i].done = e.target.checked;
      scheduleSave();
      render();
    });
  });
}

function renderExit(items) {
  $("#exitList").innerHTML = (items || [])
    .map(
      (e, i) => `
    <div class="card ${e.done ? "done" : ""}" data-exit="${i}">
      <input type="checkbox" ${e.done ? "checked" : ""} />
      <div class="card-body"><div class="card-title">${e.label}</div></div>
    </div>`
    )
    .join("");

  $("#exitList").querySelectorAll("[data-exit]").forEach((el) => {
    const i = +el.dataset.exit;
    el.querySelector("input").addEventListener("change", (ev) => {
      week().exitChecklist[i].done = ev.target.checked;
      scheduleSave();
      render();
    });
  });
}

function renderOverviewExit(items) {
  $("#overviewExit").innerHTML = (items || [])
    .map(
      (e) =>
        `<div class="card ${e.done ? "done" : ""}" style="margin-bottom:0.4rem">
      <span style="margin-right:0.5rem">${e.done ? "✓" : "○"}</span>${e.label}
    </div>`
    )
    .join("");
}

function renderReflection(r) {
  if (!r) return;
  $("#reflFinished").value = r.finished || "";
  $("#reflBlocked").value = r.blocked || "";
  $("#reflNext").value = r.nextWeek || "";
  $("#reflEnergy").value = r.energy || 0;
}

function bindSubchecks(container, key) {
  const root = document.querySelector(container);
  if (!root) return;
  root.querySelectorAll("[data-lc]").forEach((el) => {
    const i = +el.dataset.lc;
    el.querySelectorAll("input").forEach((inp) => {
      inp.addEventListener("change", () => {
        week()[key][i][inp.dataset.field] = inp.checked;
        if (key === "leetcode" && inp.dataset.field === "done") {
          const lc3 = week().exitChecklist?.find((e) => e.id === "lc3");
          if (lc3) lc3.done = week().leetcode.filter((p) => p.done).length >= 3;
        }
        scheduleSave();
        render();
      });
    });
  });
}

function escapeHtml(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((t) => t.classList.remove("active"));
    document.querySelectorAll(".panel").forEach((p) => p.classList.remove("active"));
    tab.classList.add("active");
    $(`#panel-${tab.dataset.tab}`).classList.add("active");
  });
});

["reflFinished", "reflBlocked", "reflNext", "reflEnergy"].forEach((id) => {
  const el = $(`#${id}`);
  if (!el) return;
  el.addEventListener("input", () => {
    week().reflection.finished = $("#reflFinished").value;
    week().reflection.blocked = $("#reflBlocked").value;
    week().reflection.nextWeek = $("#reflNext").value;
    week().reflection.energy = +$("#reflEnergy").value || 0;
    scheduleSave();
  });
});

$("#setTodayBtn")?.addEventListener("click", setTodayFromServer);

$("#syncBtn").addEventListener("click", async () => {
  await save();
  await saveDsaTopics();
  const res = await fetch(`/api/sync-markdown?week=${weekNum}`, { method: "POST" });
  const data = await res.json();
  if (data.ok) showToast(`Synced tracker_week${weekNum}.md`);
});

load();
