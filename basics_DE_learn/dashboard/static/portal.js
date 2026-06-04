const TOPIC_NAMES = {
  t01: "Big-O", t02: "Arrays", t03: "Strings", t04: "Hash",
  t05: "Two pointers", t06: "Sliding window", t07: "Prefix sums",
};

let progress = {};
let lcLog = { problems: [] };
let mastery = { topics: {} };
let weekPlan = null;
let viewingWeek = 2;
let saveTimer = null;

function weekFromUrl() {
  const p = new URLSearchParams(window.location.search).get("w");
  return p ? Number(p) : null;
}

async function loadWeekPlan(wk) {
  viewingWeek = wk;
  weekPlan = await api(`/api/week-plan/${wk}`);
  const sel = document.getElementById("week-select");
  if (sel) sel.value = String(wk);
  document.getElementById("legacy-badge").style.display = weekPlan.legacy ? "inline" : "none";
}

function toast(msg) {
  const el = document.getElementById("toast");
  el.textContent = msg;
  el.classList.add("show");
  setTimeout(() => el.classList.remove("show"), 2200);
}

async function api(path, opts = {}) {
  const r = await fetch(path, opts);
  if (!r.ok) throw new Error(await r.text());
  return r.json();
}

function debounceSave(fn, ms = 400) {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(fn, ms);
}

function portalState() {
  if (!progress.portal) progress.portal = { dailyTasks: {}, dailyLog: {}, reflectionDraft: {} };
  return progress.portal;
}

function todayKey() {
  return progress.meta?.today || new Date().toISOString().slice(0, 10);
}

function renderStatus(todayInfo) {
  const meta = progress.meta || {};
  const lcN = lcLog.problems?.length || 0;
  const nh = lcLog.problems?.filter((p) => p.noHints).length || 0;
  const t02 = mastery.topics?.t02 || {};
  document.getElementById("status-bar").innerHTML = `
    <span>Today: <strong>${meta.today || "—"}</strong></span>
    <span>Week: <strong>${meta.currentWeek || "—"}</strong></span>
    <span>LC: <strong>${lcN}</strong> (${nh} no-hints)</span>
    <span>t02 mastery: <strong>${t02.easyNoHints ? "Easy OK" : "needs no-hint Easy"}</strong></span>
    ${todayInfo && !todayInfo.inSync ? '<span style="color:var(--warn)">Click Set today (IST)</span>' : ""}
  `;
  document.getElementById("week-badge").textContent = `Week ${viewingWeek}`;
}

function tasksForDay(day) {
  return [
    { label: day.primary, sql: false },
    { label: day.secondary && day.secondary !== "none" ? day.secondary : null, sql: day.sql },
  ].filter((t) => t.label);
}

function bindTaskCheckboxes(container, dateKey, ps) {
  if (!ps.dailyTasks[dateKey]) ps.dailyTasks[dateKey] = [false, false];
  container.querySelectorAll("input[type=checkbox][data-date]").forEach((cb) => {
    cb.addEventListener("change", () => {
      const d = cb.dataset.date;
      const i = Number(cb.dataset.taskIdx);
      if (!ps.dailyTasks[d]) ps.dailyTasks[d] = [false, false];
      ps.dailyTasks[d][i] = cb.checked;
      debounceSave(saveProgress);
    });
  });
}

function renderTaskItems(day, dateKey, ps) {
  const tasks = tasksForDay(day);
  if (!ps.dailyTasks[dateKey]) ps.dailyTasks[dateKey] = [false, false];
  return tasks
    .map(
      (t, i) => `
    <li>
      <input type="checkbox" data-date="${dateKey}" data-task-idx="${i}" ${ps.dailyTasks[dateKey][i] ? "checked" : ""} />
      <label>${t.sql ? '<span class="badge badge-sql">SQL</span> ' : ""}${escapeHtml(t.label)}</label>
    </li>`
    )
    .join("");
}

function dayAllTasksDone(dateKey, day, ps) {
  const tasks = tasksForDay(day);
  if (!tasks.length) return false;
  const flags = ps.dailyTasks[dateKey] || [];
  return tasks.every((_, i) => flags[i]);
}

function renderWeekPlan() {
  const key = todayKey();
  const list = document.getElementById("today-tasks");
  const goal = document.getElementById("mastery-goal");
  const hint = document.getElementById("view-hint");
  const rangeEl = document.getElementById("week-range");
  const currentWk = Number(progress.meta?.currentWeek) || 2;
  const ps = portalState();

  goal.textContent = weekPlan?.masteryGoal || "";
  rangeEl.textContent = weekPlan?.range ? `${weekPlan.range} · ${weekPlan.dsaTitle || ""}` : "";

  const viewingArchive = viewingWeek !== currentWk;
  const todayInViewWeek = !!weekPlan?.days?.[key];

  hint.style.display = "block";
  hint.innerHTML = viewingArchive
    ? `Archive — calendar is on <strong>Week ${currentWk}</strong>. Synced log: <a href="../../trackers/portal_week_${String(viewingWeek).padStart(2, '0')}.md">portal_week_${String(viewingWeek).padStart(2, '0')}.md</a>`
    : `Full week below — <strong>today</strong> highlighted. Sync writes <code>trackers/portal_week_NN.md</code>.`;

  const dates = Object.keys(weekPlan?.days || {}).sort();
  if (!dates.length) {
    list.innerHTML = "<li>No week plan loaded.</li>";
    return;
  }

  list.innerHTML = dates
    .map((date) => {
      const d = weekPlan.days[date];
      const isToday = date === key && todayInViewWeek;
      const done = dayAllTasksDone(date, d, ps);
      const todayBadge = isToday ? '<span class="badge badge-today">TODAY</span>' : "";
      const doneCls = done && !isToday ? " is-done" : "";
      return `
      <li class="day-block${isToday ? " is-today" : ""}${doneCls}">
        <div class="day-head">
          <strong>${d.day}</strong>
          <span style="color:var(--muted)">${date}</span>
          ${todayBadge}
        </div>
        <ul class="task-list">${renderTaskItems(d, date, ps)}</ul>
      </li>`;
    })
    .join("");

  bindTaskCheckboxes(list, key, ps);

  const logWrap = document.getElementById("daily-log-wrap");
  logWrap.style.display = todayInViewWeek ? "block" : "none";
  if (todayInViewWeek) {
    const logs = ps.archivedDailyLog || {};
    document.getElementById("daily-log").value = ps.dailyLog[key] || logs[key] || "";
  }
}

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function renderLcTable() {
  const tbody = document.querySelector("#lc-table tbody");
  tbody.innerHTML = (lcLog.problems || [])
    .map(
      (p) => `
    <tr>
      <td><a href="https://leetcode.com/problems/${slugify(p.title)}/" target="_blank">${p.id}</a></td>
      <td><input type="checkbox" data-lc="${p.id}" data-field="done" ${p.done ? "checked" : ""} /></td>
      <td><input type="checkbox" data-lc="${p.id}" data-field="noHints" ${p.noHints ? "checked" : ""} /></td>
      <td>${p.topic || ""}</td>
    </tr>`
    )
    .join("");

  tbody.querySelectorAll("input").forEach((cb) => {
    cb.addEventListener("change", () => {
      const p = lcLog.problems.find((x) => x.id === Number(cb.dataset.lc));
      if (p) p[cb.dataset.field] = cb.checked;
      debounceSave(async () => {
        await api("/api/lc-log", { method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify(lcLog) });
        renderStatus(await api("/api/today"));
      });
    });
  });
}

function slugify(title) {
  return title.toLowerCase().replace(/'/g, "").replace(/\s+/g, "-");
}

function renderMastery() {
  const grid = document.getElementById("mastery-grid");
  const ids = ["t01", "t02", "t03", "t04", "t05", "t06", "t07"];
  grid.innerHTML = ids
    .map((id) => {
      const t = mastery.topics[id] || {};
      const complete = t.theory && t.easyNoHints && t.mediumAttempted;
      return `
      <div class="mastery-item ${complete ? "complete" : ""}" data-topic="${id}">
        <strong>${id} ${TOPIC_NAMES[id] || ""}</strong>
        <label><input type="checkbox" data-topic="${id}" data-field="theory" ${t.theory ? "checked" : ""} /> Theory</label>
        <label><input type="checkbox" data-topic="${id}" data-field="easyNoHints" ${t.easyNoHints ? "checked" : ""} /> Easy no hints</label>
        <label><input type="checkbox" data-topic="${id}" data-field="mediumAttempted" ${t.mediumAttempted ? "checked" : ""} /> Medium tried</label>
      </div>`;
    })
    .join("");

  grid.querySelectorAll("input").forEach((cb) => {
    cb.addEventListener("change", () => {
      const id = cb.dataset.topic;
      if (!mastery.topics[id]) mastery.topics[id] = {};
      mastery.topics[id][cb.dataset.field] = cb.checked;
      const t = mastery.topics[id];
      t.complete = !!(t.theory && t.easyNoHints && t.mediumAttempted);
      debounceSave(async () => {
        await api("/api/dsa-mastery", {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(mastery),
        });
        renderMastery();
        renderStatus(await api("/api/today"));
      });
    });
  });
}

function renderReflection() {
  const d = portalState().reflectionDraft || {};
  document.getElementById("refl-finished").value = d.finished || "";
  document.getElementById("refl-blocked").value = d.blocked || "";
  document.getElementById("refl-next").value = d.nextWeek || "";
  document.getElementById("refl-energy").value = d.energy || 3;
}

function bindReflection() {
  const saveRefl = () => {
    portalState().reflectionDraft = {
      finished: document.getElementById("refl-finished").value,
      blocked: document.getElementById("refl-blocked").value,
      nextWeek: document.getElementById("refl-next").value,
      energy: Number(document.getElementById("refl-energy").value) || 3,
    };
    debounceSave(saveProgress);
  };
  ["refl-finished", "refl-blocked", "refl-next", "refl-energy"].forEach((id) => {
    document.getElementById(id).addEventListener("input", saveRefl);
  });
}

async function saveProgress() {
  const key = todayKey();
  portalState().dailyLog[key] = document.getElementById("daily-log").value;
  await api("/api/progress", {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(progress),
  });
}

async function loadAll() {
  const [prog, lc, mast, todayInfo] = await Promise.all([
    api("/api/progress"),
    api("/api/lc-log"),
    api("/api/dsa-mastery"),
    api("/api/today"),
  ]);
  progress = prog;
  lcLog = lc;
  mastery = mast;
  const wk = weekFromUrl() || progress.meta?.currentWeek || todayInfo.suggestedWeek || 2;
  await loadWeekPlan(wk);
  renderStatus(todayInfo);
  renderWeekPlan();
  renderLcTable();
  renderMastery();
  renderReflection();
}

document.getElementById("daily-log").addEventListener(
  "input",
  () => debounceSave(saveProgress)
);

document.getElementById("btn-set-today").addEventListener("click", async () => {
  const r = await api("/api/set-today", { method: "POST" });
  progress.meta.today = r.today;
  progress.meta.currentWeek = r.currentWeek;
  await loadWeekPlan(r.currentWeek);
  history.replaceState({}, "", `/portal?w=${r.currentWeek}`);
  renderWeekPlan();
  renderStatus(await api("/api/today"));
  toast(`Today set to ${r.today} · Week ${r.currentWeek}`);
});

document.getElementById("week-select").addEventListener("change", async (e) => {
  const wk = Number(e.target.value);
  await loadWeekPlan(wk);
  history.replaceState({}, "", `/portal?w=${wk}`);
  renderWeekPlan();
});

document.getElementById("btn-sync").addEventListener("click", async () => {
  const week = progress.meta?.currentWeek || 2;
  const clearLogs = document.getElementById("chk-clear-logs").checked ? "1" : "0";
  const r = await api(`/api/sync-markdown?week=${week}&clear_logs=${clearLogs}`, { method: "POST" });
  let msg = `Synced: ${r.paths.join(", ")}`;
  progress = await api("/api/progress");
  const key = todayKey();
  if (r.clearedLogDates?.length) {
    msg += ` · cleared live log: ${r.clearedLogDates.join(", ")} (archived + markdown kept)`;
  }
  if (document.getElementById("daily-log")) {
    const ps = progress.portal || {};
    const arch = ps.archivedDailyLog || {};
    document.getElementById("daily-log").value = ps.dailyLog?.[key] || arch[key] || "";
  }
  document.getElementById("sync-msg").textContent = msg;
  toast("Markdown synced — ready to git commit");
});

document.getElementById("btn-copy-refl").addEventListener("click", () => {
  const d = portalState().reflectionDraft || {};
  const md = `## Week reflection\n\n- **Finished:** ${d.finished || "_"}\n- **Blocked:** ${d.blocked || "_"}\n- **Next week adjust:** ${d.nextWeek || "_"}\n- **Energy (1–5):** ${d.energy || "_"}\n`;
  navigator.clipboard.writeText(md);
  toast("Reflection copied");
});

bindReflection();
loadAll().catch((e) => {
  document.getElementById("status-bar").textContent = "Error: " + e.message;
});
